# -*- coding:utf-8 -*-
'''
@Author: zzx
@E-mail: 188891020@qq.com
@File: 快速测试.py
@CreateTime: 2020/7/22 17:15
'''

bigfile_path ="path"
small_path = "path_small"
count = 0
space = 2**20 # 每个文件大小1MB
with open(bigfile_path,'rb') as bf:
    while small_files==None:
        count +=1
        small_files = bf.read(space)
        with open(small_path+str(count),'wb') as sf:
            sf.write(small_files)