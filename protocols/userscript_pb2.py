# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: userscript.proto

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
  name='userscript.proto',
  package='OstProto',
  serialized_pb=_b('\n\x10userscript.proto\x12\x08OstProto\x1a\x0eprotocol.proto\"\x1d\n\nUserScript\x12\x0f\n\x07program\x18\x01 \x01(\t:<\n\nuserScript\x12\x12.OstProto.Protocol\x18g \x01(\x0b\x32\x14.OstProto.UserScript')
  ,
  dependencies=[protocol_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


USERSCRIPT_FIELD_NUMBER = 103
userScript = _descriptor.FieldDescriptor(
  name='userScript', full_name='OstProto.userScript', index=0,
  number=103, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_USERSCRIPT = _descriptor.Descriptor(
  name='UserScript',
  full_name='OstProto.UserScript',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='program', full_name='OstProto.UserScript.program', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=46,
  serialized_end=75,
)

DESCRIPTOR.message_types_by_name['UserScript'] = _USERSCRIPT
DESCRIPTOR.extensions_by_name['userScript'] = userScript

UserScript = _reflection.GeneratedProtocolMessageType('UserScript', (_message.Message,), dict(
  DESCRIPTOR = _USERSCRIPT,
  __module__ = 'userscript_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.UserScript)
  ))
_sym_db.RegisterMessage(UserScript)

userScript.message_type = _USERSCRIPT
protocol_pb2.Protocol.RegisterExtension(userScript)

# @@protoc_insertion_point(module_scope)