# -*- coding: utf-8 -*-
import sys,os
import time
import subprocess
import threading

class threadParseWorker(threading.Thread):
    """
    """
    def __init__(self,source_filename, save_path, json_file):
        threading.Thread.__init__(self)
        
        self.source_filename = source_filename
        self.save_path       = save_path
        self.json_file       = json_file
        self.runningOver     = False
                
    def run(self):
        """
        """        
        ########
        #Process
        filepath =  os.path.join(os.path.dirname(__file__), "RPMOparser.py")
        cmd_str  = 'python "' + filepath + '" "' + self.source_filename + '" "' + self.save_path + '" "' + self.json_file + '" '
        print "reach here:  " + cmd_str
        #print unicode(cmd_str, 'UTF-8')
        p = subprocess.Popen(cmd_str)
        p.wait()
        ### runing over
        
        self.runningOver = True
