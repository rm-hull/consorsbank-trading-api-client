import Common_pb2 as _Common_pb2
import SecurityService_pb2 as _SecurityService_pb2
import StockExchangeService_pb2 as _StockExchangeService_pb2
import AccountService_pb2 as _AccountService_pb2
import TradingTypes_pb2 as _TradingTypes_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

CANCELED: OrderStatus
CANCELED_FORCED: OrderStatus
CANCELED_NOTED: OrderStatus
CANCELED_TIMEOUT: OrderStatus
CHANGED: OrderStatus
CHANGED_NOTED: OrderStatus
DESCRIPTOR: _descriptor.FileDescriptor
EXECUTED: OrderStatus
INACTIVE: OrderStatus
INACTIVE_NOTED: OrderStatus
NEW: OrderStatus
NO_ORDER_STATUS: OrderStatus
OPEN: OrderStatus
PARTIALLY_EXECUTED: OrderStatus
STORNO: OrderStatus
TOTAL_COSTS_ONLY: Validation
VALIDATE_ONLY: Validation
VALIDATE_WITH_DETAIL_COSTS: Validation
VALIDATE_WITH_TOTAL_COSTS: Validation
WITHOUT_VALIDATION: Validation

class AcceptQuoteRequest(_message.Message):
    __slots__ = ["accept_additional_fees", "access_token", "account_number", "amount", "limit", "order_type", "quote_reference", "risk_class_override", "security_with_stockexchange", "target_market_override", "tax_nontransparent_override", "validation"]
    ACCEPT_ADDITIONAL_FEES_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUOTE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    RISK_CLASS_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_WITH_STOCKEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    TARGET_MARKET_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    TAX_NONTRANSPARENT_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    accept_additional_fees: bool
    access_token: str
    account_number: str
    amount: float
    limit: float
    order_type: _TradingTypes_pb2.OrderType
    quote_reference: str
    risk_class_override: bool
    security_with_stockexchange: _SecurityService_pb2.SecurityWithStockExchange
    target_market_override: bool
    tax_nontransparent_override: bool
    validation: Validation
    def __init__(self, access_token: _Optional[str] = ..., account_number: _Optional[str] = ..., security_with_stockexchange: _Optional[_Union[_SecurityService_pb2.SecurityWithStockExchange, _Mapping]] = ..., order_type: _Optional[_Union[_TradingTypes_pb2.OrderType, str]] = ..., amount: _Optional[float] = ..., limit: _Optional[float] = ..., quote_reference: _Optional[str] = ..., validation: _Optional[_Union[Validation, str]] = ..., risk_class_override: bool = ..., target_market_override: bool = ..., tax_nontransparent_override: bool = ..., accept_additional_fees: bool = ...) -> None: ...

