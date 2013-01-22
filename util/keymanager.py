#______________________________
HEADER_RECORD = {
    'Header Record id':0,
    'File format version':1,
    'Timestamp':2,
    'BSC ID':3,
    'Application version':4,
    'BSC name':5,
    'Cell pointer':6,
    'Cell name':7,
    'Neighbour Cell pointer':8,
    'Neighbour Cell name':9,
}

#______________________________
EVENT_NDW_DICT = (
    [3],
    [3],    
    [4],
    [4],
    None,
    [8],
    [3],  # 7 in pdf
    [16, 17], # 17 in pdf
    [9],
    [10],
    [10],
    [7],
    [3],
    [3],
    [7],
    [7],
    None,
    None,
    [18],
    [20],
    [4, 8], # 4 in pdf
    None,
    [10],
    [7],
    [2],
    [5],
    [4],
    [6],
    [5],
    [4],
    [4],
    [4],
    [4],
    [4],
    [4],
    [3],
    [17],
    [12,13,14,15],
    [20],
    [4],
    [3],
    [8],
    [18],
    [6],
    [3],
    [15],
    [8],
    [4],
    [6],
    [4],
    [3],
)

#______________________________
EVENT_TABLE_LENS = (
    18,
    18,
    20,
    20,
    None,
    28,
    18, # in the pdf, I count 26  18
    44, # in the pdf, I count 46
    30,
    32,
    32,
    26,
    18,
    18,
    26,
    26,
    None,
    None,
    48,
    20,
    28,
    None,
    32,
    26,
    16,
    22,
    20,
    24,
    22,
    20,
    20,
    20,
    20,
    20,
    20,
    18,
    46,
    42,
    52,
    20,
    18,
    28,
    48,
    24,
    18,
    42,
    28,
    20,
    24,
    20,
    18,
)

