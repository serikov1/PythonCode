import scipy.io.wavfile as wav
import scipy.signal as signal
import numpy as np
import matplotlib.pyplot as plt

# Считываем файл
fs, data = wav.read('190422.wav')

data = np.array(data, dtype=float)
n_data = (data - 128) / 128

# Преобразование Гильберта
analytical_signal = signal.hilbert(n_data)
amplitude_envelope = np.abs(analytical_signal)


# plt.plot(analytical_signal)
# plt.plot(amplitude_envelope)
# plt.xlabel("Samples")
# plt.ylabel("Amplitude")
# plt.title("Signal")
# plt.show()

# Создаю матрицу из строки
matrix = []
for i in range(len(amplitude_envelope)//5512):
    p = amplitude_envelope[i*5512:(i+1)*5512]
    matrix.append(p)

# Выбрал синхроимпульс
best = matrix[450][3700:3800]
arr_sum = []

# Выравнивание фото по синхроимпульсу
for i in range(len(amplitude_envelope)//5512):
    arr_sum.clear()
    for j in range(3500, 3500 + len(best) + 10 + i):
        diff = matrix[i][j: 100 + j] - best
        sum = 0
        for elem in diff:
            sum += abs(elem)
        arr_sum.append(sum)
    minimum = arr_sum.index(min(arr_sum))
    matrix[i] = np.roll(matrix[i], - minimum + 3500 - 1510)


# Нормировка
(low, high) = np.percentile(matrix, (0, 100))

delta = high - low
matrix = np.round(255 * (matrix - low) / delta)
matrix[matrix < 0] = 0
matrix[matrix > 255] = 255


telemetry = [matrix[596][5460],
             matrix[605][5460],
             matrix[613][5460],
             matrix[620][5460]]

T1 = 276.6067 + 0.051111 * telemetry[0] + 1.405783E-06 * telemetry[0]**2
T2 = 276.6119 + 0.051090 * telemetry[1] + 1.496037E-06 * telemetry[1]**2
T3 = 276.6311 + 0.051033 * telemetry[2] + 1.496990E-06 * telemetry[2]**2
T4 = 276.6268 + 0.051058 * telemetry[3] + 1.493110E-06 * telemetry[3]**2

Tbb = (T1 + T2 + T3 + T4)/4
Tbb_ = 1.67396 + 0.997364 * Tbb

c1 = 1.1910427E-5
c2 = 1.4387752
v = 2670
Nbb = (c1 * v**3) / (np.exp((c2 * v) / Tbb_) - 1)

Ce = matrix[637][4611]
Cs = matrix[700][2902]
Cbb = matrix[600][4600]
Ne = Nbb * (Cs - Ce) / (Cs - Cbb)

Te_ = c2 * v / (np.log(1 + (c1 * v**3)/Ne))

Te = (Te_ - 1.67396) / 0.997364
print(Te)

# np.savetxt('data_2.txt', matrix, fmt='%.2f')

plt.imshow(matrix, cmap='gray')
plt.title('Image')
# plt.savefig('1_photo')
plt.show()

