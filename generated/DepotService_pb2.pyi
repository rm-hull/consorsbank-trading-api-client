import Common_pb2 as _Common_pb2
import SecurityService_pb2 as _SecurityService_pb2
import AccountService_pb2 as _AccountService_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DepotEntries(_message.Message):
    __slots__ = ["account", "entries", "error"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ENTRIES_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    account: _AccountService_pb2.TradingAccount
    entries: _containers.RepeatedCompositeFieldContainer[DepotEntry]
    error: _Common_pb2.Error
    def __init__(self, account: _Optional[_Union[_AccountService_pb2.TradingAccount, _Mapping]] = ..., entries: _Optional[_Iterable[_Union[DepotEntry, _Mapping]]] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class DepotEntry(_message.Message):
    __slots__ = ["blocked", "effective_amount", "open_sales", "positions", "purchase_currency", "purchase_currency_rate", "purchase_quotation", "scheduled_amount", "security_code", "sell_possible", "total_amount", "unit_note"]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    EFFECTIVE_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    OPEN_SALES_FIELD_NUMBER: _ClassVar[int]
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_CURRENCY_RATE_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_QUOTATION_FIELD_NUMBER: _ClassVar[int]
    SCHEDULED_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    SECURITY_CODE_FIELD_NUMBER: _ClassVar[int]
    SELL_POSSIBLE_FIELD_NUMBER: _ClassVar[int]
    TOTAL_AMOUNT_FIELD_NUMBER: _ClassVar[int]
    UNIT_NOTE_FIELD_NUMBER: _ClassVar[int]
    blocked: bool
    effective_amount: float
    open_sales: float
    positions: _containers.RepeatedCompositeFieldContainer[DepotPosition]
    purchase_currency: str
    purchase_currency_rate: float
    purchase_quotation: float
    scheduled_amount: float
    security_code: _SecurityService_pb2.SecurityCode
    sell_possible: bool
    total_amount: float
    unit_note: _Common_pb2.UnitNote
    def __init__(self, security_code: _Optional[_Union[_SecurityService_pb2.SecurityCode, _Mapping]] = ..., positions: _Optional[_Iterable[_Union[DepotPosition, _Mapping]]] = ..., effective_amount: _Optional[float] = ..., scheduled_amount: _Optional[float] = ..., total_amount: _Optional[float] = ..., sell_possible: bool = ..., unit_note: _Optional[_Union[_Common_pb2.UnitNote, str]] = ..., blocked: bool = ..., purchase_quotation: _Optional[float] = ..., purchase_currency: _Optional[str] = ..., purchase_currency_rate: _Optional[float] = ..., open_sales: _Optional[float] = ...) -> None: ...

class DepotPosition(_message.Message):
    __slots__ = ["amount", "blocked", "position_id", "purchase_currency", "purchase_currency_rate", "purchase_quotation", "sell_possible", "unit_note"]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    BLOCKED_FIELD_NUMBER: _ClassVar[int]
    POSITION_ID_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_CURRENCY_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_CURRENCY_RATE_FIELD_NUMBER: _ClassVar[int]
    PURCHASE_QUOTATION_FIELD_NUMBER: _ClassVar[int]
    SELL_POSSIBLE_FIELD_NUMBER: _ClassVar[int]
    UNIT_NOTE_FIELD_NUMBER: _ClassVar[int]
    amount: float
    blocked: bool
    position_id: str
    purchase_currency: str
    purchase_currency_rate: float
    purchase_quotation: float
    sell_possible: bool
    unit_note: _Common_pb2.UnitNote
    def __init__(self, amount: _Optional[float] = ..., position_id: _Optional[str] = ..., sell_possible: bool = ..., unit_note: _Optional[_Union[_Common_pb2.UnitNote, str]] = ..., blocked: bool = ..., purchase_quotation: _Optional[float] = ..., purchase_currency: _Optional[str] = ..., purchase_currency_rate: _Optional[float] = ...) -> None: ...
