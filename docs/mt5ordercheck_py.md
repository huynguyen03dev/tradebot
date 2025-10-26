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
  * [![](https://c.mql5.com/i/sidebar/download.svg)Download MetaTrader 5](https://download.mql5.com/cdn/web/metaquotes.ltd/mt5/mt5setup.exe?utm_source=www.mql5.com&utm_campaign=download "Get the latest version of the trading platform for free")

DocumentationSections

Type / to search: @user, $symbol, ...

  * [Log in](https://www.mql5.com/en/auth_login "Please sign in. OpenID supported")
  * [Create an account](https://www.mql5.com/en/auth_register "Please register")

__

  * [__English](/en/docs/python_metatrader5/mt5ordercheck_py)
  * [__Русский](/ru/docs/python_metatrader5/mt5ordercheck_py)
  * [__中文](/zh/docs/python_metatrader5/mt5ordercheck_py)
  * [__Español](/es/docs/python_metatrader5/mt5ordercheck_py)
  * [__Português](/pt/docs/python_metatrader5/mt5ordercheck_py)
  * [__日本語](/ja/docs/python_metatrader5/mt5ordercheck_py)
  * [__Deutsch](/de/docs/python_metatrader5/mt5ordercheck_py)
  * [__한국어](/ko/docs/python_metatrader5/mt5ordercheck_py)
  * [__Français](/fr/docs/python_metatrader5/mt5ordercheck_py)
  * [__Italiano](/it/docs/python_metatrader5/mt5ordercheck_py)
  * [__Türkçe](/tr/docs/python_metatrader5/mt5ordercheck_py)

[MQL5 Reference](/en/docs "MQL5 Reference")[Python
Integration](/en/docs/python_metatrader5 "Python Integration")order_check

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
  * [orders_get](/en/docs/python_metatrader5/mt5ordersget_py "orders_get")
  * [order_calc_margin](/en/docs/python_metatrader5/mt5ordercalcmargin_py "order_calc_margin")
  * [order_calc_profit](/en/docs/python_metatrader5/mt5ordercalcprofit_py "order_calc_profit")
  * order_check
  * [order_send](/en/docs/python_metatrader5/mt5ordersend_py "order_send")
  * [positions_total](/en/docs/python_metatrader5/mt5positionstotal_py "positions_total")
  * [positions_get](/en/docs/python_metatrader5/mt5positionsget_py "positions_get")
  * [history_orders_total](/en/docs/python_metatrader5/mt5historyorderstotal_py "history_orders_total")
  * [history_orders_get](/en/docs/python_metatrader5/mt5historyordersget_py "history_orders_get")
  * [history_deals_total](/en/docs/python_metatrader5/mt5historydealstotal_py "history_deals_total")
  * [history_deals_get](/en/docs/python_metatrader5/mt5historydealsget_py "history_deals_get")

# order_check

Check funds sufficiency for performing a required [trading
operation](/en/docs/constants/tradingconstants/enum_trade_request_actions).
Check result are returned as the
[MqlTradeCheckResult](/en/docs/constants/structures/mqltradecheckresult)
structure.

order_check(  
   request      // request structure  
   );  
---  
  
Parameters

request

[in]
[MqlTradeRequest](/en/docs/python_metatrader5/mt5ordersend_py#traderequest)
type structure describing a required trading action. Required unnamed
parameter. Example of filling in a request and the enumeration content are
described below.

Return Value

Check result as the
[MqlTradeCheckResult](/en/docs/constants/structures/mqltradecheckresult)
structure. The request field in the answer contains the structure of a trading
request passed to order_check().

Note

Successful sending of a request does not entail that the requested trading
operation will be executed successfully. The order_check function is similar
to [OrderCheck](/en/docs/trading/ordercheck).

TRADE_REQUEST_ACTIONS

ID | Description  
---|---  
TRADE_ACTION_DEAL | Place an order for an instant deal with the specified parameters (set a market order)  
TRADE_ACTION_PENDING | Place an order for performing a deal at specified conditions (pending order)  
TRADE_ACTION_SLTP | Change open position Stop Loss and Take Profit  
TRADE_ACTION_MODIFY | Change parameters of the previously placed trading order  
TRADE_ACTION_REMOVE | Remove previously placed pending order  
TRADE_ACTION_CLOSE_BY | Close a position by an opposite one  
  
ORDER_TYPE_FILLING

ID | Description  
---|---  
ORDER_FILLING_FOK | This execution policy means that an order can be executed only in the specified volume. If the necessary amount of a financial instrument is currently unavailable in the market, the order will not be executed. The desired volume can be made up of several available offers.  
ORDER_FILLING_IOC | An agreement to execute a deal at the maximum volume available in the market within the volume specified in the order. If the request cannot be filled completely, an order with the available volume will be executed, and the remaining volume will be canceled.  
ORDER_FILLING_RETURN | This policy is used only for market (ORDER_TYPE_BUY and ORDER_TYPE_SELL), limit and stop limit orders (ORDER_TYPE_BUY_LIMIT, ORDER_TYPE_SELL_LIMIT, ORDER_TYPE_BUY_STOP_LIMIT and ORDER_TYPE_SELL_STOP_LIMIT) and only for the symbols with Market or Exchange execution [modes](/en/docs/constants/environment_state/marketinfoconstants#enum_symbol_trade_execution). If filled partially, a market or limit order with the remaining volume is not canceled, and is processed further. During activation of the ORDER_TYPE_BUY_STOP_LIMIT and ORDER_TYPE_SELL_STOP_LIMIT orders, an appropriate limit order ORDER_TYPE_BUY_LIMIT/ORDER_TYPE_SELL_LIMIT with the ORDER_FILLING_RETURN type is created.  
  
ORDER_TYPE_TIME

ID | Description  
---|---  
ORDER_TIME_GTC | The order stays in the queue until it is manually canceled  
ORDER_TIME_DAY | The order is active only during the current trading day  
ORDER_TIME_SPECIFIED | The order is active until the specified date  
ORDER_TIME_SPECIFIED_DAY | The order is active until 23:59:59 of the specified day. If this time appears to be out of a trading session, the expiration is processed at the nearest trading time.  
  
Example:

import MetaTrader5 as mt5  
# display data on the MetaTrader 5 package  
print("MetaTrader5 package author: ",mt5.__author__)  
print("MetaTrader5 package version: ",mt5.__version__)  
  
# establish connection to MetaTrader 5 terminal  
if not mt5.initialize():  
    print("initialize() failed, error code =",mt5.last_error())   
    quit()  
  
# get account currency  
account_currency=mt5.account_info().currency  
print("Account currency:",account_currency)  
    
# prepare the request structure  
symbol="USDJPY"  
symbol_info = mt5.symbol_info(symbol)  
if symbol_info is None:  
    print(symbol, "not found, can not call order_check()")   
    mt5.shutdown()   
    quit()   
    
# if the symbol is unavailable in MarketWatch, add it  
if not symbol_info.visible:  
    print(symbol, "is not visible, trying to switch on")   
    if not mt5.symbol_select(symbol,True):   
        print("symbol_select({}}) failed, exit",symbol)   
        mt5.shutdown()   
        quit()   
  
# prepare the request  
point=mt5.symbol_info(symbol).point  
request = {  
    "action": mt5.TRADE_ACTION_DEAL,  
    "symbol": symbol,  
    "volume": 1.0,  
    "type": mt5.ORDER_TYPE_BUY,  
    "price": mt5.symbol_info_tick(symbol).ask,  
    "sl": mt5.symbol_info_tick(symbol).ask-100*point,  
    "tp": mt5.symbol_info_tick(symbol).ask+100*point,  
    "deviation": 10,  
    "magic": 234000,  
    "comment": "python script",  
    "type_time": mt5.ORDER_TIME_GTC,  
    "type_filling": mt5.ORDER_FILLING_RETURN,  
}  
    
# perform the check and display the result 'as is'  
result = mt5.order_check(request)  
print(result);  
# request the result as a dictionary and display it element by element  
result_dict=result._asdict()  
for field in result_dict.keys():  
    print("   {}={}".format(field,result_dict[field]))   
    # if this is a trading request structure, display it element by element as well   
    if field=="request":   
        traderequest_dict=result_dict[field]._asdict()   
        for tradereq_filed in traderequest_dict:   
            print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))   
  
# shut down connection to the MetaTrader 5 terminal  
mt5.shutdown()  
  
  
Result:  
MetaTrader5 package author:  MetaQuotes Software Corp.  
MetaTrader5 package version:  5.0.29  
  
Account currecy: USD  
   retcode=0  
   balance=101300.53  
   equity=68319.53  
   profit=-32981.0  
   margin=51193.67  
   margin_free=17125.86  
   margin_level=133.45308121101692  
   comment=Done  
   request=TradeRequest(action=1, magic=234000, order=0, symbol='USDJPY',
volume=1.0, ...  
       traderequest: action=1   
       traderequest: magic=234000   
       traderequest: order=0   
       traderequest: symbol=USDJPY   
       traderequest: volume=1.0   
       traderequest: price=108.081   
       traderequest: stoplimit=0.0   
       traderequest: sl=107.98100000000001   
       traderequest: tp=108.181   
       traderequest: deviation=10   
       traderequest: type=0   
       traderequest: type_filling=2   
       traderequest: type_time=0   
       traderequest: expiration=0   
       traderequest: comment=python script   
       traderequest: position=0   
       traderequest: position_by=0  
---  
  
See also

[order_send](/en/docs/python_metatrader5/mt5ordersend_py),[
OrderCheck](/en/docs/trading/ordercheck), [Trading operation
types](/en/docs/constants/tradingconstants/enum_trade_request_actions),
[Trading request structure](/en/docs/constants/structures/mqltraderequest),
[Structure of the trading request check
results](/en/docs/constants/structures/mqltradecheckresult), [Structure of the
trading request result](/en/docs/constants/structures/mqltraderesult)

[order_calc_profit](/en/docs/python_metatrader5/mt5ordercalcprofit_py
"order_calc_profit")

[order_send](/en/docs/python_metatrader5/mt5ordersend_py "order_send")

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

