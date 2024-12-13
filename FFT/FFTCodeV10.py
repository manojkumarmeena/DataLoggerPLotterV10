##import matplotlib.pyplot as plt
##import numpy as np
##import pandas as pd
##
##df = pd.read_csv('output2.csv', delimiter=',', parse_dates=[1])
##df.rename(columns={'Timestamp':'Time(us)', 'Total ACC':'AY(g)'},inplace=True)
##
##plt.figure(figsize = (12, 6))
##plt.plot(df['Time(us)'], df['AY(g)'])
##plt.xlabel('Time')
##plt.ylabel('Acceleration(g)')
##plt.xticks(rotation=25) 
##plt.show()
##
##from numpy.fft import fft, ifft
##
##X = fft(x)
##N = len(X)
##n = np.arange(N)
##T = N/sr
##freq = n/T 
##
##plt.figure(figsize = (12, 6))
##plt.subplot(121)
##
##plt.stem(freq, np.abs(X), 'b', \
##         markerfmt=" ", basefmt="-b")
##plt.xlabel('Freq (Hz)')
##plt.ylabel('FFT Amplitude |X(freq)|')
##plt.xlim(0, 10)
##
##plt.subplot(122)
##plt.plot(t, ifft(X), 'r')
##plt.xlabel('Time (s)')
##plt.ylabel('Amplitude')
##plt.tight_layout()
##plt.show()
##

##import matplotlib.pyplot as plt
##import scipy.signal
##import pandas as pd
##import numpy as np
##from numpy.fft import rfft, rfftfreq
##import matplotlib.pyplot as plt
##
##t=pd.read_csv('output2.csv',usecols=[0])
##a=pd.read_csv('output2.csv',usecols=[1])
##n=len(a)                ##/no of samples
##dt=0.000333 #time increment in each data
##
##acc=a.values.flatten() #to convert DataFrame to 1D array
###acc value must be in numpy array format for half way mirror calculation
##
##fft=rfft(acc)*dt
##freq=rfftfreq(n,d=dt)
##
##FFT=abs(fft)
##
##plt.plot(freq,FFT)
##plt.xlabel('Frequency(Hz)')
##plt.ylabel('PSD')
##plt.show()


import numpy as np

from scipy import signal

import matplotlib.pyplot as plt

rng = np.random.default_rng()

fs = 4e3    #Frequency range (20-2000Hz)

N = 1e5     #Samples

amp = 40*np.sqrt(2)

freq = 1234.0

noise_power = 0.001 * fs / 2

time = np.arange(N) / fs

x = amp*np.sin(2*np.pi*freq*time)

x += rng.normal(scale=np.sqrt(noise_power), size=time.shape)

f, Pxx_den = signal.welch(x, fs, nperseg=1024)

plt.semilogy(f, Pxx_den)

#plt.ylim([0.5e-3, 1])
plt.ylim([-16, 16])

plt.xlabel('frequency [Hz]')

plt.ylabel('PSD [A**2/Hz]')

plt.show()

