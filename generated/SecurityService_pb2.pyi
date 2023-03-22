import Common_pb2 as _Common_pb2
import StockExchangeService_pb2 as _StockExchangeService_pb2
import TradingTypes_pb2 as _TradingTypes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

BOND: SecurityClass
CCALL: TradingPhase
CERTIFICATE: SecurityClass
COMMODITY: SecurityClass
CURRENCY: SecurityClass
DAY: TimeResolution
DESCRIPTOR: _descriptor.FileDescriptor
END: TradingPhase
FUNDS: SecurityClass
FUTURE: SecurityClass
FUTURE_C1: SecurityClass
FUTURE_C2: SecurityClass
FUTURE_C3: SecurityClass
HOUR: TimeResolution
ICALL: TradingPhase
ID_INSTRUMENT: SecurityCodeType
ID_NOTATION: SecurityCodeType
ID_OSI: SecurityCodeType
INDEX: SecurityClass
ISIN: SecurityCodeType
MINUTE: TimeResolution
MNEMONIC: SecurityCodeType
MNEMONIC_US: SecurityCodeType
MUTUAL_FUNDS: SecurityClass
NONE: TradingPhase
NO_CODE_TYPE: SecurityCodeType
NO_RESOLUTION: TimeResolution
NO_SECURITY_CLASS: SecurityClass
OCALL: TradingPhase
OTHERS: SecurityClass
PARTICIPATION_CERTIFICATE: SecurityClass
POSTTRADE: TradingPhase
PRECIOUS_METAL: SecurityClass
PRETRADE: TradingPhase
SECOND: TimeResolution
START: TradingPhase
STOCK: SecurityClass
TICK: TimeResolution
TRACKERS: SecurityClass
TRADE: TradingPhase
TRADE_AUCTION_NO_INDICATIVE: TradingPhase
TRADE_BEST_BID_ASK: TradingPhase
TRADE_INDICATIVE: TradingPhase
VOLA: TradingPhase
WARRANT: SecurityClass
WKN: SecurityCodeType

