# PRD: Breakout Trading Algorithm with Backtesting

## Introduction/Overview

This feature implements a breakout trading algorithm for AUD/USD currency pair on a 5-minute timeframe using MetaTrader 5 (MT5) platform. The algorithm identifies when price breaks through established support or resistance levels and executes trades accordingly. The system includes a backtesting module to evaluate the strategy's historical performance, specifically calculating winrate, total profit/loss, and number of trades executed.

**Problem Statement:** Traders need an automated way to identify and capitalize on breakout opportunities in the AUD/USD market while being able to validate the strategy's effectiveness through historical testing.

**Goal:** Create a simple, reliable breakout trading algorithm with backtesting capabilities to measure winrate and profitability before deploying to live markets.

## Goals

1. Implement a breakout detection algorithm that identifies when AUD/USD price breaks resistance or support levels on 5-minute charts
2. Execute simulated trades based on breakout signals with percentage-based position sizing
3. Backtest the strategy on historical MT5 data to calculate key performance metrics
4. Display clear, actionable results including winrate, total profit/loss, and trade count
5. Provide a foundation for future enhancement with live trading capabilities

## User Stories

1. **As a trader**, I want to automatically detect breakout patterns on AUD/USD 5-minute charts so that I can identify trading opportunities without manual chart monitoring.

2. **As a trader**, I want to backtest my breakout strategy on historical data so that I can evaluate its winrate and profitability before risking real capital.

3. **As a trader**, I want to use percentage-based position sizing so that my risk is proportional to my account balance.

4. **As a trader**, I want to see a clear summary of backtest results (winrate, profit/loss, trade count) in the console so that I can quickly assess strategy performance.

5. **As a developer**, I want the algorithm to use MT5's existing API integration so that I can leverage reliable historical data without additional data sources.

## Functional Requirements

### Breakout Algorithm

1. The system must connect to MetaTrader 5 using the existing `MetaTrader5` Python library integration.

2. The system must retrieve historical 5-minute candlestick data for AUD/USD from MT5 for the specified backtest period.

3. The system must identify support and resistance levels using a configurable lookback period (e.g., previous N candles).

4. The system must detect a bullish breakout when the closing price exceeds the resistance level.

5. The system must detect a bearish breakout when the closing price falls below the support level.

6. The system must generate a BUY signal on bullish breakouts and a SELL signal on bearish breakouts.

### Position Sizing

7. The system must calculate position size based on a configurable percentage of the starting account balance (e.g., 2% per trade).

8. The system must apply the position size calculation to each trade during backtesting.

### Backtesting Engine

9. The system must simulate trade execution based on generated signals without connecting to live trading.

10. The system must track entry price, exit price, position size, and trade direction for each simulated trade.

11. The system must implement a simple exit strategy (e.g., exit at next opposite signal, or after N candles, or at fixed profit/loss threshold).

12. The system must calculate profit/loss for each trade in the base currency (USD).

13. The system must aggregate individual trade results to calculate:
    - Total number of trades executed
    - Number of winning trades
    - Number of losing trades
    - Winrate (percentage of winning trades)
    - Total profit/loss
    - Net profit/loss percentage relative to starting balance

### Output & Reporting

14. The system must display backtest results in the console with clear formatting.

15. The system must show a summary including:
    - Backtest period (start date to end date)
    - Total trades
    - Winning trades
    - Losing trades
    - Winrate percentage
    - Total profit/loss in USD
    - Net return percentage

16. The system must handle and display MT5 connection errors gracefully with descriptive error messages.

17. The system must validate that AUD/USD symbol is available in MT5 before starting backtest.

### Configuration

18. The system must allow configuration of key parameters:
    - Backtest start date
    - Backtest end date
    - Starting account balance
    - Position size percentage
    - Breakout lookback period
    - Exit strategy parameters

19. Configuration parameters should be easily modifiable (e.g., via constants at the top of the script or a configuration file).

## Non-Goals (Out of Scope)

1. **Live trading execution** - This PRD focuses on backtesting only. Live trading will be a future enhancement.

2. **Advanced technical indicators** - Only price-based breakout detection is included. Additional indicators (RSI, MACD, etc.) are out of scope.

