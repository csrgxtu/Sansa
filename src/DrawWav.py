#!/usr/local/env python
# encoding=utf-8
#
# Author: Archer
# File: DrawWav.py
# Desc: 将wav文件通过坐标系画出来
import wave
# import pylab as pl
from matplotlib import pyplot as pl
import numpy as np

# 打开WAV文档
f = wave.open("../data/odinary-signed-16bit-pcm.wav", "rb")

# 读取格式信息
# (nchannels, sampwidth, framerate, nframes, comptype, compname)
params = f.getparams()
nchannels, sampwidth, framerate, nframes = params[:4]

# 读取波形数据
str_data = f.readframes(nframes)
f.close()

#将波形数据转换为数组
wave_data = np.fromstring(str_data, dtype=np.short)
wave_data.shape = -1, 2
wave_data = wave_data.T
time = np.arange(0, nframes) * (1.0 / framerate)

# 绘制波形
pl.subplot(211)
pl.plot(time, wave_data[0])
pl.subplot(212)
pl.plot(time, wave_data[1], c="g")
pl.xlabel("time (seconds)")
pl.show()
