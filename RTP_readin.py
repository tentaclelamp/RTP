#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 15:32:29 2018

@author: xiaosworkplace
"""

import pandas as pd
import numpy as np


f=open('/Users/xiaosworkplace/Desktop/机器学习/20140104QA/RTPfile/0010599639郑玉芳.RTP',encoding='GB2312')
df=[]


for line in f:
    df.append(line.split(','))
df = pd.DataFrame(df)
print(df)