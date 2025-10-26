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

  * [__English](/en/docs/python_metatrader5/mt5ordersend_py)
  * [__Русский](/ru/docs/python_metatrader5/mt5ordersend_py)
  * [__中文](/zh/docs/python_metatrader5/mt5ordersend_py)
  * [__Español](/es/docs/python_metatrader5/mt5ordersend_py)
  * [__Português](/pt/docs/python_metatrader5/mt5ordersend_py)
  * [__日本語](/ja/docs/python_metatrader5/mt5ordersend_py)
  * [__Deutsch](/de/docs/python_metatrader5/mt5ordersend_py)
  * [__한국어](/ko/docs/python_metatrader5/mt5ordersend_py)
  * [__Français](/fr/docs/python_metatrader5/mt5ordersend_py)
  * [__Italiano](/it/docs/python_metatrader5/mt5ordersend_py)
  * [__Türkçe](/tr/docs/python_metatrader5/mt5ordersend_py)

[MQL5 Reference](/en/docs "MQL5 Reference")[Python
Integration](/en/docs/python_metatrader5 "Python Integration")order_send

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
  * [order_check](/en/docs/python_metatrader5/mt5ordercheck_py "order_check")
  * order_send
  * [positions_total](/en/docs/python_metatrader5/mt5positionstotal_py "positions_total")
  * [positions_get](/en/docs/python_metatrader5/mt5positionsget_py "positions_get")
  * [history_orders_total](/en/docs/python_metatrader5/mt5historyorderstotal_py "history_orders_total")
  * [history_orders_get](/en/docs/python_metatrader5/mt5historyordersget_py "history_orders_get")
  * [history_deals_total](/en/docs/python_metatrader5/mt5historydealstotal_py "history_deals_total")
  * [history_deals_get](/en/docs/python_metatrader5/mt5historydealsget_py "history_deals_get")

# order_send

Send a [request](/en/docs/constants/structures/mqltraderequest) to perform a
[trading
operation](/en/docs/constants/tradingconstants/enum_trade_request_actions)
from the terminal to the trade server. The function is similar to
[OrderSend](/en/docs/trading/ordersend).

order_send(  
   request      // request structure  
   );  
---  
  
Parameters

request

[in] [MqlTradeRequest](/en/docs/constants/structures/mqltraderequest) type
structure describing a required trading action. Required unnamed parameter.
Example of filling in a request and the enumeration content are described
below.

Return Value

Execution result as the
[MqlTradeResult](/en/docs/constants/structures/mqltraderesult) structure. The
request field in the answer contains the structure of a trading request passed
to order_send(). The info on the error can be obtained using
[last_error()](/en/docs/python_metatrader5/mt5lasterror_py).

The [MqlTradeRequest](/en/docs/constants/structures/mqltraderequest) trading
request structure

