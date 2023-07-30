# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilireq.grpc.protos.bilibili/app/click/v1/heartbeat.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%bilibili/app/click/v1/heartbeat.proto\x12\x15\x62ilibili.app.click.v1\"\x1a\n\x0b\x41\x63\x63ountInfo\x12\x0b\n\x03mid\x18\x01 \x01(\x04\"=\n\x07\x41ppInfo\x12\x16\n\x0etop_page_class\x18\x01 \x01(\t\x12\r\n\x05\x66time\x18\x02 \x01(\x03\x12\x0b\n\x03\x64id\x18\x03 \x01(\t\"\'\n\x05\x45xtra\x12\x0f\n\x07session\x18\x01 \x01(\t\x12\r\n\x05refer\x18\x02 \x01(\t\"\x10\n\x0eHeartBeatReply\"\xec\x03\n\x0cHeartBeatReq\x12\x12\n\nsession_v2\x18\x01 \x01(\t\x12+\n\x05stage\x18\x02 \x01(\x0e\x32\x1c.bilibili.app.click.v1.Stage\x12\x16\n\x0estream_timeout\x18\x03 \x01(\x04\x12\x17\n\x0f\x62\x61tch_frequency\x18\x04 \x01(\x04\x12\x11\n\tfrequency\x18\x05 \x01(\x02\x12\x34\n\nvideo_meta\x18\x06 \x01(\x0b\x32 .bilibili.app.click.v1.VideoMeta\x12\x30\n\x08\x61pp_info\x18\x07 \x01(\x0b\x32\x1e.bilibili.app.click.v1.AppInfo\x12\x38\n\x0c\x61\x63\x63ount_info\x18\x08 \x01(\x0b\x32\".bilibili.app.click.v1.AccountInfo\x12\x43\n\x12pre_process_result\x18\t \x01(\x0b\x32\'.bilibili.app.click.v1.PreProcessResult\x12:\n\rplayer_status\x18\n \x03(\x0b\x32#.bilibili.app.click.v1.PlayerStatus\x12\x34\n\nvideo_info\x18\x0b \x01(\x0b\x32 .bilibili.app.click.v1.VideoInfo\"\x83\x01\n\x0cPlayerStatus\x12\x15\n\rplayback_rate\x18\x01 \x01(\x02\x12\x10\n\x08progress\x18\x02 \x01(\x04\x12\x34\n\nplay_state\x18\x03 \x01(\x0e\x32 .bilibili.app.click.v1.PlayState\x12\x14\n\x0cis_buffering\x18\x04 \x01(\x08\"\x1e\n\x10PreProcessResult\x12\n\n\x02vt\x18\x01 \x01(\x03\"!\n\tVideoInfo\x12\x14\n\x0c\x63id_duration\x18\x01 \x01(\x04\"%\n\tVideoMeta\x12\x0b\n\x03\x61id\x18\x01 \x01(\x04\x12\x0b\n\x03\x63id\x18\x02 \x01(\x04*m\n\tPlayState\x12\x11\n\rSTATE_UNKNOWN\x10\x00\x12\r\n\tPREPARING\x10\x01\x12\x0c\n\x08PREPARED\x10\x02\x12\x0b\n\x07PLAYING\x10\x03\x12\n\n\x06PAUSED\x10\x04\x12\x0b\n\x07STOPPED\x10\x05\x12\n\n\x06\x46\x41ILED\x10\x06*:\n\x05Stage\x12\x11\n\rSTAGE_UNKNOWN\x10\x00\x12\t\n\x05START\x10\x01\x12\x07\n\x03\x45ND\x10\x02\x12\n\n\x06SAMPLE\x10\x03\x32\x07\n\x05\x43lickb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.app.click.v1.heartbeat_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_PLAYSTATE']._serialized_start=949
  _globals['_PLAYSTATE']._serialized_end=1058
  _globals['_STAGE']._serialized_start=1060
  _globals['_STAGE']._serialized_end=1118
  _globals['_ACCOUNTINFO']._serialized_start=64
  _globals['_ACCOUNTINFO']._serialized_end=90
  _globals['_APPINFO']._serialized_start=92
  _globals['_APPINFO']._serialized_end=153
  _globals['_EXTRA']._serialized_start=155
  _globals['_EXTRA']._serialized_end=194
  _globals['_HEARTBEATREPLY']._serialized_start=196
  _globals['_HEARTBEATREPLY']._serialized_end=212
  _globals['_HEARTBEATREQ']._serialized_start=215
  _globals['_HEARTBEATREQ']._serialized_end=707
  _globals['_PLAYERSTATUS']._serialized_start=710
  _globals['_PLAYERSTATUS']._serialized_end=841
  _globals['_PREPROCESSRESULT']._serialized_start=843
  _globals['_PREPROCESSRESULT']._serialized_end=873
  _globals['_VIDEOINFO']._serialized_start=875
  _globals['_VIDEOINFO']._serialized_end=908
  _globals['_VIDEOMETA']._serialized_start=910
  _globals['_VIDEOMETA']._serialized_end=947
  _globals['_CLICK']._serialized_start=1120
  _globals['_CLICK']._serialized_end=1127
# @@protoc_insertion_point(module_scope)