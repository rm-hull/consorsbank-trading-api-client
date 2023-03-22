# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: OrderService.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import Common_pb2 as Common__pb2
import SecurityService_pb2 as SecurityService__pb2
import StockExchangeService_pb2 as StockExchangeService__pb2
import AccountService_pb2 as AccountService__pb2
import TradingTypes_pb2 as TradingTypes__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12OrderService.proto\x12 com.consorsbank.module.tapi.grpc\x1a\x0c\x43ommon.proto\x1a\x15SecurityService.proto\x1a\x1aStockExchangeService.proto\x1a\x14\x41\x63\x63ountService.proto\x1a\x12TradingTypes.proto\"\xaf\x07\n\x05Order\x12`\n\x1bsecurity_with_stockexchange\x18\x01 \x01(\x0b\x32;.com.consorsbank.module.tapi.grpc.SecurityWithStockExchange\x12?\n\norder_type\x18\x02 \x01(\x0e\x32+.com.consorsbank.module.tapi.grpc.OrderType\x12\x14\n\x0corder_number\x18\x03 \x01(\t\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x01\x12\x41\n\x0border_model\x18\x05 \x01(\x0e\x32,.com.consorsbank.module.tapi.grpc.OrderModel\x12K\n\x10order_supplement\x18\x06 \x01(\x0e\x32\x31.com.consorsbank.module.tapi.grpc.OrderSupplement\x12G\n\x0e\x63\x61sh_quotation\x18\x07 \x01(\x0e\x32/.com.consorsbank.module.tapi.grpc.CashQuotation\x12\x17\n\x0f\x65xecuted_amount\x18\x08 \x01(\x01\x12\x43\n\x0corder_status\x18\t \x01(\x0e\x32-.com.consorsbank.module.tapi.grpc.OrderStatus\x12\x45\n\x10status_timestamp\x18\n \x01(\x0b\x32+.com.consorsbank.module.tapi.grpc.Timestamp\x12=\n\rvalidity_date\x18\x0b \x01(\x0b\x32&.com.consorsbank.module.tapi.grpc.Date\x12\r\n\x05limit\x18\x0c \x01(\x01\x12\x0c\n\x04stop\x18\r \x01(\x01\x12\x12\n\nstop_limit\x18\x0e \x01(\x01\x12\x19\n\x11trailing_distance\x18\x0f \x01(\x01\x12M\n\x11trailing_notation\x18\x10 \x01(\x0e\x32\x32.com.consorsbank.module.tapi.grpc.TrailingNotation\x12 \n\x18trailing_limit_tolerance\x18\x11 \x01(\x01\x12\x19\n\x11\x64ripping_quantity\x18\x12 \x01(\x01\x12\x1c\n\x14trading_partner_name\x18\x13 \x01(\t\x12\x17\n\x0f\x65xecution_quote\x18\x14 \x01(\x01\x12\x11\n\tunique_id\x18\x15 \x01(\t\"\xf6\x07\n\x0f\x41\x64\x64OrderRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x02 \x01(\t\x12`\n\x1bsecurity_with_stockexchange\x18\x03 \x01(\x0b\x32;.com.consorsbank.module.tapi.grpc.SecurityWithStockExchange\x12?\n\norder_type\x18\x04 \x01(\x0e\x32+.com.consorsbank.module.tapi.grpc.OrderType\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x01\x12\x41\n\x0border_model\x18\x06 \x01(\x0e\x32,.com.consorsbank.module.tapi.grpc.OrderModel\x12K\n\x10order_supplement\x18\x07 \x01(\x0e\x32\x31.com.consorsbank.module.tapi.grpc.OrderSupplement\x12G\n\x0e\x63\x61sh_quotation\x18\x08 \x01(\x0e\x32/.com.consorsbank.module.tapi.grpc.CashQuotation\x12=\n\rvalidity_date\x18\t \x01(\x0b\x32&.com.consorsbank.module.tapi.grpc.Date\x12\r\n\x05limit\x18\n \x01(\x01\x12\x0c\n\x04stop\x18\x0b \x01(\x01\x12\x12\n\nstop_limit\x18\x0c \x01(\x01\x12\x19\n\x11trailing_distance\x18\r \x01(\x01\x12M\n\x11trailing_notation\x18\x0e \x01(\x0e\x32\x32.com.consorsbank.module.tapi.grpc.TrailingNotation\x12 \n\x18trailing_limit_tolerance\x18\x0f \x01(\x01\x12\x19\n\x11\x64ripping_quantity\x18\x10 \x01(\x01\x12\x13\n\x0bposition_id\x18\x11 \x01(\t\x12@\n\nvalidation\x18\x12 \x01(\x0e\x32,.com.consorsbank.module.tapi.grpc.Validation\x12\x1b\n\x13risk_class_override\x18\x13 \x01(\x08\x12\x1e\n\x16target_market_override\x18\x14 \x01(\x08\x12#\n\x1btax_nontransparent_override\x18\x15 \x01(\x08\x12\x1e\n\x16\x61\x63\x63\x65pt_additional_fees\x18\x16 \x01(\x08\x12\'\n\x1f\x63losed_realestate_fond_override\x18\x17 \x01(\x08\x12\x10\n\x08inactive\x18\x18 \x01(\x08\"\x83\x02\n\nOrderReply\x12\x41\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x30.com.consorsbank.module.tapi.grpc.TradingAccount\x12\x36\n\x05order\x18\x02 \x01(\x0b\x32\'.com.consorsbank.module.tapi.grpc.Order\x12\x41\n\x0border_costs\x18\x03 \x01(\x0b\x32,.com.consorsbank.module.tapi.grpc.OrderCosts\x12\x37\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\'.com.consorsbank.module.tapi.grpc.Error\"\xd5\n\n\nOrderCosts\x12\x1d\n\x15\x65stimated_total_costs\x18\x01 \x01(\x01\x12\x0f\n\x07\x63ost_id\x18\x02 \x01(\t\x12R\n\x0f\x63\x61tegorie_costs\x18\x03 \x03(\x0b\x32\x39.com.consorsbank.module.tapi.grpc.OrderCosts.CategoryCost\x12V\n\x10\x61ggregated_costs\x18\x04 \x01(\x0b\x32<.com.consorsbank.module.tapi.grpc.OrderCosts.AggregatedCosts\x1a\xd4\x01\n\x0c\x43\x61tegoryCost\x12\x13\n\x0b\x63\x61tegory_id\x18\x01 \x01(\t\x12\x16\n\x0e\x63\x61tegory_label\x18\x02 \x01(\t\x12\x1a\n\x12total_sum_absolute\x18\x03 \x01(\x01\x12\x1a\n\x12total_sum_relative\x18\x04 \x01(\x01\x12\x10\n\x08\x63urrency\x18\x05 \x01(\t\x12M\n\x0c\x64\x65tail_costs\x18\x06 \x03(\x0b\x32\x37.com.consorsbank.module.tapi.grpc.OrderCosts.DetailCost\x1a\x84\x06\n\x0f\x41ggregatedCosts\x12\x19\n\x11in_costs_absolute\x18\x01 \x01(\x01\x12\x19\n\x11in_costs_relative\x18\x02 \x01(\x01\x12\x19\n\x11in_costs_currency\x18\x03 \x01(\t\x12\x1a\n\x12out_costs_absolute\x18\x04 \x01(\x01\x12\x1a\n\x12out_costs_relative\x18\x05 \x01(\x01\x12\x1a\n\x12out_costs_currency\x18\x06 \x01(\t\x12!\n\x19instrument_costs_absolute\x18\x07 \x01(\x01\x12!\n\x19instrument_costs_relative\x18\x08 \x01(\x01\x12!\n\x19instrument_costs_currency\x18\t \x01(\t\x12\x1e\n\x16service_costs_absolute\x18\n \x01(\x01\x12\x1e\n\x16service_costs_relative\x18\x0b \x01(\x01\x12\x1e\n\x16service_costs_currency\x18\x0c \x01(\t\x12\x1e\n\x16subsidy_costs_absolute\x18\r \x01(\x01\x12\x1e\n\x16subsidy_costs_relative\x18\x0e \x01(\x01\x12\x1e\n\x16subsidy_costs_currency\x18\x0f \x01(\t\x12\'\n\x1f\x66oreign_currency_costs_absolute\x18\x10 \x01(\x01\x12\'\n\x1f\x66oreign_currency_costs_relative\x18\x11 \x01(\x01\x12\'\n\x1f\x66oreign_currency_costs_currency\x18\x12 \x01(\t\x12#\n\x1bperformance_impact_absolute\x18\x13 \x01(\x01\x12#\n\x1bperformance_impact_relative\x18\x14 \x01(\x01\x12#\n\x1bperformance_impact_currency\x18\x15 \x01(\t\x12\x17\n\x0f\x65xpected_amount\x18\x16 \x01(\x01\x12 \n\x18\x65xpected_amount_currency\x18\x17 \x01(\t\x1a\x8c\x01\n\nDetailCost\x12\x11\n\tdetail_id\x18\x01 \x01(\t\x12\x14\n\x0c\x64\x65tail_label\x18\x02 \x01(\t\x12\x16\n\x0evalue_absolute\x18\x03 \x01(\x01\x12\x16\n\x0evalue_relative\x18\x04 \x01(\x01\x12\x10\n\x08\x63urrency\x18\x05 \x01(\t\x12\x13\n\x0b\x64\x65tail_type\x18\x06 \x01(\t\"\x82\x04\n\x12\x43hangeOrderRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x02 \x01(\t\x12\x14\n\x0corder_number\x18\x03 \x01(\t\x12\r\n\x05limit\x18\x04 \x01(\x01\x12\x0c\n\x04stop\x18\x05 \x01(\x01\x12\x12\n\nstop_limit\x18\x06 \x01(\x01\x12\x0e\n\x06\x61mount\x18\x07 \x01(\x01\x12=\n\rvalidity_date\x18\x08 \x01(\x0b\x32&.com.consorsbank.module.tapi.grpc.Date\x12\x41\n\x0border_model\x18\t \x01(\x0e\x32,.com.consorsbank.module.tapi.grpc.OrderModel\x12K\n\x10order_supplement\x18\n \x01(\x0e\x32\x31.com.consorsbank.module.tapi.grpc.OrderSupplement\x12\x19\n\x11\x64ripping_quantity\x18\x0b \x01(\x01\x12@\n\nvalidation\x18\x0c \x01(\x0e\x32,.com.consorsbank.module.tapi.grpc.Validation\x12\x19\n\x11trailing_distance\x18\r \x01(\x01\x12 \n\x18trailing_limit_tolerance\x18\x0e \x01(\x01\"\x9a\x01\n\x12\x43\x61ncelOrderRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x02 \x01(\t\x12\x14\n\x0corder_number\x18\x03 \x01(\t\x12@\n\nvalidation\x18\x04 \x01(\x0e\x32,.com.consorsbank.module.tapi.grpc.Validation\"\x9c\x01\n\x14\x41\x63tivateOrderRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x02 \x01(\t\x12\x14\n\x0corder_number\x18\x03 \x01(\t\x12@\n\nvalidation\x18\x04 \x01(\x0e\x32,.com.consorsbank.module.tapi.grpc.Validation\"\x9e\x01\n\x16\x44\x65\x61\x63tivateOrderRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x02 \x01(\t\x12\x14\n\x0corder_number\x18\x03 \x01(\t\x12@\n\nvalidation\x18\x04 \x01(\x0e\x32,.com.consorsbank.module.tapi.grpc.Validation\"\xe1\x03\n\x12\x41\x63\x63\x65ptQuoteRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x16\n\x0e\x61\x63\x63ount_number\x18\x02 \x01(\t\x12`\n\x1bsecurity_with_stockexchange\x18\x03 \x01(\x0b\x32;.com.consorsbank.module.tapi.grpc.SecurityWithStockExchange\x12?\n\norder_type\x18\x04 \x01(\x0e\x32+.com.consorsbank.module.tapi.grpc.OrderType\x12\x0e\n\x06\x61mount\x18\x05 \x01(\x01\x12\r\n\x05limit\x18\x06 \x01(\x01\x12\x17\n\x0fquote_reference\x18\x07 \x01(\t\x12@\n\nvalidation\x18\x08 \x01(\x0e\x32,.com.consorsbank.module.tapi.grpc.Validation\x12\x1b\n\x13risk_class_override\x18\t \x01(\x08\x12\x1e\n\x16target_market_override\x18\n \x01(\x08\x12#\n\x1btax_nontransparent_override\x18\x0b \x01(\x08\x12\x1e\n\x16\x61\x63\x63\x65pt_additional_fees\x18\x0c \x01(\x08\"\x86\x02\n\x0cQuoteRequest\x12\x14\n\x0c\x61\x63\x63\x65ss_token\x18\x01 \x01(\t\x12\x45\n\rsecurity_code\x18\x02 \x01(\x0b\x32..com.consorsbank.module.tapi.grpc.SecurityCode\x12?\n\norder_type\x18\x03 \x01(\x0e\x32+.com.consorsbank.module.tapi.grpc.OrderType\x12\x0e\n\x06\x61mount\x18\x04 \x01(\x01\x12H\n\x0fstock_exchanges\x18\x05 \x03(\x0b\x32/.com.consorsbank.module.tapi.grpc.StockExchange\"\x92\x02\n\nQuoteReply\x12\x45\n\rsecurity_code\x18\x01 \x01(\x0b\x32..com.consorsbank.module.tapi.grpc.SecurityCode\x12?\n\norder_type\x18\x02 \x01(\x0e\x32+.com.consorsbank.module.tapi.grpc.OrderType\x12\x43\n\rprice_entries\x18\x03 \x03(\x0b\x32,.com.consorsbank.module.tapi.grpc.QuoteEntry\x12\x37\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\'.com.consorsbank.module.tapi.grpc.Error\"\xb3\x03\n\nQuoteEntry\x12G\n\x0estock_exchange\x18\x01 \x01(\x0b\x32/.com.consorsbank.module.tapi.grpc.StockExchange\x12\x11\n\tbuy_price\x18\x02 \x01(\x01\x12\x12\n\nbuy_volume\x18\x03 \x01(\x01\x12\x12\n\nsell_price\x18\x04 \x01(\x01\x12\x13\n\x0bsell_volume\x18\x05 \x01(\x01\x12\x12\n\nlast_price\x18\x06 \x01(\x01\x12\x13\n\x0blast_volume\x18\x07 \x01(\x01\x12>\n\tlast_time\x18\x08 \x01(\x0b\x32+.com.consorsbank.module.tapi.grpc.Timestamp\x12\x10\n\x08\x63urrency\x18\t \x01(\t\x12\x17\n\x0fquote_reference\x18\n \x01(\t\x12?\n\norder_type\x18\x0b \x01(\x0e\x32+.com.consorsbank.module.tapi.grpc.OrderType\x12\x37\n\x05\x65rror\x18\xe8\x07 \x01(\x0b\x32\'.com.consorsbank.module.tapi.grpc.Error\"\xbd\x01\n\x06Orders\x12\x41\n\x07\x61\x63\x63ount\x18\x01 \x01(\x0b\x32\x30.com.consorsbank.module.tapi.grpc.TradingAccount\x12\x37\n\x06orders\x18\x02 \x03(\x0b\x32\'.com.consorsbank.module.tapi.grpc.Order\x12\x37\n\x05\x65rror\x18\xa8\x46 \x01(\x0b\x32\'.com.consorsbank.module.tapi.grpc.Error*\xf6\x01\n\x0bOrderStatus\x12\x13\n\x0fNO_ORDER_STATUS\x10\x00\x12\x07\n\x03NEW\x10\x01\x12\x08\n\x04OPEN\x10\x02\x12\x0c\n\x08\x45XECUTED\x10\x03\x12\x16\n\x12PARTIALLY_EXECUTED\x10\x04\x12\x0c\n\x08\x43\x41NCELED\x10\x05\x12\x13\n\x0f\x43\x41NCELED_FORCED\x10\x06\x12\x12\n\x0e\x43\x41NCELED_NOTED\x10\x07\x12\x14\n\x10\x43\x41NCELED_TIMEOUT\x10\x08\x12\x0b\n\x07\x43HANGED\x10\t\x12\x11\n\rCHANGED_NOTED\x10\n\x12\x0c\n\x08INACTIVE\x10\x0b\x12\x12\n\x0eINACTIVE_NOTED\x10\x0c\x12\n\n\x06STORNO\x10\r*\x8c\x01\n\nValidation\x12\x16\n\x12WITHOUT_VALIDATION\x10\x00\x12\x11\n\rVALIDATE_ONLY\x10\x01\x12\x1d\n\x19VALIDATE_WITH_TOTAL_COSTS\x10\x02\x12\x1e\n\x1aVALIDATE_WITH_DETAIL_COSTS\x10\x03\x12\x14\n\x10TOTAL_COSTS_ONLY\x10\x04\x42*\n&com.consorsbank.module.tapi.grpc.orderP\x01\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'OrderService_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n&com.consorsbank.module.tapi.grpc.orderP\001'
  _ORDERSTATUS._serialized_start=6407
  _ORDERSTATUS._serialized_end=6653
  _VALIDATION._serialized_start=6656
  _VALIDATION._serialized_end=6796
  _ORDER._serialized_start=164
  _ORDER._serialized_end=1107
  _ADDORDERREQUEST._serialized_start=1110
  _ADDORDERREQUEST._serialized_end=2124
  _ORDERREPLY._serialized_start=2127
  _ORDERREPLY._serialized_end=2386
  _ORDERCOSTS._serialized_start=2389
  _ORDERCOSTS._serialized_end=3754
  _ORDERCOSTS_CATEGORYCOST._serialized_start=2624
  _ORDERCOSTS_CATEGORYCOST._serialized_end=2836
  _ORDERCOSTS_AGGREGATEDCOSTS._serialized_start=2839
  _ORDERCOSTS_AGGREGATEDCOSTS._serialized_end=3611
  _ORDERCOSTS_DETAILCOST._serialized_start=3614
  _ORDERCOSTS_DETAILCOST._serialized_end=3754
  _CHANGEORDERREQUEST._serialized_start=3757
  _CHANGEORDERREQUEST._serialized_end=4271
  _CANCELORDERREQUEST._serialized_start=4274
  _CANCELORDERREQUEST._serialized_end=4428
  _ACTIVATEORDERREQUEST._serialized_start=4431
  _ACTIVATEORDERREQUEST._serialized_end=4587
  _DEACTIVATEORDERREQUEST._serialized_start=4590
  _DEACTIVATEORDERREQUEST._serialized_end=4748
  _ACCEPTQUOTEREQUEST._serialized_start=4751
  _ACCEPTQUOTEREQUEST._serialized_end=5232
  _QUOTEREQUEST._serialized_start=5235
  _QUOTEREQUEST._serialized_end=5497
  _QUOTEREPLY._serialized_start=5500
  _QUOTEREPLY._serialized_end=5774
  _QUOTEENTRY._serialized_start=5777
  _QUOTEENTRY._serialized_end=6212
  _ORDERS._serialized_start=6215
  _ORDERS._serialized_end=6404
# @@protoc_insertion_point(module_scope)
