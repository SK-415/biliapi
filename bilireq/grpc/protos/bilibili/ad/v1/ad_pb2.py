# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilibili/ad/v1/ad.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x62ilibili/ad/v1/ad.proto\x12\x0e\x62ilibili.ad.v1\x1a\x1egoogle/protobuf/wrappers.proto\"Y\n\rAdsControlDto\x12\x11\n\thas_danmu\x18\x01 \x01(\x05\x12\x0c\n\x04\x63ids\x18\x02 \x03(\x03\x12\'\n\x03\x65ps\x18\x03 \x03(\x0b\x32\x1a.bilibili.ad.v1.AdOgvEpDto\"1\n\nAdOgvEpDto\x12\x0c\n\x04\x65pid\x18\x01 \x01(\x03\x12\x15\n\rhas_recommend\x18\x02 \x01(\x08\"\x91\x02\n\x10SourceContentDto\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x11\n\tsource_id\x18\x02 \x01(\x05\x12\x13\n\x0bresource_id\x18\x03 \x01(\x05\x12\x11\n\tis_ad_loc\x18\x04 \x01(\x08\x12\x30\n\x0bserver_type\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x11\n\tclient_ip\x18\x06 \x01(\t\x12/\n\ncard_index\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\r\n\x05index\x18\x08 \x01(\x05\x12)\n\nad_content\x18\t \x01(\x0b\x32\x15.bilibili.ad.v1.AdDto\"\x8b\x02\n\x05\x41\x64\x44to\x12\x13\n\x0b\x63reative_id\x18\x01 \x01(\x03\x12\r\n\x05\x61\x64_cb\x18\x02 \x01(\t\x12\x30\n\x05\x65xtra\x18\x03 \x01(\x0b\x32!.bilibili.ad.v1.AdContentExtraDto\x12\x0f\n\x07\x63m_mark\x18\x04 \x01(\x05\x12\x13\n\x0btop_view_id\x18\x05 \x01(\x03\x12\x15\n\rcreative_type\x18\x06 \x01(\x05\x12\x11\n\tcard_type\x18\x07 \x01(\x05\x12\x16\n\x0e\x63reative_style\x18\x08 \x01(\x05\x12\r\n\x05is_ad\x18\t \x01(\x05\x12\x35\n\x10\x63reative_content\x18\n \x01(\x0b\x32\x1b.bilibili.ad.v1.CreativeDto\"\xd2\x06\n\x11\x41\x64\x43ontentExtraDto\x12\x0e\n\x06layout\x18\x01 \x01(\t\x12\x11\n\tshow_urls\x18\x02 \x03(\t\x12\x12\n\nclick_urls\x18\x03 \x03(\t\x12\x1c\n\x14\x64\x61nmu_list_show_urls\x18\x04 \x03(\t\x12\x1d\n\x15\x64\x61nmu_list_click_urls\x18\x05 \x03(\t\x12\x1e\n\x16\x64\x61nmu_detail_show_urls\x18\x06 \x03(\t\x12\x1e\n\x16\x64\x61nmu_trolley_add_urls\x18\x07 \x03(\t\x12\x15\n\ruse_ad_web_v2\x18\x08 \x01(\x08\x12\x16\n\x0eopen_whitelist\x18\t \x03(\t\x12\x39\n\x12\x64ownload_whitelist\x18\n \x01(\x0b\x32\x1d.bilibili.ad.v1.AppPackageDto\x12\'\n\x04\x63\x61rd\x18\x0b \x01(\x0b\x32\x19.bilibili.ad.v1.AdCardDto\x12\x13\n\x0breport_time\x18\x0c \x01(\x05\x12\x19\n\x11\x61ppstore_priority\x18\r \x01(\x05\x12\x12\n\nsales_type\x18\x0e \x01(\x05\x12\x1b\n\x13preload_landingpage\x18\x0f \x01(\x05\x12\x18\n\x10special_industry\x18\x10 \x01(\x08\x12\x1d\n\x15special_industry_tips\x18\x11 \x01(\t\x12\x1e\n\x16\x65nable_download_dialog\x18\x12 \x01(\x08\x12\x14\n\x0c\x65nable_share\x18\x13 \x01(\x08\x12\x1c\n\x14upzone_entrance_type\x18\x14 \x01(\x05\x12!\n\x19upzone_entrance_report_id\x18\x15 \x01(\x05\x12\x32\n\nshare_info\x18\x16 \x01(\x0b\x32\x1e.bilibili.ad.v1.AdShareInfoDto\x12\x17\n\x0ftopview_pic_url\x18\x17 \x01(\t\x12\x19\n\x11topview_video_url\x18\x18 \x01(\t\x12\x12\n\nclick_area\x18\x19 \x01(\x05\x12\x0f\n\x07shop_id\x18\x1a \x01(\x03\x12\x0e\n\x06up_mid\x18\x1b \x01(\x03\x12\x10\n\x08track_id\x18\x1c \x01(\t\x12\"\n\x1a\x65nable_store_direct_launch\x18\x1d \x01(\x05\x12\x12\n\nproduct_id\x18\x1e \x01(\x03\"\x83\x02\n\x0b\x43reativeDto\x12\r\n\x05title\x18\x01 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x11\n\timage_url\x18\x03 \x01(\t\x12\x11\n\timage_md5\x18\x04 \x01(\t\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\x11\n\tclick_url\x18\x06 \x01(\t\x12\x10\n\x08show_url\x18\x07 \x01(\t\x12\x10\n\x08video_id\x18\x08 \x01(\x03\x12\x15\n\rthumbnail_url\x18\t \x01(\t\x12\x19\n\x11thumbnail_url_md5\x18\n \x01(\t\x12\x10\n\x08logo_url\x18\x0b \x01(\t\x12\x10\n\x08logo_md5\x18\x0c \x01(\t\x12\x10\n\x08username\x18\r \x01(\t\"\x87\x02\n\rAppPackageDto\x12\x0c\n\x04size\x18\x01 \x01(\x03\x12\x14\n\x0c\x64isplay_name\x18\x02 \x01(\t\x12\x10\n\x08\x61pk_name\x18\x03 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x10\n\x08\x62ili_url\x18\x05 \x01(\t\x12\x0b\n\x03md5\x18\x06 \x01(\t\x12\x0c\n\x04icon\x18\x07 \x01(\t\x12\x10\n\x08\x64\x65v_name\x18\x08 \x01(\t\x12\x10\n\x08\x61uth_url\x18\t \x01(\t\x12\x11\n\tauth_name\x18\n \x01(\t\x12\x0f\n\x07version\x18\x0b \x01(\t\x12\x13\n\x0bupdate_time\x18\x0c \x01(\t\x12\x14\n\x0cprivacy_name\x18\r \x01(\t\x12\x13\n\x0bprivacy_url\x18\x0e \x01(\t\"\x90\t\n\tAdCardDto\x12\x11\n\tcard_type\x18\x01 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x03 \x01(\t\x12\x12\n\nextra_desc\x18\x04 \x01(\t\x12\x11\n\tlong_desc\x18\x05 \x01(\t\x12\x13\n\x0bshort_title\x18\x06 \x01(\t\x12\x13\n\x0b\x64\x61nmu_title\x18\x07 \x01(\t\x12\x14\n\x0c\x64\x61nmu_height\x18\x08 \x01(\x05\x12\x13\n\x0b\x64\x61nmu_width\x18\t \x01(\x05\x12\x12\n\ndanmu_life\x18\n \x01(\x05\x12\x13\n\x0b\x64\x61nmu_begin\x18\x0b \x01(\x05\x12\x13\n\x0b\x64\x61nmu_color\x18\x0c \x01(\t\x12\x13\n\x0b\x64\x61nmu_h5url\x18\r \x01(\t\x12\x12\n\ndanmu_icon\x18\x0e \x01(\t\x12\x11\n\tfold_time\x18\x0f \x01(\x05\x12\x0e\n\x06\x61\x64_tag\x18\x10 \x01(\t\x12*\n\x06\x63overs\x18\x11 \x03(\x0b\x32\x1a.bilibili.ad.v1.AdCoverDto\x12\x10\n\x08jump_url\x18\x12 \x01(\t\x12%\n\x1dimax_landing_page_json_string\x18\x13 \x01(\t\x12\x12\n\ncallup_url\x18\x14 \x01(\t\x12\x15\n\runiversal_app\x18\x15 \x01(\t\x12\x11\n\tori_price\x18\x16 \x01(\t\x12\x11\n\tcur_price\x18\x17 \x01(\x05\x12\x12\n\nprice_desc\x18\x18 \x01(\t\x12\x14\n\x0cprice_symbol\x18\x19 \x01(\t\x12\x17\n\x0fgoods_cur_price\x18\x1a \x01(\t\x12\x17\n\x0fgoods_ori_price\x18\x1b \x01(\t\x12\'\n\x04good\x18\x1c \x01(\x0b\x32\x19.bilibili.ad.v1.AdGoodDto\x12\x0c\n\x04rank\x18\x1d \x01(\x05\x12\x11\n\thot_score\x18\x1e \x01(\x05\x12+\n\x06\x62utton\x18\x1f \x01(\x0b\x32\x1b.bilibili.ad.v1.AdButtonDto\x12\x12\n\nadver_logo\x18  \x01(\t\x12\x12\n\nadver_name\x18! \x01(\t\x12\x16\n\x0e\x61\x64ver_page_url\x18\" \x01(\t\x12\x15\n\rvideo_barrage\x18# \x03(\t\x12\x37\n\x0c\x61\x64_tag_style\x18$ \x01(\x0b\x32!.bilibili.ad.v1.AdBusinessMarkDto\x12\x31\n\x05video\x18% \x01(\x0b\x32\".bilibili.ad.v1.AdAutoPlayVideoDto\x12:\n\x0e\x66\x65\x65\x64\x62\x61\x63k_panel\x18& \x01(\x0b\x32\".bilibili.ad.v1.AdFeedbackPanelDto\x12\x11\n\tadver_mid\x18\' \x01(\x03\x12\x18\n\x10\x61\x64ver_account_id\x18( \x01(\x03\x12\x10\n\x08\x64uration\x18) \x01(\t\x12\x32\n\rquality_infos\x18* \x03(\x0b\x32\x1b.bilibili.ad.v1.QualityInfo\x12\x14\n\x0c\x64ynamic_text\x18+ \x01(\t\x12\'\n\x05\x61\x64ver\x18, \x01(\x0b\x32\x18.bilibili.ad.v1.AdverDto\x12\x13\n\x0bgrade_level\x18- \x01(\x05\"D\n\x0e\x41\x64ShareInfoDto\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12\x11\n\timage_url\x18\x03 \x01(\t\"y\n\nAdCoverDto\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x0c\n\x04loop\x18\x02 \x01(\x05\x12\x10\n\x08jump_url\x18\x03 \x01(\t\x12\x13\n\x0breport_urls\x18\x04 \x03(\t\x12\x14\n\x0cimage_height\x18\x05 \x01(\x05\x12\x13\n\x0bimage_width\x18\x06 \x01(\x05\"\x97\x01\n\x0b\x41\x64\x42uttonDto\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x10\n\x08jump_url\x18\x03 \x01(\t\x12\x13\n\x0breport_urls\x18\x04 \x01(\t\x12\x18\n\x10\x64lsuc_callup_url\x18\x05 \x01(\t\x12\x0f\n\x07game_id\x18\x06 \x01(\x05\x12\x1a\n\x12game_monitor_param\x18\x07 \x01(\t\"\x8a\x02\n\x11\x41\x64\x42usinessMarkDto\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x12\n\ntext_color\x18\x03 \x01(\t\x12\x18\n\x10text_color_night\x18\x04 \x01(\t\x12\x10\n\x08\x62g_color\x18\x05 \x01(\t\x12\x16\n\x0e\x62g_color_night\x18\x06 \x01(\t\x12\x14\n\x0c\x62order_color\x18\x07 \x01(\t\x12\x1a\n\x12\x62order_color_night\x18\x08 \x01(\t\x12\x0f\n\x07img_url\x18\t \x01(\t\x12\x12\n\nimg_height\x18\n \x01(\x05\x12\x11\n\timg_width\x18\x0b \x01(\x05\x12\x17\n\x0f\x62g_border_color\x18\x0c \x01(\t\"\x8f\x02\n\x12\x41\x64\x41utoPlayVideoDto\x12\x0c\n\x04\x61vid\x18\x01 \x01(\x03\x12\x0b\n\x03\x63id\x18\x02 \x01(\x03\x12\x0c\n\x04page\x18\x03 \x01(\x03\x12\x0c\n\x04\x66rom\x18\x04 \x01(\t\x12\x0b\n\x03url\x18\x05 \x01(\t\x12\r\n\x05\x63over\x18\x06 \x01(\t\x12\x11\n\tauto_play\x18\x07 \x01(\x08\x12\x15\n\rbtn_dyc_color\x18\x08 \x01(\x08\x12\x14\n\x0c\x62tn_dyc_time\x18\t \x01(\x05\x12\x0e\n\x06\x62iz_id\x18\n \x01(\x03\x12\x15\n\rprocess0_urls\x18\x0b \x03(\t\x12\x14\n\x0cplay_3s_urls\x18\x0c \x03(\t\x12\x14\n\x0cplay_5s_urls\x18\r \x03(\t\x12\x13\n\x0borientation\x18\x0e \x01(\x05\"v\n\x12\x41\x64\x46\x65\x65\x64\x62\x61\x63kPanelDto\x12\x17\n\x0fpanel_type_text\x18\x01 \x01(\t\x12G\n\x15\x66\x65\x65\x64\x62\x61\x63k_panel_detail\x18\x02 \x03(\x0b\x32(.bilibili.ad.v1.AdFeedbackPanelModuleDto\"\xb5\x01\n\x18\x41\x64\x46\x65\x65\x64\x62\x61\x63kPanelModuleDto\x12\x11\n\tmodule_id\x18\x01 \x01(\x05\x12\x10\n\x08icon_url\x18\x02 \x01(\t\x12\x11\n\tjump_type\x18\x03 \x01(\x05\x12\x10\n\x08jump_url\x18\x04 \x01(\t\x12\x0c\n\x04text\x18\x05 \x01(\t\x12\x41\n\x0fsecondary_panel\x18\x06 \x03(\x0b\x32(.bilibili.ad.v1.AdSecondFeedbackPanelDto\";\n\x18\x41\x64SecondFeedbackPanelDto\x12\x11\n\treason_id\x18\x01 \x01(\x05\x12\x0c\n\x04text\x18\x02 \x01(\t\"N\n\tAdGoodDto\x12\x0f\n\x07item_id\x18\x01 \x01(\x03\x12\x0e\n\x06sku_id\x18\x02 \x01(\x03\x12\x0f\n\x07shop_id\x18\x03 \x01(\x03\x12\x0f\n\x07sku_num\x18\x04 \x01(\x03\"b\n\x0bQualityInfo\x12\x0c\n\x04icon\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\r\n\x05is_bg\x18\x03 \x01(\x08\x12\x10\n\x08\x62g_color\x18\x04 \x01(\t\x12\x16\n\x0e\x62g_color_night\x18\x05 \x01(\t\"\x84\x01\n\x08\x41\x64verDto\x12\x10\n\x08\x61\x64ver_id\x18\x01 \x01(\x03\x12\x12\n\nadver_logo\x18\x02 \x01(\t\x12\x12\n\nadver_name\x18\x03 \x01(\t\x12\x12\n\nadver_type\x18\x04 \x01(\x05\x12\x16\n\x0e\x61\x64ver_page_url\x18\x05 \x01(\t\x12\x12\n\nadver_desc\x18\x06 \x01(\tb\x06proto3')