#______________________________
ITEM_DICT = {
    'Sequence number':0,
    'Event id':1,
    'MO':2,
    'Timestamp':3,
    'Internal event lost':4,
    'event lost 1':5,
    'event lost 2':6,
    'event lost 3':7,
    'event lost 4':8,
    'event lost 5':9,
    'event lost 6':10,
    'event lost 7':11,
    'event lost 8':12,
    'event lost 9':13,
    'event lost 10':14,
    'event lost 11':15,
    'event lost 12':16,
    'event lost 13':17,
    'event lost 14':18,
    'event lost 15':19,
    'event lost 16':20,
    'event lost cause':21,
    'BPC Cap':22,
    'Subcell type':23,
    'channel type':24,
    'deblocked channel number':25,
    'number of deblocked channels FR':26,
    'number of deblocked channels HR':27,
    'channel number related channel 1':28,
    'channel number related channel 2':29,
    'Ms individual':30,
    'cause value':31,
    'ISHO resource allocation result':32,
    'Urgency Condition':33,
    'Extended Cause':34,
    'Release Type':35,
    'Repeated SACCH Activation Indicator':36,
    'target cell indicator':37,
    'IMEI TAC':38,
    'IMEI FAC':39,
    'IMEI SNR':40,
    'IMEI SVN':41,
    'channel mode':42,
    'channel type TN':43,
    'channel type/ CDMA offset':44,
    'channel type TCS':45,
    'hopping channel':46,
    'single RF/ RF hopping channel':47,
    'Reason':48,
    'Traffic Case':49,
    'locating cause':50,
    'Ciphering Algorithm':51,
    'Start Ciphering':52,
    'DHA Evaluation Data':53,
    'MS UMTS FDD CAP':54,
    'MS SAIC CAP':55,
    'Ms supported ciphering algorithms':56,
    'MS Repeated SACCH Capability':57,
    'ISHO event reason':58,
    'GPRS Ms individual':59,
    'MS Context Id':60,
    'Num Of Rec PMR':61,
    'NC2 Profile':62,
    'NC2 Cause':63,
    'NCRPT':64,
    'Number Of UTRAN CR Prevention':65,
    'reestablish of layer 2 indicator':66,
    'handover failure message indicator':67,
    'EIT':68,
    'Direction':69,
    'Result':70,
    'Admission reject cause':71,
    'available channel number':72,
    'number of available channels FR':73,
    'number of available channels HR':74,
    'number of multi-rat mobiles':75,
    'cpich ec/n0':76,
    'blocked channel number':77,
    'Connection Type':78,
    'Alloc Band':79,
    'busy channel number':80,
    'number of busy channels FR':81,
    'number of busy channels HR':82,
    'number of busy channels HSCSD':83,
    'number of busy channels PDCH dedicated':84,
    'number of busy channels PDCH on demand':85,
    'Data Rate':86,
    'Speech version':87,
    'Time slot number':88,
    'DTM Flag':89,
    'Channel group':90,
    'Number of allocated channels':91,
    'Number of requested channels':92,
    'Allocated timeslot number':93,
    'TRXC MOID':94,
    'ABIS Config':95,
    'ABIS Rate':96,
    'Sub Slot':97,
    'Priority level':98,
    'RR cause':99,
    'Data Valid Indicator':100,
    'Timing advance(source)':101,
    'Timing advance(target)':102,
    'Mobile time difference':103,
    'Fnoffset(source)':104,
    'Fnoffset(target)':105,
    'channel requested speech/data indicator':106,
    'channel requested speech/data':107,
    'target subcell':108,
    'channel number related channel 3':109,
    'channel number related channel 4':110,
    'channel number related channel 5':111,
    'channel number related channel 6':112,
    'channel number related channel 7':113,
    'ABIS rate related channel 1':114,
    'ABIS config related channel 1':115,
    'ABIS rate related channel 2':116,
    'ABIS config related channel 2':117,
    'ABIS rate related channel 3':118,
    'ABIS config related channel 3':119,
    'ABIS rate related channel 4':120,
    'ABIS config related channel 4':121,
    'ABIS rate related channel 5':122,
    'ABIS config related channel 5':123,
    'ABIS rate related channel 6':124,
    'ABIS config related channel 6':125,
    'ABIS rate related channel 7':126,
    'ABIS config related channel 7':127,
    'timing advance':128,
    'reporting rate level':129,
    'rxqual up-link':130,
    'rxqual down-link':131,
    'rxlev up-link':132,
    'rxlev down-link':133,
    'speech quality index up-link':134,
    'speech quality index down-link':135,
    'bts power reduction':136,
    'ms power':137,
    'rxlev own bcch':138,
    'Codec type':139,
    'codec mode ul':140,
    'codec mode dl':141,
    'rxlev bss neighbour cell1':142,
    'rxlev bss neighbour cell2':143,
    'rxlev bss neighbour cell3':144,
    'rxlev bss neighbour cell4':145,
    'rxlev bss neighbour cell5':146,
    'rxlev bss neighbour cell6':147,
    'fer up-link':148,
    'fer down-link':149,
    'bcch arfcn neighbour cell1':150,
    'bcc neighbour cell1':151,
    'ncc neighbour cell1':152,
    'bcch arfcn neighbour cell2':153,
    'bcc neighbour cell2':154,
    'ncc neighbour cell2':155,
    'bcch arfcn neighbour cell3':156,
    'bcc neighbour cell3':157,
    'ncc neighbour cell3':158,
    'bcch arfcn neighbour cell4':159,
    'bcc neighbour cell4':160,
    'ncc neighbour cell4':161,
    'bcch arfcn neighbour cell5':162,
    'bcc neighbour cell5':163,
    'ncc neighbour cell5':164,
    'bcch arfcn neighbour cell6':165,
    'bcc neighbour cell6':166,
    'ncc neighbour cell6':167,
    'Repeated SACCH Repetition Indicator':168,
    'target cell':169,
    'bss neighbour cell1':170,
    'bss neighbour cell2':171,
    'bss neighbour cell3':172,
    'bss neighbour cell4':173,
    'bss neighbour cell5':174,
    'bss neighbour cell6':175,
    'IMSI Number':176,
    }

