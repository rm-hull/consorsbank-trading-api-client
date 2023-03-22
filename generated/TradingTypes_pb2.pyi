from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

ABSOLUTE: TrailingNotation
AUCTION: CashQuotation
BUY: OrderType
CLOSING: CashQuotation
DESCRIPTOR: _descriptor.FileDescriptor
FILL_OR_KILL: OrderSupplement
FORCED_COVER: OrderType
ICEBERG: OrderSupplement
IMMIDIATE_OR_CANCEL: OrderSupplement
INTRADAY: CashQuotation
KASSA: CashQuotation
LIMIT: OrderModel
MARKET: OrderModel
MARKET_PRICE: OrderSupplement
NORMAL: OrderSupplement
NOTHING: CashQuotation
NO_ORDER_MODEL: OrderModel
NO_ORDER_TYPE: OrderType
NO_TRAILING_NOTATION: TrailingNotation
ONE_CANCELS_OTHER_LIMIT: OrderModel
ONE_CANCELS_OTHER_MARKET: OrderModel
OPENING: CashQuotation
RELATIVE: TrailingNotation
SELL: OrderType
SHORT_COVER: OrderType
SHORT_SELL: OrderType
STOP_LIMIT: OrderModel
STOP_MARKET: OrderModel
TRAILING_STOP_LIMIT: OrderModel
TRAILING_STOP_MARKET: OrderModel

class TradingPossibility(_message.Message):
    __slots__ = ["cash_quotations", "order_model", "order_supplement", "trailing_notation"]
    CASH_QUOTATIONS_FIELD_NUMBER: _ClassVar[int]
    ORDER_MODEL_FIELD_NUMBER: _ClassVar[int]
    ORDER_SUPPLEMENT_FIELD_NUMBER: _ClassVar[int]
    TRAILING_NOTATION_FIELD_NUMBER: _ClassVar[int]
    cash_quotations: _containers.RepeatedScalarFieldContainer[CashQuotation]
    order_model: OrderModel
    order_supplement: OrderSupplement
    trailing_notation: TrailingNotation
    def __init__(self, order_model: _Optional[_Union[OrderModel, str]] = ..., order_supplement: _Optional[_Union[OrderSupplement, str]] = ..., trailing_notation: _Optional[_Union[TrailingNotation, str]] = ..., cash_quotations: _Optional[_Iterable[_Union[CashQuotation, str]]] = ...) -> None: ...

class OrderModel(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class OrderType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class OrderSupplement(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class TrailingNotation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class CashQuotation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
