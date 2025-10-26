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


# ============================================================================
# TRADING CLASSES
# ============================================================================

class Trade:
    """
    Represents a single trade with entry and exit information.
    
    Attributes:
        entry_time (datetime): Timestamp when trade was entered
        entry_price (float): Price at which trade was entered
        exit_time (datetime): Timestamp when trade was exited (None if still open)
        exit_price (float): Price at which trade was exited (None if still open)
        direction (str): Trade direction, either "BUY" or "SELL"
        position_size (float): Size of the position in lots/units
        profit_loss (float): Profit or loss in USD (None until trade is closed)
    """
    
    def __init__(self, entry_time, entry_price, direction, position_size):
        """
        Initialize a new trade.
        
        Args:
            entry_time (datetime): Timestamp when trade was entered
            entry_price (float): Price at which trade was entered
            direction (str): Trade direction, either "BUY" or "SELL"
            position_size (float): Size of the position in lots/units
        """
        self.entry_time = entry_time
        self.entry_price = entry_price
        self.exit_time = None
        self.exit_price = None
        self.direction = direction
        self.position_size = position_size
        self.profit_loss = None
    
    def close(self, exit_time, exit_price):
        """
        Close the trade and calculate profit/loss.
        
        Args:
            exit_time (datetime): Timestamp when trade was exited
            exit_price (float): Price at which trade was exited
        """
        self.exit_time = exit_time
        self.exit_price = exit_price
        
        # Calculate P/L based on direction
        if self.direction == "BUY":
            # BUY: profit when price goes up
            self.profit_loss = (exit_price - self.entry_price) * self.position_size
        elif self.direction == "SELL":
            # SELL: profit when price goes down
            self.profit_loss = (self.entry_price - exit_price) * self.position_size
        else:
            raise ValueError(f"Invalid trade direction: {self.direction}")
    
    def is_open(self):
        """
        Check if trade is still open.
        
        Returns:
            bool: True if trade is open, False if closed
        """
        return self.exit_time is None


class BreakoutStrategy:
    """
    Breakout trading strategy that identifies support and resistance levels
    and generates trading signals when price breaks through these levels.
    
    The strategy looks back over a configurable period to find the highest high
    (resistance) and lowest low (support). When price closes above resistance,
    a BUY signal is generated. When price closes below support, a SELL signal
    is generated.
    
    Attributes:
        lookback_period (int): Number of candles to use for calculating support/resistance
    """
    
    def __init__(self, lookback_period=20):
        """
        Initialize the breakout strategy.
        
        Args:
            lookback_period (int): Number of candles to look back for support/resistance
                                   Default is 20 candles
        """
        self.lookback_period = lookback_period
    
    def calculate_resistance(self, data, current_index):
        """
        Calculate resistance level as the highest high over the lookback period.
        
        Args:
            data (pd.DataFrame): DataFrame containing price data with 'high' column
            current_index (int): Current candle index in the DataFrame
        
        Returns:
            float: Resistance level (highest high), or None if insufficient data
        """
        # Check if we have enough data for lookback period
        if current_index < self.lookback_period:
            return None
        
        # Get the lookback window (excluding current candle)
        start_index = current_index - self.lookback_period
        end_index = current_index
        
        # Calculate resistance as the highest high in the lookback period
        resistance = data.iloc[start_index:end_index]['high'].max()
        
        return resistance
    
    def calculate_support(self, data, current_index):
        """
        Calculate support level as the lowest low over the lookback period.
        
        Args:
            data (pd.DataFrame): DataFrame containing price data with 'low' column
            current_index (int): Current candle index in the DataFrame
        
        Returns:
            float: Support level (lowest low), or None if insufficient data
        """
        # Check if we have enough data for lookback period
        if current_index < self.lookback_period:
            return None
        
        # Get the lookback window (excluding current candle)
        start_index = current_index - self.lookback_period
        end_index = current_index
        
        # Calculate support as the lowest low in the lookback period
        support = data.iloc[start_index:end_index]['low'].min()
        
        return support
    
    def detect_bullish_breakout(self, data, current_index):
        """
        Detect bullish breakout when close price breaks above resistance level.
        
        A bullish breakout occurs when the current candle's close price is higher
        than the resistance level (highest high over the lookback period).
        
        Args:
            data (pd.DataFrame): DataFrame containing price data with 'close' column
            current_index (int): Current candle index in the DataFrame
        
        Returns:
            bool: True if bullish breakout detected, False otherwise
        """
        # Calculate resistance level
        resistance = self.calculate_resistance(data, current_index)
        
        # If we don't have enough data, no breakout
        if resistance is None:
            return False
        
        # Get current close price
        current_close = data.iloc[current_index]['close']
        
        # Bullish breakout: close price > resistance
        return current_close > resistance
    
    def detect_bearish_breakout(self, data, current_index):
        """
        Detect bearish breakout when close price breaks below support level.
        
        A bearish breakout occurs when the current candle's close price is lower
        than the support level (lowest low over the lookback period).
        
        Args:
            data (pd.DataFrame): DataFrame containing price data with 'close' column
            current_index (int): Current candle index in the DataFrame
        
        Returns:
            bool: True if bearish breakout detected, False otherwise
        """
        # Calculate support level
        support = self.calculate_support(data, current_index)
        
        # If we don't have enough data, no breakout
        if support is None:
            return False
        
        # Get current close price
        current_close = data.iloc[current_index]['close']
        
        # Bearish breakout: close price < support
        return current_close < support
    
    def generate_signal(self, data, current_index, in_position=False):
        """
        Generate trading signal based on breakout detection.
        
        Returns "BUY" on bullish breakout, "SELL" on bearish breakout, or None
        if no signal is generated. Prevents multiple signals while already in a position.
        
        Args:
            data (pd.DataFrame): DataFrame containing price data
            current_index (int): Current candle index in the DataFrame
            in_position (bool): Whether currently in an open position (default False)
        
        Returns:
            str: "BUY", "SELL", or None
        """
        # If already in a position, don't generate new entry signals
        if in_position:
            return None
        
        # Check for bullish breakout
        if self.detect_bullish_breakout(data, current_index):
            return "BUY"
        
        # Check for bearish breakout
        if self.detect_bearish_breakout(data, current_index):
            return "SELL"
        
        # No breakout detected
        return None
