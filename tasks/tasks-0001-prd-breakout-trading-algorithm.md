# Task List: Breakout Trading Algorithm with Backtesting

Generated from: `0001-prd-breakout-trading-algorithm.md`

## Relevant Files

- `breakout_backtest.py` - Main script containing the breakout trading algorithm and backtesting engine.
- `config.py` (optional) - Configuration file for backtest parameters (alternative to constants in main script).

### Notes

- This project does not have a configured test framework. Run the script directly with `python breakout_backtest.py` to execute.
- Follow existing patterns from `mt5_btc_chart.py` for MT5 connection, error handling, and data retrieval.
- Use `python -m py_compile breakout_backtest.py` to check syntax before running.

## Tasks

- [x] 1.0 Set up project structure and configuration system
  - [x] 1.1 Create `breakout_backtest.py` file in project root
  - [x] 1.2 Add imports for required libraries (MetaTrader5, pandas, pytz, datetime)
  - [x] 1.3 Define configuration constants at top of script (SYMBOL, TIMEFRAME, START_DATE, END_DATE, STARTING_BALANCE, POSITION_SIZE_PCT, LOOKBACK_PERIOD)
  - [x] 1.4 Set default configuration values (AUD/USD symbol, 5-minute timeframe, $10,000 balance, 2% position size, 20 candle lookback)
  - [x] 1.5 Add docstring explaining the script's purpose and configuration parameters
- [x] 2.0 Implement MT5 data retrieval and validation
  - [x] 2.1 Create MT5 initialization function following pattern from `mt5_btc_chart.py`
  - [x] 2.2 Add MT5 login functionality (handle credentials appropriately, consider environment variables)
  - [x] 2.3 Implement function to validate AUD/USD symbol availability using `mt5.symbol_select()`
  - [x] 2.4 Create function to fetch 5-minute historical data using `mt5.copy_rates_range()` with configured date range
  - [x] 2.5 Convert MT5 rates data to pandas DataFrame with proper datetime conversion
  - [x] 2.6 Add error handling for MT5 connection failures with `mt5.last_error()` calls
  - [x] 2.7 Add validation for date range (start < end) and data availability
  - [x] 2.8 Implement MT5 shutdown function to be called at script end
- [ ] 3.0 Implement breakout detection algorithm
  - [ ] 3.1 Create `Trade` class with attributes: entry_time, entry_price, exit_time, exit_price, direction (BUY/SELL), position_size, profit_loss
  - [ ] 3.2 Create `BreakoutStrategy` class with initialization method accepting lookback_period parameter
  - [ ] 3.3 Implement method to calculate resistance level (highest high over lookback period)
  - [ ] 3.4 Implement method to calculate support level (lowest low over lookback period)
  - [ ] 3.5 Implement method to detect bullish breakout (close price > resistance level)
  - [ ] 3.6 Implement method to detect bearish breakout (close price < support level)
  - [ ] 3.7 Create method to generate trading signals (BUY on bullish breakout, SELL on bearish breakout, None otherwise)
  - [ ] 3.8 Add logic to prevent multiple signals while already in a position
- [ ] 4.0 Build backtesting engine with trade simulation
  - [ ] 4.1 Create `Backtester` class with initialization accepting strategy, data, starting_balance, and position_size_pct
  - [ ] 4.2 Implement main backtest loop that iterates through historical candles
  - [ ] 4.3 Add logic to track current position state (in_trade flag, current_trade object)
  - [ ] 4.4 Implement trade entry logic: calculate position size based on balance percentage and current price
  - [ ] 4.5 Implement exit strategy (exit on opposite signal per PRD recommendation)
  - [ ] 4.6 Calculate profit/loss for each trade in USD (consider direction: BUY profit = (exit - entry) * size, SELL profit = (entry - exit) * size)
  - [ ] 4.7 Store completed trades in a list for later analysis
  - [ ] 4.8 Add progress indicator to show processing status (e.g., print every 500 candles)
  - [ ] 4.9 Handle edge case where final trade is still open at backtest end (force close at last price)
- [ ] 5.0 Implement results calculation and console output
  - [ ] 5.1 Create method to calculate total number of trades executed
  - [ ] 5.2 Create method to calculate number of winning trades (profit > 0) and losing trades (profit <= 0)
  - [ ] 5.3 Calculate winrate percentage (winning trades / total trades * 100)
  - [ ] 5.4 Calculate total profit/loss by summing all individual trade P/L
  - [ ] 5.5 Calculate net return percentage ((total P/L / starting balance) * 100)
  - [ ] 5.6 Format console output with clear section headers and aligned values
  - [ ] 5.7 Display backtest summary including: backtest period, total trades, winning/losing trades, winrate %, total P/L USD, net return %
  - [ ] 5.8 Handle zero trades scenario gracefully (display message if no breakouts detected)
  - [ ] 5.9 Create main execution block that orchestrates: MT5 connection → data retrieval → strategy creation → backtesting → results display → MT5 shutdown
  - [ ] 5.10 Add try-except-finally block to ensure MT5 shutdown is always called
