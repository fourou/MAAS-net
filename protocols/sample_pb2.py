# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sample.proto

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
  name='sample.proto',
  package='OstProto',
  serialized_pb=_b('\n\x0csample.proto\x12\x08OstProto\x1a\x0eprotocol.proto\"x\n\x06Sample\x12\x1c\n\x14is_override_checksum\x18\x01 \x01(\x08\x12\n\n\x02\x61\x62\x18\x02 \x01(\r\x12\x16\n\x0epayload_length\x18\x03 \x01(\r\x12\x10\n\x08\x63hecksum\x18\x04 \x01(\r\x12\x0f\n\x01x\x18\x05 \x01(\r:\x04\x31\x32\x33\x34\x12\t\n\x01y\x18\x06 \x01(\r:4\n\x06sample\x12\x12.OstProto.Protocol\x18\x66 \x01(\x0b\x32\x10.OstProto.Sample')
  ,
  dependencies=[protocol_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


SAMPLE_FIELD_NUMBER = 102
sample = _descriptor.FieldDescriptor(
  name='sample', full_name='OstProto.sample', index=0,
  number=102, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_SAMPLE = _descriptor.Descriptor(
  name='Sample',
  full_name='OstProto.Sample',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_override_checksum', full_name='OstProto.Sample.is_override_checksum', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ab', full_name='OstProto.Sample.ab', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='payload_length', full_name='OstProto.Sample.payload_length', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='OstProto.Sample.checksum', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='x', full_name='OstProto.Sample.x', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=1234,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='OstProto.Sample.y', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=42,
  serialized_end=162,
)

DESCRIPTOR.message_types_by_name['Sample'] = _SAMPLE
DESCRIPTOR.extensions_by_name['sample'] = sample

Sample = _reflection.GeneratedProtocolMessageType('Sample', (_message.Message,), dict(
  DESCRIPTOR = _SAMPLE,
  __module__ = 'sample_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.Sample)
  ))
_sym_db.RegisterMessage(Sample)

sample.message_type = _SAMPLE
protocol_pb2.Protocol.RegisterExtension(sample)

# @@protoc_insertion_point(module_scope)