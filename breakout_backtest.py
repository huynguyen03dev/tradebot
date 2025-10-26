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
import os

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


# ============================================================================
# MT5 CONNECTION AND DATA RETRIEVAL
# ============================================================================

def initialize_mt5():
    """
    Initialize connection to MetaTrader 5.
    
    Returns:
        bool: True if initialization successful, False otherwise
    """
    if not mt5.initialize():
        print(f"ERROR: MT5 initialization failed, error code = {mt5.last_error()}")
        return False
    
    print("MT5 initialized successfully")
    return True


def login_mt5(account=None, password=None, server=None):
    """
    Login to MetaTrader 5 account.
    
    Credentials can be provided via parameters or environment variables:
    - MT5_ACCOUNT, MT5_PASSWORD, MT5_SERVER
    
    Args:
        account (int, optional): MT5 account number
        password (str, optional): MT5 account password
        server (str, optional): MT5 server name
    
    Returns:
        bool: True if login successful, False otherwise
    """
    # Try to get credentials from parameters or environment variables
    account = account or os.getenv('MT5_ACCOUNT')
    password = password or os.getenv('MT5_PASSWORD')
    server = server or os.getenv('MT5_SERVER')
    
    # Check if credentials are provided
    if not all([account, password, server]):
        print("ERROR: MT5 credentials not provided. Set MT5_ACCOUNT, MT5_PASSWORD, MT5_SERVER environment variables or pass as parameters.")
        return False
    
    # Convert account to int if it's a string
    if isinstance(account, str):
        account = int(account)
    
    # Attempt login
    authorized = mt5.login(account, password=password, server=server)
    if not authorized:
        print(f"ERROR: MT5 login failed, error code = {mt5.last_error()}")
        return False
    
    print(f"Logged in successfully to account {account} on server {server}")
    return True


def validate_symbol(symbol):
    """
    Validate that the specified symbol is available in MT5.
    
    Args:
        symbol (str): Symbol name to validate (e.g., "AUDUSD")
    
    Returns:
        bool: True if symbol is available, False otherwise
    """
    # Try to select the symbol
    selected = mt5.symbol_select(symbol, True)
    if not selected:
        print(f"ERROR: Failed to select symbol {symbol}, error code = {mt5.last_error()}")
        return False
    
    # Get symbol info to verify it's available
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(f"ERROR: Symbol {symbol} not found")
        return False
    
    if not symbol_info.visible:
        print(f"ERROR: Symbol {symbol} is not visible in Market Watch")
        return False
    
    print(f"Symbol {symbol} validated successfully")
    return True


def fetch_historical_data(symbol, timeframe, start_date, end_date):
    """
    Fetch historical candlestick data from MT5 and convert to pandas DataFrame.
    
    Args:
        symbol (str): Trading symbol (e.g., "AUDUSD")
        timeframe: MT5 timeframe constant (e.g., mt5.TIMEFRAME_M5)
        start_date (datetime): Start date for historical data (timezone-aware)
        end_date (datetime): End date for historical data (timezone-aware)
    
    Returns:
        pd.DataFrame: DataFrame with columns [time, open, high, low, close, tick_volume, spread, real_volume]
                      Returns None if fetch fails
    """
    # Fetch rates using copy_rates_range
    rates = mt5.copy_rates_range(symbol, timeframe, start_date, end_date)
    
    if rates is None:
        print(f"ERROR: Failed to fetch rates for {symbol}, error code = {mt5.last_error()}")
        return None
    
    if len(rates) == 0:
        print(f"ERROR: No data returned for {symbol} between {start_date} and {end_date}")
        return None
    
    # Convert to DataFrame
    df = pd.DataFrame(rates)
    
    # Convert time from Unix timestamp to datetime
    df['time'] = pd.to_datetime(df['time'], unit='s')
    
    print(f"Successfully fetched {len(df)} candles for {symbol} from {df['time'].iloc[0]} to {df['time'].iloc[-1]}")
    
    return df


def validate_date_range(start_date, end_date):
    """
    Validate that the date range is valid for backtesting.
    
    Args:
        start_date (datetime): Start date
        end_date (datetime): End date
    
    Returns:
        bool: True if date range is valid, False otherwise
    """
    if start_date >= end_date:
        print(f"ERROR: Start date ({start_date}) must be before end date ({end_date})")
        return False
    
    # Check if dates are in the future
    now = datetime.now(pytz.UTC)
    if start_date > now:
        print(f"ERROR: Start date ({start_date}) is in the future")
        return False
    
    if end_date > now:
        print(f"WARNING: End date ({end_date}) is in the future, adjusting to current time")
    
    print(f"Date range validated: {start_date} to {end_date}")
    return True


def shutdown_mt5():
    """
    Shutdown MT5 connection.
    Should be called at the end of script execution.
    """
    mt5.shutdown()
    print("MT5 connection closed")
