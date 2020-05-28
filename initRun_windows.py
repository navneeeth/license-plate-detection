#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 18 00:23:53 2020

@author: navneethkrishna
"""

import os
import asyncio
async def abc():
    await os.system('python predict_characters.py '+directory_name + " " + str(i) + " " + str(count+1) + " "+str(len(files_list))+" > a.txt")
    
directory_name = input("Enter the absolute path of the directory in which frames are located:\n")
#if(directory_name[-1] != '\\'):
#  directory_name += '\\'
count = 0
#execfile()
files_list = [f for f in os.listdir(directory_name) if os.path.isfile(os.path.join(directory_name, f))]
#print(files_list)
#os.listdir(directory_name)
for i in files_list:
    print(str(i))
    print(i)
    #os.system('python segment_characters.py '+directory_name + " " + i)
    asyncio.run(abc())
    count += 1
#print(files_list)
