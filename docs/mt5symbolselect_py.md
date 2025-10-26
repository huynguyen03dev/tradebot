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

  * [__English](/en/docs/python_metatrader5/mt5symbolselect_py)
  * [__Русский](/ru/docs/python_metatrader5/mt5symbolselect_py)
  * [__中文](/zh/docs/python_metatrader5/mt5symbolselect_py)
  * [__Español](/es/docs/python_metatrader5/mt5symbolselect_py)
  * [__Português](/pt/docs/python_metatrader5/mt5symbolselect_py)
  * [__日本語](/ja/docs/python_metatrader5/mt5symbolselect_py)
  * [__Deutsch](/de/docs/python_metatrader5/mt5symbolselect_py)
  * [__한국어](/ko/docs/python_metatrader5/mt5symbolselect_py)
  * [__Français](/fr/docs/python_metatrader5/mt5symbolselect_py)
  * [__Italiano](/it/docs/python_metatrader5/mt5symbolselect_py)
  * [__Türkçe](/tr/docs/python_metatrader5/mt5symbolselect_py)

[MQL5 Reference](/en/docs "MQL5 Reference")[Python
Integration](/en/docs/python_metatrader5 "Python Integration")symbol_select

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
  * symbol_select
  * [market_book_add](/en/docs/python_metatrader5/mt5marketbookadd_py "market_book_add")
  * [market_book_get](/en/docs/python_metatrader5/mt5marketbookget_py "market_book_get")
  * [market_book_release](/en/docs/python_metatrader5/mt5marketbookrelease_py "market_book_release")
  * [copy_rates_from](/en/docs/python_metatrader5/mt5copyratesfrom_py "copy_rates_from")
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

# symbol_select