#______________________________
# RPMOTABLENAME = {
#     'header':"HeaderRecord", 
#     'event':"EventRecord", 
#     'footer':"FooterRecord"} 
RPMOTABLENAME = {
    'event':"EventRecord",} 

#______________________________


# EID = 0
Assignment_Request_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
    ('MO', 16, 0, 16),
    ('channel requested speech/data', 18, 0, 8),
    ('channel requested speech/data indicator', 18, 8, 4),
)

#______________________________
# EID = 1
Assignment_Failed_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    ('cause value',18,0,16),
)

#______________________________
# EID = 2
Clear_Request_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',18, 0, 16),
    ('channel type',16,12,4),
    ('cause value',20,0,16),

)

#______________________________
# EID = 3
Clear_Command_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
    ('channel type',16,12,4),
	('MO',18, 0, 16),
    ('cause value',20,0,16),
)

#______________________________
# EID = 5

Handover_Command_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    
    ('target cell', 18, 0, 16),
    ('target cell indicator', 18, 0, 1),

    ('Start Ciphering',20,0,1),
    ('Ciphering Algorithm',20,1,3),
    ('target subcell',20,4,4),
    
    ('channel type TN',21,5,3),
    ('channel type/ CDMA offset',21,0,5),
    ('single RF/ RF hopping channel',22,4,12),
    ('hopping channel',22,3,1),
    ('channel type TCS',22,0,3),
    
    ('Reason',24,0,8),
    ('Traffic Case',24,8,8),
    ('locating cause',26,0,16),
    ('channel mode',28,6,8),
    ('DHA Evaluation Data',28,14,2),
)

#______________________________
# EID = 6
Handover_Complete_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    #('Data Valid Indicator',18,3,1),
    ('Subcell type',18,4,4),
    ('RR cause',19,0,8),
    #('Timing advance(source)',20,0,8),
    #('Timing advance(target)',20,8,8),
    #('Mobile time difference',22,0,21),
    #('Fnoffset(source)',24,5,11),
    #('Fnoffset(target)',26,5,11),

)

#______________________________
# EID = 7
Channel_Busy_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    ('Connection Type',18,0,4),
    ('Subcell type',18,4,4),
    ('Alloc Band',18,8,4),
    ('channel type',19,4,4),
    ('busy channel number',20,0,16),
    ('number of busy channels FR',24,0,16),
    ('number of busy channels HR',26,0,16),
    ('number of busy channels HSCSD',28,0,16),
    ('number of busy channels PDCH dedicated',30,0,16),
    ('number of busy channels PDCH on demand',32,0,16),
    ('number of deblocked channels FR',34,0,16),
    ('number of deblocked channels HR',36,0,16),
    ('Data Rate',38,0,4),
    ('Speech version',38,4,4),
    ('BPC Cap',38,8,4),
    ('Time slot number',38,12,4),
    ('Priority level',40,3,4),
    ('ABIS Config',40,7,1),
    ('ABIS Rate',40,8,2),
    ('Sub Slot',40,10,1),
    ('Channel group',40,11,4),
    ('DTM Flag',40,15,1),
    ('number of multi-rat mobiles',42,0,16),
    ('TRXC MOID',44,0,16),
    # ('Number of allocated channels',46,0,4),
    # ('Number of requested channels',46,4,4),
    # ('Allocated timeslot number',47,0,8),

)

#______________________________
# EID = 8
Channel_Available_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
	('MO',14, 0, 16),
    ('BPC Cap',16,0,4),
    ('Subcell type',16,4,4),
    ('channel type',16,12,4),
    ('available channel number',18,0,16),
    ('number of available channels FR',22,0,16),
    ('number of available channels HR',24,0,16),
    ('number of deblocked channels FR',26,0,16),
    ('number of deblocked channels HR',28,0,16),
    ('number of multi-rat mobiles',30,0,16),
)

