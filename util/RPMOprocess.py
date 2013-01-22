# -*- coding: utf-8 -*-
import os, sys
from util.threadParse import threadParseWorker
from config.strConfig import *
from util.keymanager import *

class RPMOprocess:
    def __init__(self, source_filename = None, save_path = None, json_file = None, filelogid_str = None, mr_python = None):
        self.source_filename = source_filename
        self.source_basename = [os.path.basename(f) for f in self.source_filename]
        self.save_path = save_path
        self.filelogid_str = filelogid_str
        self.mr_python = mr_python
        self.json_file  = json_file
        self.json_files = []
        self.isgzfile = False
        self.json_ret = {"EventRecord":[],
                         "EXCEPTION":[],
                         "WARNING"  :[],
                        }
        self.split_source_files = []
        self.split_source_jsons = []
    def parse_header(self):
        '''
        parse header record
        '''
        f = open(self.source_filename, 'rb')
        f.seek(HEADER_BSC_POS)
        number_of_bscs = ord(f.read(1))
        pos = HEADER_BSC_POS + 1

        while number_of_bscs:
            f.seek(pos + 10)
            number_of_cells = ord(f.read(1)) * 256 + ord(f.read(1)) # pos + 12
            # get info of cells and refresh pos
            pos += 12 + number_of_cells * 11
            f.seek(pos)
            number_of_ncells = ord(f.read(1)) * 256 + ord(f.read(1))
            # get info of ncells and refresh pos
            pos += 2 + number_of_ncells * 11
            number_of_bscs -= 1
        return pos

    def extrgz(self, filename):
        import gzip
        instream = gzip.open(filename, 'rb')
        retfilename = os.path.join(self.save_path, self.source_basename[:-3])
        outstream = open(retfilename, 'wb')
        while True:
            data = instream.read(100000000)
            outstream.write(data)
            if data == '': break
        outstream.close()
        return retfilename

    def parseProcess(self):
        try:
            #-----------------------------------------------------------
            # to check the complete of the args
            if self.source_filename == None:
                raise Exception("Lose Args Element: RPMO source file")            
            if self.save_path == None:
                raise Exception("Lose Args Element: Save Path")
            if self.json_file == None:
                raise Exception("Lose Args Element: Json File")
            if self.filelogid_str == None:
                raise Exception("Lose Args Element: File Log_Id")
            if self.mr_python == None:
                raise Exception("Lose Args Element: MR python")
            #-----------------------------------------------------------               
            self.source_filename = self.source_filename[0]
            #-----------------------------------------------------------
            # to check the existence of the source file            
            if not os.path.isfile(self.source_filename):
                raise Exception("Can't find source file %s"% self.source_filename)
            #-----------------------------------------------------------

            self.source_basename = os.path.basename(self.source_filename)
            if self.source_filename.endswith('.gz'):
                self.source_filename = self.extrgz(self.source_filename)
                self.isgzfile = True
            filesize = os.path.getsize(self.source_filename)

            header_size = self.parse_header()
            i = 0
            f = open(self.source_filename, 'rb')
            header = f.read(header_size)
            pos    = f.tell()

            self.split_source_files = []
            self.split_source_jsons = []

            threads = []
            while pos < filesize:
                tmp_name = self.source_basename.split('.')[0]
                _json  = os.path.join(self.save_path, tmp_name + "_json_" + str(i) + '.json')
                _fname = os.path.join(self.save_path, tmp_name + "_file_" + str(i) + '.bin')
                self.split_source_files.append(_fname)
                self.split_source_jsons.append(_json)
                _f = open(_fname, 'wb')
                _f.write(header)
                _f.write(f.read(SPLIT_FILE_SIZE))
                _f.close()
                i += 1
                pos = f.tell()

            f.close()
            ############
            #run threads
            print "----------------------split process over-------------------------------"
            self.run_threads(self.split_source_files[:], self.split_source_jsons[:], 3)      

        except Exception, e:
            self.json_ret['EXCEPTION'].append(str(e));
        # self.merge_file()
        self.merge_json()
        # delete mid files
        # self.delMidFiles()

    def run_threads(self, source_files, source_json, proc_num):
        """
        Threads Pool
        """
        import time
        _lens = len(source_files)
        threads = []
        _proc_num = _lens if _lens <= proc_num else proc_num
        for i in range(_proc_num):
            _thread = threadParseWorker(source_filename= source_files.pop(), save_path = self.save_path, json_file = source_json.pop())
            _thread.start()
            threads.append(_thread)

        while True:
            if not source_files: break
            for i in range(_proc_num):
                if threads[i].runningOver:
                    threads[i] = threadParseWorker(source_filename= source_files.pop(), save_path = self.save_path, json_file = source_json.pop())
                    threads[i].start()
            time.sleep(1)

        for i in range(_proc_num):
            if not threads[i].runningOver:
                threads[i].join()

    def delMidFiles(self):
        for f in self.split_source_files:
            os.remove(f)
        for f in self.split_source_jsons:
            os.remove(f)
        if self.isgzfile:
            os.remove(self.source_filename)

    def merge_json(self):
        """
        """
        import simplejson

        for file in self.split_source_jsons:
            with open(file, "r+") as f:
                fileStr = f.read()
                python_object = simplejson.loads(fileStr) 
                # print python_object
                for key_file in ['EXCEPTION', 'WARNING', 'EventRecord']:
                    self.json_ret[key_file].extend(python_object[key_file])
        # write to json file
        target_file = open(self.json_file, "w")
        print self.json_file
        simplejson.dump(self.json_ret, target_file)
        target_file.close()
    def merge_file(self):
        for _str in RPMOTABLENAME.values():
            cmd_str = 'copy /b ' + '+'.join([os.path.join(self.save_path, f + '_' + _str + '.txt') for f in self.source_basename]) + ' ' + os.path.join(self.save_path, _str + '.txt')
            os.system(cmd_str)

