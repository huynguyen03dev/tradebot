[](https://www.mql5.com "MQL5 - Language of trade strategies built-in the
MetaTrader 5 client terminal")

  * [Forum](/en/forum)
  * [Market](/en/market)
  * [Signals](/en/signals)
  * [Freelance](/en/job)
  * [VPS](/en/vps)
  * [Quotes](/en/quotes/overview)

  * [![](https://c.mql5.com/i/menu/icon-articles4.svg)Articles](/en/articles)
  * [![](https://c.mql5.com/i/menu/icon-code4.svg)CodeBase](/en/code)
  * [![](https://c.mql5.com/i/menu/icon-algoforge4.svg)Algo Forge](https://forge.mql5.io/?lang=en)
  * [![](https://c.mql5.com/i/menu/icon-docs4.svg)Documentation](/en/docs)
  * [![](https://c.mql5.com/i/menu/icon-book4.svg)AlgoBook](/en/book)
  * [![](https://c.mql5.com/i/menu/icon-neurobook4.svg)NeuroBook](/en/neurobook)
  * [![](https://c.mql5.com/i/menu/icon-economic-calendar4.svg)Calendar](/en/economic-calendar)
  * [![](https://c.mql5.com/i/menu/icon-trading4.svg)WebTerminal](https://web.metatrader.app/terminal?mode=demo&lang=en)
  * [About](/en/about)
  * [![](https://c.mql5.com/i/sidebar/tg.svg)Algo Trading Channel](https://t.me/mql5dev "Follow us on socials for top articles and CodeBase updates")

DocumentationSections

Type / to search: @user, $symbol, ...

  * [Log in](https://www.mql5.com/en/auth_login "Please sign in. OpenID supported")
  * [Create an account](https://www.mql5.com/en/auth_register "Please register")

__

  * [__English](/en/docs/python_metatrader5/mt5copyratesfrom_py)
  * [__Русский](/ru/docs/python_metatrader5/mt5copyratesfrom_py)
  * [__中文](/zh/docs/python_metatrader5/mt5copyratesfrom_py)
  * [__Español](/es/docs/python_metatrader5/mt5copyratesfrom_py)
  * [__Português](/pt/docs/python_metatrader5/mt5copyratesfrom_py)
  * [__日本語](/ja/docs/python_metatrader5/mt5copyratesfrom_py)
  * [__Deutsch](/de/docs/python_metatrader5/mt5copyratesfrom_py)
  * [__한국어](/ko/docs/python_metatrader5/mt5copyratesfrom_py)
  * [__Français](/fr/docs/python_metatrader5/mt5copyratesfrom_py)
  * [__Italiano](/it/docs/python_metatrader5/mt5copyratesfrom_py)
  * [__Türkçe](/tr/docs/python_metatrader5/mt5copyratesfrom_py)

[MQL5 Reference](/en/docs "MQL5 Reference")[Python
Integration](/en/docs/python_metatrader5 "Python Integration")copy_rates_from

  * [initialize](/en/docs/python_metatrader5/mt5initialize_py "initialize")
  * [login](/en/docs/python_metatrader5/mt5login_py "login")
  * [shutdown](/en/docs/python_metatrader5/mt5shutdown_py "shutdown")
  * [version](/en/docs/python_metatrader5/mt5version_py "version")
  * [last_error](/en/docs/python_metatrader5/mt5lasterror_py "last_error")
  * [account_info](/en/docs/python_metatrader5/mt5accountinfo_py "account_info")
  * [terminal_info](/en/docs/python_metatrader5/mt5terminalinfo_py "terminal_info")
  * [symbols_total](/en/docs/python_metatrader5/mt5symbolstotal_py "symbols_total")
  * [symbols_get](/en/docs/python_metatrader5/mt5symbolsget_py "symbols_get")
  * [symbol_info](/en/docs/python_metatrader5/mt5symbolinfo_py "symbol_info")
  * [symbol_info_tick](/en/docs/python_metatrader5/mt5symbolinfotick_py "symbol_info_tick")
  * [symbol_select](/en/docs/python_metatrader5/mt5symbolselect_py "symbol_select")
  * [market_book_add](/en/docs/python_metatrader5/mt5marketbookadd_py "market_book_add")
  * [market_book_get](/en/docs/python_metatrader5/mt5marketbookget_py "market_book_get")
  * [market_book_release](/en/docs/python_metatrader5/mt5marketbookrelease_py "market_book_release")
  * copy_rates_from
  * [copy_rates_from_pos](/en/docs/python_metatrader5/mt5copyratesfrompos_py "copy_rates_from_pos")
  * [copy_rates_range](/en/docs/python_metatrader5/mt5copyratesrange_py "copy_rates_range")
  * [copy_ticks_from](/en/docs/python_metatrader5/mt5copyticksfrom_py "copy_ticks_from")
  * [copy_ticks_range](/en/docs/python_metatrader5/mt5copyticksrange_py "copy_ticks_range")
  * [orders_total](/en/docs/python_metatrader5/mt5orderstotal_py "orders_total")
  * [orders_get](/en/docs/python_metatrader5/mt5ordersget_py "orders_get")
  * [order_calc_margin](/en/docs/python_metatrader5/mt5ordercalcmargin_py "order_calc_margin")
  * [order_calc_profit](/en/docs/python_metatrader5/mt5ordercalcprofit_py "order_calc_profit")
  * [order_check](/en/docs/python_metatrader5/mt5ordercheck_py "order_check")
  * [order_send](/en/docs/python_metatrader5/mt5ordersend_py "order_send")
  * [positions_total](/en/docs/python_metatrader5/mt5positionstotal_py "positions_total")
  * [positions_get](/en/docs/python_metatrader5/mt5positionsget_py "positions_get")
  * [history_orders_total](/en/docs/python_metatrader5/mt5historyorderstotal_py "history_orders_total")
  * [history_orders_get](/en/docs/python_metatrader5/mt5historyordersget_py "history_orders_get")
  * [history_deals_total](/en/docs/python_metatrader5/mt5historydealstotal_py "history_deals_total")
  * [history_deals_get](/en/docs/python_metatrader5/mt5historydealsget_py "history_deals_get")

# copy_rates_from

Get bars from the MetaTrader 5 terminal starting from the specified date.

copy_rates_from(  
   symbol,       // symbol name  
   timeframe,    // timeframe  
   date_from,    // initial bar open date  
   count         // number of bars  
   )  
---  
  
Parameters

symbol

[in]  Financial instrument name, for example, "EURUSD". Required unnamed
parameter.

timeframe

[in]  Timeframe the bars are requested for. Set by a value from the
[TIMEFRAME](/en/docs/python_metatrader5/mt5copyratesfrom_py#timeframe)
enumeration. Required unnamed parameter.

date_from

[in]  Date of opening of the first bar from the requested sample. Set by the
'datetime' object or as a number of seconds elapsed since 1970.01.01. Required
unnamed parameter.

count

[in]  Number of bars to receive. Required unnamed parameter.

Return Value

Returns bars as the numpy array with the named time, open, high, low, close,
tick_volume, spread and real_volume columns. Return None in case of an error.
The info on the error can be obtained using
[last_error()](/en/docs/python_metatrader5/mt5lasterror_py).

Note

See the [CopyRates()](/en/docs/series/copyrates) function for more
information.

Only data whose date is less than (earlier) or equal to the date specified
will be returned. It means, the open time of any bar is always less or equal
to the specified one.

MetaTrader 5 terminal provides bars only within a history available to a user
on charts. The number of bars available to users is set in the "[Max. bars in
chart](https://www.metatrader5.com/en/terminal/help/startworking/settings#max_bars)"
parameter.

When creating the 'datetime' object, Python uses the local time zone, while
MetaTrader 5 stores tick and bar open time in UTC time zone (without the
shift). Therefore, 'datetime' should be created in UTC time for executing
functions that use time. Data received from the MetaTrader 5 terminal has UTC
time.  

TIMEFRAME is an enumeration with possible chart period values

ID | Description  
---|---  
TIMEFRAME_M1 | 1 minute  
TIMEFRAME_M2 | 2 minutes  
TIMEFRAME_M3 | 3 minutes  
TIMEFRAME_M4 | 4 minutes  
TIMEFRAME_M5 | 5 minutes  
TIMEFRAME_M6 | 6 minutes  
TIMEFRAME_M10 | 10 minutes  
TIMEFRAME_M12 | 12 minutes  
TIMEFRAME_M12 | 15 minutes  
TIMEFRAME_M20 | 20 minutes  
TIMEFRAME_M30 | 30 minutes  
TIMEFRAME_H1 | 1 hour  
TIMEFRAME_H2 | 2 hours  
TIMEFRAME_H3 | 3 hours  
TIMEFRAME_H4 | 4 hours  
TIMEFRAME_H6 | 6 hours  
TIMEFRAME_H8 | 8 hours  
TIMEFRAME_H12 | 12 hours  
TIMEFRAME_D1 | 1 day  
TIMEFRAME_W1 | 1 week  
TIMEFRAME_MN1 | 1 month  
  


Example:

from datetime import datetime  
import MetaTrader5 as mt5  
# display data on the MetaTrader 5 package  
print("MetaTrader5 package author: ",mt5.__author__)  
print("MetaTrader5 package version: ",mt5.__version__)  
    
# import the 'pandas' module for displaying data obtained in the tabular form  
import pandas as pd  
pd.set_option('display.max_columns', 500) # number of columns to be displayed  
pd.set_option('display.width', 1500)      # max table width to display  
# import pytz module for working with time zone  
import pytz  
    
# establish connection to MetaTrader 5 terminal  
if not mt5.initialize():  
    print("initialize() failed, error code =",mt5.last_error())   
    quit()   
    
# set time zone to UTC  
timezone = pytz.timezone("Etc/UTC")  
# create 'datetime' object in UTC time zone to avoid the implementation of a
local time zone offset  
utc_from = datetime(2020, 1, 10, tzinfo=timezone)  
# get 10 EURUSD H4 bars starting from 01.10.2020 in UTC time zone  
rates = mt5.copy_rates_from("EURUSD", mt5.TIMEFRAME_H4, utc_from, 10)  
    
# shut down connection to the MetaTrader 5 terminal  
mt5.shutdown()  
# display each element of obtained data in a new line  
print("Display obtained data 'as is'")  
for rate in rates:  
    print(rate)   
    
# create DataFrame out of the obtained data  
rates_frame = pd.DataFrame(rates)  
# convert time in seconds into the datetime format  
rates_frame['time']=pd.to_datetime(rates_frame['time'], unit='s')  
                              
# display data  
print("\nDisplay dataframe with data")  
print(rates_frame)  
    
    
Result:  
MetaTrader5 package author:  MetaQuotes Software Corp.  
MetaTrader5 package version:  5.0.29  
    
Display obtained data 'as is'  
(1578484800, 1.11382, 1.11385, 1.1111, 1.11199, 9354, 1, 0)  
(1578499200, 1.11199, 1.11308, 1.11086, 1.11179, 10641, 1, 0)  
(1578513600, 1.11178, 1.11178, 1.11016, 1.11053, 4806, 1, 0)  
(1578528000, 1.11053, 1.11193, 1.11033, 1.11173, 3480, 1, 0)  
(1578542400, 1.11173, 1.11189, 1.11126, 1.11182, 2236, 1, 0)  
(1578556800, 1.11181, 1.11203, 1.10983, 1.10993, 7984, 1, 0)  
(1578571200, 1.10994, 1.11173, 1.10965, 1.11148, 7406, 1, 0)  
(1578585600, 1.11149, 1.11149, 1.10923, 1.11046, 7468, 1, 0)  
(1578600000, 1.11046, 1.11097, 1.11033, 1.11051, 3450, 1, 0)  
(1578614400, 1.11051, 1.11093, 1.11017, 1.11041, 2448, 1, 0)  
    
Display dataframe with data  
                 time     open     high      low    close  tick_volume  spread  real_volume   
0 2020-01-08 12:00:00  1.11382  1.11385  1.11110  1.11199         9354       1
0  
1 2020-01-08 16:00:00  1.11199  1.11308  1.11086  1.11179        10641       1
0  
2 2020-01-08 20:00:00  1.11178  1.11178  1.11016  1.11053         4806       1
0  
3 2020-01-09 00:00:00  1.11053  1.11193  1.11033  1.11173         3480       1
0  
4 2020-01-09 04:00:00  1.11173  1.11189  1.11126  1.11182         2236       1
0  
5 2020-01-09 08:00:00  1.11181  1.11203  1.10983  1.10993         7984       1
0  
6 2020-01-09 12:00:00  1.10994  1.11173  1.10965  1.11148         7406       1
0  
7 2020-01-09 16:00:00  1.11149  1.11149  1.10923  1.11046         7468       1
0  
8 2020-01-09 20:00:00  1.11046  1.11097  1.11033  1.11051         3450       1
0  
9 2020-01-10 00:00:00  1.11051  1.11093  1.11017  1.11041         2448       1
0  
---  
  
See also

[CopyRates](/en/docs/series/copyrates),
[copy_rates_from_pos](/en/docs/python_metatrader5/mt5copyratesfrompos_py),
[copy_rates_range](/en/docs/python_metatrader5/mt5copyratesrange_py),
[copy_ticks_from](/en/docs/python_metatrader5/mt5copyticksfrom_py),
[copy_ticks_range](/en/docs/python_metatrader5/mt5copyticksrange_py)

[market_book_release](/en/docs/python_metatrader5/mt5marketbookrelease_py
"market_book_release")

[copy_rates_from_pos](/en/docs/python_metatrader5/mt5copyratesfrompos_py
"copy_rates_from_pos")

  * **MQL5.community**
    * [Online trading / WebTerminal](https://web.metatrader.app/terminal?mode=demo&lang=en)
    * [Free technical indicators and robots](/en/code)
    * [Articles about programming and trading](/en/articles)
    * [Order trading robots on the Freelance](/en/job)
    * [Market of Expert Advisors and applications ](/en/market)
    * [Follow forex signals](/en/signals)
    * [Low latency forex VPS](/en/vps)
    * [Traders forum](/en/forum)
    * [Trading blogs](/en/blogs)
    * [Charts](/en/charts)
  * **MetaTrader 5**
    * [MetaTrader 5 Trading Platform](https://www.metatrader5.com)
    * [MetaTrader 5 latest updates](https://www.metatrader5.com/en/releasenotes)
    * [News, implementations and technology](https://www.metatrader5.com/en/news)
    * [MetaTrader 5 User Manual](https://www.metatrader5.com/en/terminal/help)
    * [MQL5 language of trading strategies](/en/docs)
    * [MQL5 Cloud Network](https://cloud.mql5.com)
    * [MQL5 Algo Forge](https://forge.mql5.io/?lang=en)
    * [Download MetaTrader 5](https://download.mql5.com/cdn/web/metaquotes.ltd/mt5/mt5setup.exe?utm_source=www.mql5.com&utm_campaign=download)
    * [Install Platform](https://www.metatrader5.com/en/terminal/help/start_advanced/installation)
    * [Uninstall Platform](https://www.metatrader5.com/en/terminal/help/start_advanced/deinstallation)
  * **Website**
    * [About](/en/about)
    * [Timeline](/en/wall)
    * [Terms and Conditions](/en/about/terms)
    * [Recurring Payment Agreement](/en/about/autopayments)
    * [Agency Agreement – Offer](/en/about/agencyagreement)
    * [Privacy and Data Protection Policy](/en/about/privacy)
    * [Cookies Policy](/en/about/cookies)
    * [Contacts and requests](/en/contact)
  * [MetaTrader 5](https://www.metatrader5.com)

[Download MetaTrader 5 for
Windows](https://download.mql5.com/cdn/web/metaquotes.ltd/mt5/mt5setup.exe?utm_source=www.mql5.com&utm_campaign=download)
[Download MetaTrader 5 for
MacOS](https://download.mql5.com/cdn/web/metaquotes.ltd/mt5/MetaTrader5.pkg.zip?utm_source=www.mql5.com&utm_campaign=download)
[Download MetaTrader 5 for
Linux](https://www.mql5.com/en/articles/625?utm_source=www.mql5.com&utm_campaign=download)
[Open MetaTrader 5
WebTerminal](https://web.metatrader.app/terminal?mode=demo&lang=en) [Scan to
install from App
Store](https://download.mql5.com/cdn/mobile/mt5/ios?utm_source=www.mql5.com&utm_campaign=install.metaquotes&hl=en)
[Scan to install from Google
Play](https://download.mql5.com/cdn/mobile/mt5/android?utm_source=www.mql5.com&utm_campaign=install.metaquotes&hl=en)
[Scan to install from Huawei
AppGallery](https://download.mql5.com/cdn/mobile/mt5/android/app-
gallery?utm_source=www.mql5.com&utm_campaign=install.metaquotes) [Scan to get
Android APK
file](https://download.mql5.com/cdn/web/metaquotes.software.corp/mt5/metatrader5.apk?utm_source=www.mql5.com&utm_campaign=install.metaquotes)

[MQL5 Channels](https://www.metatrader5.com/en/news/2270)

[Scan to install from App
Store](https://download.mql5.com/cdn/mobile/mql5.channels/ios?utm_source=www.mql5.com&utm_campaign=download&hl=en)
[Scan to install from Google
Play](https://download.mql5.com/cdn/mobile/mql5.channels/android?utm_source=www.mql5.com&utm_campaign=download&hl=en)
[Scan to install from Huawei
AppGallery](https://download.mql5.com/cdn/mobile/mql5.channels/android/app-
gallery?utm_source=www.mql5.com&utm_campaign=download) [Scan to get Android
APK
file](https://download.mql5.com/cdn/web/metaquotes.software.corp/mql5channels/mql5channels.apk?utm_source=www.mql5.com&utm_campaign=download)

[Economic
Calendar](https://www.tradays.com/en/download?utm_source=www.mql5.com&utm_campaign=download)

[Scan to install from App
Store](https://download.mql5.com/cdn/mobile/tradays/ios?utm_source=www.mql5.com&utm_campaign=download&hl=en)
[Scan to install from Google
Play](https://download.mql5.com/cdn/mobile/tradays/android?utm_source=www.mql5.com&utm_campaign=download&hl=en)
[Scan to install from Huawei
AppGallery](https://download.mql5.com/cdn/mobile/tradays/android/app-
gallery?utm_source=www.mql5.com&utm_campaign=download) [Scan to get Android
APK
file](https://download.mql5.com/cdn/web/metaquotes.software.corp/tradays/tradays.apk?utm_source=www.mql5.com&utm_campaign=download)

[__](https://www.facebook.com/mql5.community/
"Facebook")[__](https://t.me/mql5dev "Telegram")[__](https://x.com/mql5com "X
\(Twitter\)")

Follow us on socials for top articles and CodeBase updates

Not a broker, no real trading accounts

35 Dodekanisou str, Germasogeia, 4043, Limassol, Cyprus

Copyright 2000-2025, MetaQuotes Ltd

