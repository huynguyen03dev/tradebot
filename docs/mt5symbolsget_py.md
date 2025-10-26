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

  * [__English](/en/docs/python_metatrader5/mt5symbolsget_py)
  * [__Русский](/ru/docs/python_metatrader5/mt5symbolsget_py)
  * [__中文](/zh/docs/python_metatrader5/mt5symbolsget_py)
  * [__Español](/es/docs/python_metatrader5/mt5symbolsget_py)
  * [__Português](/pt/docs/python_metatrader5/mt5symbolsget_py)
  * [__日本語](/ja/docs/python_metatrader5/mt5symbolsget_py)
  * [__Deutsch](/de/docs/python_metatrader5/mt5symbolsget_py)
  * [__한국어](/ko/docs/python_metatrader5/mt5symbolsget_py)
  * [__Français](/fr/docs/python_metatrader5/mt5symbolsget_py)
  * [__Italiano](/it/docs/python_metatrader5/mt5symbolsget_py)
  * [__Türkçe](/tr/docs/python_metatrader5/mt5symbolsget_py)

[MQL5 Reference](/en/docs "MQL5 Reference")[Python
Integration](/en/docs/python_metatrader5 "Python Integration")symbols_get

  * [initialize](/en/docs/python_metatrader5/mt5initialize_py "initialize")
  * [login](/en/docs/python_metatrader5/mt5login_py "login")
  * [shutdown](/en/docs/python_metatrader5/mt5shutdown_py "shutdown")
  * [version](/en/docs/python_metatrader5/mt5version_py "version")
  * [last_error](/en/docs/python_metatrader5/mt5lasterror_py "last_error")
  * [account_info](/en/docs/python_metatrader5/mt5accountinfo_py "account_info")
  * [terminal_info](/en/docs/python_metatrader5/mt5terminalinfo_py "terminal_info")
  * [symbols_total](/en/docs/python_metatrader5/mt5symbolstotal_py "symbols_total")
  * symbols_get
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

# symbols_get

Get all financial instruments from the MetaTrader 5 terminal.

symbols_get(  
   group="GROUP"      // symbol selection filter  
)  
---  
  
group="GROUP"

[in]  The filter for arranging a group of necessary symbols. Optional
parameter. If the group is specified, the function returns only symbols
meeting a specified criteria.

Return Value

Return symbols in the form of a tuple. Return None in case of an error. The
info on the error can be obtained using
[last_error()](/en/docs/python_metatrader5/mt5lasterror_py).

Note

The group parameter allows sorting out symbols by name. '*' can be used at the
beginning and the end of a string.

The group parameter can be used as a named or an unnamed one. Both options
work the same way. The named option (group="GROUP") makes the code easier to
read.

The group parameter may contain several comma separated conditions. A
condition can be set as a mask using '*'. The logical negation symbol '!' can
be used for an exclusion. All conditions are applied sequentially, which means
conditions of including to a group should be specified first followed by an
exclusion condition. For example, group="*, !EUR" means that all symbols
should be selected first and the ones containing "EUR" in their names should
be excluded afterwards.

Unlike [symbol_info()](/en/docs/python_metatrader5/mt5symbolinfo_py), the
symbols_get() function returns data on all requested symbols within a single
call.

Example:

import MetaTrader5 as mt5  
# display data on the MetaTrader 5 package  
print("MetaTrader5 package author: ",mt5.__author__)  
print("MetaTrader5 package version: ",mt5.__version__)  
    
# establish connection to the MetaTrader 5 terminal  
if not mt5.initialize():  
    print("initialize() failed, error code =",mt5.last_error())   
    quit()   
    
# get all symbols  
symbols=mt5.symbols_get()  
print('Symbols: ', len(symbols))  
count=0  
# display the first five ones  
for s in symbols:  
    count+=1   
    print("{}. {}".format(count,s.name))   
    if count==5: break   
print()  
    
# get symbols containing RU in their names  
ru_symbols=mt5.symbols_get("*RU*")  
print('len(*RU*): ', len(ru_symbols))  
for s in ru_symbols:  
    print(s.name)   
print()  
    
# get symbols whose names do not contain USD, EUR, JPY and GBP  
group_symbols=mt5.symbols_get(group="*,!*USD*,!*EUR*,!*JPY*,!*GBP*")  
print('len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):', len(group_symbols))  
for s in group_symbols:  
    print(s.name,":",s)   
    
# shut down connection to the MetaTrader 5 terminal  
mt5.shutdown()  
    
Result:  
MetaTrader5 package author:  MetaQuotes Software Corp.  
MetaTrader5 package version:  5.0.29  
Symbols:  84  
1. EURUSD   
2. GBPUSD   
3. USDCHF   
4. USDJPY   
5. USDCNH   
    
len(*RU*):  8  
EURUSD  
USDRUB  
USDRUR  
EURRUR  
EURRUB  
FORTS.RUB.M5  
EURUSD_T20  
EURUSD4  
    
len(*,!*USD*,!*EUR*,!*JPY*,!*GBP*):  13  
AUDCAD : SymbolInfo(custom=False, chart_mode=0, select=True, visible=True,
session_deals=0, session_buy_orders=0, session...  
AUDCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False,
session_deals=0, session_buy_orders=0, sessi...  
AUDNZD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False,
session_deals=0, session_buy_orders=0, sessi...  
CADCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False,
session_deals=0, session_buy_orders=0, sessi...  
NZDCAD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False,
session_deals=0, session_buy_orders=0, sessi...  
NZDCHF : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False,
session_deals=0, session_buy_orders=0, sessi...  
NZDSGD : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False,
session_deals=0, session_buy_orders=0, sessi...  
CADMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False,
session_deals=0, session_buy_orders=0, sessi...  
CHFMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False,
session_deals=0, session_buy_orders=0, sessi...  
NZDMXN : SymbolInfo(custom=False, chart_mode=0, select=False, visible=False,
session_deals=0, session_buy_orders=0, sessi...  
FORTS.RTS.M5 : SymbolInfo(custom=True, chart_mode=0, select=False,
visible=False, session_deals=0, session_buy_orders=0, ...  
FORTS.RUB.M5 : SymbolInfo(custom=True, chart_mode=0, select=False,
visible=False, session_deals=0, session_buy_orders=0, ...  
FOREX.CHF.M5 : SymbolInfo(custom=True, chart_mode=0, select=False,
visible=False, session_deals=0, session_buy_orders=0, ...  
---  
  
See also

[symbols_total](/en/docs/python_metatrader5/mt5symbolstotal_py),
[symbol_select](/en/docs/python_metatrader5/mt5symbolselect_py),
[symbol_info](/en/docs/python_metatrader5/mt5symbolinfo_py)

[symbols_total](/en/docs/python_metatrader5/mt5symbolstotal_py
"symbols_total")

[symbol_info](/en/docs/python_metatrader5/mt5symbolinfo_py "symbol_info")

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

