# Safari Assistant - Architecture Specification

## System Overview
The Safari Assistant is a web-based tool for analyzing markdown files to identify and count concept frequencies. The system follows a simple client-server architecture with a Python backend and Streamlit frontend.

## Architecture Diagram
```
┌─────────────────────────────────────────────────────────────┐
│                    Safari Assistant                         │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────┐    ┌─────────────────────────────────┐ │
│  │   Frontend      │    │         Backend                 │ │
│  │   (Streamlit)   │◄──►│      (Python Core)              │ │
│  │                 │    │                                 │ │
│  │ • File Upload   │    │ ┌─────────────────────────────┐ │ │
│  │ • Config UI     │    │ │    Text Processing          │ │ │
│  │ • Results View  │    │ │  • Markdown Parser          │ │ │
│  │ • Charts/Tables │    │ │  • Content Extraction       │ │ │
│  └─────────────────┘    │ │  • Regex Cleaning           │ │ │
│                         │ └─────────────────────────────┘ │ │
│                         │                                 │ │
│                         │ ┌─────────────────────────────┐ │ │
│                         │ │    Concept Analysis         │ │ │
│                         │ │  • Pattern Matching         │ │ │
│                         │ │  • Word Boundary Detection  │ │ │
│                         │ │  • Case Sensitivity         │ │ │
│                         │ │  • Frequency Counting       │ │ │
│                         │ └─────────────────────────────┘ │ │
│                         │                                 │ │
│                         │ ┌─────────────────────────────┐ │ │
│                         │ │    File Management          │ │ │
│                         │ │  • Single File Processing   │ │ │
│                         │ │  • Directory Traversal      │ │ │
│                         │ │  • File Type Filtering      │ │ │
│                         │ └─────────────────────────────┘ │ │
│                         └─────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

## Component Architecture

### 1. Frontend Layer (Streamlit)
**Purpose**: User interface and interaction management

**Responsibilities**:
- File upload interface (single files or directories)
- Concept configuration (manual entry or file upload)
- Analysis parameter settings (case sensitivity, output format)
- Results visualization (tables, charts, summaries)
- User feedback and error handling

**Key Components**:
- `streamlit_app.py` - Main application entry point
- UI components for file selection and configuration
- Interactive data visualization widgets

### 2. Backend Core (Python)

#### 2.1 Text Processing Module
**Purpose**: Extract and clean text from markdown files

**Responsibilities**:
- Parse markdown files
- Remove frontmatter (YAML/TOML headers)
- Strip code blocks (```...```)
- Clean markdown formatting (headers, links, emphasis)
- Extract plain text content

**Key Functions**:
- `parse_markdown(file_path)` - Main parsing function
- `remove_frontmatter(content)` - Strip metadata
- `remove_code_blocks(content)` - Filter code sections
- `clean_markdown_formatting(content)` - Remove MD syntax

#### 2.2 Concept Analysis Module
**Purpose**: Analyze text for concept frequency

**Responsibilities**:
- Load concept lists from files or user input
- Perform regex-based word boundary matching
- Handle case-sensitive/insensitive matching
- Count concept occurrences per file
- Generate frequency statistics

**Key Functions**:
- `load_concepts(source)` - Load concept list
- `analyze_concepts(text, concepts, options)` - Main analysis
- `count_matches(text, pattern, case_sensitive)` - Pattern matching
- `generate_statistics(results)` - Summary calculations

#### 2.3 File Management Module
**Purpose**: Handle file system operations

**Responsibilities**:
- Process single files or entire directories
- Filter for markdown files (.md, .markdown)
- Handle file reading and error management
- Manage temporary uploads from Streamlit

**Key Functions**:
- `process_directory(path, recursive=True)` - Directory traversal
- `is_markdown_file(filename)` - File type checking
- `read_file_safely(path)` - Error-handled file reading

## Data Flow

### 1. Input Processing
```
User Input → File Upload/Selection → Concept Configuration → Analysis Parameters
```

### 2. Analysis Pipeline
```
Files → Text Extraction → Concept Matching → Frequency Counting → Results Aggregation
```

### 3. Output Generation
```
Raw Results → Statistical Processing → Visualization → Interactive Display
```

## Key Design Decisions

### Technology Stack
- **Python**: Core language for text processing and analysis
- **Streamlit**: Web framework for rapid prototyping and easy deployment
- **Regex**: Pattern matching for reliable concept detection
- **Pandas**: Data manipulation and table generation

### Processing Approach
- **Word Boundary Matching**: Ensures accurate concept detection (avoids partial matches)
- **Streaming Processing**: Handle large files without memory issues
- **Modular Design**: Separate concerns for maintainability and testing

### User Experience
- **Progressive Disclosure**: Simple interface with advanced options available
- **Real-time Feedback**: Progress indicators for long-running operations
- **Interactive Results**: Sortable tables and filterable views

## Scalability Considerations

### Current MVP Limitations
- Single-user application
- Local file processing only
- Limited to markdown files
- In-memory processing

### Future Enhancement Opportunities
- Multi-user support with session management
- Cloud file storage integration
- Support for additional file formats
- Database storage for analysis history
- API endpoints for programmatic access
- Advanced analytics and trend analysis

## Security Considerations
- File upload validation and sanitization
- Path traversal protection for directory processing
- Content size limits to prevent resource exhaustion
- Safe regex patterns to avoid ReDoS attacks

## Deployment Architecture
```
Development: Local Streamlit server
Production: Streamlit Cloud / Docker container
```

## Dependencies
- **Core**: `streamlit`, `pandas`, `regex`
- **Text Processing**: `markdown`, `pyyaml`
- **Visualization**: `plotly`, `matplotlib`
- **File Handling**: `pathlib`, `os`