#______________________________
# EID = 9
Channel_Blocked_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
	('MO',14, 0, 16),
    ('BPC Cap',16,0,4),
    ('Subcell type',16,4,4),
    ('channel type',16,12,4),
    ('number of deblocked channels FR',22,0,16),
    ('number of deblocked channels HR',24,0,16),


)

#______________________________
# EID = 10
Channel_Deblocked_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
	('MO',14, 0, 16),
    ('BPC Cap',16,0,4),
    ('Subcell type',16,4,4),
    ('channel type',16,12,4),
    ('number of deblocked channels FR',22,0,16),
    ('number of deblocked channels HR',24,0,16),


)

#______________________________
# EID = 11
Assignment_Command_Correspond = (

    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    ('Start Ciphering',18,0,1),
    ('Ciphering Algorithm',18,1,3),
    ('Subcell type',18,4,4),
    ('channel mode',18,8,8),
    ('DHA Evaluation Data',20,6,2),
    
    ('channel type TN',21,5,3),
    ('channel type/ CDMA offset',21,0,5),
    ('single RF/ RF hopping channel',22,4,12),
    ('hopping channel',22,3,1),
    ('channel type TCS',22,0,3),
    
    ('Reason',24,0,8),
    ('Traffic Case',24,8,8),
    ('locating cause',26,0,16),


)

#______________________________
# EID = 12
Assignment_Complete_Correspond = (

    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    ('Subcell type',18,4,4),
    ('RR cause',19,0,8),
    #('')


)

#______________________________
# EID = 13
Assignment_Failed_MS_to_BSC_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    ('Subcell type',18,4,4),


)

#______________________________
# EID = 14
Cipher_Mode_Complete_Correspond = (

    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    
    # ('IMEI TAC',18,4,24),
    # ('IMEI FAC',21,4,8),
    # ('IMEI SNR',22,4,24),
    # ('IMEI SVN',25,4,8),
    #have problem imeisv

)

#______________________________
# EID = 15
GPRS_Flush_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
	('MO',16, 0, 16),
    ('MS Context Id',18,0,16),
    ('Data Valid Indicator',22,7,1),
    ('MS SAIC CAP',22,8,2),



)

#______________________________
# EID = 18
Channel_Busy_Extended_event_Correspond = (

    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    
    # ('channel number related channel 1',18,0,16),
    # ('channel number related channel 2',22,0,16),
    # ('channel number related channel 3',26,0,16),
    # ('channel number related channel 4',30,0,16),
    # ('channel number related channel 5',34,0,16),
    # ('channel number related channel 6',38,0,16),
    # ('channel number related channel 7',42,0,16),
    # attention-------------------------------
    # ('channel number related channel 1',18,0,32),
    # ('channel number related channel 2',22,0,32),
    # ('channel number related channel 3',26,0,32),
    # ('channel number related channel 4',30,0,32),
    # ('channel number related channel 5',34,0,32),
    # ('channel number related channel 6',38,0,32),
    # ('channel number related channel 7',42,0,32),
    ('ABIS config related channel 5',46,1,1),
    ('ABIS rate related channel 5',46,2,2),
    ('ABIS config related channel 4',46,4,1),
    ('ABIS rate related channel 4',46,5,2),
    ('ABIS config related channel 3',46,7,1),
    ('ABIS rate related channel 3',47,0,2),
    ('ABIS config related channel 2',47,2,1),
    ('ABIS rate related channel 2',47,3,2),
    ('ABIS config related channel 1',47,5,1),
    ('ABIS rate related channel 1',47,6,2),
    ('ABIS config related channel 7',49,2,1),
    ('ABIS rate related channel 7',49,3,2),
    ('ABIS config related channel 6',49,5,1),
    ('ABIS rate related channel 6',49,6,2),

)

#______________________________
# EID = 19
DTM_Establishment_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
    ('MS Context Id',16,0,16),
	('MO',20, 0, 16),



)

