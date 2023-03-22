import Common_pb2 as _Common_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TradingAccount(_message.Message):
    __slots__ = ["account_number", "depot_number", "name", "tradable"]
    ACCOUNT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    DEPOT_NUMBER_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TRADABLE_FIELD_NUMBER: _ClassVar[int]
    account_number: str
    depot_number: str
    name: str
    tradable: bool
    def __init__(self, account_number: _Optional[str] = ..., depot_number: _Optional[str] = ..., name: _Optional[str] = ..., tradable: bool = ...) -> None: ...

class TradingAccountInformation(_message.Message):
    __slots__ = ["account", "balance", "buying_power", "buying_power_intraday", "credit_limit", "credit_limit_intraday", "error"]
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    BALANCE_FIELD_NUMBER: _ClassVar[int]
    BUYING_POWER_FIELD_NUMBER: _ClassVar[int]
    BUYING_POWER_INTRADAY_FIELD_NUMBER: _ClassVar[int]
    CREDIT_LIMIT_FIELD_NUMBER: _ClassVar[int]
    CREDIT_LIMIT_INTRADAY_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    account: TradingAccount
    balance: float
    buying_power: float
    buying_power_intraday: float
    credit_limit: float
    credit_limit_intraday: float
    error: _Common_pb2.Error
    def __init__(self, account: _Optional[_Union[TradingAccount, _Mapping]] = ..., balance: _Optional[float] = ..., credit_limit: _Optional[float] = ..., buying_power: _Optional[float] = ..., credit_limit_intraday: _Optional[float] = ..., buying_power_intraday: _Optional[float] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class TradingAccountRequest(_message.Message):
    __slots__ = ["access_token", "trading_account"]
    ACCESS_TOKEN_FIELD_NUMBER: _ClassVar[int]
    TRADING_ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    access_token: str
    trading_account: TradingAccount
    def __init__(self, access_token: _Optional[str] = ..., trading_account: _Optional[_Union[TradingAccount, _Mapping]] = ...) -> None: ...

class TradingAccountTransactions(_message.Message):
    __slots__ = ["account", "error", "transactions"]
    class Transaction(_message.Message):
        __slots__ = ["amount", "information", "opponent", "transaction_date", "value_date"]
        AMOUNT_FIELD_NUMBER: _ClassVar[int]
        INFORMATION_FIELD_NUMBER: _ClassVar[int]
        OPPONENT_FIELD_NUMBER: _ClassVar[int]
        TRANSACTION_DATE_FIELD_NUMBER: _ClassVar[int]
        VALUE_DATE_FIELD_NUMBER: _ClassVar[int]
        amount: float
        information: str
        opponent: str
        transaction_date: _Common_pb2.Date
        value_date: _Common_pb2.Date
        def __init__(self, transaction_date: _Optional[_Union[_Common_pb2.Date, _Mapping]] = ..., amount: _Optional[float] = ..., opponent: _Optional[str] = ..., information: _Optional[str] = ..., value_date: _Optional[_Union[_Common_pb2.Date, _Mapping]] = ...) -> None: ...
    ACCOUNT_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    TRANSACTIONS_FIELD_NUMBER: _ClassVar[int]
    account: TradingAccount
    error: _Common_pb2.Error
    transactions: _containers.RepeatedCompositeFieldContainer[TradingAccountTransactions.Transaction]
    def __init__(self, account: _Optional[_Union[TradingAccount, _Mapping]] = ..., transactions: _Optional[_Iterable[_Union[TradingAccountTransactions.Transaction, _Mapping]]] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...

class TradingAccounts(_message.Message):
    __slots__ = ["accounts", "error"]
    ACCOUNTS_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    accounts: _containers.RepeatedCompositeFieldContainer[TradingAccount]
    error: _Common_pb2.Error
    def __init__(self, accounts: _Optional[_Iterable[_Union[TradingAccount, _Mapping]]] = ..., error: _Optional[_Union[_Common_pb2.Error, _Mapping]] = ...) -> None: ...
