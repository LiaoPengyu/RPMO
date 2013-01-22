# -*- coding: utf-8 -*-


import sys,os
import pymssql
import binascii
from config.DBConfig import *

class loadInfo(object):
    """
    load the information(key-dictionary especially) from db or file
    """
    def __init__(self, max_conn = 25):
        self.key_dict = {}
        self.cell_dict = {}
        
        self.max_conn = max_conn
        self.DBConfig()
        
    
    def DBConfig(self):
        print SQL_HOST,USER,PASSWORD,DATABASE
        self.conn = pymssql.connect(host=SQL_HOST,
                                    user=USER,
                                    password=PASSWORD,
                                    database=DATABASE,
                                    max_conn = self.max_conn)
        self.current = self.conn.cursor()
    
    def loadkey(self):
        #此处需要载入cellFileData: Cell - CI 对应关系
        self.key_dict = {
                        
                         }
        return self.key_dict
    
    def insertCellName(self, bscid, bscname, cellpoint, cellname):
        pass

    def getCellName(self, bscid, cellpoint):
        pass
    
    
    def close(self):
        self.conn.commit()
        self.conn.close()    
    
DBInfo = loadInfo()

if __name__ == "__main__":
    print "start"
    #print DBInfo.loadOutputPower()
    print DBInfo.loadCellInfo(CellName="LFG507B")