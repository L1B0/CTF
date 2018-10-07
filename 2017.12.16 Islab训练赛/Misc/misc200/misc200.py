# -*- coding:utf-8 -*-
__Author__ = "LB@10.0.0.55"
import tarfile
dstPath = ''
tar = tarfile.open("800.tar","r")
now = tar.getnames()[0]
tar.extractall(dstPath)

while now != 'flag':
         tar = tarfile.open(now,"r")
         now = tar.getnames()[0]
         tar.extractall(dstPath)