Select a symbol in the
[MarketWatch](https://www.metatrader5.com/en/terminal/help/trading/market_watch)
window or remove a symbol from the window.

symbol_select(  
   symbol,      // financial instrument name  
   enable=None  // enable or disable  
)  
---  
  
symbol

[in]  Financial instrument name. Required unnamed parameter.

enable

[in]  Switch. Optional unnamed parameter. If 'false', a symbol should be
removed from the MarketWatch window. Otherwise, it should be selected in the
MarketWatch window. A symbol cannot be removed if open charts with this symbol
are currently present or positions are opened on it.

Return Value

True if successful, otherwise – False.

Note

The function is similar to
[SymbolSelect](/en/docs/marketinformation/symbolselect).

Example:

import MetaTrader5 as mt5  
import pandas as pd  
# display data on the MetaTrader 5 package  
print("MetaTrader5 package author: ",mt5.__author__)  
print("MetaTrader5 package version: ",mt5.__version__)  
print()  
# establish connection to the MetaTrader 5 terminal  
if not mt5.initialize(login=25115284, server="MetaQuotes-
Demo",password="4zatlbqx"):  
    print("initialize() failed, error code =",mt5.last_error())   
    quit()   
    
# attempt to enable the display of the EURCAD in MarketWatch  
selected=mt5.symbol_select("EURCAD",True)  
if not selected:  
    print("Failed to select EURCAD, error code =",mt5.last_error())   
else:  
    symbol_info=mt5.symbol_info("EURCAD")   
    print(symbol_info)   
    print("EURCAD: currency_base =",symbol_info.currency_base,"  currency_profit =",symbol_info.currency_profit,"  currency_margin =",symbol_info.currency_margin)   
    print()   
    
    # get symbol properties in the form of a dictionary   
    print("Show symbol_info()._asdict():")   
    symbol_info_dict = symbol_info._asdict()   
    for prop in symbol_info_dict:   
        print("  {}={}".format(prop, symbol_info_dict[prop]))   
    print()   
    
    # convert the dictionary into DataFrame and print   
    df=pd.DataFrame(list(symbol_info_dict.items()),columns=['property','value'])   
    print("symbol_info_dict() as dataframe:")   
    print(df)   
    
# shut down connection to the MetaTrader 5 terminal  
mt5.shutdown()  
    
    
Result:  
MetaTrader5 package author:  MetaQuotes Software Corp.  
MetaTrader5 package version:  5.0.29  
SymbolInfo(custom=False, chart_mode=0, select=True, visible=True,
session_deals=0, session_buy_orders=0, session_sell_orders=0, volume=0,
volumehigh=0, ....  
EURCAD: currency_base = EUR   currency_profit = CAD   currency_margin = EUR  
    
Show symbol_info()._asdict():  
  custom=False  
  chart_mode=0  
  select=True  
  visible=True  
  session_deals=0  
  session_buy_orders=0  
  session_sell_orders=0  
  volume=0  
  volumehigh=0  
  volumelow=0  
  time=1585217595  
  digits=5  
  spread=39  
  spread_float=True  
  ticks_bookdepth=10  
  trade_calc_mode=0  
  trade_mode=4  
  start_time=0  
  expiration_time=0  
  trade_stops_level=0  
  trade_freeze_level=0  
  trade_exemode=1  
  swap_mode=1  
  swap_rollover3days=3  
  margin_hedged_use_leg=False  
  expiration_mode=7  
  filling_mode=1  
  order_mode=127  
  order_gtc_mode=0  
  option_mode=0  
  option_right=0  
  bid=1.55192  
  bidhigh=1.55842  
  bidlow=1.5419800000000001  
  ask=1.5523099999999999  
  askhigh=1.55915  
  asklow=1.5436299999999998  
  last=0.0  
  lasthigh=0.0  
  lastlow=0.0  
  volume_real=0.0  
  volumehigh_real=0.0  
  volumelow_real=0.0  
  option_strike=0.0  
  point=1e-05  
  trade_tick_value=0.7043642408362214  
  trade_tick_value_profit=0.7043642408362214  
  trade_tick_value_loss=0.7044535553770941  
  trade_tick_size=1e-05  
  trade_contract_size=100000.0  
  trade_accrued_interest=0.0  
  trade_face_value=0.0  
  trade_liquidity_rate=0.0  
  volume_min=0.01  
  volume_max=500.0  
  volume_step=0.01  
  volume_limit=0.0  
  swap_long=-1.1  
  swap_short=-0.9  
  margin_initial=0.0  
  margin_maintenance=0.0  
  session_volume=0.0  
  session_turnover=0.0  
  session_interest=0.0  
  session_buy_orders_volume=0.0  
  session_sell_orders_volume=0.0  
  session_open=0.0  
  session_close=0.0  
  session_aw=0.0  
  session_price_settlement=0.0  
  session_price_limit_min=0.0  
  session_price_limit_max=0.0  
  margin_hedged=100000.0  
  price_change=0.0  
  price_volatility=0.0  
  price_theoretical=0.0  
  price_greeks_delta=0.0  
  price_greeks_theta=0.0  
  price_greeks_gamma=0.0  
  price_greeks_vega=0.0  
  price_greeks_rho=0.0  
  price_greeks_omega=0.0  
  price_sensitivity=0.0  
  basis=  
  category=  
  currency_base=EUR  
  currency_profit=CAD  
  currency_margin=EUR  
  bank=  
  description=Euro vs Canadian Dollar  
  exchange=  
  formula=  
  isin=  
  name=EURCAD  
  page=http://www.google.com/finance?q=EURCAD  
  path=Forex\EURCAD  
    
symbol_info_dict() as dataframe:  
         property                                   value   
0          custom                                   False  
1      chart_mode                                       0  
2          select                                    True  
3         visible                                    True  
4   session_deals                                       0  
..            ...                                     ...  
91        formula  
92           isin  
93           name                                  EURCAD  
94           page  http://www.google.com/finance?q=EURCAD  
95           path                            Forex\EURCAD  
    
[96 rows x 2 columns]  
---  
  
See also

[symbol_info](/en/docs/python_metatrader5/mt5symbolinfo_py)

[symbol_info_tick](/en/docs/python_metatrader5/mt5symbolinfotick_py
"symbol_info_tick")

[market_book_add](/en/docs/python_metatrader5/mt5marketbookadd_py
"market_book_add")

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

