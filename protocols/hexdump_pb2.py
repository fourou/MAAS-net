# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hexdump.proto

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
  name='hexdump.proto',
  package='OstProto',
  serialized_pb=_b('\n\rhexdump.proto\x12\x08OstProto\x1a\x0eprotocol.proto\"7\n\x07HexDump\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\x0c\x12\x1b\n\rpad_until_end\x18\x02 \x01(\x08:\x04true:6\n\x07hexDump\x12\x12.OstProto.Protocol\x18h \x01(\x0b\x32\x11.OstProto.HexDump')
  ,
  dependencies=[protocol_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


HEXDUMP_FIELD_NUMBER = 104
hexDump = _descriptor.FieldDescriptor(
  name='hexDump', full_name='OstProto.hexDump', index=0,
  number=104, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_HEXDUMP = _descriptor.Descriptor(
  name='HexDump',
  full_name='OstProto.HexDump',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='OstProto.HexDump.content', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pad_until_end', full_name='OstProto.HexDump.pad_until_end', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
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
  serialized_start=43,
  serialized_end=98,
)

DESCRIPTOR.message_types_by_name['HexDump'] = _HEXDUMP
DESCRIPTOR.extensions_by_name['hexDump'] = hexDump

HexDump = _reflection.GeneratedProtocolMessageType('HexDump', (_message.Message,), dict(
  DESCRIPTOR = _HEXDUMP,
  __module__ = 'hexdump_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.HexDump)
  ))
_sym_db.RegisterMessage(HexDump)

hexDump.message_type = _HEXDUMP
protocol_pb2.Protocol.RegisterExtension(hexDump)

# @@protoc_insertion_point(module_scope)
