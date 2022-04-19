import scipy.io.wavfile as wav
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

def hilbert(data):
    analytical_signal = signal.hilbert(data)
    amplitude_envelope = np.abs(analytical_signal)
    return amplitude_envelope

audio_data = 'signal.wav'
fs, data = wav.read(audio_data)


data_crop = data[20*fs:21*fs]
plt.figure(figsize=(12,4))

#plot recieved signal
plt.plot(data_crop)
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.title("Signal")
plt.show()

#hilbert function call
data_am = hilbert(data)

frame_width = int(0.5*fs)
w, h = frame_width, data_am.shape[0]//frame_width

matrix = np.zeros((h, w, 3))

image = Image.new('RGB', (w, h))
px, py = 0, 0
for p in range(data_am.shape[0]):
    lum = int((data_am[p]-130)*5)
    if lum < 0: lum = 0
    if lum > 255: lum = 255
    image.putpixel((px, py), (lum, lum, lum))

    matrix[py, px, 0] = lum
    matrix[py, px, 1] = lum
    matrix[py, px, 2] = lum

    px += 1
    if px >= w:
        if (py % 50) == 0:
            print(f"Line saved {py} of {h}")
        px = 0
        py += 1
        if py >= h:
            break

image = image.resize((w, 4*h))
plt.imshow(image)
plt.show()