class ActivateOrderRequest(_message.Message):
    __slots__ = ["access_token", "account_number", "order_number", "validation"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    account_number: str
    order_number: str
    validation: Validation
    def __init__(self, access_token: _Optional[str] = ..., account_number: _Optional[str] = ..., order_number: _Optional[str] = ..., validation: _Optional[_Union[Validation, str]] = ...) -> None: ...

class AddOrderRequest(_message.Message):
    __slots__ = ["accept_additional_fees", "access_token", "account_number", "amount", "cash_quotation", "closed_realestate_fond_override", "dripping_quantity", "inactive", "limit", "order_model", "order_supplement", "order_type", "position_id", "risk_class_override", "security_with_stockexchange", "stop", "stop_limit", "target_market_override", "tax_nontransparent_override", "trailing_distance", "trailing_limit_tolerance", "trailing_notation", "validation", "validity_date"]
    ACCEPT_ADDITIONAL_FEES_FIELD_NUMBER: _ClassVar[int]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CASH_QUOTATION_FIELD_NUMBER: _ClassVar[int]
    CLOSED_REALESTATE_FOND_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    DRIPPING_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    INACTIVE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    ORDER_MODEL_FIELD_NUMBER: _ClassVar[int]
    ORDER_SUPPLEMENT_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    POSITION_ID_FIELD_NUMBER: _ClassVar[int]
    RISK_CLASS_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_WITH_STOCKEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    STOP_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TARGET_MARKET_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    TAX_NONTRANSPARENT_OVERRIDE_FIELD_NUMBER: _ClassVar[int]
    TRAILING_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    TRAILING_LIMIT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    TRAILING_NOTATION_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    VALIDITY_DATE_FIELD_NUMBER: _ClassVar[int]
    accept_additional_fees: bool
    access_token: str
    account_number: str
    amount: float
    cash_quotation: _TradingTypes_pb2.CashQuotation
    closed_realestate_fond_override: bool
    dripping_quantity: float
    inactive: bool
    limit: float
    order_model: _TradingTypes_pb2.OrderModel
    order_supplement: _TradingTypes_pb2.OrderSupplement
    order_type: _TradingTypes_pb2.OrderType
    position_id: str
    risk_class_override: bool
    security_with_stockexchange: _SecurityService_pb2.SecurityWithStockExchange
    stop: float
    stop_limit: float
    target_market_override: bool
    tax_nontransparent_override: bool
    trailing_distance: float
    trailing_limit_tolerance: float
    trailing_notation: _TradingTypes_pb2.TrailingNotation
    validation: Validation
    validity_date: _Common_pb2.Date
    def __init__(self, access_token: _Optional[str] = ..., account_number: _Optional[str] = ..., security_with_stockexchange: _Optional[_Union[_SecurityService_pb2.SecurityWithStockExchange, _Mapping]] = ..., order_type: _Optional[_Union[_TradingTypes_pb2.OrderType, str]] = ..., amount: _Optional[float] = ..., order_model: _Optional[_Union[_TradingTypes_pb2.OrderModel, str]] = ..., order_supplement: _Optional[_Union[_TradingTypes_pb2.OrderSupplement, str]] = ..., cash_quotation: _Optional[_Union[_TradingTypes_pb2.CashQuotation, str]] = ..., validity_date: _Optional[_Union[_Common_pb2.Date, _Mapping]] = ..., limit: _Optional[float] = ..., stop: _Optional[float] = ..., stop_limit: _Optional[float] = ..., trailing_distance: _Optional[float] = ..., trailing_notation: _Optional[_Union[_TradingTypes_pb2.TrailingNotation, str]] = ..., trailing_limit_tolerance: _Optional[float] = ..., dripping_quantity: _Optional[float] = ..., position_id: _Optional[str] = ..., validation: _Optional[_Union[Validation, str]] = ..., risk_class_override: bool = ..., target_market_override: bool = ..., tax_nontransparent_override: bool = ..., accept_additional_fees: bool = ..., closed_realestate_fond_override: bool = ..., inactive: bool = ...) -> None: ...

class CancelOrderRequest(_message.Message):
    __slots__ = ["access_token", "account_number", "order_number", "validation"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    account_number: str
    order_number: str
    validation: Validation
    def __init__(self, access_token: _Optional[str] = ..., account_number: _Optional[str] = ..., order_number: _Optional[str] = ..., validation: _Optional[_Union[Validation, str]] = ...) -> None: ...

class ChangeOrderRequest(_message.Message):
    __slots__ = ["access_token", "account_number", "amount", "dripping_quantity", "limit", "order_model", "order_number", "order_supplement", "stop", "stop_limit", "trailing_distance", "trailing_limit_tolerance", "validation", "validity_date"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    DRIPPING_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    ORDER_MODEL_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORDER_SUPPLEMENT_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    STOP_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TRAILING_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    TRAILING_LIMIT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    VALIDITY_DATE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    account_number: str
    amount: float
    dripping_quantity: float
    limit: float
    order_model: _TradingTypes_pb2.OrderModel
    order_number: str
    order_supplement: _TradingTypes_pb2.OrderSupplement
    stop: float
    stop_limit: float
    trailing_distance: float
    trailing_limit_tolerance: float
    validation: Validation
    validity_date: _Common_pb2.Date
    def __init__(self, access_token: _Optional[str] = ..., account_number: _Optional[str] = ..., order_number: _Optional[str] = ..., limit: _Optional[float] = ..., stop: _Optional[float] = ..., stop_limit: _Optional[float] = ..., amount: _Optional[float] = ..., validity_date: _Optional[_Union[_Common_pb2.Date, _Mapping]] = ..., order_model: _Optional[_Union[_TradingTypes_pb2.OrderModel, str]] = ..., order_supplement: _Optional[_Union[_TradingTypes_pb2.OrderSupplement, str]] = ..., dripping_quantity: _Optional[float] = ..., validation: _Optional[_Union[Validation, str]] = ..., trailing_distance: _Optional[float] = ..., trailing_limit_tolerance: _Optional[float] = ...) -> None: ...

class DeactivateOrderRequest(_message.Message):
    __slots__ = ["access_token", "account_number", "order_number", "validation"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    VALIDATION_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    account_number: str
    order_number: str
    validation: Validation
    def __init__(self, access_token: _Optional[str] = ..., account_number: _Optional[str] = ..., order_number: _Optional[str] = ..., validation: _Optional[_Union[Validation, str]] = ...) -> None: ...

class Order(_message.Message):
    __slots__ = ["amount", "cash_quotation", "dripping_quantity", "executed_amount", "execution_quote", "limit", "order_model", "order_number", "order_status", "order_supplement", "order_type", "security_with_stockexchange", "status_timestamp", "stop", "stop_limit", "trading_partner_name", "trailing_distance", "trailing_limit_tolerance", "trailing_notation", "unique_id", "validity_date"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    CASH_QUOTATION_FIELD_NUMBER: _ClassVar[int]
    DRIPPING_QUANTITY_FIELD_NUMBER: _ClassVar[int]
    EXECUTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    EXECUTION_QUOTE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    ORDER_MODEL_FIELD_NUMBER: _ClassVar[int]
    ORDER_NUMBER_FIELD_NUMBER: _ClassVar[int]
    ORDER_STATUS_FIELD_NUMBER: _ClassVar[int]
    ORDER_SUPPLEMENT_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_WITH_STOCKEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    STATUS_TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    STOP_FIELD_NUMBER: _ClassVar[int]
    STOP_LIMIT_FIELD_NUMBER: _ClassVar[int]
    TRADING_PARTNER_NAME_FIELD_NUMBER: _ClassVar[int]
    TRAILING_DISTANCE_FIELD_NUMBER: _ClassVar[int]
    TRAILING_LIMIT_TOLERANCE_FIELD_NUMBER: _ClassVar[int]
    TRAILING_NOTATION_FIELD_NUMBER: _ClassVar[int]
    UNIQUE_ID_FIELD_NUMBER: _ClassVar[int]
    VALIDITY_DATE_FIELD_NUMBER: _ClassVar[int]
    amount: float
    cash_quotation: _TradingTypes_pb2.CashQuotation
    dripping_quantity: float
    executed_amount: float
    execution_quote: float
    limit: float
    order_model: _TradingTypes_pb2.OrderModel
    order_number: str
    order_status: OrderStatus
    order_supplement: _TradingTypes_pb2.OrderSupplement
    order_type: _TradingTypes_pb2.OrderType
    security_with_stockexchange: _SecurityService_pb2.SecurityWithStockExchange
    status_timestamp: _Common_pb2.Timestamp
    stop: float
    stop_limit: float
    trading_partner_name: str
    trailing_distance: float
    trailing_limit_tolerance: float
    trailing_notation: _TradingTypes_pb2.TrailingNotation
    unique_id: str
    validity_date: _Common_pb2.Date
    def __init__(self, security_with_stockexchange: _Optional[_Union[_SecurityService_pb2.SecurityWithStockExchange, _Mapping]] = ..., order_type: _Optional[_Union[_TradingTypes_pb2.OrderType, str]] = ..., order_number: _Optional[str] = ..., amount: _Optional[float] = ..., order_model: _Optional[_Union[_TradingTypes_pb2.OrderModel, str]] = ..., order_supplement: _Optional[_Union[_TradingTypes_pb2.OrderSupplement, str]] = ..., cash_quotation: _Optional[_Union[_TradingTypes_pb2.CashQuotation, str]] = ..., executed_amount: _Optional[float] = ..., order_status: _Optional[_Union[OrderStatus, str]] = ..., status_timestamp: _Optional[_Union[_Common_pb2.Timestamp, _Mapping]] = ..., validity_date: _Optional[_Union[_Common_pb2.Date, _Mapping]] = ..., limit: _Optional[float] = ..., stop: _Optional[float] = ..., stop_limit: _Optional[float] = ..., trailing_distance: _Optional[float] = ..., trailing_notation: _Optional[_Union[_TradingTypes_pb2.TrailingNotation, str]] = ..., trailing_limit_tolerance: _Optional[float] = ..., dripping_quantity: _Optional[float] = ..., trading_partner_name: _Optional[str] = ..., execution_quote: _Optional[float] = ..., unique_id: _Optional[str] = ...) -> None: ...

class OrderCosts(_message.Message):
    __slots__ = ["aggregated_costs", "categorie_costs", "cost_id", "estimated_total_costs"]
    class AggregatedCosts(_message.Message):
        __slots__ = ["expected_amount", "expected_amount_currency", "foreign_currency_costs_absolute", "foreign_currency_costs_currency", "foreign_currency_costs_relative", "in_costs_absolute", "in_costs_currency", "in_costs_relative", "instrument_costs_absolute", "instrument_costs_currency", "instrument_costs_relative", "out_costs_absolute", "out_costs_currency", "out_costs_relative", "performance_impact_absolute", "performance_impact_currency", "performance_impact_relative", "service_costs_absolute", "service_costs_currency", "service_costs_relative", "subsidy_costs_absolute", "subsidy_costs_currency", "subsidy_costs_relative"]
        EXPECTED_AMOUNT_CURRENCY_FIELD_NUMBER: _ClassVar[int]
        EXPECTED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
        FOREIGN_CURRENCY_COSTS_ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
        FOREIGN_CURRENCY_COSTS_CURRENCY_FIELD_NUMBER: _ClassVar[int]
        FOREIGN_CURRENCY_COSTS_RELATIVE_FIELD_NUMBER: _ClassVar[int]
        INSTRUMENT_COSTS_ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
        INSTRUMENT_COSTS_CURRENCY_FIELD_NUMBER: _ClassVar[int]
        INSTRUMENT_COSTS_RELATIVE_FIELD_NUMBER: _ClassVar[int]
        IN_COSTS_ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
        IN_COSTS_CURRENCY_FIELD_NUMBER: _ClassVar[int]
        IN_COSTS_RELATIVE_FIELD_NUMBER: _ClassVar[int]
        OUT_COSTS_ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
        OUT_COSTS_CURRENCY_FIELD_NUMBER: _ClassVar[int]
        OUT_COSTS_RELATIVE_FIELD_NUMBER: _ClassVar[int]
        PERFORMANCE_IMPACT_ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
        PERFORMANCE_IMPACT_CURRENCY_FIELD_NUMBER: _ClassVar[int]
        PERFORMANCE_IMPACT_RELATIVE_FIELD_NUMBER: _ClassVar[int]
        SERVICE_COSTS_ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
        SERVICE_COSTS_CURRENCY_FIELD_NUMBER: _ClassVar[int]
        SERVICE_COSTS_RELATIVE_FIELD_NUMBER: _ClassVar[int]
        SUBSIDY_COSTS_ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
        SUBSIDY_COSTS_CURRENCY_FIELD_NUMBER: _ClassVar[int]
        SUBSIDY_COSTS_RELATIVE_FIELD_NUMBER: _ClassVar[int]
        expected_amount: float
        expected_amount_currency: str
        foreign_currency_costs_absolute: float
        foreign_currency_costs_currency: str
        foreign_currency_costs_relative: float
        in_costs_absolute: float
        in_costs_currency: str
        in_costs_relative: float
        instrument_costs_absolute: float
        instrument_costs_currency: str
        instrument_costs_relative: float
        out_costs_absolute: float
        out_costs_currency: str
        out_costs_relative: float
        performance_impact_absolute: float
        performance_impact_currency: str
        performance_impact_relative: float
        service_costs_absolute: float
        service_costs_currency: str
        service_costs_relative: float
        subsidy_costs_absolute: float
        subsidy_costs_currency: str
        subsidy_costs_relative: float
        def __init__(self, in_costs_absolute: _Optional[float] = ..., in_costs_relative: _Optional[float] = ..., in_costs_currency: _Optional[str] = ..., out_costs_absolute: _Optional[float] = ..., out_costs_relative: _Optional[float] = ..., out_costs_currency: _Optional[str] = ..., instrument_costs_absolute: _Optional[float] = ..., instrument_costs_relative: _Optional[float] = ..., instrument_costs_currency: _Optional[str] = ..., service_costs_absolute: _Optional[float] = ..., service_costs_relative: _Optional[float] = ..., service_costs_currency: _Optional[str] = ..., subsidy_costs_absolute: _Optional[float] = ..., subsidy_costs_relative: _Optional[float] = ..., subsidy_costs_currency: _Optional[str] = ..., foreign_currency_costs_absolute: _Optional[float] = ..., foreign_currency_costs_relative: _Optional[float] = ..., foreign_currency_costs_currency: _Optional[str] = ..., performance_impact_absolute: _Optional[float] = ..., performance_impact_relative: _Optional[float] = ..., performance_impact_currency: _Optional[str] = ..., expected_amount: _Optional[float] = ..., expected_amount_currency: _Optional[str] = ...) -> None: ...
    class CategoryCost(_message.Message):
        __slots__ = ["category_id", "category_label", "currency", "detail_costs", "total_sum_absolute", "total_sum_relative"]
        CATEGORY_ID_FIELD_NUMBER: _ClassVar[int]
        CATEGORY_LABEL_FIELD_NUMBER: _ClassVar[int]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        DETAIL_COSTS_FIELD_NUMBER: _ClassVar[int]
        TOTAL_SUM_ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
        TOTAL_SUM_RELATIVE_FIELD_NUMBER: _ClassVar[int]
        category_id: str
        category_label: str
        currency: str
        detail_costs: _containers.RepeatedCompositeFieldContainer[OrderCosts.DetailCost]
        total_sum_absolute: float
        total_sum_relative: float
        def __init__(self, category_id: _Optional[str] = ..., category_label: _Optional[str] = ..., total_sum_absolute: _Optional[float] = ..., total_sum_relative: _Optional[float] = ..., currency: _Optional[str] = ..., detail_costs: _Optional[_Iterable[_Union[OrderCosts.DetailCost, _Mapping]]] = ...) -> None: ...
    class DetailCost(_message.Message):
        __slots__ = ["currency", "detail_id", "detail_label", "detail_type", "value_absolute", "value_relative"]
        CURRENCY_FIELD_NUMBER: _ClassVar[int]
        DETAIL_ID_FIELD_NUMBER: _ClassVar[int]
        DETAIL_LABEL_FIELD_NUMBER: _ClassVar[int]
        DETAIL_TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_ABSOLUTE_FIELD_NUMBER: _ClassVar[int]
        VALUE_RELATIVE_FIELD_NUMBER: _ClassVar[int]
        currency: str
        detail_id: str
        detail_label: str
        detail_type: str
        value_absolute: float
        value_relative: float
        def __init__(self, detail_id: _Optional[str] = ..., detail_label: _Optional[str] = ..., value_absolute: _Optional[float] = ..., value_relative: _Optional[float] = ..., currency: _Optional[str] = ..., detail_type: _Optional[str] = ...) -> None: ...
    AGGREGATED_COSTS_FIELD_NUMBER: _ClassVar[int]
    CATEGORIE_COSTS_FIELD_NUMBER: _ClassVar[int]
    COST_ID_FIELD_NUMBER: _ClassVar[int]
    ESTIMATED_TOTAL_COSTS_FIELD_NUMBER: _ClassVar[int]
    aggregated_costs: OrderCosts.AggregatedCosts
    categorie_costs: _containers.RepeatedCompositeFieldContainer[OrderCosts.CategoryCost]
    cost_id: str
    estimated_total_costs: float
    def __init__(self, estimated_total_costs: _Optional[float] = ..., cost_id: _Optional[str] = ..., categorie_costs: _Optional[_Iterable[_Union[OrderCosts.CategoryCost, _Mapping]]] = ..., aggregated_costs: _Optional[_Union[OrderCosts.AggregatedCosts, _Mapping]] = ...) -> None: ...

class OrderReply(_message.Message):
    __slots__ = ["account", "error", "order", "order_costs"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORDER_COSTS_FIELD_NUMBER: _ClassVar[int]
    ORDER_FIELD_NUMBER: _ClassVar[int]
    account: _AccountService_pb2.TradingAccount
    error: _Common_pb2.Error
    order: Order
    order_costs: OrderCosts
    def __init__(self, account: _Optional[_Union[_AccountService_pb2.TradingAccount, _Mapping]] = ..., order: _Optional[_Union[Order, _Mapping]] = ..., order_costs: _Optional[_Union[OrderCosts, _Mapping]] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class Orders(_message.Message):
    __slots__ = ["account", "error", "orders"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORDERS_FIELD_NUMBER: _ClassVar[int]
    account: _AccountService_pb2.TradingAccount
    error: _Common_pb2.Error
    orders: _containers.RepeatedCompositeFieldContainer[Order]
    def __init__(self, account: _Optional[_Union[_AccountService_pb2.TradingAccount, _Mapping]] = ..., orders: _Optional[_Iterable[_Union[Order, _Mapping]]] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class QuoteEntry(_message.Message):
    __slots__ = ["buy_price", "buy_volume", "currency", "error", "last_price", "last_time", "last_volume", "order_type", "quote_reference", "sell_price", "sell_volume", "stock_exchange"]
    BUY_PRICE_FIELD_NUMBER: _ClassVar[int]
    BUY_VOLUME_FIELD_NUMBER: _ClassVar[int]
    CURRENCY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    LAST_PRICE_FIELD_NUMBER: _ClassVar[int]
    LAST_TIME_FIELD_NUMBER: _ClassVar[int]
    LAST_VOLUME_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    QUOTE_REFERENCE_FIELD_NUMBER: _ClassVar[int]
    SELL_PRICE_FIELD_NUMBER: _ClassVar[int]
    SELL_VOLUME_FIELD_NUMBER: _ClassVar[int]
    STOCK_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    buy_price: float
    buy_volume: float
    currency: str
    error: _Common_pb2.Error
    last_price: float
    last_time: _Common_pb2.Timestamp
    last_volume: float
    order_type: _TradingTypes_pb2.OrderType
    quote_reference: str
    sell_price: float
    sell_volume: float
    stock_exchange: _StockExchangeService_pb2.StockExchange
    def __init__(self, stock_exchange: _Optional[_Union[_StockExchangeService_pb2.StockExchange, _Mapping]] = ..., buy_price: _Optional[float] = ..., buy_volume: _Optional[float] = ..., sell_price: _Optional[float] = ..., sell_volume: _Optional[float] = ..., last_price: _Optional[float] = ..., last_volume: _Optional[float] = ..., last_time: _Optional[_Union[_Common_pb2.Timestamp, _Mapping]] = ..., currency: _Optional[str] = ..., quote_reference: _Optional[str] = ..., order_type: _Optional[_Union[_TradingTypes_pb2.OrderType, str]] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class QuoteReply(_message.Message):
    __slots__ = ["error", "order_type", "price_entries", "security_code"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    PRICE_ENTRIES_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CODE_FIELD_NUMBER: _ClassVar[int]
    error: _Common_pb2.Error
    order_type: _TradingTypes_pb2.OrderType
    price_entries: _containers.RepeatedCompositeFieldContainer[QuoteEntry]
    security_code: _SecurityService_pb2.SecurityCode
    def __init__(self, security_code: _Optional[_Union[_SecurityService_pb2.SecurityCode, _Mapping]] = ..., order_type: _Optional[_Union[_TradingTypes_pb2.OrderType, str]] = ..., price_entries: _Optional[_Iterable[_Union[QuoteEntry, _Mapping]]] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class QuoteRequest(_message.Message):
    __slots__ = ["access_token", "amount", "order_type", "security_code", "stock_exchanges"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    ORDER_TYPE_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CODE_FIELD_NUMBER: _ClassVar[int]
    STOCK_EXCHANGES_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    amount: float
    order_type: _TradingTypes_pb2.OrderType
    security_code: _SecurityService_pb2.SecurityCode
    stock_exchanges: _containers.RepeatedCompositeFieldContainer[_StockExchangeService_pb2.StockExchange]
    def __init__(self, access_token: _Optional[str] = ..., security_code: _Optional[_Union[_SecurityService_pb2.SecurityCode, _Mapping]] = ..., order_type: _Optional[_Union[_TradingTypes_pb2.OrderType, str]] = ..., amount: _Optional[float] = ..., stock_exchanges: _Optional[_Iterable[_Union[_StockExchangeService_pb2.StockExchange, _Mapping]]] = ...) -> None: ...

class OrderStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class Validation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