_ADSCONTROLDTO = DESCRIPTOR.message_types_by_name['AdsControlDto']
_ADOGVEPDTO = DESCRIPTOR.message_types_by_name['AdOgvEpDto']
_SOURCECONTENTDTO = DESCRIPTOR.message_types_by_name['SourceContentDto']
_ADDTO = DESCRIPTOR.message_types_by_name['AdDto']
_ADCONTENTEXTRADTO = DESCRIPTOR.message_types_by_name['AdContentExtraDto']
_CREATIVEDTO = DESCRIPTOR.message_types_by_name['CreativeDto']
_APPPACKAGEDTO = DESCRIPTOR.message_types_by_name['AppPackageDto']
_ADCARDDTO = DESCRIPTOR.message_types_by_name['AdCardDto']
_ADSHAREINFODTO = DESCRIPTOR.message_types_by_name['AdShareInfoDto']
_ADCOVERDTO = DESCRIPTOR.message_types_by_name['AdCoverDto']
_ADBUTTONDTO = DESCRIPTOR.message_types_by_name['AdButtonDto']
_ADBUSINESSMARKDTO = DESCRIPTOR.message_types_by_name['AdBusinessMarkDto']
_ADAUTOPLAYVIDEODTO = DESCRIPTOR.message_types_by_name['AdAutoPlayVideoDto']
_ADFEEDBACKPANELDTO = DESCRIPTOR.message_types_by_name['AdFeedbackPanelDto']
_ADFEEDBACKPANELMODULEDTO = DESCRIPTOR.message_types_by_name['AdFeedbackPanelModuleDto']
_ADSECONDFEEDBACKPANELDTO = DESCRIPTOR.message_types_by_name['AdSecondFeedbackPanelDto']
_ADGOODDTO = DESCRIPTOR.message_types_by_name['AdGoodDto']
_QUALITYINFO = DESCRIPTOR.message_types_by_name['QualityInfo']
_ADVERDTO = DESCRIPTOR.message_types_by_name['AdverDto']
AdsControlDto = _reflection.GeneratedProtocolMessageType('AdsControlDto', (_message.Message,), {
  'DESCRIPTOR' : _ADSCONTROLDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdsControlDto)
  })
