#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 21:00:26 2020

@author: navneethkrishna
"""

import cv2
import os


vid=cv2.VideoCapture('')
try: 
    if not os.path.exists('data'):  # creating directory if doesnt exist
        os.makedirs('data')
        
except OSError:
    print('Error creating directory of data')

currentframe = 0
i=0
while(True):
    ret,frame=vid.read() #reading from frame
    if ret:
          # if video is still left continue creating images 
        
         # writing the extracted images 
        if i%20==0:
            name = './data/frame' + str(currentframe) + '.jpg'
            cv2.imwrite(name, frame) 
            print ('Creating...' + name) 
            currentframe+=1
  
        # increasing counter so that it will 
        # show how many frames are created 
        
        i+=1
    else: 
        break
# Release all space and windows once done 
vid.release() 
cv2.destroyAllWindows()   