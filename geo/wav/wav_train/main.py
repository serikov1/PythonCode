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

# plt.plot(analytical_signal)
# plt.plot(amplitude_envelope)
# plt.xlabel("Samples")
# plt.ylabel("Amplitude")
# plt.title("Signal")
# plt.show()

# print(len(amplitude_envelope)//5512)
matrix = []
for i in range(len(amplitude_envelope)//5512):
    p = amplitude_envelope[i*5512:(i+1)*5512]
    # p = p[i:]
    matrix.append(p)

best = matrix[740][1830:1930]
arr_sum = []

for i in range(len(amplitude_envelope)//5512):
    arr_sum.clear()
    for j in range(1450, 1450 + len(best) + 20 + i):
        diff = matrix[i][j: 100 + j] - best
        sum = 0
        for elem in diff:
            sum += abs(elem)
        arr_sum.append(sum)
    minimum = arr_sum.index(min(arr_sum))
    matrix[i] = np.roll(matrix[i], - minimum - 1450)

# Последний элемент убираем, потому что он (может быть) заполнен не полностью
plt.imshow(matrix, cmap='gray')
plt.title('Image')
plt.show()