# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: payload.proto

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
  name='payload.proto',
  package='OstProto',
  serialized_pb=_b('\n\rpayload.proto\x12\x08OstProto\x1a\x0eprotocol.proto\"\xb2\x01\n\x07Payload\x12\x37\n\x0cpattern_mode\x18\x01 \x01(\x0e\x32!.OstProto.Payload.DataPatternMode\x12\x0f\n\x07pattern\x18\x02 \x01(\r\"]\n\x0f\x44\x61taPatternMode\x12\x13\n\x0f\x65_dp_fixed_word\x10\x00\x12\x11\n\re_dp_inc_byte\x10\x01\x12\x11\n\re_dp_dec_byte\x10\x02\x12\x0f\n\x0b\x65_dp_random\x10\x03:6\n\x07payload\x12\x12.OstProto.Protocol\x18\x65 \x01(\x0b\x32\x11.OstProto.Payload')
  ,
  dependencies=[protocol_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


PAYLOAD_FIELD_NUMBER = 101
payload = _descriptor.FieldDescriptor(
  name='payload', full_name='OstProto.payload', index=0,
  number=101, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)

_PAYLOAD_DATAPATTERNMODE = _descriptor.EnumDescriptor(
  name='DataPatternMode',
  full_name='OstProto.Payload.DataPatternMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='e_dp_fixed_word', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='e_dp_inc_byte', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='e_dp_dec_byte', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='e_dp_random', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=129,
  serialized_end=222,
)
_sym_db.RegisterEnumDescriptor(_PAYLOAD_DATAPATTERNMODE)


_PAYLOAD = _descriptor.Descriptor(
  name='Payload',
  full_name='OstProto.Payload',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pattern_mode', full_name='OstProto.Payload.pattern_mode', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pattern', full_name='OstProto.Payload.pattern', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PAYLOAD_DATAPATTERNMODE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=44,
  serialized_end=222,
)

_PAYLOAD.fields_by_name['pattern_mode'].enum_type = _PAYLOAD_DATAPATTERNMODE
_PAYLOAD_DATAPATTERNMODE.containing_type = _PAYLOAD
DESCRIPTOR.message_types_by_name['Payload'] = _PAYLOAD
DESCRIPTOR.extensions_by_name['payload'] = payload

Payload = _reflection.GeneratedProtocolMessageType('Payload', (_message.Message,), dict(
  DESCRIPTOR = _PAYLOAD,
  __module__ = 'payload_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.Payload)
  ))
_sym_db.RegisterMessage(Payload)

payload.message_type = _PAYLOAD
protocol_pb2.Protocol.RegisterExtension(payload)

# @@protoc_insertion_point(module_scope)