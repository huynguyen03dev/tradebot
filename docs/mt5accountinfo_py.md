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

  * [__English](/en/docs/python_metatrader5/mt5accountinfo_py)
  * [__Русский](/ru/docs/python_metatrader5/mt5accountinfo_py)
  * [__中文](/zh/docs/python_metatrader5/mt5accountinfo_py)
  * [__Español](/es/docs/python_metatrader5/mt5accountinfo_py)
  * [__Português](/pt/docs/python_metatrader5/mt5accountinfo_py)
  * [__日本語](/ja/docs/python_metatrader5/mt5accountinfo_py)
  * [__Deutsch](/de/docs/python_metatrader5/mt5accountinfo_py)
  * [__한국어](/ko/docs/python_metatrader5/mt5accountinfo_py)
  * [__Français](/fr/docs/python_metatrader5/mt5accountinfo_py)
  * [__Italiano](/it/docs/python_metatrader5/mt5accountinfo_py)
  * [__Türkçe](/tr/docs/python_metatrader5/mt5accountinfo_py)

[MQL5 Reference](/en/docs "MQL5 Reference")[Python
Integration](/en/docs/python_metatrader5 "Python Integration")account_info

  * [initialize](/en/docs/python_metatrader5/mt5initialize_py "initialize")
  * [login](/en/docs/python_metatrader5/mt5login_py "login")
  * [shutdown](/en/docs/python_metatrader5/mt5shutdown_py "shutdown")
  * [version](/en/docs/python_metatrader5/mt5version_py "version")
  * [last_error](/en/docs/python_metatrader5/mt5lasterror_py "last_error")
  * account_info
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

# account_info

Get info on the current trading account.

account_info()  
---  
  
Return Value

Return info in the form of a named tuple structure (namedtuple). Return None
in case of an error. The info on the error can be obtained using
[last_error()](/en/docs/python_metatrader5/mt5lasterror_py).

Note

The function returns all data that can be obtained using
[AccountInfoInteger](/en/docs/account/accountinfointeger),
[AccountInfoDouble](/en/docs/account/accountinfodouble) and
[AccountInfoString](/en/docs/account/accountinfostring) in one call.

Example:

import MetaTrader5 as mt5  
import pandas as pd  
# display data on the MetaTrader 5 package  
print("MetaTrader5 package author: ",mt5.__author__)  
print("MetaTrader5 package version: ",mt5.__version__)  
    
# establish connection to the MetaTrader 5 terminal  
if not mt5.initialize():  
    print("initialize() failed, error code =",mt5.last_error())   
    quit()   
    
# connect to the trade account specifying a password and a server  
authorized=mt5.login(25115284, password="gqz0343lbdm")  
if authorized:  
    account_info=mt5.account_info()   
    if account_info!=None:   
        # display trading account data 'as is'   
        print(account_info)   
        # display trading account data in the form of a dictionary   
        print("Show account_info()._asdict():")   
        account_info_dict = mt5.account_info()._asdict()   
        for prop in account_info_dict:   
            print("  {}={}".format(prop, account_info_dict[prop]))   
        print()   
    
        # convert the dictionary into DataFrame and print   
        df=pd.DataFrame(list(account_info_dict.items()),columns=['property','value'])   
        print("account_info() as dataframe:")   
        print(df)   
else:  
    print("failed to connect to trade account 25115284 with password=gqz0343lbdm, error code =",mt5.last_error())   
    
# shut down connection to the MetaTrader 5 terminal  
mt5.shutdown()  
    
    
Result:  
MetaTrader5 package author:  MetaQuotes Software Corp.  
MetaTrader5 package version:  5.0.29  
AccountInfo(login=25115284, trade_mode=0, leverage=100, limit_orders=200,
margin_so_mode=0, ....  
Show account_info()._asdict():  
  login=25115284  
  trade_mode=0  
  leverage=100  
  limit_orders=200  
  margin_so_mode=0  
  trade_allowed=True  
  trade_expert=True  
  margin_mode=2  
  currency_digits=2  
  fifo_close=False  
  balance=99511.4  
  credit=0.0  
  profit=41.82  
  equity=99553.22  
  margin=98.18  
  margin_free=99455.04  
  margin_level=101398.67590140559  
  margin_so_call=50.0  
  margin_so_so=30.0  
  margin_initial=0.0  
  margin_maintenance=0.0  
  assets=0.0  
  liabilities=0.0  
  commission_blocked=0.0  
  server=MetaQuotes-Demo  
  currency=USD  
  company=MetaQuotes Software Corp.  
    
account_info() as dataframe  
              property                      value   
0                login                   25115284  
1           trade_mode                          0  
2             leverage                        100  
3         limit_orders                        200  
4       margin_so_mode                          0  
5        trade_allowed                       True  
6         trade_expert                       True  
7          margin_mode                          2  
8      currency_digits                          2  
9           fifo_close                      False  
10             balance                    99588.3  
11              credit                          0  
12              profit                     -45.13  
13              equity                    99543.2  
14              margin                      54.37  
15         margin_free                    99488.8  
16        margin_level                     183085  
17      margin_so_call                         50  
18        margin_so_so                         30  
19      margin_initial                          0  
20  margin_maintenance                          0  
21              assets                          0  
22         liabilities                          0  
23  commission_blocked                          0  
24                name                James Smith  
25              server            MetaQuotes-Demo  
26            currency                        USD  
27             company  MetaQuotes Software Corp.  
---  
  
See also

[initialize](/en/docs/python_metatrader5/mt5initialize_py),
[shutdown](/en/docs/python_metatrader5/mt5shutdown_py),
[login](/en/docs/python_metatrader5/mt5login_py)

[last_error](/en/docs/python_metatrader5/mt5lasterror_py "last_error")

[terminal_info](/en/docs/python_metatrader5/mt5terminalinfo_py
"terminal_info")

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