#______________________________
# EID = 20
MS_Context_Established_Correspond = (

    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('GPRS Ms individual',14,0,16),
	('MO',16, 0, 16),
    ('IMSI Number',22,4,60),

    #('')


)

#______________________________
# EID = 22
Data_Activity_Ends_Correspond = (

    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('MS Context Id',14,0,16),
	('MO',18, 0, 16),
    ('Data Valid Indicator',28,7,1),
    ('MS SAIC CAP',28,8,2),
    ('DTM Flag',28,11,1),
    ('Direction',28,13,1),
    #('')



)

#______________________________
# EID = 23
TBF_Changes_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('MS Context Id',14,0,16),
	('MO',18, 0, 16),
    ('Direction',20,15,1),



)

#______________________________
# EID = 24
Connect_Acknowledge_Correspond = (

    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    #('')


)

#______________________________
# EID = 25
IP_Buffer_Discard_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('MS Context Id',14,0,16),
	('MO',18, 0, 16),
    ('Subcell type',22,12,4),


)

#______________________________
# EID = 26
Admission_Control_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('MS Context Id',14,0,16),
	('MO',18, 0, 16),
    ('Admission reject cause',20,0,4),
    ('Result',20,13,1),
    ('Direction',20,14,1),
    ('EIT',20,15,1),
)


#______________________________
# EID = 27
Handover_Failure_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual',14,0,16),
	('MO',16, 0, 16),
    #attention
	('target cell', 18, 0, 16),
    ('target cell indicator', 18, 0, 1),
    ('cause value',20,0,16),
    ('Reason',22,0,8),
    ('Traffic Case',22,8,8),
    ('reestablish of layer 2 indicator',24,6,1),
    ('handover failure message indicator',24,7,1),
    ('Extended Cause',24,8,8),



)

#______________________________
# EID = 28
Inter_System_Handover_Command_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual',14,0,16),
	('MO',16, 0, 16),
    ('target cell', 18, 0, 16),
    ('target cell indicator', 18, 0, 1),
    ('locating cause',20,0,16),
    ('DHA Evaluation Data',22,6,2),
    ('cpich ec/n0',22,8,8),

)

#______________________________
# EID = 29
Incoming_Inter_System_Handover_Result_Correspond = (

    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual',14,0,16),
	('MO',16, 0, 16),
    ('cause value',18,0,16),
    ('ISHO resource allocation result',20,12,4),
)

#______________________________
# EID = 30
Outgoing_Inter_System_Handover_Result_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual',14,0,16),
	('MO',16, 0, 16),
	('target cell', 18, 0, 16),
    ('target cell indicator', 18, 0, 1),
    ('ISHO resource allocation result',20,12,4),
    #('')


)

#______________________________
# EID = 31
VGCS_Notification_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
	('MO',14, 0, 16),
    ('Priority level',20,12,4),


)

#______________________________
# EID = 32
VGCS_Channel_Setup_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
	('MO',14, 0, 16),
    ('channel mode',20,0,8),
    ('channel type',20,12,4),


)

#______________________________
# EID = 33
VGCS_Call_Release_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
	('MO',14, 0, 16),
    ('cause value',20,0,16),


)

#______________________________
# EID = 34
CS_Call_Release_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual',14,0,16),
    ('Repeated SACCH Activation Indicator',17,0,2),
    ('Release Type',17,2,2),
    ('channel type',17,4,4),
	('MO',18, 0, 16),
    ('Urgency Condition',20,0,8),
    ('Extended Cause',20,8,8),


)