_sym_db.RegisterMessage(AdsControlDto)

AdOgvEpDto = _reflection.GeneratedProtocolMessageType('AdOgvEpDto', (_message.Message,), {
  'DESCRIPTOR' : _ADOGVEPDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdOgvEpDto)
  })
_sym_db.RegisterMessage(AdOgvEpDto)

SourceContentDto = _reflection.GeneratedProtocolMessageType('SourceContentDto', (_message.Message,), {
  'DESCRIPTOR' : _SOURCECONTENTDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.SourceContentDto)
  })
_sym_db.RegisterMessage(SourceContentDto)

AdDto = _reflection.GeneratedProtocolMessageType('AdDto', (_message.Message,), {
  'DESCRIPTOR' : _ADDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdDto)
  })
_sym_db.RegisterMessage(AdDto)

AdContentExtraDto = _reflection.GeneratedProtocolMessageType('AdContentExtraDto', (_message.Message,), {
  'DESCRIPTOR' : _ADCONTENTEXTRADTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdContentExtraDto)
  })
_sym_db.RegisterMessage(AdContentExtraDto)

CreativeDto = _reflection.GeneratedProtocolMessageType('CreativeDto', (_message.Message,), {
  'DESCRIPTOR' : _CREATIVEDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.CreativeDto)
  })
