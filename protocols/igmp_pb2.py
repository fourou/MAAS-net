# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: igmp.proto

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
import gmp_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='igmp.proto',
  package='OstProto',
  serialized_pb=_b('\n\nigmp.proto\x12\x08OstProto\x1a\x0eprotocol.proto\x1a\tgmp.proto:0\n\x04igmp\x12\x12.OstProto.Protocol\x18\x93\x03 \x01(\x0b\x32\r.OstProto.Gmp')
  ,
  dependencies=[protocol_pb2.DESCRIPTOR,gmp_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


IGMP_FIELD_NUMBER = 403
igmp = _descriptor.FieldDescriptor(
  name='igmp', full_name='OstProto.igmp', index=0,
  number=403, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)

DESCRIPTOR.extensions_by_name['igmp'] = igmp

igmp.message_type = gmp_pb2._GMP
protocol_pb2.Protocol.RegisterExtension(igmp)

# @@protoc_insertion_point(module_scope)
