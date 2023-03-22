import Common_pb2 as _Common_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoginReply(_message.Message):
    __slots__ = ["access_token", "error"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    error: _Common_pb2.Error
    def __init__(self, access_token: _Optional[str] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class LoginRequest(_message.Message):
    __slots__ = ["secret"]
    SECRET_FIELD_NUMBER: _ClassVar[int]
    secret: str
    def __init__(self, secret: _Optional[str] = ...) -> None: ...

class LogoutReply(_message.Message):
    __slots__ = ["error"]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    error: _Common_pb2.Error
    def __init__(self, error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class LogoutRequest(_message.Message):
    __slots__ = ["access_token"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    def __init__(self, access_token: _Optional[str] = ...) -> None: ...
