# -*- coding: utf-8 -*-
import os, sys

######################
#importer
encoding = sys.getfilesystemencoding()
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(unicode(__file__,encoding)), os.path.pardir))
if os.path.exists(os.path.join(ROOT_DIR,'util')):
    sys.path.insert(0, ROOT_DIR)
    sys.path.insert(0, os.path.join(ROOT_DIR, 'bin'))
    sys.path.insert(0, os.path.join(ROOT_DIR, 'config'))    
    sys.path.insert(0, os.path.join(ROOT_DIR, 'util'))
else:
    raise Exception("Cannot find root dir.")

from config.strConfig import *
from util.keymanager import *
import datetime

class FakeStream(object):
    def __init__(self, filename, mode = 'r+'):
        if filename.endswith('.gz'):
            import gzip
            self.instream = gzip.open(filename).read()
        else:
            with file(filename, mode) as f:
                self.instream = f.read()
        self.filesize = len(self.instream)
        self.pos = 0
    def seek(self, pos):
        self.pos = pos
    def read(self, bytes):
        ret = self.instream[self.pos: self.pos + bytes]
        self.pos += bytes
        return ret
        
    def seekAndReads(self, pos, bytes):
        _data = [ord(self.instream[pos + i]) * pow(256, bytes - i - 1) for i in range(bytes)]
        return sum(_data)

    def seekAndRead(self, pos):
        return ord(self.instream[pos])
    
    def getsize(self):
        return len(self.instream)
    
    def close(self):
        pass
        
    
		

