import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

filename = 'output2.csv'
data = pd.read_csv(filename)
ConvertToMatrix = data.values

time = data[['Time(us)']]
#np.delete(ConvertToMatrix,[0,1],axis=1)
#print(time)
#voltage = np.delete(ConvertToMatrix,[1,1],axis=1)
accx = data[['AX(g)']]
accy = data[['AY(g)']]
accz = data[['AZ(g)']]
#print(voltage)

NumOfSampels= len(time)-5

#plt.plot(voltage)

accx1 = accx.transpose()
accy1 = accy.transpose()
accz1 = accz.transpose()

samplFreq = 3003

Pxx, freqs = plt.psd(accx1,   
NFFT=256,Fs=samplFreq,
detrend=mlab.detrend_mean,
window=mlab.window_hanning,noverlap=0,sides='onesided',scale_by_freq=True, 
return_line=None)

Pxx, freqs = plt.psd(accy1,   
NFFT=256,Fs=samplFreq,
detrend=mlab.detrend_mean,
window=mlab.window_hanning,noverlap=0,sides='onesided',scale_by_freq=True, 
return_line=None)

Pxx, freqs = plt.psd(accz1,   
NFFT=256,Fs=samplFreq,
detrend=mlab.detrend_mean,
window=mlab.window_hanning,noverlap=0,sides='onesided',scale_by_freq=True, 
return_line=None)

plt.xlim([20, 2000])
plt.xlabel('frequency [Hz]')
plt.ylabel('PSD [V**2/Hz]')

plt.show()
