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
    matrix.append(p)


best = matrix[740][1830:1930]
arr_sum = []

for i in range(len(amplitude_envelope)//5512):
    arr_sum.clear()
    for j in range(1450, 1450 + len(best) + 10 + i):
        diff = matrix[i][j: 100 + j] - best
        sum = 0
        for elem in diff:
            sum += abs(elem)
        arr_sum.append(sum)
        # print('1')
    minimum = arr_sum.index(min(arr_sum))
    matrix[i] = np.roll(matrix[i], - minimum - 1450)

(low, high) = np.percentile(matrix, (0.5, 99.5))
delta = high - low
matrix = np.round(255 * (matrix - low) / delta)
matrix[matrix < 0] = 0
matrix[matrix > 255] = 255

telemetry = [matrix[645][5460], matrix[652][5460], matrix[660][5460],
             matrix[667][5460], matrix[667][5460], matrix[677][5460],
             matrix[685][5460], matrix[692][5460], matrix[701][5460],
             matrix[708][5460]]
print(telemetry)
plt.imshow(matrix, cmap='gray')
plt.title('Image')
plt.show()