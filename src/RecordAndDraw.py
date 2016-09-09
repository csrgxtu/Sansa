#!/usr/local/env python
# encoding=utf-8
#
# Author: Archer
# File: RecordAndDraw.py
# Desc: Record and DrawWav
from pyaudio import PyAudio, paInt16
import numpy as np
from datetime import datetime
import wave
from matplotlib import pyplot as pl

NUM_SAMPLES = 2000      # pyAudio内部缓存的块的大小
SAMPLING_RATE = 8000    # 取样频率
LEVEL = 1500            # 声音保存的阈值
COUNT_NUM = 20          # NUM_SAMPLES个取样之内出现COUNT_NUM个大于LEVEL的取样则记录声音
SAVE_LENGTH = 8         # 声音记录的最小长度：SAVE_LENGTH * NUM_SAMPLES 个取样

# 开启声音输入
pa = PyAudio()
stream = pa.open(format=paInt16, channels=1, rate=SAMPLING_RATE, input=True,
                frames_per_buffer=NUM_SAMPLES)

save_count = 0
save_buffer = []

while True:
    # 读入NUM_SAMPLES个取样
    string_audio_data = stream.read(NUM_SAMPLES)
    # 将读入的数据转换为数组
    audio_data = np.fromstring(string_audio_data, dtype=np.short)
    # 计算大于LEVEL的取样的个数
    large_sample_count = np.sum( audio_data > LEVEL )
    print np.max(audio_data)
    # 如果个数大于COUNT_NUM，则至少保存SAVE_LENGTH个块
    if large_sample_count > COUNT_NUM:
        save_count = SAVE_LENGTH
    else:
        save_count -= 1

    if save_count < 0:
        save_count = 0

    if save_count > 0:
        # 将要保存的数据存放到save_buffer中
        save_buffer.append( string_audio_data )

    params = f.getparams()
    nchannels, sampwidth, framerate, nframes = params[:4]
    time = np.arange(0, nframes) * (1.0 / framerate)
    plt.ion() # interactive plotting
    pl.subplot(211)
    pl.plot(time, audio_data[0])
    pl.subplot(212)
    pl.plot(time, audio_data[1], c="g")
    pl.xlabel("time (seconds)")
