import scipy.io.wavfile as wav
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt


fs, data = wav.read('signal.wav')
# Срез для отображения преобразования Гильберта
# data = data[300 * fs:301 * fs]

data = np.array(data, dtype=float)
n_data = (data - 128) / 128

analytical_signal = signal.hilbert(n_data)
amplitude_envelope = np.abs(analytical_signal)

plt.plot(analytical_signal)
plt.plot(amplitude_envelope)
plt.xlabel("Samples")
plt.ylabel("Amplitude")
plt.title("Signal")
plt.show()

# print(len(amplitude_envelope)//5512)
matrix = []
for i in range(len(amplitude_envelope)//5512):
    p = amplitude_envelope[i*5512:(i+1)*5512]
    p = p[i:]
    matrix.append(p)
# Последний элемент убираем, потому что он (может быть) заполнен не полностью

mat = []
for i in range(len(amplitude_envelope)//5512):
    if amplitude_envelope[i] == 0 and amplitude_envelope[i + 1] == 256:
        p = amplitude_envelope[i:]
        mat.append(p)


plt.imshow(matrix, cmap='gray')
plt.title('Image')
plt.show()
