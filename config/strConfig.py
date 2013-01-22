
JOINSTR = '\t'

#--------------------------------------------------
# Header record
HEADER_RECORD_ID_POS = 0
HEADER_FILE_FORMAT_VERSION = 1
HEADER_TIMESTAMP_POS = 2
HEADER_BSC_POS = 10 # the pos of "Number of BSC's"
HEADER_END_POS = 6822

# SPLIT_FILE_SIZE = 80000000 # 80m
SPLIT_FILE_SIZE = 25000000 # 25m
#--------------------------------------------------
# Event record
EVENT_START_POS = 6823
TIMESTAMP_DIV_ODD = 1000
TIMESTAMP_DIV_EVEN = 16.667

#--------------------------------------------------
# Footer record
FOOTER_RECORD_SIZE = 9
FOOTER_TIMESTAMP_POS = -8

#--------------------------------------------------
# func dict
# from util.RPMOprocess import *
# parse_func_dict = {
#     0:RPMOparse.Assignment_Request,
#     1:RPMOparse.Assignment_Failed,
#     2:RPMOparse.Clear_Request,
#     3:RPMOparse.Clear_Command,
#     4:None,
#     5:RPMOparse.Handover_Command,
#     6:RPMOparse.Handover_Complete,
#     7:RPMOparse.Channel_Busy,
#     8:RPMOparse.Channel_Available,
#     9:RPMOparse.Channel_Blocked,
#     10:RPMOparse.Channel_Deblocked,
#     11:RPMOparse.Assignment_Command,
#     12:RPMOparse.Assignment_Complete,
#     13:RPMOparse.Assignment_Failed_MS_to_BSC,
#     14:RPMOparse.Cipher_Mode_Complete,
#     15:RPMOparse.GPRS_Flush,
#     16:None,
#     17:None,
#     18:RPMOparse.Channel_Busy_Extended_event, # look at pdf 4.2.9
#     19:RPMOparse.DTM_Establishment,
#     20:RPMOparse.MS_Context_Established,
#     21:None,
#     22:RPMOparse.Data_Activity_Ends,
#     23:RPMOparse.TBF_Changes,
#     24:RPMOparse.Connect_Acknowledge,
#     25:RPMOparse.IP_Buffer_Discard,
#     26:RPMOparse.Admission_Control,
#     27:RPMOparse.Handover Failure,
#     28:RPMOparse.Inter_System_Handover_Command,
#     29:RPMOparse.Incoming_Inter_System_Handover_Result,
#     30:RPMOparse.Outgoing_Inter_System_Handover_Result,
#     31:RPMOparse.VGCS_Notification,
#     32:RPMOparse.VGCS_Channel_Setup,
#     33:RPMOparse.VGCS_Call_Release,
#     34:RPMOparse.CS_Call_Release,
#     35:RPMOparse.DTM_Ends,
#     36:RPMOparse.Measurement_Result_Large,
#     37:RPMOparse.Measurement_Result_Medium,
#     38:RPMOparse.TBF_Ends,
#     39:RPMOparse.Inter_System_Handover_Information,
#     40:RPMOparse.VGCS_Channel_Release,
#     41:RPMOparse.VGCS_Notification_Response,
#     42:RPMOparse.Packet_Measurement_Report,
#     43:RPMOparse.NC2_Session_Ends,
#     44:RPMOparse.Classmark_Information,
#     45:RPMOparse.RTT_Mapping
#     46:RPMOparse.RTT_Status,
#     47:RPMOparse.PS_Handover_Preparation_Outgoing,
#     48:RPMOparse.PS_Handover_Execution_Attempt,
#     49:RPMOparse.PS_Handover_Result,
#     50:RPMOparse.PS_Handover_Preparation_Incoming,
# }