_sym_db.RegisterMessage(CreativeDto)

AppPackageDto = _reflection.GeneratedProtocolMessageType('AppPackageDto', (_message.Message,), {
  'DESCRIPTOR' : _APPPACKAGEDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AppPackageDto)
  })
_sym_db.RegisterMessage(AppPackageDto)

AdCardDto = _reflection.GeneratedProtocolMessageType('AdCardDto', (_message.Message,), {
  'DESCRIPTOR' : _ADCARDDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdCardDto)
  })
_sym_db.RegisterMessage(AdCardDto)

AdShareInfoDto = _reflection.GeneratedProtocolMessageType('AdShareInfoDto', (_message.Message,), {
  'DESCRIPTOR' : _ADSHAREINFODTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdShareInfoDto)
  })
_sym_db.RegisterMessage(AdShareInfoDto)

AdCoverDto = _reflection.GeneratedProtocolMessageType('AdCoverDto', (_message.Message,), {
  'DESCRIPTOR' : _ADCOVERDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdCoverDto)
  })
_sym_db.RegisterMessage(AdCoverDto)

AdButtonDto = _reflection.GeneratedProtocolMessageType('AdButtonDto', (_message.Message,), {
  'DESCRIPTOR' : _ADBUTTONDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdButtonDto)
  })
