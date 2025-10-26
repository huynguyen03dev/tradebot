from datetime import datetime, timedelta
import MetaTrader5 as mt5
import pandas as pd
import pytz

if not mt5.initialize():
    print("initialize() failed, error code =", mt5.last_error())
    quit()

account = 10008099775
password = "U_C0GfOs"
server = "MetaQuotes-Demo"

authorized = mt5.login(account, password=password, server=server)
if not authorized:
    print("Login failed, error code =", mt5.last_error())
    mt5.shutdown()
    quit()

print("Logged in successfully!")

timezone = pytz.timezone("Etc/UTC")
today = datetime.now(timezone).replace(hour=0, minute=0, second=0, microsecond=0)

rates = mt5.copy_rates_from("AUDUSD", mt5.TIMEFRAME_D1, today, 1)

if rates is None:
    print("Failed to get rates, error code =", mt5.last_error())
else:
    df = pd.DataFrame(rates)
    df['time'] = pd.to_datetime(df['time'], unit='s')
    print("\nToday's AUDUSD Chart:")
    print(df)

mt5.shutdown()
