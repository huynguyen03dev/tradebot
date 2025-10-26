# Agent Guidelines

## Build/Test Commands
- No test framework configured. Run Python scripts directly: `python <script>.py`
- No linting configured. Consider running `python -m py_compile <script>.py` to check syntax

## Code Style
- Language: Python 3
- Imports: Standard library first, then third-party (requests, bs4, html2text)
- Formatting: 4 spaces indentation, no explicit line length limit observed
- Naming: snake_case for variables/functions (e.g., `base_url`, `doc_links`)
- Types: No type hints used
- Error handling: Try-except blocks with descriptive error messages; check status codes
- File operations: Use `os.path.join()` for paths, `with` statements for file handling
- String handling: Use f-strings for formatting
- External requests: Add delays (`time.sleep()`) to avoid overwhelming servers
- Directories: Use `os.makedirs(exist_ok=True)` for safe directory creation

## Project Context
- Trading bot project with MT5 (MetaTrader 5) Python API documentation
- Main script: `crawler.py` - web scraper for MT5 docs
- Documentation stored in `docs/` as markdown files
- No package manager or virtual environment configured yet