_sym_db.RegisterMessage(AdButtonDto)

AdBusinessMarkDto = _reflection.GeneratedProtocolMessageType('AdBusinessMarkDto', (_message.Message,), {
  'DESCRIPTOR' : _ADBUSINESSMARKDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdBusinessMarkDto)
  })
_sym_db.RegisterMessage(AdBusinessMarkDto)

AdAutoPlayVideoDto = _reflection.GeneratedProtocolMessageType('AdAutoPlayVideoDto', (_message.Message,), {
  'DESCRIPTOR' : _ADAUTOPLAYVIDEODTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdAutoPlayVideoDto)
  })
_sym_db.RegisterMessage(AdAutoPlayVideoDto)

AdFeedbackPanelDto = _reflection.GeneratedProtocolMessageType('AdFeedbackPanelDto', (_message.Message,), {
  'DESCRIPTOR' : _ADFEEDBACKPANELDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdFeedbackPanelDto)
  })
_sym_db.RegisterMessage(AdFeedbackPanelDto)

AdFeedbackPanelModuleDto = _reflection.GeneratedProtocolMessageType('AdFeedbackPanelModuleDto', (_message.Message,), {
  'DESCRIPTOR' : _ADFEEDBACKPANELMODULEDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdFeedbackPanelModuleDto)
  })
