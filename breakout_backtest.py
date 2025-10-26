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


class Backtester:
    """
    Backtesting engine that simulates trading strategy on historical data.
    
    The backtester runs through historical price data, generates trading signals
    using the provided strategy, executes simulated trades, and tracks performance.
    
    Attributes:
        strategy (BreakoutStrategy): The trading strategy to backtest
        data (pd.DataFrame): Historical price data with OHLC columns
        starting_balance (float): Initial account balance in USD
        position_size_pct (float): Percentage of balance to risk per trade
        balance (float): Current account balance
        trades (list): List of completed Trade objects
        current_trade (Trade): Currently open trade (None if no open position)
    """
    
    def __init__(self, strategy, data, starting_balance=10000.0, position_size_pct=2.0):
        """
        Initialize the backtester.
        
        Args:
            strategy (BreakoutStrategy): Trading strategy instance to use for signal generation
            data (pd.DataFrame): Historical price data with columns: time, open, high, low, close
            starting_balance (float): Initial account balance in USD (default 10000.0)
            position_size_pct (float): Percentage of balance to use per trade (default 2.0%)
        """
        self.strategy = strategy
        self.data = data
        self.starting_balance = starting_balance
        self.position_size_pct = position_size_pct
        self.balance = starting_balance
        self.trades = []
        self.current_trade = None
    
    def is_in_position(self):
        """
        Check if currently in an open position.
        
        Returns:
            bool: True if there's an open trade, False otherwise
        """
        return self.current_trade is not None
    
    def enter_trade(self, entry_time, entry_price, direction):
        """
        Enter a new trade by creating a Trade object.
        
        Calculates position size based on the configured percentage of current balance
        and the entry price. Position size represents the amount in USD to trade.
        
        Args:
            entry_time (datetime): Timestamp when entering the trade
            entry_price (float): Price at which to enter the trade
            direction (str): Trade direction, either "BUY" or "SELL"
        """
        # Calculate position size in USD based on percentage of balance
        position_size_usd = self.balance * (self.position_size_pct / 100.0)
        
        # For forex, position size is typically in units of the base currency
        # Position size = USD amount / price
        position_size = position_size_usd / entry_price
        
        # Create new trade
        self.current_trade = Trade(entry_time, entry_price, direction, position_size)
        
        print(f"  ENTRY: {direction} at {entry_price:.5f} | Position: ${position_size_usd:.2f} ({position_size:.2f} units) | Time: {entry_time}")
    
    def exit_trade(self, exit_time, exit_price):
        """
        Exit the current open trade and update balance.
        
        Closes the trade at the specified price, calculates P/L, updates balance,
        and adds the completed trade to the trades list.
        
        Args:
            exit_time (datetime): Timestamp when exiting the trade
            exit_price (float): Price at which to exit the trade
        """
        if self.current_trade is None:
            print("ERROR: Attempted to exit trade when no position is open")
            return
        
        # Close the trade and calculate P/L
        self.current_trade.close(exit_time, exit_price)
        
        # Update balance with profit/loss
        self.balance += self.current_trade.profit_loss
        
        # Add to completed trades list
        self.trades.append(self.current_trade)
        
        # Print exit information
        pl_str = f"+${self.current_trade.profit_loss:.2f}" if self.current_trade.profit_loss >= 0 else f"-${abs(self.current_trade.profit_loss):.2f}"
        print(f"  EXIT:  {self.current_trade.direction} at {exit_price:.5f} | P/L: {pl_str} | Balance: ${self.balance:.2f} | Time: {exit_time}")
        
        # Clear current trade
        self.current_trade = None
    
    def run(self):
        """
        Run the backtest by iterating through all historical candles.
        
        For each candle:
        1. Generate trading signal from strategy
        2. Execute entry if signal received and not in position
        3. Execute exit if opposite signal received while in position
        4. Track all completed trades
        
        Returns:
            list: List of completed Trade objects
        """
        print(f"Starting backtest with {len(self.data)} candles...")
        print(f"Initial balance: ${self.starting_balance:,.2f}")
        print(f"Position size: {self.position_size_pct}% of balance")
        print("-" * 60)
        
        # Iterate through each candle in the historical data
        for i in range(len(self.data)):
            # Show progress indicator every 500 candles
            if i > 0 and i % 500 == 0:
                print(f"Processing candle {i}/{len(self.data)}...")
            
            # Check if we're currently in a position
            in_position = self.is_in_position()
            
            # Generate signal from strategy
            signal = self.strategy.generate_signal(self.data, i, in_position)
            
            # Get current candle data
            candle = self.data.iloc[i]
            current_time = candle['time']
            current_close = candle['close']
            
            # Trade entry logic: if signal received and not in position, enter trade
            if signal is not None and not in_position:
                self.enter_trade(current_time, current_close, signal)
            
            # Trade exit logic: exit on opposite signal
            # If in position and receive opposite signal, close the trade
            elif in_position and signal is not None:
                # Check if signal is opposite to current trade direction
                if (self.current_trade.direction == "BUY" and signal == "SELL") or \
                   (self.current_trade.direction == "SELL" and signal == "BUY"):
                    self.exit_trade(current_time, current_close)
        
        # Handle edge case: if trade is still open at end, force close at last price
        if self.is_in_position():
            last_candle = self.data.iloc[-1]
            print(f"\n  Closing final open trade at last price...")
            self.exit_trade(last_candle['time'], last_candle['close'])
        
        print("-" * 60)
        print(f"Backtest complete. Processed {len(self.data)} candles.")
        print(f"Total trades executed: {len(self.trades)}")
        
        return self.trades
    
    def calculate_total_trades(self):
        """
        Calculate the total number of trades executed.
        
        Returns:
            int: Total number of trades
        """
        return len(self.trades)
    
    def calculate_winning_losing_trades(self):
        """
        Calculate the number of winning and losing trades.
        
        A winning trade has profit_loss > 0, a losing trade has profit_loss <= 0.
        
        Returns:
            tuple: (winning_trades, losing_trades) as integers
        """
        winning_trades = sum(1 for trade in self.trades if trade.profit_loss > 0)
        losing_trades = sum(1 for trade in self.trades if trade.profit_loss <= 0)
        return winning_trades, losing_trades
    
    def calculate_winrate(self):
        """
        Calculate the winrate percentage.
        
        Winrate = (winning trades / total trades) * 100
        Returns 0.0 if no trades were executed.
        
        Returns:
            float: Winrate percentage (0-100)
        """
        total_trades = self.calculate_total_trades()
        if total_trades == 0:
            return 0.0
        
        winning_trades, _ = self.calculate_winning_losing_trades()
        return (winning_trades / total_trades) * 100.0
    
    def calculate_total_profit_loss(self):
        """
        Calculate the total profit/loss across all trades.
        
        Returns:
            float: Total profit/loss in USD
        """
        return sum(trade.profit_loss for trade in self.trades)
    
    def calculate_net_return(self):
        """
        Calculate the net return percentage.
        
        Net return = (total P/L / starting balance) * 100
        Returns 0.0 if starting balance is 0.
        
        Returns:
            float: Net return percentage
        """
        if self.starting_balance == 0:
            return 0.0
        
        total_pl = self.calculate_total_profit_loss()
        return (total_pl / self.starting_balance) * 100.0
    
    def print_results(self):
        """
        Display comprehensive backtest results in formatted console output.
        
        Includes:
        - Backtest period (start and end dates)
        - Total trades executed
        - Winning and losing trades breakdown
        - Winrate percentage
        - Total profit/loss in USD
        - Final balance
        - Net return percentage
        
        Handles zero trades scenario gracefully by displaying appropriate message.
        """
        print("\n")
        print("=" * 60)
        print("BACKTEST RESULTS")
        print("=" * 60)
        
        # Backtest period
        start_date = self.data.iloc[0]['time']
        end_date = self.data.iloc[-1]['time']
        print(f"\nBacktest Period:")
        print(f"  Start: {start_date}")
        print(f"  End:   {end_date}")
        
        # Check for zero trades scenario
        total_trades = self.calculate_total_trades()
        if total_trades == 0:
            print(f"\nNo trades executed during backtest period.")
            print(f"No breakout signals were detected with current strategy parameters.")
            print(f"\nStarting Balance: ${self.starting_balance:,.2f}")
            print(f"Final Balance:    ${self.balance:,.2f}")
            print("=" * 60)
            return
        
        # Trade statistics
        winning_trades, losing_trades = self.calculate_winning_losing_trades()
        winrate = self.calculate_winrate()
        
        print(f"\nTrade Statistics:")
        print(f"  Total Trades:   {total_trades}")
        print(f"  Winning Trades: {winning_trades}")
        print(f"  Losing Trades:  {losing_trades}")
        print(f"  Winrate:        {winrate:.2f}%")
        
        # Financial results
        total_pl = self.calculate_total_profit_loss()
        net_return = self.calculate_net_return()
        
        print(f"\nFinancial Results:")
        print(f"  Starting Balance: ${self.starting_balance:,.2f}")
        print(f"  Final Balance:    ${self.balance:,.2f}")
        print(f"  Total P/L:        ${total_pl:,.2f}")
        print(f"  Net Return:       {net_return:+.2f}%")
        
        print("=" * 60)


