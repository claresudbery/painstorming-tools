# Safari Assistant

## What It Does
The long term plan is to create a tool that will help us to analyse our Sales Safari data so that we can spot trends, pains, and common behaviour patterns in our target audience.
We're going to start with an MVP with just one simple feature: The ability to analyse markdown files to count how often specified concepts appear.

## Key sub-features
- Processes single files or entire directories
- Ignores code blocks, frontmatter, and markdown formatting
- Supports concepts from command line or file
- Case-sensitive/insensitive matching
- Clean table output with totals and per-file breakdown

## Implementation
- **Text Processing**: Extract plain text, remove markdown formatting with regex
- **Matching**: Word boundary regex matching for accurate concept detection
- **Output**: Rich library for formatted tables and progress bars
