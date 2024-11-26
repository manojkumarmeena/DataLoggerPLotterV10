import argparse
import serial
import datetime
import time
import os

import csv
import string
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

ser = serial.Serial("COM7", 115200)

print("stage-01")

ser.flush()
rxdata = ser.read(26)
while rxdata != b'\n1-STORE  2-RELAY  3-ERASE':
    ser.flush()
    rxdata = ser.read(26)
    print(rxdata)
    time.sleep(0.5)
print(rxdata)

ser.write(str.encode('1'))
time.sleep(0.1)

ser.flush()
rxdata = ser.read(26)
while rxdata != b'\n[-Logging Data: S Stops-]':
    rxdata = ser.read(26)
    print(rxdata)
    time.sleep(0.5)
print(rxdata)

ser.flush()
rxdata = ser.read(26)
while rxdata != b'\n[-Logging Data Stopped -]':
    ser.flush()
    rxdata = ser.read(26)
    print(rxdata)
    time.sleep(0.5)
print(rxdata)

print("stage-02")

ser.flush()
rxdata = ser.read(26)
while rxdata != b'\n1-STORE  2-RELAY  3-ERASE':
    ser.flush()
    rxdata = ser.read(26)
    print(rxdata)
    time.sleep(0.5)
print(rxdata)

ser.write(str.encode('2'))
time.sleep(0.1)

ser.flush()
rxdata = ser.read(26)
while rxdata != b'\n[-Get Ready To Log Data-]':
    rxdata = ser.read(26)
    print(rxdata)
    time.sleep(0.5)
print(rxdata)

ser.flush()
rxdata = ser.read(26)
while rxdata != b'\n[---Stored  Data Ends---]':
    ser.flush()
    rxdata = ser.read(26)
    print(rxdata)
print(rxdata)

print("stage-03")

ser.flush()
rxdata = ser.read(26)
while rxdata != b'\n1-STORE  2-RELAY  3-ERASE':
    ser.flush()
    rxdata = ser.read(26)
    print(rxdata)
    time.sleep(0.5)
print(rxdata)

ser.write(str.encode('3'))
time.sleep(0.1)

ser.flush()
rxdata = ser.read(26)
while rxdata != b'\n[Erasing Required Memory]':
    rxdata = ser.read(26)
    print(rxdata)
    time.sleep(0.5)
print(rxdata)

ser.flush()
rxdata = ser.read(26)
while rxdata != b'\n[Memory Erasing Complete]':
    ser.flush()
    rxdata = ser.read(26)
    print(rxdata)
    time.sleep(0.5)
print(rxdata)

ser.close()

from matplotlib.backends.backend_pdf import PdfPages

parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-d", "--device", help="device to read from", default="COM6")
parser.add_argument("-s", "--speed", help="speed in bps", default=115200, type=int)
args = parser.parse_args()

outputFilePath = os.path.join(os.path.dirname(__file__),
                 #datetime.datetime.now().strftime("%Y-%m-%dT%H.%M.%S") + ".csv")
                datetime.datetime.now().strftime("data") + ".csv")


with serial.Serial(args.device, args.speed) as ser, open(outputFilePath, mode='wb') as outputFile:
    print("Logging started. Wait 4 Data to Complete or Press Ctrl-C to stop.") 
    ser.timeout=5
    try:
        while True:
            time.sleep(1)
            outputFile.write((ser.read(ser.inWaiting())))
            outputFile.flush()
    except KeyboardInterrupt:
        print("Logging stopped")

    except ser.SerialException:
    #There is no new data from serial port
        print("No data")

input_file = open('data.csv', 'r')
output_file = open('Output.csv', 'w')
data = csv.reader(input_file)
writer = csv.writer(output_file)
specials = '$'

for line in data:
    line = [value.replace(specials,'') for value in line]
    writer.writerow(line)

input_file.close()
output_file.close()

df = pd.read_csv('output.csv')
df.dropna(axis=0, how='all',inplace=True)
df.to_csv('output1.csv', index=False)

# read contents of csv file 
file = pd.read_csv("output1.csv") 
##print("\nOriginal file:")
##print(file) 
  
# adding header 
headerList = ['Pkt','AX', 'AY', 'AZ'] 
  
# converting data frame to csv 
file.to_csv("output2.csv", header=headerList, index=False) 
  
data = pd.read_csv("output2.csv")
#print(data.head())

fig = px.line(data, x="Pkt",y=["AX", "AY", "AZ"],title="ACC data over time")
        
fig.show()
