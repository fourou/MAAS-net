# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ip6over6.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import protocol_pb2
import ip6_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ip6over6.proto',
  package='OstProto',
  serialized_pb=_b('\n\x0eip6over6.proto\x12\x08OstProto\x1a\x0eprotocol.proto\x1a\tip6.proto\"\x10\n\x08Ip6over6*\x04\x08\x01\x10\x03:4\n\tip6_outer\x12\x12.OstProto.Ip6over6\x18\x01 \x01(\x0b\x32\r.OstProto.Ip6:4\n\tip6_inner\x12\x12.OstProto.Ip6over6\x18\x02 \x01(\x0b\x32\r.OstProto.Ip6:9\n\x08ip6over6\x12\x12.OstProto.Protocol\x18\xb2\x02 \x01(\x0b\x32\x12.OstProto.Ip6over6')
  ,
  dependencies=[protocol_pb2.DESCRIPTOR,ip6_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


IP6_OUTER_FIELD_NUMBER = 1
ip6_outer = _descriptor.FieldDescriptor(
  name='ip6_outer', full_name='OstProto.ip6_outer', index=0,
  number=1, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
IP6_INNER_FIELD_NUMBER = 2
ip6_inner = _descriptor.FieldDescriptor(
  name='ip6_inner', full_name='OstProto.ip6_inner', index=1,
  number=2, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
IP6OVER6_FIELD_NUMBER = 306
ip6over6 = _descriptor.FieldDescriptor(
  name='ip6over6', full_name='OstProto.ip6over6', index=2,
  number=306, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_IP6OVER6 = _descriptor.Descriptor(
  name='Ip6over6',
  full_name='OstProto.Ip6over6',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=True,
  extension_ranges=[(1, 3), ],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=71,
)

DESCRIPTOR.message_types_by_name['Ip6over6'] = _IP6OVER6
DESCRIPTOR.extensions_by_name['ip6_outer'] = ip6_outer
DESCRIPTOR.extensions_by_name['ip6_inner'] = ip6_inner
DESCRIPTOR.extensions_by_name['ip6over6'] = ip6over6

Ip6over6 = _reflection.GeneratedProtocolMessageType('Ip6over6', (_message.Message,), dict(
  DESCRIPTOR = _IP6OVER6,
  __module__ = 'ip6over6_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.Ip6over6)
  ))
_sym_db.RegisterMessage(Ip6over6)

ip6_outer.message_type = ip6_pb2._IP6
Ip6over6.RegisterExtension(ip6_outer)
ip6_inner.message_type = ip6_pb2._IP6
Ip6over6.RegisterExtension(ip6_inner)
ip6over6.message_type = _IP6OVER6
protocol_pb2.Protocol.RegisterExtension(ip6over6)

# @@protoc_insertion_point(module_scope)
