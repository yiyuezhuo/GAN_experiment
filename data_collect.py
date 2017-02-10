#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 21:32:40 2017

@author: yiyuezhuo
"""

import os
import numpy as np
from PIL import Image
from sklearn.externals import joblib


base_id = 29335 # first epsilon need +0 second +1 etc.

you_get_command_format = 'you-get http://bangumi.bilibili.com/anime/1600/play#{}'
name_format = '灼眼的夏娜 [{}].flv'

for i in range(base_id, base_id+10):
    command = you_get_command_format.format(i)
    os.system(command)
    
ffmpeg_command = 'ffmpeg -i {root}/"灼眼的夏娜 [{id}].flv" -an -r 1  {target_root}/%d.jpg'

command = ffmpeg_command.format(root='hidden', id=base_id+1, target_root='hidden/'+str(base_id+1))
os.system(command)

def convert(id):
    os.mkdir(os.path.join('hidden',str(id)))
    command = ffmpeg_command.format(root='hidden', id=id, target_root='hidden/'+str(id))
    os.system(command)

120,1350

arr_list = []
for i in range(base_id,base_id+10):
    for j in range(120,1350):
        path = 'hidden/{}/{}.jpg'.format(i,j)
        im = Image.open(path)
        a = np.asarray(im.crop((210,0,590,380)).resize((96,96)))
        arr_list.append(a)
        im.close()
arr = np.zeros((len(arr_list),96,96,3))
for i,a in enumerate(arr_list):
    arr[i,:,:,:] = a
       
arr /= 255.0
       
joblib.dump({'X':arr},'video.frame.96.dump')