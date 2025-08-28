# Markdown Concept Analyzer - Project Specification

## Overview

A Python command-line application that analyzes markdown files to determine the frequency of specified concepts. The tool will process markdown content intelligently, ignoring formatting elements while providing detailed frequency analysis.

## Core Functionality

### Input Processing
- **File Input**: Accept single markdown files or directories containing markdown files
- **Concept Input**: Support two methods for specifying concepts:
  - Command-line arguments (`--concepts "concept1" --concepts "concept2"`)
  - Concepts file (`--concepts-file path/to/concepts.txt`)
- **Recursive Directory Processing**: When given a directory, recursively find all `.md` files

### Markdown Processing
- **Content Extraction**: Extract plain text from markdown while preserving semantic meaning
- **Ignore Elements**:
  - YAML frontmatter
  - Code blocks (both inline `code` and fenced ```code```)
  - Markdown links and images
  - HTML tags
  - Markdown formatting symbols (headers, bold, italic)
- **Text Normalization**: Clean extracted text for accurate concept matching

### Concept Matching
- **Word Boundary Matching**: Use regex word boundaries to match whole words only
- **Case Sensitivity**: Support both case-sensitive and case-insensitive matching (default: case-insensitive)
- **Exact Concept Matching**: Count exact matches of specified concepts

### Output and Reporting
- **Summary Table**: Display total occurrences of each concept across all files
- **Detailed Table**: Show per-file breakdown of concept frequencies
- **Rich Formatting**: Use Rich library for attractive console output
- **Progress Indication**: Show progress when processing multiple files

## Technical Architecture

### Core Components

1. **ConceptAnalyzer Class**
   - Main orchestrator for the analysis process
   - Handles file loading, text processing, and concept counting
   - Manages case sensitivity settings

2. **File Processing Module**
   - Load markdown files from paths (files or directories)
   - Handle file encoding and error cases
   - Recursive directory traversal

3. **Text Processing Module**
   - Extract plain text from markdown content
   - Remove frontmatter using python-frontmatter library
   - Clean markdown formatting with regex patterns

4. **Concept Matching Engine**
   - Regex-based word boundary matching
   - Case-sensitive/insensitive options
   - Frequency counting and aggregation

5. **Output Formatter**
   - Rich-based table formatting
   - Summary and detailed views
   - Progress tracking during analysis

### Dependencies
- **click**: Command-line interface framework
- **rich**: Console formatting and progress bars
- **python-frontmatter**: YAML frontmatter processing
- **markdown**: Markdown parsing utilities
- **pathlib**: Modern path handling
- **re**: Regular expression processing

## Command-Line Interface

### Basic Usage
```bash
python3 concept_analyzer.py <PATH> [OPTIONS]
```

### Arguments
- `PATH`: Required. Path to markdown file or directory

### Options
- `--concepts, -c`: Specify concepts to search for (repeatable)
- `--concepts-file`: Path to file containing concepts (one per line)
- `--case-sensitive/--no-case-sensitive`: Enable/disable case-sensitive matching (default: False)

### Examples
```bash
# Single file with inline concepts
python3 concept_analyzer.py document.md --concepts "AI" --concepts "machine learning"

# Directory with concepts file
python3 concept_analyzer.py ./docs --concepts-file concepts.txt

# Case-sensitive analysis
python3 concept_analyzer.py notes/ --concepts "Python" --case-sensitive
```

## Error Handling

### File Access Errors
- Handle missing files/directories gracefully
- Provide clear error messages for permission issues
- Skip unreadable files with warnings

### Content Processing Errors
- Handle malformed markdown gracefully
- Continue processing if individual files fail
- Report processing errors without stopping analysis

### Input Validation
- Validate concept inputs (non-empty, valid strings)
- Ensure at least one concept is specified
- Check file path existence before processing

## Output Format

### Summary Table
Shows total occurrences of each concept across all analyzed files

### Detailed Table
Shows per-file breakdown with concept counts for each file

## Implementation Plan

1. **Setup Project Structure**
   - Create main application file (`concept_analyzer.py`)
   - Set up dependencies (`requirements.txt`)
   - Create documentation (`README.md`)

2. **Core Implementation**
   - Implement ConceptAnalyzer class
   - Add file loading and markdown processing
   - Implement concept matching with regex
   - Add Rich-based output formatting

3. **CLI Interface**
   - Implement Click-based command-line interface
   - Add argument parsing and validation
   - Handle error cases gracefully

4. **Testing and Validation**
   - Test with various markdown files
   - Validate concept matching accuracy
   - Ensure proper error handling