# ============================================================================
# MAIN EXECUTION
# ============================================================================

def main():
    """
    Main execution function that orchestrates the entire backtest workflow.
    
    Steps:
    1. Initialize MT5 connection
    2. Login to MT5 account (optional - requires credentials)
    3. Validate symbol availability
    4. Validate date range
    5. Fetch historical data
    6. Create strategy instance
    7. Create backtester instance
    8. Run backtest
    9. Display results
    10. Shutdown MT5 connection
    
    All steps include proper error handling with try-except-finally to ensure
    MT5 connection is always closed properly.
    """
    try:
        # Step 1: Initialize MT5
        print("Initializing MetaTrader 5...")
        if not initialize_mt5():
            return
        
        # Step 2: Login (optional - comment out if using terminal's default account)
        # Uncomment the following lines if you want to login to a specific account:
        # if not login_mt5():
        #     return
        
        # Step 3: Validate symbol
        print(f"\nValidating symbol {SYMBOL}...")
        if not validate_symbol(SYMBOL):
            return
        
        # Step 4: Validate date range
        print(f"\nValidating date range...")
        if not validate_date_range(START_DATE, END_DATE):
            return
        
        # Step 5: Fetch historical data
        print(f"\nFetching historical data for {SYMBOL}...")
        data = fetch_historical_data(SYMBOL, TIMEFRAME, START_DATE, END_DATE)
        if data is None:
            return
        
        # Step 6: Create strategy instance
        print(f"\nCreating breakout strategy (lookback period: {LOOKBACK_PERIOD})...")
        strategy = BreakoutStrategy(lookback_period=LOOKBACK_PERIOD)
        
        # Step 7: Create backtester instance
        print(f"Creating backtester...")
        backtester = Backtester(
            strategy=strategy,
            data=data,
            starting_balance=STARTING_BALANCE,
            position_size_pct=POSITION_SIZE_PCT
        )
        
        # Step 8: Run backtest
        print("\n" + "=" * 60)
        print("RUNNING BACKTEST")
        print("=" * 60 + "\n")
        trades = backtester.run()
        
        # Step 9: Display results
        backtester.print_results()
        
    except Exception as e:
        print(f"\nERROR: An unexpected error occurred during backtest execution:")
        print(f"  {type(e).__name__}: {e}")
        import traceback
        traceback.print_exc()
    
    finally:
        # Step 10: Always shutdown MT5 connection
        print("\nShutting down MT5 connection...")
        shutdown_mt5()


if __name__ == "__main__":
    main()

