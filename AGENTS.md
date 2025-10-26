# Agent Guidelines

## Build/Test Commands
- No test framework configured. Run Python scripts directly: `python <script>.py`
- Example: `python breakout_backtest.py` to run backtest
- Syntax check: `python -m py_compile <script>.py`
- Dependencies: `pip install MetaTrader5 pandas pytz requests beautifulsoup4 html2text`
- No linting configured (consider adding flake8/pylint/black)

## Code Style
- Language: Python 3.13 (based on __pycache__)
- Imports: Standard library first, then third-party, in alphabetical order when possible
- Formatting: 4 spaces indentation, no line length limit enforced
- Naming: snake_case for variables/functions/files; UPPER_CASE for constants
- Classes: PascalCase (Trade, BreakoutStrategy, Backtester)
- Types: No type hints used currently
- Docstrings: Use triple-quoted strings with Google-style format describing parameters, returns, and behavior
- Error handling: Try-except-finally blocks; check return values before proceeding; use descriptive error messages
- File operations: Use `os.path.join()` for paths, `with` statements for file I/O
- String handling: Prefer f-strings for formatting
- External requests: Add `time.sleep(1)` delays between requests to avoid rate limiting
- Directory creation: Use `os.makedirs(exist_ok=True)`

## MT5-Specific Patterns
- Connection lifecycle: Always `mt5.initialize()` at start, `mt5.shutdown()` in finally block
- Error checking: Check all MT5 function return values; call `mt5.last_error()` on failures
- Symbol validation: Use `mt5.symbol_select()` before trading
- Credentials: Load from environment variables using `os.getenv()` (see .env file); never hardcode in production

## Project Context
- MT5 algorithmic trading system with backtesting capabilities
- `breakout_backtest.py` - Main breakout strategy with full backtesting engine
- `crawler.py` - Utility to download MT5 API docs from mql5.com
- `mt5_btc_chart.py` - Example connection/data retrieval (contains demo credentials - not for production)
- `docs/` - MT5 API documentation in markdown
- `ai-tasks/` - AI agent task definitions
- `.env` - MT5 credentials (currently demo account - use real credentials carefully)