_sym_db.RegisterMessage(AdFeedbackPanelModuleDto)

AdSecondFeedbackPanelDto = _reflection.GeneratedProtocolMessageType('AdSecondFeedbackPanelDto', (_message.Message,), {
  'DESCRIPTOR' : _ADSECONDFEEDBACKPANELDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdSecondFeedbackPanelDto)
  })
_sym_db.RegisterMessage(AdSecondFeedbackPanelDto)

AdGoodDto = _reflection.GeneratedProtocolMessageType('AdGoodDto', (_message.Message,), {
  'DESCRIPTOR' : _ADGOODDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdGoodDto)
  })
_sym_db.RegisterMessage(AdGoodDto)

QualityInfo = _reflection.GeneratedProtocolMessageType('QualityInfo', (_message.Message,), {
  'DESCRIPTOR' : _QUALITYINFO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.QualityInfo)
  })
_sym_db.RegisterMessage(QualityInfo)

AdverDto = _reflection.GeneratedProtocolMessageType('AdverDto', (_message.Message,), {
  'DESCRIPTOR' : _ADVERDTO,
  '__module__' : 'bilibili.ad.v1.ad_pb2'
  # @@protoc_insertion_point(class_scope:bilibili.ad.v1.AdverDto)
  })
_sym_db.RegisterMessage(AdverDto)

if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _ADSCONTROLDTO._serialized_start=75
  _ADSCONTROLDTO._serialized_end=164
  _ADOGVEPDTO._serialized_start=166
  _ADOGVEPDTO._serialized_end=215
  _SOURCECONTENTDTO._serialized_start=218
  _SOURCECONTENTDTO._serialized_end=491
  _ADDTO._serialized_start=494
  _ADDTO._serialized_end=761
  _ADCONTENTEXTRADTO._serialized_start=764
  _ADCONTENTEXTRADTO._serialized_end=1614
  _CREATIVEDTO._serialized_start=1617
  _CREATIVEDTO._serialized_end=1876
  _APPPACKAGEDTO._serialized_start=1879
  _APPPACKAGEDTO._serialized_end=2142
  _ADCARDDTO._serialized_start=2145
  _ADCARDDTO._serialized_end=3313
  _ADSHAREINFODTO._serialized_start=3315
  _ADSHAREINFODTO._serialized_end=3383
  _ADCOVERDTO._serialized_start=3385
  _ADCOVERDTO._serialized_end=3506
  _ADBUTTONDTO._serialized_start=3509
  _ADBUTTONDTO._serialized_end=3660
  _ADBUSINESSMARKDTO._serialized_start=3663
  _ADBUSINESSMARKDTO._serialized_end=3929
  _ADAUTOPLAYVIDEODTO._serialized_start=3932
  _ADAUTOPLAYVIDEODTO._serialized_end=4203
  _ADFEEDBACKPANELDTO._serialized_start=4205
  _ADFEEDBACKPANELDTO._serialized_end=4323
  _ADFEEDBACKPANELMODULEDTO._serialized_start=4326
  _ADFEEDBACKPANELMODULEDTO._serialized_end=4507
  _ADSECONDFEEDBACKPANELDTO._serialized_start=4509
  _ADSECONDFEEDBACKPANELDTO._serialized_end=4568
  _ADGOODDTO._serialized_start=4570
  _ADGOODDTO._serialized_end=4648
  _QUALITYINFO._serialized_start=4650
  _QUALITYINFO._serialized_end=4748
  _ADVERDTO._serialized_start=4751
  _ADVERDTO._serialized_end=4883
# @@protoc_insertion_point(module_scope)