# -*- coding: utf-8 -*-

import os,sys

App_config_path = os.path.join(os.path.dirname(__file__),"App.Config")
SQL_HOST = ""
USER = ""
PASSWORD = ""
DATABASE = ""

#Table
Column_AllocBand   = "AllocBand"
Column_MSPower     = "MSPower"
Column_OutputPower = "OutputPower"
MSPowerDef_Table   = "Dict_MSPowerDefinition"

#storage process
STORE_PROCESS_FUNC = "RefreshCellInfo"
cell_name_pos = 0
bsc_name_pos = 1
cid_pos = 2

################
#XML DB App.conf
if SQL_HOST == "" and USER =="" and PASSWORD == "" and DATABASE =="":
    from xml.etree import ElementTree
    root_node = ElementTree.parse(App_config_path)
    
    #1. Get connectionStrings Node
    add_nodes = root_node.findall("connectionStrings/add")
    
    #2. Get 'EricssonUEHContainer' from Add node
    for add in add_nodes:
        if "EricssonMRContainer" == add.attrib["name"]:
            #Parse this line
            connectionString = (add.attrib["connectionString"]).split(";")
            for item in connectionString:
                if "data source=" in item:
                    start = item.find("data source=") 
                    start = start + len("data source=")
                    SQL_HOST = item[start:]
                elif "user id=" in item:
                    start = item.find("user id=") 
                    start = start + len("user id=")                    
                    USER = item[start:]
                elif "password=" in item:
                    start = item.find("password=") 
                    start = start + len("password=")                    
                    PASSWORD =  item[start:]
                elif "initial catalog=" in item:
                    start = item.find("initial catalog=") 
                    start = start + len("initial catalog=")                    
                    DATABASE = item[start:]
        else:
            continue

print "##########################"            
print SQL_HOST
print USER  
print PASSWORD
print DATABASE      
print "#########################"       
    
    
    
    
    
    
    
    
    
    
    
