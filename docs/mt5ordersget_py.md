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
  * [![](https://c.mql5.com/i/sidebar/vpstrial2.svg)Start VPS Trial](/en/vps "Reliable trader hosting for uninterrupted operation of robots and instant copying of trades")

DocumentationSections

Type / to search: @user, $symbol, ...

  * [Log in](https://www.mql5.com/en/auth_login "Please sign in. OpenID supported")
  * [Create an account](https://www.mql5.com/en/auth_register "Please register")

__

  * [__English](/en/docs/python_metatrader5/mt5ordersget_py)
  * [__Русский](/ru/docs/python_metatrader5/mt5ordersget_py)
  * [__中文](/zh/docs/python_metatrader5/mt5ordersget_py)
  * [__Español](/es/docs/python_metatrader5/mt5ordersget_py)
  * [__Português](/pt/docs/python_metatrader5/mt5ordersget_py)
  * [__日本語](/ja/docs/python_metatrader5/mt5ordersget_py)
  * [__Deutsch](/de/docs/python_metatrader5/mt5ordersget_py)
  * [__한국어](/ko/docs/python_metatrader5/mt5ordersget_py)
  * [__Français](/fr/docs/python_metatrader5/mt5ordersget_py)
  * [__Italiano](/it/docs/python_metatrader5/mt5ordersget_py)
  * [__Türkçe](/tr/docs/python_metatrader5/mt5ordersget_py)

[MQL5 Reference](/en/docs "MQL5 Reference")[Python
Integration](/en/docs/python_metatrader5 "Python Integration")orders_get

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
  * [copy_rates_from](/en/docs/python_metatrader5/mt5copyratesfrom_py "copy_rates_from")
  * [copy_rates_from_pos](/en/docs/python_metatrader5/mt5copyratesfrompos_py "copy_rates_from_pos")
  * [copy_rates_range](/en/docs/python_metatrader5/mt5copyratesrange_py "copy_rates_range")
  * [copy_ticks_from](/en/docs/python_metatrader5/mt5copyticksfrom_py "copy_ticks_from")
  * [copy_ticks_range](/en/docs/python_metatrader5/mt5copyticksrange_py "copy_ticks_range")
  * [orders_total](/en/docs/python_metatrader5/mt5orderstotal_py "orders_total")
  * orders_get
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

# orders_get

Get active orders with the ability to filter by symbol or ticket. There are
three call options.

Call without parameters. Return active orders on all symbols.

orders_get()  
---  
  
Call specifying a symbol active orders should be received for.

orders_get(  
   symbol="SYMBOL"      // symbol name  
)  
---  
  
Call specifying a group of symbols active orders should be received for.

orders_get(  
   group="GROUP"        // filter for selecting orders for symbols  
)  
---  
  
Call specifying the order ticket.

orders_get(  
   ticket=TICKET        // ticket  
)  
---  
  
symbol="SYMBOL"

[in]  Symbol name. Optional named parameter. If a symbol is specified, the
ticket parameter is ignored.

group="GROUP"

[in]  The filter for arranging a group of necessary symbols. Optional named
parameter. If the group is specified, the function returns only active orders
meeting a specified criteria for a symbol name.

ticket=TICKET

[in]  Order ticket
([ORDER_TICKET](/en/docs/constants/tradingconstants/orderproperties#enum_order_property_integer)).
Optional named parameter.

Return Value

Return info in the form of a named tuple structure (namedtuple). Return None
in case of an error. The info on the error can be obtained using
[last_error()](/en/docs/python_metatrader5/mt5lasterror_py).

Note

The function allows receiving all active orders within one call similar to the
[OrdersTotal](/en/docs/trading/orderstotal) and
[OrderSelect](/en/docs/trading/orderselect) tandem.

The group parameter allows sorting out orders by symbols. '*' can be used at
the beginning and the end of a string.

The group parameter may contain several comma separated conditions. A
condition can be set as a mask using '*'. The logical negation symbol '!' can
be used for an exclusion. All conditions are applied sequentially, which means
conditions of including to a group should be specified first followed by an
exclusion condition. For example, group="*, !EUR" means that orders for all
symbols should be selected first and the ones containing "EUR" in symbol names
should be excluded afterwards.

Example:

import MetaTrader5 as mt5  
import pandas as pd  
pd.set_option('display.max_columns', 500) # number of columns to be displayed  
pd.set_option('display.width', 1500)      # max table width to display  
# display data on the MetaTrader 5 package  
print("MetaTrader5 package author: ",mt5.__author__)  
print("MetaTrader5 package version: ",mt5.__version__)  
print()  
# establish connection to the MetaTrader 5 terminal  
if not mt5.initialize():  
    print("initialize() failed, error code =",mt5.last_error())   
    quit()   
    
# display data on active orders on GBPUSD  
orders=mt5.orders_get(symbol="GBPUSD")  
if orders is None:  
    print("No orders on GBPUSD, error code={}".format(mt5.last_error()))   
else:  
    print("Total orders on GBPUSD:",len(orders))  
    # display all active orders   
    for order in orders:   
        print(order)   
print()  
    
# get the list of orders on symbols whose names contain "*GBP*"  
gbp_orders=mt5.orders_get(group="*GBP*")  
if gbp_orders is None:  
    print("No orders with group=\"*GBP*\", error code={}".format(mt5.last_error()))   
else:  
    print("orders_get(group=\"*GBP*\")={}".format(len(gbp_orders)))   
    # display these orders as a table using pandas.DataFrame   
    df=pd.DataFrame(list(gbp_orders),columns=gbp_orders[0]._asdict().keys())   
    df.drop(['time_done', 'time_done_msc', 'position_id', 'position_by_id', 'reason', 'volume_initial', 'price_stoplimit'], axis=1, inplace=True)   
    df['time_setup'] = pd.to_datetime(df['time_setup'], unit='s')   
    print(df)   
    
# shut down connection to the MetaTrader 5 terminal  
mt5.shutdown()  
    
Result:  
MetaTrader5 package author:  MetaQuotes Software Corp.  
MetaTrader5 package version:  5.0.29  
    
Total orders on GBPUSD: 2  
TradeOrder(ticket=554733548, time_setup=1585153667,
time_setup_msc=1585153667718, time_done=0, time_done_msc=0, time_expiration=0,
type=3, type_time=0, ...  
TradeOrder(ticket=554733621, time_setup=1585153671,
time_setup_msc=1585153671419, time_done=0, time_done_msc=0, time_expiration=0,
type=2, type_time=0, ...  
    
orders_get(group="*GBP*")=4  
      ticket          time_setup  time_setup_msc  time_expiration  type  type_time  type_filling  state  magic  volume_current  price_open   sl   tp  price_current  symbol comment external_id   
0  554733548 2020-03-25 16:27:47   1585153667718                0     3
0             2      1      0             0.2     1.25379  0.0  0.0
1.16803  GBPUSD  
1  554733621 2020-03-25 16:27:51   1585153671419                0     2
0             2      1      0             0.2     1.14370  0.0  0.0
1.16815  GBPUSD  
2  554746664 2020-03-25 16:38:14   1585154294401                0     3
0             2      1      0             0.2     0.93851  0.0  0.0
0.92428  EURGBP  
3  554746710 2020-03-25 16:38:17   1585154297022                0     2
0             2      1      0             0.2     0.90527  0.0  0.0
0.92449  EURGBP  
---  
  
See also

[orders_total](/en/docs/python_metatrader5/mt5orderstotal_py),
[positions_get](/en/docs/python_metatrader5/mt5positionsget_py)

[orders_total](/en/docs/python_metatrader5/mt5orderstotal_py "orders_total")

[order_calc_margin](/en/docs/python_metatrader5/mt5ordercalcmargin_py
"order_calc_margin")

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

