#!/usr/local/env python
# encoding=utf-8
#
# Author: Archer
# File: PlayWav.py
# Desc: 通过声卡播放音频
import pyaudio
import wave

chunk = 1024

wf = wave.open('../data/odinary-signed-16bit-pcm.wav', 'rb')

p = pyaudio.PyAudio()

# 打开声音输出流
stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                channels = wf.getnchannels(),
                rate = wf.getframerate(),
                output = True)

# 写声音输出流进行播放
while True:
    data = wf.readframes(chunk)
    if data == "": break
    stream.write(data)

stream.close()
p.terminate()
