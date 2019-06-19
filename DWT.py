import pywt
import matplotlib.pyplot as plt
from operator import add
import numpy as np
import statistics

signal = [1, 1, 1, 1, 1, 1, 1, 1]

wavelet = pywt.Wavelet("db4")
print(wavelet.filter_bank)
cA, cD = pywt.dwt(signal, "db4")


print(signal)
print(cA)
print(len(cD))
#
# signal = []
#
# file = open("signal.txt", "r")
# line = file.readline()
#
# while line:
#     signal.append(int(round(float((line[:len(line) - 2])))))
#     line = file.readline()
# file.close()
#
# # print(signal)
#
# noise = np.random.normal(0, 3, len(signal))
# noisySignal = list(map(add, signal, noise))
#
# cA, cD = pywt.dwt(noisySignal, 'haar')
# cA2, cD2 = pywt.dwt(cA, 'haar')
#
# print(len(signal))
# print(len(noisySignal))
# print(len(cA))
# print(len(cD))
# print(len(cA2))
# print(len(cD2))
#
# # print(w)
# # print(w.filter_bank)
#
# std_cD = statistics.stdev(cD)
# std_cD2 = statistics.stdev(cD2)
#
# denoised_cD = pywt.threshold(cD, std_cD, mode='garrote')
# denoised_cD2 = pywt.threshold(cD2, std_cD2, mode='garrote')
#
#
# icA = pywt.idwt(cA2, denoised_cD2, 'haar')
# denoised_signal = pywt.idwt(icA, denoised_cD, 'haar')
#
# plt.figure(1)
# plt.subplot(421)
# plt.plot(signal)
# plt.title("original")
# plt.subplot(422)
# plt.plot(noisySignal)
# plt.title("noisy")
# plt.subplot(423)
# plt.plot(cD)
# plt.title("1 level detail")
# plt.subplot(424)
# plt.plot(denoised_cD)
# plt.title("1 level detail denoised")
#
# plt.subplot(425)
# plt.plot(cD2)
# plt.title("2 level detail")
# plt.subplot(426)
# plt.plot(denoised_cD2)
# plt.title("2 level detail denoised")
# plt.subplot(427)
# plt.plot(cA2)
# plt.title("2 level approximation")
# plt.subplot(428)
# plt.plot(denoised_signal)
# plt.title("denoised signal....")
#
# plt.subplots_adjust(top=0.92, bottom=0.08, left=0.10, right=0.95, hspace=0.25,
#                     wspace=0.35)
# plt.show()