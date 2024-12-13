import numpy as np
import matplotlib.pyplot as plt
import scipy

np.random.seed(0)

fs = 3000                       # sampling frequency in Hz
t = np.linspace(0, 5, fs * 100)   # 5 seconds of data
f0 = 1
f1 = 75
chirp = np.sin(2 * np.pi * (f0 + (f1 - f0) * t / max(t)) * t)
tone = np.sin(2 * np.pi * 100 * t)
modulation = 1 + 0.5 * np.sin(2 * np.pi * 0.3 * t)
non_stationary_signal = modulation * chirp + tone + 0.001 * np.random.randn(len(t)) # add Gaussian noise

noise = np.random.normal(0, 1, 5000)


plt.figure(figsize=(12, 4))

plt.subplot(2, 2, 1)
frequencies, times, Sxx = scipy.signal.spectrogram(non_stationary_signal, fs=1000)
plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), cmap=plt.cm.Purples)
plt.title("Non-Stationary Signal Spectrogram")
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")

plt.subplot(2, 2, 2)
frequencies, times, Sxx = scipy.signal.spectrogram(noise, fs=1000)
plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), cmap=plt.cm.Purples)
plt.title("Noise Spectrogram")
plt.xlabel("Time [s]")
plt.ylabel("Frequency [Hz]")

plt.subplot(2, 2, 3)
plt.plot(non_stationary_signal, c="indigo")
plt.title("harmonic_signal")

plt.subplot(2, 2, 4)
plt.plot(noise, c="indigo")
plt.title("Noise")

plt.show()
