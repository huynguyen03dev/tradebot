"""
Breakout Trading Algorithm with Backtesting

This script implements a breakout trading strategy for AUD/USD on 5-minute charts.
It identifies when price breaks through support or resistance levels and simulates
trades to evaluate the strategy's historical performance.

Configuration Parameters:
- SYMBOL: Trading pair (default: AUDUSD)
- TIMEFRAME: Chart timeframe (default: 5-minute)
- START_DATE: Backtest start date
- END_DATE: Backtest end date
- STARTING_BALANCE: Initial account balance in USD
- POSITION_SIZE_PCT: Percentage of balance to risk per trade
- LOOKBACK_PERIOD: Number of candles to determine support/resistance levels

Results Include:
- Total number of trades
- Winning and losing trades
- Winrate percentage
- Total profit/loss in USD
- Net return percentage
"""

from datetime import datetime, timedelta
import MetaTrader5 as mt5
import pandas as pd
import pytz

# ============================================================================
# CONFIGURATION PARAMETERS
# ============================================================================

# Trading symbol
SYMBOL = "AUDUSD"

# Timeframe for analysis (5-minute chart)
TIMEFRAME = mt5.TIMEFRAME_M5

# Backtest date range
START_DATE = datetime(2024, 1, 1, tzinfo=pytz.UTC)
END_DATE = datetime(2024, 3, 31, tzinfo=pytz.UTC)

# Account settings
STARTING_BALANCE = 10000.0  # USD

# Position sizing (percentage of balance per trade)
POSITION_SIZE_PCT = 2.0  # 2% of balance per trade

# Strategy parameters
LOOKBACK_PERIOD = 20  # Number of candles to identify support/resistance levels
