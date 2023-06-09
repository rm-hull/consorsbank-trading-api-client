# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TradingTypes.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12TradingTypes.proto\x12 com.consorsbank.module.tapi.grpc\"\xbd\x02\n\x12TradingPossibility\x12\x41\n\x0border_model\x18\x01 \x01(\x0e\x32,.com.consorsbank.module.tapi.grpc.OrderModel\x12K\n\x10order_supplement\x18\x02 \x01(\x0e\x32\x31.com.consorsbank.module.tapi.grpc.OrderSupplement\x12M\n\x11trailing_notation\x18\x03 \x01(\x0e\x32\x32.com.consorsbank.module.tapi.grpc.TrailingNotation\x12H\n\x0f\x63\x61sh_quotations\x18\x04 \x03(\x0e\x32/.com.consorsbank.module.tapi.grpc.CashQuotation*\xc6\x01\n\nOrderModel\x12\x12\n\x0eNO_ORDER_MODEL\x10\x00\x12\n\n\x06MARKET\x10\x01\x12\t\n\x05LIMIT\x10\x02\x12\x0f\n\x0bSTOP_MARKET\x10\x03\x12\x0e\n\nSTOP_LIMIT\x10\x04\x12\x1c\n\x18ONE_CANCELS_OTHER_MARKET\x10\x05\x12\x1b\n\x17ONE_CANCELS_OTHER_LIMIT\x10\x06\x12\x18\n\x14TRAILING_STOP_MARKET\x10\x07\x12\x17\n\x13TRAILING_STOP_LIMIT\x10\x08*d\n\tOrderType\x12\x11\n\rNO_ORDER_TYPE\x10\x00\x12\x07\n\x03\x42UY\x10\x01\x12\x08\n\x04SELL\x10\x02\x12\x0e\n\nSHORT_SELL\x10\x03\x12\x0f\n\x0bSHORT_COVER\x10\x04\x12\x10\n\x0c\x46ORCED_COVER\x10\x05*g\n\x0fOrderSupplement\x12\n\n\x06NORMAL\x10\x00\x12\x17\n\x13IMMIDIATE_OR_CANCEL\x10\x01\x12\x10\n\x0c\x46ILL_OR_KILL\x10\x02\x12\x0b\n\x07ICEBERG\x10\x03\x12\x10\n\x0cMARKET_PRICE\x10\x04*H\n\x10TrailingNotation\x12\x18\n\x14NO_TRAILING_NOTATION\x10\x00\x12\x0c\n\x08\x41\x42SOLUTE\x10\x01\x12\x0c\n\x08RELATIVE\x10\x02*\\\n\rCashQuotation\x12\x0b\n\x07NOTHING\x10\x00\x12\t\n\x05KASSA\x10\x01\x12\x0b\n\x07\x41UCTION\x10\x02\x12\x0b\n\x07OPENING\x10\x03\x12\x0c\n\x08INTRADAY\x10\x04\x12\x0b\n\x07\x43LOSING\x10\x05\x42,\n(com.consorsbank.module.tapi.grpc.tradingP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'TradingTypes_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n(com.consorsbank.module.tapi.grpc.tradingP\001'
  _ORDERMODEL._serialized_start=377
  _ORDERMODEL._serialized_end=575
  _ORDERTYPE._serialized_start=577
  _ORDERTYPE._serialized_end=677
  _ORDERSUPPLEMENT._serialized_start=679
  _ORDERSUPPLEMENT._serialized_end=782
  _TRAILINGNOTATION._serialized_start=784
  _TRAILINGNOTATION._serialized_end=856
  _CASHQUOTATION._serialized_start=858
  _CASHQUOTATION._serialized_end=950
  _TRADINGPOSSIBILITY._serialized_start=57
  _TRADINGPOSSIBILITY._serialized_end=374
# @@protoc_insertion_point(module_scope)
