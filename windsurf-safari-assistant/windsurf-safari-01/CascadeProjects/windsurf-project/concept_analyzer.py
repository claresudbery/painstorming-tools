#!/usr/bin/env python3
"""
Markdown Concept Analyzer

This script analyzes markdown files to determine the frequency of specified concepts.
It can process both individual files and directories of markdown files.
"""

import os
import re
import click
from collections import defaultdict
from pathlib import Path
from typing import List, Dict, Tuple
import frontmatter
from rich.console import Console
from rich.table import Table
from rich.progress import track


class ConceptAnalyzer:
    def __init__(self, case_sensitive: bool = False):
        self.case_sensitive = case_sensitive
        self.console = Console()

    def load_markdown_files(self, path: str) -> List[Tuple[str, str]]:
        """Load markdown files from a file or directory."""
        path = Path(path)
        files = []

        if path.is_file():
            if path.suffix.lower() == '.md':
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                files.append((str(path), content))
        else:
            for root, _, filenames in os.walk(path):
                for filename in filenames:
                    if filename.lower().endswith('.md'):
                        filepath = Path(root) / filename
                        with open(filepath, 'r', encoding='utf-8') as f:
                            content = f.read()
                        files.append((str(filepath), content))

        return files

    def extract_text_from_markdown(self, content: str) -> str:
        """Extract plain text from markdown content, removing frontmatter and code blocks."""
        # Remove YAML frontmatter if present
        try:
            post = frontmatter.loads(content)
            content = post.content
        except:
            pass

        # Remove code blocks
        content = re.sub(r'```[\s\S]*?```', '', content)
        content = re.sub(r'`[^`]*`', '', content)
        
        # Remove markdown links and images
        content = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', '', content)
        
        # Remove HTML tags if any
        content = re.sub(r'<[^>]+>', '', content)
        
        # Remove markdown headers and formatting
        content = re.sub(r'^#+\s*', '', content, flags=re.MULTILINE)
        content = re.sub(r'[\*_]{1,3}([^\*_]*)[\*_]{1,3}', r'\1', content)
        
        return content.strip()

    def count_concepts(self, text: str, concepts: List[str]) -> Dict[str, int]:
        """Count occurrences of each concept in the text."""
        counts = defaultdict(int)
        flags = 0 if self.case_sensitive else re.IGNORECASE
        
        for concept in concepts:
            # Create a regex pattern that matches whole words only
            pattern = r'\b' + re.escape(concept) + r'\b'
            matches = re.findall(pattern, text, flags=flags)
            counts[concept] = len(matches)
            
        return dict(counts)

    def analyze_files(self, files: List[Tuple[str, str]], concepts: List[str]) -> Dict[str, Dict[str, int]]:
        """Analyze multiple files and return concept frequencies."""
        results = {}
        
        for filepath, content in track(files, description="Analyzing files..."):
            text = self.extract_text_from_markdown(content)
            counts = self.count_concepts(text, concepts)
            results[filepath] = counts
            
        return results

    def print_results(self, results: Dict[str, Dict[str, int]], concepts: List[str]):
        """Display analysis results in a formatted table."""
        if not results:
            self.console.print("[yellow]No markdown files found or processed.[/yellow]")
            return

        # Create a summary table
        summary_table = Table(title="Concept Frequency Analysis", show_header=True, header_style="bold magenta")
        summary_table.add_column("Concept", style="cyan", no_wrap=True)
        summary_table.add_column("Total Occurrences", justify="right", style="green")
        
        # Create a detailed table
        detailed_table = Table(title="Detailed Analysis by File", show_header=True, header_style="bold blue")
        detailed_table.add_column("File", style="cyan", no_wrap=True)
        for concept in concepts:
            detailed_table.add_column(concept, justify="right", style="green")
        
        # Calculate totals
        totals = {concept: 0 for concept in concepts}
        
        # Process each file's results
        for filepath, counts in results.items():
            row = [os.path.basename(filepath)]
            for concept in concepts:
                count = counts.get(concept, 0)
                row.append(str(count) if count > 0 else "-")
                totals[concept] += count
            detailed_table.add_row(*row)
        
        # Add totals to summary
        for concept in concepts:
            summary_table.add_row(concept, str(totals[concept]))
        
        # Print the tables
        self.console.print(summary_table)
        self.console.print("\n")
        self.console.print(detailed_table)


@click.command()
@click.argument('path', type=click.Path(exists=True))
@click.option('--concepts', '-c', multiple=True, help='Concepts to search for (can be specified multiple times)')
@click.option('--case-sensitive/--no-case-sensitive', default=False, help='Perform case-sensitive search')
@click.option('--concepts-file', type=click.Path(exists=True), 
              help='File containing one concept per line (alternative to --concepts)')
def main(path: str, concepts: tuple, case_sensitive: bool, concepts_file: str):
    """
    Analyze markdown files for concept frequencies.
    
    PATH can be either a single markdown file or a directory containing markdown files.
    """
    # Process concepts from command line and/or file
    concept_list = list(concepts)
    
    if concepts_file:
        with open(concepts_file, 'r', encoding='utf-8') as f:
            file_concepts = [line.strip() for line in f if line.strip()]
            concept_list.extend(file_concepts)
    
    if not concept_list:
        click.echo("Error: No concepts specified. Use --concepts or --concepts-file.", err=True)
        return
    
    analyzer = ConceptAnalyzer(case_sensitive=case_sensitive)
    
    try:
        # Load and process files
        files = analyzer.load_markdown_files(path)
        if not files:
            click.echo(f"No markdown files found at {path}")
            return
            
        # Analyze files
        results = analyzer.analyze_files(files, concept_list)
        
        # Display results
        analyzer.print_results(results, concept_list)
        
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}", err=True)
        if __debug__:
            raise


if __name__ == "__main__":
    main()