#______________________________
# EID = 35
DTM_Ends_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual',14,0,16),
    #('')

)
# ---------EID = 36
Measurement_Result_Large_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    #---------------------- 
    #special treatment
    ('ncell bitmap', 18, 0, 6),
    #----------------------
    ('reporting rate level', 18, 6, 2),
    ('rxqual up-link', 19, 0, 4),
    ('rxqual down-link', 19, 4, 4),
    ('rxlev up-link', 20, 0, 8),
    ('rxlev down-link', 21, 0, 8),
    ('speech quality index up-link', 22, 0, 8),
    ('speech quality index down-link', 23, 0, 8),
    ('timing advance', 24, 0, 8),
    ('ms power', 25, 0, 8),
    ('Repeated SACCH Repetition Indicator', 26, 0, 1),
    ('codec mode ul', 26, 1, 2),
    ('codec mode dl', 26, 3, 2),
    ('rxlev own bcch', 26, 5, 3),
    ('Codec type', 27, 0, 4),
    ('bts power reduction', 27, 4, 4),
    ('bss neighbour cell1', 28, 0, 16),
    ('bss neighbour cell2', 30, 0, 16),
    ('bss neighbour cell3', 32, 0, 16),
    ('bss neighbour cell4', 34, 0, 16),
    ('bss neighbour cell5', 36, 0, 16),
    ('bss neighbour cell6', 38, 0, 16),
    ('rxlev bss neighbour cell1', 40, 0, 8),
    ('rxlev bss neighbour cell2', 41, 0, 8),
    ('rxlev bss neighbour cell3', 42, 0, 8),
    ('rxlev bss neighbour cell4', 43, 0, 8),
    ('rxlev bss neighbour cell5', 44, 0, 8),
    ('rxlev bss neighbour cell6', 45, 0, 8),
    ('fer up-link', 46, 0, 8),
    ('fer down-link', 47, 0, 8),
)
# ---------EID = 37
Measurement_Result_Medium_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    ('Repeated SACCH Repetition Indicator', 18, 5, 1),
    ('reporting rate level', 18, 6, 2),
    ('rxqual up-link', 19, 0, 4),
    ('rxqual down-link', 19, 4, 4),
    ('rxlev up-link', 20, 0, 8),
    ('rxlev down-link', 21, 0, 8),
    ('speech quality index up-link', 22, 0, 8),
    ('speech quality index down-link', 23, 0, 8),
    ('timing advance', 24, 0, 8),
    ('ms power', 25, 0, 8),
    ('rxlev own bcch', 26, 0, 8),
    ('Codec type', 27, 0, 4),
    ('bts power reduction', 27, 4, 4),
    ('fer up-link', 28, 0, 8),
    ('fer down-link', 29, 0, 8),
)
# ---------EID = 38
TBF_Ends_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('MS Context Id', 14, 0, 16),
	('MO',18, 0, 16),
    #('wait'),

)
# ---------EID = 39
Inter_System_Handover_Information_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    ('ISHO event reason', 20, 0, 16),
)
# ---------EID = 40
VGCS_Channel_Release_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
)
# ---------EID = 41
VGCS_Notification_Response_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
	('MO',14, 0, 16),
)
# ---------EID = 42
Packet_Measurement_Report_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('MS Context Id', 14, 0, 16),
	('MO',18, 0, 16),
    ('rxlev down-link', 21, 0, 8),
)
# ---------EID = 43
NC2_Session_Ends_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('MS Context Id', 14, 0, 16),
	('MO',18, 0, 16),
    ('Num Of Rec PMR', 20, 0, 16),
    ('NC2 Profile', 22, 0, 8),
    ('NC2 Cause', 23, 0, 5),
    ('NCRPT', 23, 5, 3),
    ('Number Of UTRAN CR Prevention', 24, 0, 16),
)
# ---------EID = 44
Classmark_Information_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    ('MS Repeated SACCH Capability', 18, 5, 1),
    ('Ms supported ciphering algorithms', 18, 6, 7),
    ('MS UMTS FDD CAP', 19, 5, 1),
    ('MS SAIC CAP', 19, 6, 2),
)
# ---------EID = 45
RTT_Mapping_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
    ('IMEI SVN', 28, 0, 80),
    ('MS Context Id', 38, 0, 16),
)
# ---------EID = 46
RTT_Status_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('Ms individual', 14, 0, 16),
	('MO',16, 0, 16),
)
# ---------EID = 47
PS_Handover_Preparation_Outgoing_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('MS Context Id', 14, 0, 16),
	('MO',16, 0, 16),

)
# ---------EID = 48
PS_Handover_Execution_Attempt_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('MS Context Id', 14, 0, 16),
	('MO',16, 0, 16),
    ('Data Valid Indicator', 21, 2, 1),
    ('MS SAIC CAP', 21, 3, 2),
)
# ---------EID = 49
PS_Handover_Result_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('MS Context Id', 14, 0, 16),
	('MO',16, 0, 16),
    ('Data Valid Indicator', 20, 2, 1),
    ('MS SAIC CAP', 20, 3, 2),

)
# ---------EID = 50
PS_Handover_Preparation_Incoming_Correspond = (
    ('Event id', 2, 0, 16),
    ('Timestamp', 6, 0, 64),
    ('MS Context Id', 14, 0, 16),
	('MO',16, 0, 16),
)








