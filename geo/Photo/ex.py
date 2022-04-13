import numpy
import scipy.signal
from scipy.io import wavfile
from PIL import Image


class NOAA:
    # Нужная частота
    RATE = 2400

    def __init__(self, filename):
        # Берем частоту и сигнал из файла
        rate, self.signal = wavfile.read(filename)
        if rate != self.RATE:
            # Меняем частоту на 2400 Гц
            coef = self.RATE / rate
            samples = int(coef * len(self.signal))
            signal = scipy.signal.resample(self.signal, samples)
            # Создаём новый файл с полученными данными
            scipy.io.wavfile.write("photo.wav", self.RATE, signal)
        truncate = self.RATE * int(len(self.signal) // self.RATE)
        self.signal = self.signal[:truncate]
        # print(self.signal)

        # Преобразования Гильберта
        hilbert = scipy.signal.hilbert(self.signal)
        # print("Hilbert ", hilbert, '\n')
        # Фильтруем сигнал
        filtered = scipy.signal.medfilt(numpy.abs(hilbert), 5)
        # print("filtered ", filtered, '\n')
        # Изменяем
        reshaped = filtered.reshape(len(filtered) // 5, 5)
        # print("reshaped ", reshaped, '\n')
        # Форматируем от 0 до 255
        digitized = self._digitize(reshaped[:, 2])
        # print("digitized ", digitized, '\n')
        # Преобразуем в матрицу
        matrix = self.reshape(digitized)
        # print("matrix ", matrix, '\n')
        # Делаем фото
        image = Image.fromarray(matrix)
        image.show()

    def _digitize(self, signal, plow=0.5, phigh=99.5):
        (low, high) = numpy.percentile(signal, (plow, phigh))
        delta = high - low
        data = numpy.round(255 * (signal - low) / delta)
        data[data < 0] = 0
        data[data > 255] = 255
        return data.astype(numpy.uint8)

    def reshape(self, signal):

        # sync frame to find: seven impulses and some black pixels (some lines
        # have something like 8 black pixels and then white ones)
        syncA = [0, 128, 255, 128] * 7 + [0] * 7

        # list of maximum correlations found: (index, value)
        peaks = [(0, 0)]

        # minimum distance between peaks
        mindistance = 2080

        # need to shift the values down to get meaningful correlation values
        signalshifted = [x - 128 for x in signal]
        syncA = [x - 128 for x in syncA]
        for i in range(len(signal) - len(syncA)):
            corr = numpy.dot(syncA, signalshifted[i: i + len(syncA)])

            # if previous peak is too far, keep it and add this value to the
            # list as a new peak
            if i - peaks[-1][0] > mindistance:
                peaks.append((i, corr))

            # else if this value is bigger than the previous maximum, set this
            # one
            elif corr > peaks[-1][1]:
                peaks[-1] = (i, corr)

        # create image matrix starting each line on the peaks found
        matrix = []
        for i in range(len(peaks) - 1):
            matrix.append(signal[peaks[i][0]: peaks[i][0] + 2080])

        return numpy.array(matrix)


filename = 'photo.wav'
NOAA(filename)
