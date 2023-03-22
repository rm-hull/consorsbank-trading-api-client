import Common_pb2 as _Common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StockExchange(_message.Message):
    __slots__ = ["id", "issuer"]
    ID_FIELD_NUMBER: _ClassVar[int]
    ISSUER_FIELD_NUMBER: _ClassVar[int]
    id: str
    issuer: str
    def __init__(self, id: _Optional[str] = ..., issuer: _Optional[str] = ...) -> None: ...

class StockExchangeDescription(_message.Message):
    __slots__ = ["error", "stock_exchange_info"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STOCK_EXCHANGE_INFO_FIELD_NUMBER: _ClassVar[int]
    error: _Common_pb2.Error
    stock_exchange_info: StockExchangeInfo
    def __init__(self, stock_exchange_info: _Optional[_Union[StockExchangeInfo, _Mapping]] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class StockExchangeDescriptions(_message.Message):
    __slots__ = ["error", "stock_exchange_infos"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    STOCK_EXCHANGE_INFOS_FIELD_NUMBER: _ClassVar[int]
    error: _Common_pb2.Error
    stock_exchange_infos: _containers.RepeatedCompositeFieldContainer[StockExchangeInfo]
    def __init__(self, stock_exchange_infos: _Optional[_Iterable[_Union[StockExchangeInfo, _Mapping]]] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class StockExchangeInfo(_message.Message):
    __slots__ = ["name", "stockExchange"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STOCKEXCHANGE_FIELD_NUMBER: _ClassVar[int]
    name: str
    stockExchange: StockExchange
    def __init__(self, stockExchange: _Optional[_Union[StockExchange, _Mapping]] = ..., name: _Optional[str] = ...) -> None: ...

class StockExchangeRequest(_message.Message):
    __slots__ = ["access_token", "stock_exchange"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    STOCK_EXCHANGE_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    stock_exchange: StockExchange
    def __init__(self, access_token: _Optional[str] = ..., stock_exchange: _Optional[_Union[StockExchange, _Mapping]] = ...) -> None: ...
