# -*- coding: utf-8 -*-
import sys,os,time

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

from optparse import OptionParser
from util.threadParse import threadParseWorker
from util.RPMOprocess import RPMOprocess 

def main():
    result_information = []
    load_key = {}
    
    ####################
    #command line parser
    
    parser =   OptionParser()
    parser.add_option('-f','--file',
                     action = 'store',
                     type = 'string',
                     dest = 'file_str'
                     )  
    parser.add_option('-s','--savedir',
                     action = 'store',
                      type = 'string',
                      dest = 'save_path'
                    )  
    parser.add_option('-r','--return',
                      action = 'store', 
                      type = 'string',
                      dest = 'return_file'
                    )
    parser.add_option('-t', '--filelogid',
                      action = 'store',
                      type = 'string',
                      dest = 'filelogid_str'
                      )
    parser.add_option('-m', '--mrpythonpath',
                      action = 'store',
                      type = 'string',
                      dest = 'mr_python_str'
                      )               
    #------------------------------------------------------------- test_cases
    #eventData_110608_170719.bin.gz
    #CSMRL1299350010731363030201210291800.xml_121029_180003.bin.gz
    #CSMRL1299350010731363030201210291800.xml_121029_180003.bin.gz
    #eventData_110331_085507b.bin.gz
    #eventData_110331_085429.bin.gz
    #eventData_110608_170531.bin.gz
    #D:\\Ericsson Project\\FAS\\hehe.txt
    #bordercell2325556428753796655201207041614_120704_161403.bin.gz
    #CSMRL6559002814084013914201210292000.xml_121029_200003.bin.gz
    #------------------------------------------------------------- test_cases
    arge_test = ['--file', 'D:\\Ericsson Project\\RPMO\RPMO\\test\\eventData_110608_170719.bin',
                 '--savedir', 'D:\\Ericsson Project\\RPMO\\RPMO\\result',
                 '--return', 'D:\\Ericsson Project\\RPMO\\RPMO\\output.json',
                 '--filelogid', 'hehe',
                 '--mrpythonpath', 'D:\\Ericsson Project\\RPMO\\MR_new\\bin\\mrprocess.pyc'
                 ]
    arge = sys.argv[1:] if len(sys.argv) > 1 else arge_test
    
    (options,args) = parser.parse_args(arge)

    print '_'*40
    try:
        print 'Save Path:', unicode(options.save_path, encoding)
        print 'RPMO files:', unicode(', '.join(options.file_str.split('|')), encoding)
        print 'File Log ID:', options.filelogid_str
        print 'MR python:', options.mr_python_str 
    except:
        print 'Args input Error:%s, %s' %(options.save_path,options.file_str)
    ############
    #start parsing
    mr_python = options.mr_python_str
    files_str = options.file_str.split('|')
    save_path = options.save_path
    if not os.path.exists(save_path):
        os.mkdir(save_path) 
    rpmo_json_file = options.return_file[:-5] + '_rpmo.json'
    save_json_file = options.return_file
    filelogid_str = options.filelogid_str
    
    p = RPMOprocess(files_str, save_path, rpmo_json_file, filelogid_str, mr_python)
    p.parseProcess() 

    ############
    #App end
    print '_'*40
    
    
    # # call for mr
    # save_json_files = []
    # try:
        # import simplejson, multiprocessing
        # #-------------------------------------------
        # pool = multiprocessing.Pool(processes = 3) 
        # # make a process pool
        
        # json_val = simplejson.load(file(rpmo_json_file))
        # txtinfos = json_val.get("EventRecord")
        
        # if txtinfos == None:
            # raise
        # # exception exists
        
        # for txtinfo in txtinfos:
            # txtfile = txtinfo.get("SaveFileName")
            # txtfile = txtfile.encode(encoding)
            # _json   = os.path.join(save_path, os.path.basename(txtfile) + "_json" + '.json')
            # save_json_files.append(_json)
            
            # pool.apply_async(mr_main, (save_path, _json, mr_python, filelogid_str, txtfile, ))
            
        # pool.close()
        # pool.join()
        # merge_json(rpmo_json_file, save_json_file, save_json_files)
        # # ----------------------------------
        # # delete the mid_files
        # for single_file in save_json_files:
            # os.remove(single_file)
        # # ----------------------------------
    # except Exception, e:
        # print e
        # source_file = open(rpmo_json_file, 'r')
        # target_file = open(save_json_file, 'w')
        # json_val = simplejson.load(source_file)
        # ret =   {"MeasurementData":[],
                # "EventData":[],
                # "CallInformation":[],
                # "EXCEPTION":[],
                # "WARNING":[]
                # }
        # for key_file in ["EXCEPTION", "WARNING"]:
            # ret[key_file] = json_val[key_file]
        # simplejson.dump(ret, target_file)
        # source_file.close()
        # target_file.close()
        
        
        
    # ############
    # #delete the useless output files
    # process_json(save_json_file)
    
