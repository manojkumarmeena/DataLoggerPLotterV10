##import numpy as np
##import matplotlib.pyplot as plt
##from scipy.fftpack import fft, rfft,ifft
##import pandas as pd
##
### Import csv file
##df = pd.read_csv('1ogsample.csv')
###print(df.head())
##
###plot data
####plt.figure(figsize=(12,4))
####df.plot(linestyle = '', marker = '*', color='r')
####plt.savefig('log4fft.jpg')
####plt.show()
##
###FFT
###number of sample points
##N = 283280
###frequency of signal (us)
##T = 333
###create x-axis for time length of signal
##x = np.linspace(0, N*T, N)
###create array that corresponds to values in signal
##y = df
###perform FFT on signal
##yf = rfft(y)
###create new x-axis: frequency from signal
##xf = np.linspace(0.0, 1.0/(2.0*T), N//2) * 10000
###plot results
##
####plt.xlim(-20,20)
####plt.ylim(-16,16)
##
##plt.plot(xf, abs(yf[0:N//2]), label = 'signal')
##plt.grid()
##plt.xlabel('FRQ(Hz)')
##plt.ylabel(r'PSD')
##
##plt.legend(loc=1)
##plt.savefig('log4fft.jpg')
##plt.show()

##import numpy as np
##import pandas as pd
##import matplotlib.pyplot as plt
##
###df = pd.read_csv('1.csv')
##df = pd.read_csv('logsample.csv')
##
##
### The horizontal index must be linear
###assert np.all(df.Time.diff()[1:] == 1)
###assert (df['Time'].str.len() == 8).all()
###padded_array = np.pad('AX',pad_width=8,mode='constant',constant_values=0)
##
##yf = np.fft.rfft(df.AX, norm='forward')
###ff = np.fft.rfftfreq(n=len(df), d=0.000333)
##ff = np.fft.rfftfreq(2803280, d=0.000333)
##
##fig, ax = plt.subplots()
##ax.loglog(ff, yf)
##
##plt.xlim(0,2000)
##plt.ylim(0,16)
##
##ax.set_xlabel('Frequency (Hz)')
##ax.set_ylabel('PSD(AXg)')
##plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('1.csv')

# The horizontal index must be linear
assert np.all(df.epoch.diff()[1:] == 1)

yf = np.fft.rfft(df.voltage, norm='forward')
ff = np.fft.rfftfreq(n=len(df), d=2)

fig, ax = plt.subplots()
ax.loglog(ff, np.abs(yf))
ax.set_xlabel('Frequency (Hz)')
ax.set_ylabel('Amplitude (V)')
plt.show()
