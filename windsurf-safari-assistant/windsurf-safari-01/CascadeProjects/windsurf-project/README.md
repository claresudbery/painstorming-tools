# Markdown Concept Analyzer

A Python tool to analyze markdown files and determine the frequency of specified concepts.

## Features

- Analyze individual markdown files or directories containing markdown files
- Search for multiple concepts at once
- Case-sensitive or case-insensitive search
- Support for reading concepts from a file
- Clean, formatted output with Rich
- Handles markdown formatting (ignores code blocks, links, images, etc.)
- Processes YAML frontmatter

## Installation

1. Clone this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python concept_analyzer.py PATH --concepts "concept1" --concepts "concept2"
```

### Options

- `PATH`: Path to a markdown file or directory containing markdown files
- `-c, --concepts`: Concepts to search for (can be specified multiple times)
- `--case-sensitive/--no-case-sensitive`: Perform case-sensitive search (default: False)
- `--concepts-file`: File containing one concept per line (alternative to --concepts)

### Examples

1. Search for specific concepts in a single file:
   ```bash
   python concept_analyzer.py notes.md --concepts "machine learning" --concepts "AI"
   ```

2. Search for concepts from a file in a directory of markdown files:
   ```bash
   python concept_analyzer.py ./my_notes --concepts-file concepts.txt
   ```

3. Perform a case-sensitive search:
   ```bash
   python concept_analyzer.py docs/ --concepts "Python" --concepts "python" --case-sensitive
   ```

## Example concepts.txt

```
machine learning
AI
Python
Data Science
Neural Networks
```

## Output

The tool will display two tables:
1. A summary of total occurrences for each concept across all files
2. A detailed breakdown showing counts for each concept in each file

## Notes

- The tool ignores code blocks, YAML frontmatter, and markdown formatting when searching
- Concepts are matched as whole words only (using word boundaries)
- The tool will recursively search through subdirectories if a directory is provided
