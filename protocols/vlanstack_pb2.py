# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: vlanstack.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='vlanstack.proto',
  package='OstProto',
  serialized_pb=_b('\n\x0fvlanstack.proto\x12\x08OstProto\x1a\x0eprotocol.proto\"\x0b\n\tVlanStack:;\n\tvlanStack\x12\x12.OstProto.Protocol\x18\xd0\x01 \x01(\x0b\x32\x13.OstProto.VlanStack')
  ,
  dependencies=[protocol_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


VLANSTACK_FIELD_NUMBER = 208
vlanStack = _descriptor.FieldDescriptor(
  name='vlanStack', full_name='OstProto.vlanStack', index=0,
  number=208, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_VLANSTACK = _descriptor.Descriptor(
  name='VlanStack',
  full_name='OstProto.VlanStack',
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
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=56,
)

DESCRIPTOR.message_types_by_name['VlanStack'] = _VLANSTACK
DESCRIPTOR.extensions_by_name['vlanStack'] = vlanStack

VlanStack = _reflection.GeneratedProtocolMessageType('VlanStack', (_message.Message,), dict(
  DESCRIPTOR = _VLANSTACK,
  __module__ = 'vlanstack_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.VlanStack)
  ))
_sym_db.RegisterMessage(VlanStack)

vlanStack.message_type = _VLANSTACK
protocol_pb2.Protocol.RegisterExtension(vlanStack)

# @@protoc_insertion_point(module_scope)
