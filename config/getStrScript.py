instream = open('str.txt', 'r')

temp = []
num = []
import re
for line in instream.readlines():
    if 'self' in line:
        name = line[line.find('.') + 1:line.find(',')]
        _num = re.findall('\d+',line)[0]
        num.append(_num)
        temp.append(name)
print len(temp), len(num)
for i in range(len(temp)):
    print '    #' + '_'*30
    print '    # EID = %s' % num[i]
    print '    ' + 'def ' + temp[i] + '(self, pos):'
    print '        pass\n\n'

for i in range(len(temp)):
    print '#' + '_'*30
    print '# EID = %s' % num[i]
    print temp[i] + '_Correspond = {'
    print '}\n'
instream.close()

#--------------------------------------
# result
# 47 47
#     #______________________________
#     # EID = 0
#     def Assignment_Request(self, pos):
#         pass


#     #______________________________
#     # EID = 1
#     def Assignment_Failed(self, pos):
#         pass


#     #______________________________
#     # EID = 2
#     def Clear_Request(self, pos):
#         pass


#     #______________________________
#     # EID = 3
#     def Clear_Command(self, pos):
#         pass


#     #______________________________
#     # EID = 5
#     def Handover_Command(self, pos):
#         pass


#     #______________________________
#     # EID = 6
#     def Handover_Complete(self, pos):
#         pass


#     #______________________________
#     # EID = 7
#     def Channel_Busy(self, pos):
#         pass


#     #______________________________
#     # EID = 8
#     def Channel_Available(self, pos):
#         pass


#     #______________________________
#     # EID = 9
#     def Channel_Blocked(self, pos):
#         pass


#     #______________________________
#     # EID = 10
#     def Channel_Deblocked(self, pos):
#         pass


#     #______________________________
#     # EID = 11
#     def Assignment_Command(self, pos):
#         pass


#     #______________________________
#     # EID = 12
#     def Assignment_Complete(self, pos):
#         pass


#     #______________________________
#     # EID = 13
#     def Assignment_Failed_MS_to_BSC(self, pos):
#         pass


#     #______________________________
#     # EID = 14
#     def Cipher_Mode_Complete(self, pos):
#         pass


#     #______________________________
#     # EID = 15
#     def GPRS_Flush(self, pos):
#         pass


#     #______________________________
#     # EID = 18
#     def Channel_Busy_Extended_event(self, pos):
#         pass


#     #______________________________
#     # EID = 19
#     def DTM_Establishment(self, pos):
#         pass


#     #______________________________
#     # EID = 20
#     def MS_Context_Established(self, pos):
#         pass


#     #______________________________
#     # EID = 22
#     def Data_Activity_Ends(self, pos):
#         pass


#     #______________________________
#     # EID = 23
#     def TBF_Changes(self, pos):
#         pass


#     #______________________________
#     # EID = 24
#     def Connect_Acknowledge(self, pos):
#         pass


#     #______________________________
#     # EID = 25
#     def IP_Buffer_Discard(self, pos):
#         pass


#     #______________________________
#     # EID = 26
#     def Admission_Control(self, pos):
#         pass


#     #______________________________
#     # EID = 27
#     def Handover Failure(self, pos):
#         pass


#     #______________________________
#     # EID = 28
#     def Inter_System_Handover_Command(self, pos):
#         pass


#     #______________________________
#     # EID = 29
#     def Incoming_Inter_System_Handover_Result(self, pos):
#         pass


#     #______________________________
#     # EID = 30
#     def Outgoing_Inter_System_Handover_Result(self, pos):
#         pass


#     #______________________________
#     # EID = 31
#     def VGCS_Notification(self, pos):
#         pass


#     #______________________________
#     # EID = 32
#     def VGCS_Channel_Setup(self, pos):
#         pass


#     #______________________________
#     # EID = 33
#     def VGCS_Call_Release(self, pos):
#         pass


#     #______________________________
#     # EID = 34
#     def CS_Call_Release(self, pos):
#         pass


#     #______________________________
#     # EID = 35
#     def DTM_Ends(self, pos):
#         pass


#     #______________________________
#     # EID = 36
#     def Measurement_Result_Large(self, pos):
#         pass


#     #______________________________
#     # EID = 37
#     def Measurement_Result_Medium(self, pos):
#         pass


#     #______________________________
#     # EID = 38
#     def TBF_Ends(self, pos):
#         pass


#     #______________________________
#     # EID = 39
#     def Inter_System_Handover_Information(self, pos):
#         pass


#     #______________________________
#     # EID = 40
#     def VGCS_Channel_Release(self, pos):
#         pass


#     #______________________________
#     # EID = 41
#     def VGCS_Notification_Response(self, pos):
#         pass


#     #______________________________
#     # EID = 42
#     def Packet_Measurement_Report(self, pos):
#         pass


#     #______________________________
#     # EID = 43
#     def NC2_Session_Ends(self, pos):
#         pass


#     #______________________________
#     # EID = 44
#     def Classmark_Information(self, pos):
#         pass


#     #______________________________
#     # EID = 45
#     def RTT_Mapping(self, pos):
#         pass


#     #______________________________
#     # EID = 46
#     def RTT_Status(self, pos):
#         pass


#     #______________________________
#     # EID = 47
#     def PS_Handover_Preparation_Outgoing(self, pos):
#         pass


#     #______________________________
#     # EID = 48
#     def PS_Handover_Execution_Attempt(self, pos):
#         pass


#     #______________________________
#     # EID = 49
#     def PS_Handover_Result(self, pos):
#         pass


#     #______________________________
#     # EID = 50
#     def PS_Handover_Preparation_Incoming(self, pos):
#         pass


# [Finished in 0.2s]