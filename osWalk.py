# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 21:54:11 2018

@author: blindness
"""
import os
import fnmatch

rootDir ="."
for root, dir, files in os.walk(rootDir):
    for name in files:
        #print('files\t%s' % name)
        if fnmatch.fnmatch(name, '*Silique*'):
            print ("files:",name)
        print(os.path.join(root, name))
