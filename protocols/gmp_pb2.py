# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: gmp.proto

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
  name='gmp.proto',
  package='OstProto',
  serialized_pb=_b('\n\tgmp.proto\x12\x08OstProto\x1a\x0eprotocol.proto\"\xf0\x08\n\x03Gmp\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x1d\n\x15is_override_rsvd_code\x18\x02 \x01(\x08\x12\x11\n\trsvd_code\x18\x03 \x01(\r\x12\x1e\n\x11max_response_time\x18\x04 \x01(\r:\x03\x31\x30\x30\x12\x1c\n\x14is_override_checksum\x18\x05 \x01(\x08\x12\x10\n\x08\x63hecksum\x18\x06 \x01(\r\x12.\n\rgroup_address\x18\n \x01(\x0b\x32\x17.OstProto.Gmp.IpAddress\x12\x33\n\ngroup_mode\x18\x0b \x01(\x0e\x32\x17.OstProto.Gmp.GroupMode:\x06kFixed\x12\x17\n\x0bgroup_count\x18\x0c \x01(\r:\x02\x31\x36\x12\x18\n\x0cgroup_prefix\x18\r \x01(\r:\x02\x32\x34\x12\x0e\n\x06s_flag\x18\x14 \x01(\x08\x12\x0e\n\x03qrv\x18\x15 \x01(\r:\x01\x32\x12\x10\n\x03qqi\x18\x16 \x01(\r:\x03\x31\x32\x35\x12(\n\x07sources\x18\x17 \x03(\x0b\x32\x17.OstProto.Gmp.IpAddress\x12 \n\x18is_override_source_count\x18\x18 \x01(\x08\x12\x14\n\x0csource_count\x18\x19 \x01(\r\x12\x30\n\rgroup_records\x18\x1e \x03(\x0b\x32\x19.OstProto.Gmp.GroupRecord\x12&\n\x1eis_override_group_record_count\x18\x1f \x01(\x08\x12\x1a\n\x12group_record_count\x18  \x01(\r\x1a\x35\n\tIpAddress\x12\n\n\x02v4\x18\x01 \x01(\x07\x12\r\n\x05v6_hi\x18\x02 \x01(\x06\x12\r\n\x05v6_lo\x18\x03 \x01(\x06\x1a\xaa\x03\n\x0bGroupRecord\x12>\n\x04type\x18\x01 \x01(\x0e\x32$.OstProto.Gmp.GroupRecord.RecordType:\nkIsInclude\x12.\n\rgroup_address\x18\x02 \x01(\x0b\x32\x17.OstProto.Gmp.IpAddress\x12(\n\x07sources\x18\x03 \x03(\x0b\x32\x17.OstProto.Gmp.IpAddress\x12 \n\x18is_override_source_count\x18\x04 \x01(\x08\x12\x14\n\x0csource_count\x18\x05 \x01(\r\x12\x10\n\x08\x61ux_data\x18\x06 \x01(\x0c\x12#\n\x1bis_override_aux_data_length\x18\x07 \x01(\x08\x12\x17\n\x0f\x61ux_data_length\x18\x08 \x01(\r\"y\n\nRecordType\x12\r\n\tkReserved\x10\x00\x12\x0e\n\nkIsInclude\x10\x01\x12\x0e\n\nkIsExclude\x10\x02\x12\x0e\n\nkToInclude\x10\x03\x12\x0e\n\nkToExclude\x10\x04\x12\r\n\tkAllowNew\x10\x05\x12\r\n\tkBlockOld\x10\x06\"S\n\tGroupMode\x12\n\n\x06kFixed\x10\x00\x12\x13\n\x0fkIncrementGroup\x10\x01\x12\x13\n\x0fkDecrementGroup\x10\x02\x12\x10\n\x0ckRandomGroup\x10\x03')
  ,
  dependencies=[protocol_pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GMP_GROUPRECORD_RECORDTYPE = _descriptor.EnumDescriptor(
  name='RecordType',
  full_name='OstProto.Gmp.GroupRecord.RecordType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kReserved', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kIsInclude', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kIsExclude', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kToInclude', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kToExclude', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kAllowNew', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kBlockOld', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=970,
  serialized_end=1091,
)
_sym_db.RegisterEnumDescriptor(_GMP_GROUPRECORD_RECORDTYPE)

_GMP_GROUPMODE = _descriptor.EnumDescriptor(
  name='GroupMode',
  full_name='OstProto.Gmp.GroupMode',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kFixed', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kIncrementGroup', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kDecrementGroup', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kRandomGroup', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1093,
  serialized_end=1176,
)
_sym_db.RegisterEnumDescriptor(_GMP_GROUPMODE)


_GMP_IPADDRESS = _descriptor.Descriptor(
  name='IpAddress',
  full_name='OstProto.Gmp.IpAddress',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='v4', full_name='OstProto.Gmp.IpAddress.v4', index=0,
      number=1, type=7, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v6_hi', full_name='OstProto.Gmp.IpAddress.v6_hi', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v6_lo', full_name='OstProto.Gmp.IpAddress.v6_lo', index=2,
      number=3, type=6, cpp_type=4, label=1,
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
  serialized_start=609,
  serialized_end=662,
)

_GMP_GROUPRECORD = _descriptor.Descriptor(
  name='GroupRecord',
  full_name='OstProto.Gmp.GroupRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='OstProto.Gmp.GroupRecord.type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_address', full_name='OstProto.Gmp.GroupRecord.group_address', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sources', full_name='OstProto.Gmp.GroupRecord.sources', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_override_source_count', full_name='OstProto.Gmp.GroupRecord.is_override_source_count', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_count', full_name='OstProto.Gmp.GroupRecord.source_count', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aux_data', full_name='OstProto.Gmp.GroupRecord.aux_data', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_override_aux_data_length', full_name='OstProto.Gmp.GroupRecord.is_override_aux_data_length', index=6,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aux_data_length', full_name='OstProto.Gmp.GroupRecord.aux_data_length', index=7,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GMP_GROUPRECORD_RECORDTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=665,
  serialized_end=1091,
)

_GMP = _descriptor.Descriptor(
  name='Gmp',
  full_name='OstProto.Gmp',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='OstProto.Gmp.type', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_override_rsvd_code', full_name='OstProto.Gmp.is_override_rsvd_code', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rsvd_code', full_name='OstProto.Gmp.rsvd_code', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_response_time', full_name='OstProto.Gmp.max_response_time', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=100,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_override_checksum', full_name='OstProto.Gmp.is_override_checksum', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='OstProto.Gmp.checksum', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_address', full_name='OstProto.Gmp.group_address', index=6,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_mode', full_name='OstProto.Gmp.group_mode', index=7,
      number=11, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_count', full_name='OstProto.Gmp.group_count', index=8,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=16,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_prefix', full_name='OstProto.Gmp.group_prefix', index=9,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=24,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='s_flag', full_name='OstProto.Gmp.s_flag', index=10,
      number=20, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qrv', full_name='OstProto.Gmp.qrv', index=11,
      number=21, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='qqi', full_name='OstProto.Gmp.qqi', index=12,
      number=22, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=125,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sources', full_name='OstProto.Gmp.sources', index=13,
      number=23, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_override_source_count', full_name='OstProto.Gmp.is_override_source_count', index=14,
      number=24, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='source_count', full_name='OstProto.Gmp.source_count', index=15,
      number=25, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_records', full_name='OstProto.Gmp.group_records', index=16,
      number=30, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_override_group_record_count', full_name='OstProto.Gmp.is_override_group_record_count', index=17,
      number=31, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='group_record_count', full_name='OstProto.Gmp.group_record_count', index=18,
      number=32, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_GMP_IPADDRESS, _GMP_GROUPRECORD, ],
  enum_types=[
    _GMP_GROUPMODE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=1176,
)

_GMP_IPADDRESS.containing_type = _GMP
_GMP_GROUPRECORD.fields_by_name['type'].enum_type = _GMP_GROUPRECORD_RECORDTYPE
_GMP_GROUPRECORD.fields_by_name['group_address'].message_type = _GMP_IPADDRESS
_GMP_GROUPRECORD.fields_by_name['sources'].message_type = _GMP_IPADDRESS
_GMP_GROUPRECORD.containing_type = _GMP
_GMP_GROUPRECORD_RECORDTYPE.containing_type = _GMP_GROUPRECORD
_GMP.fields_by_name['group_address'].message_type = _GMP_IPADDRESS
_GMP.fields_by_name['group_mode'].enum_type = _GMP_GROUPMODE
_GMP.fields_by_name['sources'].message_type = _GMP_IPADDRESS
_GMP.fields_by_name['group_records'].message_type = _GMP_GROUPRECORD
_GMP_GROUPMODE.containing_type = _GMP
DESCRIPTOR.message_types_by_name['Gmp'] = _GMP

Gmp = _reflection.GeneratedProtocolMessageType('Gmp', (_message.Message,), dict(

  IpAddress = _reflection.GeneratedProtocolMessageType('IpAddress', (_message.Message,), dict(
    DESCRIPTOR = _GMP_IPADDRESS,
    __module__ = 'gmp_pb2'
    # @@protoc_insertion_point(class_scope:OstProto.Gmp.IpAddress)
    ))
  ,

  GroupRecord = _reflection.GeneratedProtocolMessageType('GroupRecord', (_message.Message,), dict(
    DESCRIPTOR = _GMP_GROUPRECORD,
    __module__ = 'gmp_pb2'
    # @@protoc_insertion_point(class_scope:OstProto.Gmp.GroupRecord)
    ))
  ,
  DESCRIPTOR = _GMP,
  __module__ = 'gmp_pb2'
  # @@protoc_insertion_point(class_scope:OstProto.Gmp)
  ))
_sym_db.RegisterMessage(Gmp)
_sym_db.RegisterMessage(Gmp.IpAddress)
_sym_db.RegisterMessage(Gmp.GroupRecord)


# @@protoc_insertion_point(module_scope)
