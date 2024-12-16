# Matplotlib 
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal

fs = 1/3003.0 # 3 kHz sampling frequency
F1 = 20 # First signal component at 10 Hz
F2 = 2000 # Second signal component at 60 Hz
T = 100 # 100s signal length
N0 = -10 # Noise level (dB)

t = np.r_[0:T:(1/fs)] # Sample times

# Two Sine signal components at frequencies F1 and F2.
signal = np.sin(2 * F1 * np.pi * t) + np.sin(2 * F2 * np.pi * t) 

# White noise with power N0
signal += np.random.randn(len(signal)) * 10**(N0/20.0) 


(S, f) = plt.psd(signal, Fs=fs)

plt.semilogy(f, S)
plt.xlim([20, 2000])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')
plt.show()