# if name == '__name__':
    # parse_list = {
            # 0:Assignment_Request_Correspond,
            # 1:Assignment_Failed_Correspond,
            # 2:Clear_Request_Correspond,
            # 3:Clear_Command_Correspond,
            # 4:None,            
            # 5:Handover_Command_Correspond,
            # 6:Handover_Complete_Correspond,
            # 7:Channel_Busy_Correspond,
            # 8:Channel_Available_Correspond,
            # 9:Channel_Blocked_Correspond,
            # 10:Channel_Deblocked_Correspond,
            # 11:Assignment_Command_Correspond,
            # 12:Assignment_Complete_Correspond,
            # 13:Assignment_Failed_MS_to_BSC_Correspond,
            # 14:Cipher_Mode_Complete_Correspond,
            # 15:GPRS_Flush_Correspond,
            # 16:None,                
            # 17:None,               
            # 18:Channel_Busy_Extended_event_Correspond, # look at pdf 4.2.9
            # 19:DTM_Establishment_Correspond,
            # 20:MS_Context_Established_Correspond,
            # 21:None,               
            # 22:Data_Activity_Ends_Correspond,
            # 23:TBF_Changes_Correspond,
            # 24:Connect_Acknowledge_Correspond,
            # 25:IP_Buffer_Discard_Correspond,
            # 26:Admission_Control_Correspond,
            # 27:Handover_Failure_Correspond,
            # 28:Inter_System_Handover_Command_Correspond,
            # 29:Incoming_Inter_System_Handover_Result_Correspond,
            # 30:Outgoing_Inter_System_Handover_Result_Correspond,
            # 31:VGCS_Notification_Correspond,
            # 32:VGCS_Channel_Setup_Correspond,
            # 33:VGCS_Call_Release_Correspond,
            # 34:CS_Call_Release_Correspond,
            # 35:DTM_Ends_Correspond,
            # 36:Measurement_Result_Large_Correspond,
            # 37:Measurement_Result_Medium_Correspond,
            # 38:TBF_Ends_Correspond,
            # 39:Inter_System_Handover_Information_Correspond,
            # 40:VGCS_Channel_Release_Correspond,
            # 41:VGCS_Notification_Response_Correspond,
            # 42:Packet_Measurement_Report_Correspond,
            # 43:NC2_Session_Ends_Correspond,
            # 44:Classmark_Information_Correspond,
            # 45:RTT_Mapping_Correspond,
            # 46:RTT_Status_Correspond,
            # 47:PS_Handover_Preparation_Outgoing_Correspond,
            # 48:PS_Handover_Execution_Attempt_Correspond,
            # 49:PS_Handover_Result_Correspond,
            # 50:PS_Handover_Preparation_Incoming_Correspond,
        # }

    # for item in parse_list:
        # table = parse_list[item]
        # if table == None: continue
        # for element in table:
            # if element[0] not in ITEM_DICT:
                # print 'find error in %s which is %s!' % (item, element[0])