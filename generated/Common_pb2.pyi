from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor
MISK: UnitNote
NOT_TRADABLE: TradingState
NO_TRADING_STATE: TradingState
NO_UNIT_NOTE: UnitNote
PERCENT: UnitNote
PERMIL: UnitNote
PIECE: UnitNote
POINTS: UnitNote
TRADABLE: TradingState

class AccessTokenRequest(_message.Message):
    __slots__ = ["access_token"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    def __init__(self, access_token: _Optional[str] = ...) -> None: ...

class Date(_message.Message):
    __slots__ = ["day", "month", "year"]
    DAY_FIELD_NUMBER: _ClassVar[int]
    MONTH_FIELD_NUMBER: _ClassVar[int]
    YEAR_FIELD_NUMBER: _ClassVar[int]
    day: int
    month: int
    year: int
    def __init__(self, year: _Optional[int] = ..., month: _Optional[int] = ..., day: _Optional[int] = ...) -> None: ...

class Empty(_message.Message):
    __slots__ = []
    def __init__(self) -> None: ...

class Error(_message.Message):
    __slots__ = ["code", "message"]
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    code: str
    message: str
    def __init__(self, code: _Optional[str] = ..., message: _Optional[str] = ...) -> None: ...

class Timestamp(_message.Message):
    __slots__ = ["nanos", "seconds"]
    NANOS_FIELD_NUMBER: _ClassVar[int]
    SECONDS_FIELD_NUMBER: _ClassVar[int]
    nanos: int
    seconds: int
    def __init__(self, seconds: _Optional[int] = ..., nanos: _Optional[int] = ...) -> None: ...

class TradingState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []

class UnitNote(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
