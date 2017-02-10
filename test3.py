#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  5 16:13:36 2017

@author: yiyuezhuo
"""

import keras
from keras.models import Sequential
from keras.layers import Deconvolution2D

import numpy as np

model = Sequential()
model.add(Deconvolution2D(3, 3, 3, output_shape=(None, 3, 14, 14),
                          border_mode='valid',
                          input_shape=(3, 12, 12)))

dummy_input = np.ones((32, 3, 12, 12))
preds = model.predict(dummy_input)
print(preds.shape)