class CurrencyRateReply(_message.Message):
    __slots__ = ["currency_from", "currency_rate", "currency_to", "error"]
    CURRENCY_FROM_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_RATE_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_TO_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    currency_from: str
    currency_rate: float
    currency_to: str
    error: _Common_pb2.Error
    def __init__(self, currency_from: _Optional[str] = ..., currency_to: _Optional[str] = ..., currency_rate: _Optional[float] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class CurrencyRateRequest(_message.Message):
    __slots__ = ["access_token", "currency_from", "currency_to"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FROM_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_TO_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    currency_from: str
    currency_to: str
    def __init__(self, access_token: _Optional[str] = ..., currency_from: _Optional[str] = ..., currency_to: _Optional[str] = ...) -> None: ...

class PriceEntry(_message.Message):
    __slots__ = ["close_price", "close_time", "high_price", "low_price", "open_price", "open_time", "volume"]
    CLOSE_PRICE_FIELD_NUMBER: _ClassVar[int]
    CLOSE_TIME_FIELD_NUMBER: _ClassVar[int]
    HIGH_PRICE_FIELD_NUMBER: _ClassVar[int]
    LOW_PRICE_FIELD_NUMBER: _ClassVar[int]
    OPEN_PRICE_FIELD_NUMBER: _ClassVar[int]
    OPEN_TIME_FIELD_NUMBER: _ClassVar[int]
    VOLUME_FIELD_NUMBER: _ClassVar[int]
    close_price: float
    close_time: _Common_pb2.Timestamp
    high_price: float
    low_price: float
    open_price: float
    open_time: _Common_pb2.Timestamp
    volume: float
    def __init__(self, open_price: _Optional[float] = ..., close_price: _Optional[float] = ..., high_price: _Optional[float] = ..., low_price: _Optional[float] = ..., volume: _Optional[float] = ..., open_time: _Optional[_Union[_Common_pb2.Timestamp, _Mapping]] = ..., close_time: _Optional[_Union[_Common_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class SecurityCode(_message.Message):
    __slots__ = ["code", "code_type"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    CODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    code: str
    code_type: SecurityCodeType
    def __init__(self, code: _Optional[str] = ..., code_type: _Optional[_Union[SecurityCodeType, str]] = ...) -> None: ...

class SecurityInfoReply(_message.Message):
    __slots__ = ["error", "name", "security_class", "security_codes", "stock_exchange_infos", "unit_note"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CLASS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CODES_FIELD_NUMBER: _ClassVar[int]
    STOCK_EXCHANGE_INFOS_FIELD_NUMBER: _ClassVar[int]
    UNIT_NOTE_FIELD_NUMBER: _ClassVar[int]
    error: _Common_pb2.Error
    name: str
    security_class: SecurityClass
    security_codes: _containers.RepeatedCompositeFieldContainer[SecurityCode]
    stock_exchange_infos: _containers.RepeatedCompositeFieldContainer[SecurityStockExchangeInfo]
    unit_note: _Common_pb2.UnitNote
    def __init__(self, name: _Optional[str] = ..., security_class: _Optional[_Union[SecurityClass, str]] = ..., security_codes: _Optional[_Iterable[_Union[SecurityCode, _Mapping]]] = ..., stock_exchange_infos: _Optional[_Iterable[_Union[SecurityStockExchangeInfo, _Mapping]]] = ..., unit_note: _Optional[_Union[_Common_pb2.UnitNote, str]] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class SecurityInfoRequest(_message.Message):
    __slots__ = ["access_token", "security_code"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CODE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    security_code: SecurityCode
    def __init__(self, access_token: _Optional[str] = ..., security_code: _Optional[_Union[SecurityCode, _Mapping]] = ...) -> None: ...

class SecurityMarketDataReply(_message.Message):
    __slots__ = ["abs_diff", "ask_price", "ask_time", "ask_volume", "bid_price", "bid_time", "bid_volume", "changed_fields", "currency", "date_month_high", "date_month_low", "date_week_high", "date_week_low", "date_year_high", "date_year_low", "error", "high_price", "indicative_price", "last_addendum", "last_date_time", "last_price", "last_volume", "low_price", "month_high_price", "month_low_price", "open_price", "prevalence_volume", "previous_date", "previous_price", "relative_diff", "security_with_stockexchange", "today_num_trades", "today_volume", "trading_phase", "week_high_price", "week_low_price", "year_high_price", "year_low_price"]
    class SecurityChangedField(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    ABS_DIFF: SecurityMarketDataReply.SecurityChangedField
    ABS_DIFF_FIELD_NUMBER: _ClassVar[int]
    ASK_PRICE: SecurityMarketDataReply.SecurityChangedField
    ASK_PRICE_FIELD_NUMBER: _ClassVar[int]
    ASK_TIME: SecurityMarketDataReply.SecurityChangedField
    ASK_TIME_FIELD_NUMBER: _ClassVar[int]
    ASK_VOLUME: SecurityMarketDataReply.SecurityChangedField
    ASK_VOLUME_FIELD_NUMBER: _ClassVar[int]
    BID_PRICE: SecurityMarketDataReply.SecurityChangedField
    BID_PRICE_FIELD_NUMBER: _ClassVar[int]
    BID_TIME: SecurityMarketDataReply.SecurityChangedField
    BID_TIME_FIELD_NUMBER: _ClassVar[int]
    BID_VOLUME: SecurityMarketDataReply.SecurityChangedField
    BID_VOLUME_FIELD_NUMBER: _ClassVar[int]
    CHANGED_FIELDS_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    DATE_MONTH_HIGH: SecurityMarketDataReply.SecurityChangedField
    DATE_MONTH_HIGH_FIELD_NUMBER: _ClassVar[int]
    DATE_MONTH_LOW: SecurityMarketDataReply.SecurityChangedField
    DATE_MONTH_LOW_FIELD_NUMBER: _ClassVar[int]
    DATE_WEEK_HIGH: SecurityMarketDataReply.SecurityChangedField
    DATE_WEEK_HIGH_FIELD_NUMBER: _ClassVar[int]
    DATE_WEEK_LOW: SecurityMarketDataReply.SecurityChangedField
    DATE_WEEK_LOW_FIELD_NUMBER: _ClassVar[int]
    DATE_YEAR_HIGH: SecurityMarketDataReply.SecurityChangedField
    DATE_YEAR_HIGH_FIELD_NUMBER: _ClassVar[int]
    DATE_YEAR_LOW: SecurityMarketDataReply.SecurityChangedField
    DATE_YEAR_LOW_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    HIGH_PRICE: SecurityMarketDataReply.SecurityChangedField
    HIGH_PRICE_FIELD_NUMBER: _ClassVar[int]
    INDICATIVE_PRICE: SecurityMarketDataReply.SecurityChangedField
    INDICATIVE_PRICE_FIELD_NUMBER: _ClassVar[int]
    LAST_ADDENDUM: SecurityMarketDataReply.SecurityChangedField
    LAST_ADDENDUM_FIELD_NUMBER: _ClassVar[int]
    LAST_DATE_TIME: SecurityMarketDataReply.SecurityChangedField
    LAST_DATE_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE: SecurityMarketDataReply.SecurityChangedField
    LAST_PRICE_FIELD_NUMBER: _ClassVar[int]
    LAST_VOLUME: SecurityMarketDataReply.SecurityChangedField
    LAST_VOLUME_FIELD_NUMBER: _ClassVar[int]
    LOW_PRICE: SecurityMarketDataReply.SecurityChangedField
    LOW_PRICE_FIELD_NUMBER: _ClassVar[int]
    MONTH_HIGH_PRICE: SecurityMarketDataReply.SecurityChangedField
    MONTH_HIGH_PRICE_FIELD_NUMBER: _ClassVar[int]
    MONTH_LOW_PRICE: SecurityMarketDataReply.SecurityChangedField
    MONTH_LOW_PRICE_FIELD_NUMBER: _ClassVar[int]
    NONE: SecurityMarketDataReply.SecurityChangedField
    OPEN_PRICE: SecurityMarketDataReply.SecurityChangedField
    OPEN_PRICE_FIELD_NUMBER: _ClassVar[int]
    PREVALENCE_VOLUME: SecurityMarketDataReply.SecurityChangedField
    PREVALENCE_VOLUME_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_DATE: SecurityMarketDataReply.SecurityChangedField
    PREVIOUS_DATE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_PRICE: SecurityMarketDataReply.SecurityChangedField
    PREVIOUS_PRICE_FIELD_NUMBER: _ClassVar[int]
    RELATIVE_DIFF: SecurityMarketDataReply.SecurityChangedField
    RELATIVE_DIFF_FIELD_NUMBER: _ClassVar[int]
    SECURITY_WITH_STOCKEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    TODAY_NUM_TRADES: SecurityMarketDataReply.SecurityChangedField
    TODAY_NUM_TRADES_FIELD_NUMBER: _ClassVar[int]
    TODAY_VOLUME: SecurityMarketDataReply.SecurityChangedField
    TODAY_VOLUME_FIELD_NUMBER: _ClassVar[int]
    TRADING_PHASE: SecurityMarketDataReply.SecurityChangedField
    TRADING_PHASE_FIELD_NUMBER: _ClassVar[int]
    WEEK_HIGH_PRICE: SecurityMarketDataReply.SecurityChangedField
    WEEK_HIGH_PRICE_FIELD_NUMBER: _ClassVar[int]
    WEEK_LOW_PRICE: SecurityMarketDataReply.SecurityChangedField
    WEEK_LOW_PRICE_FIELD_NUMBER: _ClassVar[int]
    YEAR_HIGH_PRICE: SecurityMarketDataReply.SecurityChangedField
    YEAR_HIGH_PRICE_FIELD_NUMBER: _ClassVar[int]
    YEAR_LOW_PRICE: SecurityMarketDataReply.SecurityChangedField
    YEAR_LOW_PRICE_FIELD_NUMBER: _ClassVar[int]
    abs_diff: float
    ask_price: float
    ask_time: _Common_pb2.Timestamp
    ask_volume: float
    bid_price: float
    bid_time: _Common_pb2.Timestamp
    bid_volume: float
    changed_fields: _containers.RepeatedScalarFieldContainer[SecurityMarketDataReply.SecurityChangedField]
    currency: str
    date_month_high: _Common_pb2.Date
    date_month_low: _Common_pb2.Date
    date_week_high: _Common_pb2.Date
    date_week_low: _Common_pb2.Date
    date_year_high: _Common_pb2.Date
    date_year_low: _Common_pb2.Date
    error: _Common_pb2.Error
    high_price: float
    indicative_price: float
    last_addendum: str
    last_date_time: _Common_pb2.Timestamp
    last_price: float
    last_volume: float
    low_price: float
    month_high_price: float
    month_low_price: float
    open_price: float
    prevalence_volume: float
    previous_date: _Common_pb2.Date
    previous_price: float
    relative_diff: float
    security_with_stockexchange: SecurityWithStockExchange
    today_num_trades: int
    today_volume: float
    trading_phase: TradingPhase
    week_high_price: float
    week_low_price: float
    year_high_price: float
    year_low_price: float
    def __init__(self, security_with_stockexchange: _Optional[_Union[SecurityWithStockExchange, _Mapping]] = ..., changed_fields: _Optional[_Iterable[_Union[SecurityMarketDataReply.SecurityChangedField, str]]] = ..., currency: _Optional[str] = ..., last_price: _Optional[float] = ..., last_volume: _Optional[float] = ..., last_date_time: _Optional[_Union[_Common_pb2.Timestamp, _Mapping]] = ..., today_num_trades: _Optional[int] = ..., today_volume: _Optional[float] = ..., ask_price: _Optional[float] = ..., ask_volume: _Optional[float] = ..., ask_time: _Optional[_Union[_Common_pb2.Timestamp, _Mapping]] = ..., bid_price: _Optional[float] = ..., bid_volume: _Optional[float] = ..., bid_time: _Optional[_Union[_Common_pb2.Timestamp, _Mapping]] = ..., previous_price: _Optional[float] = ..., previous_date: _Optional[_Union[_Common_pb2.Date, _Mapping]] = ..., relative_diff: _Optional[float] = ..., abs_diff: _Optional[float] = ..., high_price: _Optional[float] = ..., low_price: _Optional[float] = ..., open_price: _Optional[float] = ..., week_high_price: _Optional[float] = ..., date_week_high: _Optional[_Union[_Common_pb2.Date, _Mapping]] = ..., week_low_price: _Optional[float] = ..., date_week_low: _Optional[_Union[_Common_pb2.Date, _Mapping]] = ..., month_high_price: _Optional[float] = ..., date_month_high: _Optional[_Union[_Common_pb2.Date, _Mapping]] = ..., month_low_price: _Optional[float] = ..., date_month_low: _Optional[_Union[_Common_pb2.Date, _Mapping]] = ..., year_high_price: _Optional[float] = ..., date_year_high: _Optional[_Union[_Common_pb2.Date, _Mapping]] = ..., year_low_price: _Optional[float] = ..., date_year_low: _Optional[_Union[_Common_pb2.Date, _Mapping]] = ..., last_addendum: _Optional[str] = ..., trading_phase: _Optional[_Union[TradingPhase, str]] = ..., indicative_price: _Optional[float] = ..., prevalence_volume: _Optional[float] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class SecurityMarketDataRequest(_message.Message):
    __slots__ = ["access_token", "currency", "security_with_stockexchange"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    SECURITY_WITH_STOCKEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    currency: str
    security_with_stockexchange: SecurityWithStockExchange
    def __init__(self, access_token: _Optional[str] = ..., security_with_stockexchange: _Optional[_Union[SecurityWithStockExchange, _Mapping]] = ..., currency: _Optional[str] = ...) -> None: ...

class SecurityOrderBookReply(_message.Message):
    __slots__ = ["currency", "error", "order_book_entries", "security_with_stockexchange"]
    class OrderBookEntry(_message.Message):
        __slots__ = ["ask_price", "ask_volume", "bid_price", "bid_volume"]
        ASK_PRICE_FIELD_NUMBER: _ClassVar[int]
        ASK_VOLUME_FIELD_NUMBER: _ClassVar[int]
        BID_PRICE_FIELD_NUMBER: _ClassVar[int]
        BID_VOLUME_FIELD_NUMBER: _ClassVar[int]
        ask_price: float
        ask_volume: float
        bid_price: float
        bid_volume: float
        def __init__(self, bid_price: _Optional[float] = ..., ask_price: _Optional[float] = ..., bid_volume: _Optional[float] = ..., ask_volume: _Optional[float] = ...) -> None: ...
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORDER_BOOK_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    SECURITY_WITH_STOCKEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    currency: str
    error: _Common_pb2.Error
    order_book_entries: _containers.RepeatedCompositeFieldContainer[SecurityOrderBookReply.OrderBookEntry]
    security_with_stockexchange: SecurityWithStockExchange
    def __init__(self, security_with_stockexchange: _Optional[_Union[SecurityWithStockExchange, _Mapping]] = ..., currency: _Optional[str] = ..., order_book_entries: _Optional[_Iterable[_Union[SecurityOrderBookReply.OrderBookEntry, _Mapping]]] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class SecurityOrderBookRequest(_message.Message):
    __slots__ = ["access_token", "currency", "security_with_stockexchange"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    SECURITY_WITH_STOCKEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    currency: str
    security_with_stockexchange: SecurityWithStockExchange
    def __init__(self, access_token: _Optional[str] = ..., security_with_stockexchange: _Optional[_Union[SecurityWithStockExchange, _Mapping]] = ..., currency: _Optional[str] = ...) -> None: ...

class SecurityPriceHistoryReply(_message.Message):
    __slots__ = ["currency", "error", "price_entries", "security_with_stockexchange"]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    PRICE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    SECURITY_WITH_STOCKEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    currency: str
    error: _Common_pb2.Error
    price_entries: _containers.RepeatedCompositeFieldContainer[PriceEntry]
    security_with_stockexchange: SecurityWithStockExchange
    def __init__(self, security_with_stockexchange: _Optional[_Union[SecurityWithStockExchange, _Mapping]] = ..., currency: _Optional[str] = ..., price_entries: _Optional[_Iterable[_Union[PriceEntry, _Mapping]]] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class SecurityPriceHistoryRequest(_message.Message):
    __slots__ = ["access_token", "days", "security_with_stockexchange", "time_resolution"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    DAYS_FIELD_NUMBER: _ClassVar[int]
    SECURITY_WITH_STOCKEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    TIME_RESOLUTION_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    days: int
    security_with_stockexchange: SecurityWithStockExchange
    time_resolution: TimeResolution
    def __init__(self, access_token: _Optional[str] = ..., security_with_stockexchange: _Optional[_Union[SecurityWithStockExchange, _Mapping]] = ..., days: _Optional[int] = ..., time_resolution: _Optional[_Union[TimeResolution, str]] = ...) -> None: ...

class SecurityStockExchangeInfo(_message.Message):
    __slots__ = ["buy_limit_token", "buy_trading_types", "maximal_order_date", "sell_limit_token", "sell_trading_types", "short_mode", "stock_exchange"]
    class LimitToken(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class ShortMode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    BUY_LIMIT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    BUY_TRADING_TYPES_FIELD_NUMBER: _ClassVar[int]
    INTRADAY: SecurityStockExchangeInfo.ShortMode
    INTRADAY_AND_OVERNIGHT: SecurityStockExchangeInfo.ShortMode
    LIMIT_AND_QUOTE: SecurityStockExchangeInfo.LimitToken
    LIMIT_ONLY: SecurityStockExchangeInfo.LimitToken
    MAXIMAL_ORDER_DATE_FIELD_NUMBER: _ClassVar[int]
    NO: SecurityStockExchangeInfo.ShortMode
    NO_SHORT_MODE: SecurityStockExchangeInfo.ShortMode
    OVERNIGHT: SecurityStockExchangeInfo.ShortMode
    QUOTE_ONLY: SecurityStockExchangeInfo.LimitToken
    SELL_LIMIT_TOKEN_FIELD_NUMBER: _ClassVar[int]
    SELL_TRADING_TYPES_FIELD_NUMBER: _ClassVar[int]
    SHORT_MODE_FIELD_NUMBER: _ClassVar[int]
    STOCK_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    TEMPORARY_NO: SecurityStockExchangeInfo.ShortMode
    YES: SecurityStockExchangeInfo.ShortMode
    buy_limit_token: SecurityStockExchangeInfo.LimitToken
    buy_trading_types: _containers.RepeatedCompositeFieldContainer[_TradingTypes_pb2.TradingPossibility]
    maximal_order_date: _Common_pb2.Date
    sell_limit_token: SecurityStockExchangeInfo.LimitToken
    sell_trading_types: _containers.RepeatedCompositeFieldContainer[_TradingTypes_pb2.TradingPossibility]
    short_mode: SecurityStockExchangeInfo.ShortMode
    stock_exchange: _StockExchangeService_pb2.StockExchange
    def __init__(self, stock_exchange: _Optional[_Union[_StockExchangeService_pb2.StockExchange, _Mapping]] = ..., buy_limit_token: _Optional[_Union[SecurityStockExchangeInfo.LimitToken, str]] = ..., sell_limit_token: _Optional[_Union[SecurityStockExchangeInfo.LimitToken, str]] = ..., buy_trading_types: _Optional[_Iterable[_Union[_TradingTypes_pb2.TradingPossibility, _Mapping]]] = ..., sell_trading_types: _Optional[_Iterable[_Union[_TradingTypes_pb2.TradingPossibility, _Mapping]]] = ..., maximal_order_date: _Optional[_Union[_Common_pb2.Date, _Mapping]] = ..., short_mode: _Optional[_Union[SecurityStockExchangeInfo.ShortMode, str]] = ...) -> None: ...

class SecurityWithStockExchange(_message.Message):
    __slots__ = ["security_code", "stock_exchange"]
    SECURITY_CODE_FIELD_NUMBER: _ClassVar[int]
    STOCK_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    security_code: SecurityCode
    stock_exchange: _StockExchangeService_pb2.StockExchange
    def __init__(self, security_code: _Optional[_Union[SecurityCode, _Mapping]] = ..., stock_exchange: _Optional[_Union[_StockExchangeService_pb2.StockExchange, _Mapping]] = ...) -> None: ...

class TimeResolution(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SecurityCodeType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class SecurityClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TradingPhase(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