def mr_main(save_path, save_json_file, mr_python, filelogid_str, txtfile):
    """
    excecute the mr.py
    """
    import subprocess
    cmd_str = 'python "' + mr_python + '" -f "' + txtfile + '" -s "' + save_path + '" -r "' + save_json_file + '" -t "' + filelogid_str + '" '
    print cmd_str
    p = subprocess.Popen(cmd_str)
    p.wait()
    
    
def merge_json(rpmo_json_file, mr_json_file, save_json_files):
    """
    merge the json files into mr_json_file
    """
    import simplejson
            
    ret =   {"MeasurementData":[],
            "EventData":[],
            "CallInformation":[],
            "EXCEPTION":[],
            "WARNING":[]
            }
    rpmo_json_val = simplejson.load(file(rpmo_json_file))
    for key_file in ['EXCEPTION', 'WARNING']:
        ret[key_file].extend(rpmo_json_val[key_file])
        
    for single_file in save_json_files:
        with open(single_file, "r+") as f:
            python_object = simplejson.load(f)
            for key_file in ['EXCEPTION', 'WARNING', "MeasurementData", "EventData" , "CallInformation"]:
                ret[key_file].extend(python_object[key_file])
                    
    #-----------------------------------------
    #write into json
    target_file = open(mr_json_file, 'w')
    simplejson.dump(ret, target_file)
    target_file.close()
    
    
def process_json(json_file):
    import simplejson
    target_file = open(json_file, "r")
    json_val = simplejson.load(target_file)
    target_file.close()
    
    exception_data = json_val["EXCEPTION"]
    _exception_data = []
    for item in exception_data:
        if item != "string index out of range":
            _exception_data.append(item)
            
    warning_data = json_val["WARNING"]
    _warning_data = []
    for item in warning_data:
        if item != "string index out of range":
            _warning_data.append(item)
            
    json_val["EXCEPTION"] = _exception_data
    json_val["WARNING"] = _warning_data
    
    ###########################
    #check the EventData
    event_data = json_val["EventData"]
    _event_data = []
    for out_file in event_data:
        if out_file["SuccessCount"]:
            _event_data.append(out_file)
    ###########################
    #check the MeasurementData
    mea_data = json_val["MeasurementData"]
    _mea_data = []
    for out_file in mea_data:
        if out_file["SuccessCount"]:
            _mea_data.append(out_file)
    ###########################
    #check the CallInformation
    call_data = json_val["CallInformation"]
    _call_data = []
    for out_file in call_data:
        if out_file["SuccessCount"]:
            _call_data.append(out_file)
    ###########################
    if (not _event_data) and (not _mea_data) and (not _call_data):
        json_val["EXCEPTION"].append("No output, please check the input file")
        
    json_val["EventData"] = _event_data    
    json_val["MeasurementData"] = _mea_data
    json_val["CallInformation"] = _call_data
    
    #write the new file into json
    target_file = open(json_file, "w")
    simplejson.dump(json_val, target_file)
    target_file.close()
    
    
st = time.time()
if __name__ == "__main__":
    print "App start!"
    main()
    print "App end!"

print 'total time usage is: ' + str(time.time() - st)