3. **Multiple currency pairs** - Only AUD/USD is supported initially. Multi-pair support is a future consideration.

4. **Multiple timeframes** - Only 5-minute charts are supported. Multi-timeframe analysis is out of scope.

5. **Advanced risk management** - Stop-loss, take-profit, trailing stops, and dynamic position sizing are not included in this version.

6. **Graphical output** - No charts or visual plots. Console output only.

7. **Data export** - No CSV/Excel export of trade logs or results.

8. **Optimization features** - No parameter optimization or walk-forward analysis.

9. **Slippage and commission modeling** - Assumes perfect execution without transaction costs.

10. **Fundamental analysis** - Only technical price action is considered.

## Design Considerations

### Code Structure

- Create a new Python script: `breakout_backtest.py`
- Use object-oriented design with classes for:
  - `BreakoutStrategy` - Contains breakout detection logic
  - `Backtester` - Handles trade simulation and results calculation
  - `Trade` - Represents a single trade with entry/exit details

### MT5 Integration

- Follow existing patterns from `mt5_btc_chart.py` for MT5 connection and data retrieval
- Use `mt5.copy_rates_range()` to fetch historical 5-minute data
- Ensure proper initialization and shutdown of MT5 connection

### User Experience

- Display progress indicators during backtesting (e.g., "Processing 1000 candles...")
- Use clear, formatted console output with aligned columns for readability
- Show percentage values with 2 decimal places, currency with 2 decimal places

## Technical Considerations

### Dependencies

- `MetaTrader5` - Already installed, used for data retrieval
- `pandas` - Already installed, used for data manipulation
- `pytz` - Already installed, for timezone handling
- No additional dependencies required

### MT5 Requirements

- User must have MT5 installed and configured
- AUD/USD symbol must be available in MT5 market watch
- Historical 5-minute data must be available for the requested backtest period

### Performance

- Should handle backtests of several months of 5-minute data (tens of thousands of candles) efficiently
- Expected runtime: Under 30 seconds for 3 months of data on standard hardware

### Error Handling

- Check MT5 initialization success, call `mt5.last_error()` on failure
- Validate date ranges (start date < end date)
- Validate configuration parameters (percentages in valid ranges, positive balance)
- Handle cases where no breakouts are detected (zero trades)

### Data Assumptions

- 5-minute candle data is complete without gaps (handle missing data gracefully if gaps exist)
- Price data is in standard OHLC format
- Account balance is in USD

## Success Metrics

1. **Functional Success**: The backtester successfully executes and displays results without errors for a 3-month historical period.

2. **Accuracy**: Manual verification of a small sample of trades (5-10) confirms correct breakout detection and profit/loss calculation.

3. **Performance**: Backtesting 3 months of 5-minute data completes in under 30 seconds.

4. **Usability**: A junior developer can understand the code structure and modify configuration parameters within 15 minutes.

5. **Output Clarity**: Results display includes all required metrics (winrate, P/L, trade count) in a readable format.

## Open Questions

1. **Exit Strategy Details**: What specific exit logic should be used?
   - Option A: Exit on opposite signal (bullish breakout exits when bearish breakout occurs)
   - Option B: Fixed number of candles (e.g., exit after 10 candles)
   - Option C: Fixed profit/loss threshold (e.g., exit at +/-50 pips)
   - **Recommendation**: Start with Option A (exit on opposite signal) for simplicity.

2. **Breakout Confirmation**: Should breakouts require confirmation (e.g., close above resistance for 2 consecutive candles) or is single candle close sufficient?
   - **Recommendation**: Start with single candle close for simplicity, add confirmation as enhancement.

3. **Starting Balance**: What should the default starting account balance be for backtesting?
   - **Recommendation**: $10,000 USD as a reasonable starting point.

4. **Position Size Percentage**: What default percentage of balance per trade?
   - **Recommendation**: 2% per trade as a conservative starting point.

5. **Lookback Period**: How many candles should be used to identify support/resistance levels?
   - **Recommendation**: 20 candles (100 minutes on 5-minute chart) as a starting point.

6. **Handling Multiple Signals**: If already in a trade and a new signal in the same direction occurs, should it be ignored or should the position be increased?
   - **Recommendation**: Ignore new signals while in a trade (one position at a time).
