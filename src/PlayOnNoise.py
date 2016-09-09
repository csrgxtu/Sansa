#!/usr/local/env python
# encoding=utf-8
#
# Author: Archer
# File: PlayOnNoise.py
# Desc: play a net mp3 when noise greater than a threshhold
# Date: 09/Sep/2016
from pyaudio import PyAudio, paInt16
import numpy as np
from datetime import datetime
import wave
import subprocess

Mplayer = '/usr/bin/mplayer'    # mplayer
Mp3File = 'http://7u2q8y.com2.z0.glb.qiniucdn.com/c1_96k/7bfa281f257c0d94288da6566c7f26d6ec5c57a57331b355632dbcda7a25f51f8d485902.mp3'


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
    if np.max(audio_data) > 12000:
        print np.max(audio_data), 'big noise'
        subprocess.call([Mplayer, Mp3File])
    else:
        print 'so quiet ...'
