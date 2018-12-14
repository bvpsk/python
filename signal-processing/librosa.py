import IPython.display as ipd
ipd.Audio('SoundHelix-Song-1.mp3')

import librosa
data, sampling_rate = librosa.load('SoundHelix-Song-1.mp3')

import os
import pandas as pd
import librosa,librosa.display
import glob 

plt.figure(figsize=(12, 4))
librosa.display.waveplot(data, sr=sampling_rate)
