import librosa
import soundfile
import os
import numpy as np
#convert a soundfile to stft and return 



working_direc=os.getcwd()
def convert_to_stft(path):
    amp,sr=librosa.load(path,sr=16000)
    return librosa.stft(amp)


def convert_to_magnitude(path):
    amp,sr=librosa.load(path,sr=16000)
    return np.abs(librosa.stft(amp))


def get_duration_difference_ms(file1, file2, sr=16000):
    y1, _ = librosa.load(file1, sr=sr)
    y2, _ = librosa.load(file2, sr=sr)

    len1 = len(y1)
    len2 = len(y2)

    diff_samples = abs(len1 - len2)
    diff_ms = (diff_samples / sr) * 1000

    print(f"Length 1: {len1} samples ({len1/sr:.3f} s)")
    print(f"Length 2: {len2} samples ({len2/sr:.3f} s)")
    print(f"Difference: {diff_samples} samples = {diff_ms:.2f} ms")

    return diff_ms