class RPMOparse(object):
    def __init__(self, infile = None, outpath = None, jsonfile = None):

        infile = unicode(infile, encoding)
        outpath = unicode(outpath, encoding)
        jsonfile = unicode(jsonfile, encoding)

        self.source_file      = infile

        #self.source_file_size = os.path.getsize(infile)
        self.source_basename  = os.path.basename(self.source_file)
        self.source_path      = os.path.dirname(infile)
        self.save_path        = outpath
        self.jsonfile         = jsonfile
        
        self.warning_list     = []
        self.exception_list   = []
        #save the exception info for json
        
        #self.instream = file(self.source_file, 'rb')
        self.instream = FakeStream(self.source_file, 'rb')
        
        
        # save_file_header      = os.path.join(self.save_path, self.source_basename + '_' + RPMOTABLENAME['header'] + '.txt')
        save_file_event       = os.path.join(self.save_path, self.source_basename + '_' + RPMOTABLENAME['event'] + '.txt')
        # self.outstream_header = file(save_file_header, 'w')
        self.outstream_event  = file(save_file_event, 'w')

        # print start line
        self.printStartLine()

        self.startDateTime = datetime.datetime(1970, 1, 1, 0, 0, 0)

        self.item_dict_len = len(ITEM_DICT)

        self.init_dict()
        self.seqnumber = 0

    def printStartLine(self):
        _temp = {}
        for key, value in ITEM_DICT.items(): 
            _temp[value] = key

        self.outstream_event.write('\t'.join([_temp[i] for i in range(len(_temp))]) + '\n')


    def init_dict(self):
        '''
        init the func-index dict 
        '''
        self.parse_list = {
            0:Assignment_Request_Correspond,
            1:Assignment_Failed_Correspond,
            2:Clear_Request_Correspond,
            3:Clear_Command_Correspond,
            4:None,            
            5:Handover_Command_Correspond,
            6:Handover_Complete_Correspond,
            7:Channel_Busy_Correspond,
            8:Channel_Available_Correspond,
            9:Channel_Blocked_Correspond,
            10:Channel_Deblocked_Correspond,
            11:Assignment_Command_Correspond,
            12:Assignment_Complete_Correspond,
            13:Assignment_Failed_MS_to_BSC_Correspond,
            14:Cipher_Mode_Complete_Correspond,
            15:GPRS_Flush_Correspond,
            16:None,                
            17:None,               
            18:Channel_Busy_Extended_event_Correspond, # look at pdf 4.2.9
            19:DTM_Establishment_Correspond,
            20:MS_Context_Established_Correspond,
            21:None,               
            22:Data_Activity_Ends_Correspond,
            23:TBF_Changes_Correspond,
            24:Connect_Acknowledge_Correspond,
            25:IP_Buffer_Discard_Correspond,
            26:Admission_Control_Correspond,
            27:Handover_Failure_Correspond,
            28:Inter_System_Handover_Command_Correspond,
            29:Incoming_Inter_System_Handover_Result_Correspond,
            30:Outgoing_Inter_System_Handover_Result_Correspond,
            31:VGCS_Notification_Correspond,
            32:VGCS_Channel_Setup_Correspond,
            33:VGCS_Call_Release_Correspond,
            34:CS_Call_Release_Correspond,
            35:DTM_Ends_Correspond,
            36:Measurement_Result_Large_Correspond,
            37:Measurement_Result_Medium_Correspond,
            38:TBF_Ends_Correspond,
            39:Inter_System_Handover_Information_Correspond,
            40:VGCS_Channel_Release_Correspond,
            41:VGCS_Notification_Response_Correspond,
            42:Packet_Measurement_Report_Correspond,
            43:NC2_Session_Ends_Correspond,
            44:Classmark_Information_Correspond,
            45:RTT_Mapping_Correspond,
            46:RTT_Status_Correspond,
            47:PS_Handover_Preparation_Outgoing_Correspond,
            48:PS_Handover_Execution_Attempt_Correspond,
            49:PS_Handover_Result_Correspond,
            50:PS_Handover_Preparation_Incoming_Correspond,
        }

        self.BSCINFO = {} # The dict of bsc info (Tree structure)
        self.CELLINFO = {} # conserve cell info (cell : (cell point, bscname))
        self.ncell_list = (
                            'bss neighbour cell1',
                            'bss neighbour cell2',
                            'bss neighbour cell3',
                            'bss neighbour cell4',
                            'bss neighbour cell5',
                            'bss neighbour cell6',
                            'target cell',
        )
        self.IMEI = (
            (8, 4, 0, 28, 24, 20),
            (16, 44),
            (40, 36, 32, 60, 56, 52),
            (48, 76)
        )
        self.TABLE_LENS = len(EVENT_TABLE_LENS)

    def getDateTime(self, pos):
        '''
        get date and time
        '''
        _days = self.instream.seekAndReads(pos, 8) / 3600 /24
        return str(self.startDateTime + datetime.timedelta(_days))

    def getTimeStamp(self, pos):
        '''
        get time stamp
        '''
        _ = self.instream.seekAndRead(pos + 7) 
        _div = TIMESTAMP_DIV_ODD if _ % 2 else TIMESTAMP_DIV_EVEN
        _days = self.instream.seekAndReads(pos, 8) / 3600 / 24 / _div
        return str(self.startDateTime + datetime.timedelta(_days))
    
    def getName(self, pos, bytes):
        '''
        read and convert to ascii
        '''
        self.instream.seek(pos)
        return self.instream.read(bytes).strip(chr(0))

    def getCells(self, pos, num):
        '''
        return pos and a "(cellpoint, cellname)"-like list
        '''
        ret_list = []
        for i in range(num):
            _cellpointer = self.instream.seekAndReads(pos, 2)
            _cellname    = self.getName(pos + 2, 9)
            ret_list.append((_cellpointer, _cellname))
            pos += 11
        return pos, ret_list

    def write_header(self, cells, ncells):
        '''
        write header record to file
        '''
        _bscinfo = {'NAME':self.bsc_name, 'CELL':{}, 'NCELL':{}}
        for _item in cells:
            _bscinfo['CELL'][_item[0]] = _item[1]
            self.CELLINFO[_item[0]] = (_item[1], self.bsc_name)
        for _item in ncells:
            _bscinfo['NCELL'][_item[0]] = _item[1]
            if not self.CELLINFO.get(_item[0], None):
                self.CELLINFO[_item[0]] = (_item[1], 'Unknown')
        self.BSCINFO[self.bsc_id] = _bscinfo
        import simplejson
        with file('cellinfo.txt', 'w') as f:
            simplejson.dump(self.CELLINFO, f)
        # line = []
        # line.append(str(self.header_record_id))
        # line.append(str(self.file_format_version))
        # line.append(str(self.timestamp))
        # line.append(str(self.bsc_id))
        # line.append(str(self.application_version))
        # line.append(str(self.bsc_name))
        # for _item in cells:
        #     line.append('Cell point=%s,Cell name=%s'%(_item[0],_item[1]))
        # for _item in ncells:
        #     line.append('neighbour Cell point=%s,neighbour Cell name=%s'%(_item[0],_item[1]))
        # self.outstream_header.write(JOINSTR.join(line))
     
    def parse_footer(self):
        '''
        parse footer record
        '''
        # self.endtimestamp = self.getDateTime(FOOTER_TIMESTAMP_POS)
        # self.maxdays = self.instream.seekAndReads(FOOTER_TIMESTAMP_POS, 8) / 3600 /24 + 2
        #print self.endtimestamp
        self.maxdays = self.mindays + 365

    def parse_header(self):
        '''
        parse header record
        '''
        self.header_record_id = self.instream.seekAndRead(HEADER_RECORD_ID_POS)
        self.file_format_version = self.instream.seekAndRead(HEADER_FILE_FORMAT_VERSION)
        # count the datetime
        self.timestamp = self.getDateTime(HEADER_TIMESTAMP_POS)
        self.mindays = self.instream.seekAndReads(HEADER_TIMESTAMP_POS, 8) / 3600 / 24 - 2
        #------------------------------------------
        number_of_bscs = self.instream.seekAndRead(HEADER_BSC_POS)
        pos = HEADER_BSC_POS + 1
        while number_of_bscs:
            self.bsc_id = self.instream.seekAndRead(pos)
            self.application_version = self.instream.seekAndRead(pos + 1)
            self.bsc_name = self.getName(pos + 2, 8)
            number_of_cells = self.instream.seekAndReads(pos + 10, 2)
            # get info of cells and refresh pos
            pos, cells_list = self.getCells(pos + 12, number_of_cells)
            number_of_ncells = self.instream.seekAndReads(pos, 2)
            # get info of ncells and refresh pos
            pos, ncells_list = self.getCells(pos + 2, number_of_ncells)
            number_of_bscs -= 1

            self.write_header(cells_list, ncells_list)
           
        # self.outstream_header.close()

    def parse_event(self):
        '''
        parse event record
        '''
        pos = EVENT_START_POS
        self.instream.seek(pos)
        i = 0
        while pos < self.instream.filesize - FOOTER_RECORD_SIZE:
            try:
                eid = self.instream.seekAndReads(pos + 2, 2)
                ndw = self.instream.seekAndReads(pos + 4, 2)

                if eid == 36 and ndw in EVENT_NDW_DICT[eid]:
                    pos = self.parseList_EID_36(pos, eid)
                elif eid == 7 and ndw in EVENT_NDW_DICT[eid]:
                    pos = self.parseList(pos, eid)
                    if self.instream.seekAndRead(pos) != 1 or not self.parse_list.get(self.instream.seekAndReads(pos + 2, 2), None):
                        pos += 2
                elif eid == 6 and ndw in EVENT_NDW_DICT[eid]:
                    pos = self.parseList(pos, eid)
                    if self.instream.seekAndRead(pos) != 1 or not self.parse_list.get(self.instream.seekAndReads(pos + 2, 2), None):
                        pos += 8
                elif eid < self.TABLE_LENS and EVENT_TABLE_LENS[eid] != None and ndw in EVENT_NDW_DICT[eid]:
                    pos = self.parseList(pos, eid)
                else:
                    pos += 1
                    while pos < self.instream.filesize - FOOTER_RECORD_SIZE:
                        _eid = self.instream.seekAndReads(pos + 2, 2)
                        _ndw = self.instream.seekAndReads(pos + 4, 2)
                        if _eid < self.TABLE_LENS and EVENT_TABLE_LENS[_eid] != None and _ndw in EVENT_NDW_DICT[_eid]:
                            break
                        pos += 1
            # except 
            except Exception, e:
                self.warning_list.append(str(e))

    def posCount(self, pos):
        pos += 2
        while True:
            if self.instream.seekAndReads(pos, 2) == 36 and self.instream.seekAndReads(pos + 2, 2) == 17:
                return pos
            pos += 1
    def parseList_EID_36(self, pos, tabindex = 36):
        '''
        
        '''
        lens = EVENT_TABLE_LENS[tabindex] + 2
        # get the length of the data in stream
        try:
            tabinfo = self.parse_list[tabindex]
            if not tabinfo: 
                return EVENT_TABLE_LENS[tabindex] + 2 + pos 

            line= [''] * self.item_dict_len
            
            #self.instream.seek(pos + 1)
            #_bsc_id = ord(self.instream.read(1))
            _bsc_id = self.instream.seekAndRead(pos + 1)
            
            _table = bin(self.instream.seekAndReads(pos, lens)).lstrip('0b')
            _table = '0' * (lens * 8 - len(_table)) + _table
            
            _index = []
            _map = None
            for it in tabinfo:
                start = it[1] * 8 + it[2]
                try:
                    _data = int(_table[start:start + it[3]], 2)
                except:
                    print _table,len(_table),'eid=%s'%tabindex, start, it
                
                
                #--------------------------
                # sentence for int-convert-to-str
                #--------------------------
                if it[0] == 'ncell bitmap':
                    _map = map(int, _table[start:start + it[3]])
                
                elif it[0] in self.ncell_list: 
                    _index.append(_data)
                elif it[0] == 'Timestamp':
                    try:
                        #_data = self.num2date(_data)
                        line[ITEM_DICT[it[0]]] = self.num2date(_data)
                    except OverflowError, e:
                        return pos + lens
                elif it[0] == 'MO':
                    _bscdic = self.BSCINFO.get(_bsc_id, 'Unknown')
                    _bsc = 'Unknown' if _bscdic == 'Unknown' else _bscdic['NAME']
                    _cell = 'Unknown' if _bsc == 'Unknown' else _bscdic['CELL'].get(_data, 'Unknown')
                    line[ITEM_DICT['MO']] = 'NW=Network,BSC=%s,CELL=%s'%(_bsc, _cell)
                
                #else: it[0] != 'ncell bitmap' and it[0] != 'MO' and it[0] not in self.ncell_list: line[ITEM_DICT[it[0]]] = _data       
                else: line[ITEM_DICT[it[0]]] = _data 

            for i in xrange(6):
                _id = 6 - i
                start = (28 + 2 * i) * 8
                if _map[i] == 1:
                    line[ITEM_DICT['bcch arfcn neighbour cell%s'%_id]] = int(_table[start + 0 : start + 0 + 10], 2)
                    line[ITEM_DICT['bcc neighbour cell%s'%_id]] = int(_table[start + 10 : start + 10 + 3], 2)
                    line[ITEM_DICT['ncc neighbour cell%s'%_id]] = int(_table[start + 13 : start + 13 + 3], 2)
                    line[ITEM_DICT['bss neighbour cell%s'%_id]] = 'NW=Network,BSC=Unknown,CELL=Unknown'
                else:
                    _cellinfo = self.CELLINFO.get(_index[_id - 1], ('Unknown', 'Unknown'))
                    line[ITEM_DICT['bss neighbour cell%s'%_id]] = 'NW=Network,BSC=%s,CELL=%s'%(_cellinfo[1], _cellinfo[0])
                    #line[ITEM_DICT['bss neighbour cell%s'%_id]] = 'NW=Network,BSC=%s,CELL=%s'%(self.BSCINFO[_bsc_id]['NAME'], self.BSCINFO[_bsc_id]['NCELL'].get(_index[_id - 1], 'UNKNOWN'))
            
            # sequnce name
            line[0] = self.seqnumber
            self.seqnumber += 1
            # Mo
            #line[ITEM_DICT['MO']] = 'NW=Network,BSC=Unknown,CELL=Unknown'
            
            self.outstream_event.write(JOINSTR.join([str(_) for _ in line]) + '\n')
        except Exception, e:
            self.warning_list.append(str(e))
            
        return pos + lens
    
    
    def parseList(self, pos, tabindex):
        '''
        
        '''
        lens = EVENT_TABLE_LENS[tabindex] + 2
        # get the length of the data in stream
        
        try:
            tabinfo = self.parse_list[tabindex]
            if not tabinfo: 
                return EVENT_TABLE_LENS[tabindex] + 2 + pos 

            line= [''] * self.item_dict_len
            self.instream.seek(pos + 1)
            _bsc_id = ord(self.instream.read(1))
            _table = bin(self.instream.seekAndReads(pos, lens)).lstrip('0b')
            _table = '0' * (lens * 8 - len(_table)) + _table
            
            for it in tabinfo:
                start = it[1] * 8 + it[2]
                try:
                    _data = int(_table[start:start + it[3]], 2)
                except:
                    print _table,len(_table),'eid=%s'%tabindex, start, it
                
                #--------------------------
                # sentence for int-convert-to-str
                #--------------------------
                if it[0] == 'Timestamp':
                    try:
                        _data = self.num2date(_data)
                    except OverflowError, e:
                        return pos + lens
                elif it[0] == 'target cell': 
                    _cellinfo = self.CELLINFO.get(_data, ('Unknown', 'Unknown'))
                    _data = 'NW=Network,BSC=%s,CELL=%s'%(_cellinfo[1], _cellinfo[0])
                    #_data = 'NW=Network,BSC=%s,CELL=%s'%(self.BSCINFO[_bsc_id]['NAME'], self.BSCINFO[_bsc_id]['NCELL'].get(_data, 'Unknown'))
                elif it[0] == 'MO':
                    _bscdic = self.BSCINFO.get(_bsc_id, 'Unknown')
                    _bsc = 'Unknown' if _bscdic == 'Unknown' else _bscdic['NAME']
                    _cell = 'Unknown' if _bsc == 'Unknown' else _bscdic['CELL'].get(_data, 'Unknown')
                    _data = 'NW=Network,BSC=%s,CELL=%s'%(_bsc, _cell)
                
                #line[ITEM_DICT[it[0]]] = it[0] + ': ' + str(_data)
                line[ITEM_DICT[it[0]]] = _data
            #---------------------------
            #special treat for eid = 14 IMEISV
            if tabindex == 14:
                start = 18 * 8
                # get IMEI TAC
                _data = 0
                for i in xrange(6):
                    _data = _data * 10 + int(_table[start + self.IMEI[0][i] : start + self.IMEI[0][i] + 4], 2)
                line[ITEM_DICT['IMEI TAC']] = _data
                # get IMEI FAC
                _data = 0
                for i in xrange(2):
                    _data = _data * 10 + int(_table[start + self.IMEI[1][i] : start + self.IMEI[1][i] + 4], 2)
                line[ITEM_DICT['IMEI FAC']] = _data
                # get IMEI SNR
                _data = 0
                for i in xrange(6):
                    _data = _data * 10 + int(_table[start + self.IMEI[2][i] : start + self.IMEI[2][i] + 4], 2)
                line[ITEM_DICT['IMEI SNR']] = _data
                # get IMEI SVN
                _data = 0
                for i in xrange(2):
                    _data = _data * 10 + int(_table[start + self.IMEI[3][i] : start + self.IMEI[3][i] + 4], 2)
                line[ITEM_DICT['IMEI SVN']] = _data
            #------------------------------
            
            #---------------------------
            # sequnce name
            line[0] = self.seqnumber
            self.seqnumber += 1
            # Mo
            #line[ITEM_DICT['MO']] = 'NW=Network,BSC=Unknown,CELL=Unknown'

            self.outstream_event.write(JOINSTR.join([str(_) for _ in line]) + '\n')
        except Exception, e:
            self.warning_list.append(str(e))
            
        return pos + lens

    def num2date(self, dec):
        '''
        convert num to date
        '''
        _days =  float(dec) / (dec & 1 and TIMESTAMP_DIV_ODD or TIMESTAMP_DIV_EVEN) / 3600 / 24
        if _days >= self.maxdays or _days <= self.mindays:              
            raise OverflowError