Field | Description  
---|---  
action | Trading operation type. The value can be one of the values of the [TRADE_REQUEST_ACTIONS](/en/docs/python_metatrader5/mt5ordercheck_py#trade_request_actions) enumeration  
magic | EA ID. Allows arranging the analytical handling of trading orders. Each EA can set a unique ID when sending a trading request  
order | Order ticket. Required for modifying pending orders  
symbol | The name of the trading instrument, for which the order is placed. Not required when modifying orders and closing positions  
volume | Requested volume of a deal in lots. A real volume when making a deal depends on an [order execution type](/en/docs/python_metatrader5/mt5ordercheck_py#order_type_filling).  
price | Price at which an order should be executed. The price is not set in case of market orders for instruments of the "Market Execution" ([SYMBOL_TRADE_EXECUTION_MARKET](/en/docs/constants/environment_state/marketinfoconstants#enum_symbol_trade_execution)) type having the [TRADE_ACTION_DEAL](/en/docs/python_metatrader5/mt5ordercheck_py#trade_request_actions) type  
stoplimit | A price a pending Limit order is set at when the price reaches the 'price' value (this condition is mandatory). The pending order is not passed to the trading system until that moment  
sl | A price a Stop Loss order is activated at when the price moves in an unfavorable direction  
tp | A price a Take Profit order is activated at when the price moves in a favorable direction  
deviation | Maximum acceptable deviation from the requested price, specified in [points](/en/docs/predefined/_point)  
type | Order type. The value can be one of the values of the [ORDER_TYPE](/en/docs/python_metatrader5/mt5ordercalcmargin_py#order_type) enumeration  
type_filling | Order filling type. The value can be one of the [ORDER_TYPE_FILLING](/en/docs/python_metatrader5/mt5ordercheck_py#order_type_filling) values  
type_time | Order type by expiration. The value can be one of the [ORDER_TYPE_TIME](/en/docs/python_metatrader5/mt5ordercheck_py#order_type_time) values  
expiration | Pending order expiration time (for [TIME_SPECIFIED](/en/docs/python_metatrader5/mt5ordercheck_py#order_type_time) type orders)  
comment | Comment to an order  
position | Position ticket. Fill it when changing and closing a position for its clear identification. Usually, it is the same as the ticket of the order that opened the position.  
position_by | Opposite position ticket. It is used when closing a position by an opposite one (opened at the same symbol but in the opposite direction).  
  
Note

A trading request passes several verification stages on the trade server.
First, the validity of all the necessary request fields is checked. If there
are no errors, the server accepts the order for further handling. See the
[OrderSend](/en/docs/trading/ordersend) function description for the details
about executing trading operations.

Example:

import time  
import MetaTrader5 as mt5  
    
# display data on the MetaTrader 5 package  
print("MetaTrader5 package author: ", mt5.__author__)  
print("MetaTrader5 package version: ", mt5.__version__)  
    
# establish connection to the MetaTrader 5 terminal  
if not mt5.initialize():  
    print("initialize() failed, error code =",mt5.last_error())   
    quit()   
    
# prepare the buy request structure  
symbol = "USDJPY"  
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
    
lot = 0.1  
point = mt5.symbol_info(symbol).point  
price = mt5.symbol_info_tick(symbol).ask  
deviation = 20  
request = {  
    "action": mt5.TRADE_ACTION_DEAL,   
    "symbol": symbol,   
    "volume": lot,   
    "type": mt5.ORDER_TYPE_BUY,   
    "price": price,   
    "sl": price - 100 * point,   
    "tp": price + 100 * point,   
    "deviation": deviation,   
    "magic": 234000,   
    "comment": "python script open",   
    "type_time": mt5.ORDER_TIME_GTC,   
    "type_filling": mt5.ORDER_FILLING_RETURN,   
}  
    
# send a trading request  
result = mt5.order_send(request)  
# check the execution result  
print("1. order_send(): by {} {} lots at {} with deviation={}
points".format(symbol,lot,price,deviation));  
if result.retcode != mt5.TRADE_RETCODE_DONE:  
    print("2. order_send failed, retcode={}".format(result.retcode))   
    # request the result as a dictionary and display it element by element   
    result_dict=result._asdict()   
    for field in result_dict.keys():   
        print("   {}={}".format(field,result_dict[field]))   
        # if this is a trading request structure, display it element by element as well   
        if field=="request":   
            traderequest_dict=result_dict[field]._asdict()   
            for tradereq_filed in traderequest_dict:   
                print("       traderequest: {}={}".format(tradereq_filed,traderequest_dict[tradereq_filed]))   
    print("shutdown() and quit")   
    mt5.shutdown()   
    quit()   
    
print("2. order_send done, ", result)  
print("   opened position with POSITION_TICKET={}".format(result.order))  
print("   sleep 2 seconds before closing position #{}".format(result.order))  
time.sleep(2)  
# create a close request  
position_id=result.order  
price=mt5.symbol_info_tick(symbol).bid  
deviation=20  
request={  
    "action": mt5.TRADE_ACTION_DEAL,   
    "symbol": symbol,   
    "volume": lot,   
    "type": mt5.ORDER_TYPE_SELL,   
    "position": position_id,   
    "price": price,   
    "deviation": deviation,   
    "magic": 234000,   
    "comment": "python script close",   
    "type_time": mt5.ORDER_TIME_GTC,   
    "type_filling": mt5.ORDER_FILLING_RETURN,   
}  
# send a trading request  
result=mt5.order_send(request)  
# check the execution result  
print("3. close position #{}: sell {} {} lots at {} with deviation={}
points".format(position_id,symbol,lot,price,deviation));  
if result.retcode != mt5.TRADE_RETCODE_DONE:  
    print("4. order_send failed, retcode={}".format(result.retcode))   
    print("   result",result)   
else:  
    print("4. position #{} closed, {}".format(position_id,result))   
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
    
Result  
MetaTrader5 package author:  MetaQuotes Software Corp.  
MetaTrader5 package version:  5.0.29  
1. order_send(): by USDJPY 0.1 lots at 108.023 with deviation=20 points   
2. order_send done,  OrderSendResult(retcode=10009, deal=535084512, order=557416535, volume=0.1, price=108.023, ...   
   opened position with POSITION_TICKET=557416535  
   sleep 2 seconds before closing position #557416535  
3. close position #557416535: sell USDJPY 0.1 lots at 108.018 with deviation=20 points   
4. position #557416535 closed, OrderSendResult(retcode=10009, deal=535084631, order=557416654, volume=0.1, price=...   
   retcode=10009  
   deal=535084631  
   order=557416654  
   volume=0.1  
   price=108.015  
   bid=108.015  
   ask=108.02  
   comment=Request executed  
   request_id=55  
   retcode_external=0  
   request=TradeRequest(action=1, magic=234000, order=0, symbol='USDJPY',
volume=0.1, price=108.018, stoplimit=0.0, ...  
       traderequest: action=1   
       traderequest: magic=234000   
       traderequest: order=0   
       traderequest: symbol=USDJPY   
       traderequest: volume=0.1   
       traderequest: price=108.018   
       traderequest: stoplimit=0.0   
       traderequest: sl=0.0   
       traderequest: tp=0.0   
       traderequest: deviation=20   
       traderequest: type=1   
       traderequest: type_filling=2   
       traderequest: type_time=0   
       traderequest: expiration=0   
       traderequest: comment=python script close   
       traderequest: position=557416535   
       traderequest: position_by=0  
---  
  
See also

[order_check](/en/docs/python_metatrader5/mt5ordercheck_py),
[OrderSend](/en/docs/trading/ordersend),[Trading operation
types](/en/docs/constants/tradingconstants/enum_trade_request_actions),
[Trading request structure](/en/docs/constants/structures/mqltraderequest),
[Structure of the trading request check
results](/en/docs/constants/structures/mqltradecheckresult), [Structure of the
trading request result](/en/docs/constants/structures/mqltraderesult)

[order_check](/en/docs/python_metatrader5/mt5ordercheck_py "order_check")

[positions_total](/en/docs/python_metatrader5/mt5positionstotal_py
"positions_total")

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

