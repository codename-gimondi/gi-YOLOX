#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Copyright (c) Megvii, Inc. and its affiliates.

# nano-golf

# lower resolution and shallower neural network than default nano
# so as to run it faster on Jetson Nano
# for pretraining on COCO

import os

import torch.nn as nn

from yolox.exp import Exp as MyExp

'''
small_kilo

Based on pretrained YOLOX_small
Intended for offline inference for making demonstration videos on desktop GPUs.

'''

class Exp(MyExp):
    def __init__(self):
        super(Exp, self).__init__()
        self.num_classes = 7 # remember to change to 7 when fine tuning
        self.depth = 0.33
        self.width = 0.50
        self.data_num_workers = 12
        self.exp_name = os.path.split(os.path.realpath(__file__))[1].split(".")[0]
