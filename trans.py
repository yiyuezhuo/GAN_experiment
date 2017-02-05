#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 13:04:19 2017

@author: yiyuezhuo
"""

from PIL import Image
import os

root = 'con3'
target_root = 'images'

base_m = 6
base_n = 6

img_shape1 = base_n * 2**4
img_shape2 = base_m * 2**4

for name in os.listdir(root):
    path = os.path.join(root, name)
    target_path = os.path.join(target_root,name)
    im = Image.open(path)
    im.resize((img_shape1,img_shape2)).save(target_path)
    