#        _days = dec / (TIMESTAMP_DIV_ODD if dec % 2 else TIMESTAMP_DIV_EVEN) / 3600 / 24
        _datetime = self.startDateTime + datetime.timedelta(_days)
        _retdate = _datetime.__str__()
        retdatestr = ''.join(''.join(''.join(_retdate.split()).split(":")).split("-"))
        if not '.' in retdatestr:
            retdatestr += '.000000'
        return retdatestr[:-3] # 三位有效数字
        #return str(self.startDateTime + datetime.timedelta(_days))

    def num2str(self, dec):
        '''
        convert num to ascii str
        '''
        try:
            _hex = hex(dec).lstrip('0x').rstrip('L')
        except:
            print dec
            raise
        ret = []
        for i in xrange(0, len(_hex), 2):
            ret.append(chr(int(_hex[i: i+2], 16)))
        return ''.join(ret)

    def parse(self):
        '''
        '''
    #-------------------------------------------
    
        try:
            # parse header record
            try:
                self.parse_header()
            except Exception:
                print "head parse error"
                raise Exception('Fail to parse header')
            #-------------------------------------------
            # parse footer record
            try:
                self.parse_footer()
            except Exception:
                print "footer parse error"
                raise Exception('Fail to parse footer')                
            #-------------------------------------------
            # parse event record
            self.parse_event()

            # self.outstream_header.close()
            self.outstream_event.close()
        except Exception, e:
            print "I found a exception: ", e
            self.exception_list.append(str(e))
            
        self.instream.close()
        self.store_result()

    def store_result(self):
        """
        Store the result
        """
        start_time = self.timestamp

        ret = {}
        for key in ['EventRecord']:
            ret[key] = [{"FileName":self.source_file, 
            "SaveFileName":os.path.join(self.save_path, self.source_basename + '_' + key + '.txt'),  # With (save_file_cell,save_file_ncell) counterpart
            "DataStartTime":start_time, 
            "Interval":604800
            }]       
        ret['EXCEPTION'] = self.exception_list
        ret['WARNING']   = self.warning_list
        # write to json
        import simplejson
        target_file = open(self.jsonfile,"w")
        simplejson.dump(ret,target_file)
        target_file.close() 

    #------------------------------------------------------------               

if __name__ == '__main__':
    if len(sys.argv) == 4:
        _ = RPMOparse(infile = sys.argv[1], outpath = sys.argv[2], jsonfile = sys.argv[3])
        _.parse()
    else:
        print "Error: the count of the argv"