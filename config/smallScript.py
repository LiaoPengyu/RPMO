instream = open('str1.txt', 'r')

import os, sys, re
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(unicode(__file__,sys.getfilesystemencoding())), os.path.pardir))
sys.path.insert(0, ROOT_DIR)
sys.path.insert(0, os.path.join(ROOT_DIR, 'util'))

from util.keymanager import *

result = {}
for line in instream.readlines():
    if 'eid' in line:
        _l = [int(i) for i in re.findall('\d+', line)]
        if EVENT_NDW_DICT[_l[1]] != _l[2]:
            if _l[1] in result and not _l[2] in result[_l[1]]:
                result[_l[1]].append(_l[2])
            else:
                result[_l[1]] = [_l[2]]

for i in result:
    print 'eid:%s, ndw:%s'%(i, result[i])