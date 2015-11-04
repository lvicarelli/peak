import numpy as np
import re
import matplotlib.pyplot as plt
%matplotlib inline

def readFileData(file):
    #load the file into np array
    data1 = open(file,'r')
    np.array1 = []
    for line in data1:
        #print(line.split())
        newLine = line.split()
        for number in newLine:
            number2 = re.sub(',','',number)
            np.array1 = np.append(np.array1,float(number2))
    return np.array1

x1 = readFileData('frequency_sample1.txt')
x2 = readFileData('frequency_sample2.txt')
y1 = readFileData('S21_magn_sample1.txt')
y2 = readFileData('S21_magn_sample2.txt')
"""
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.xlim
plt.show()
"""
direv = np.diff(y1)
plt.plot(x1[0:-1],direv)
plt.plot(x1,y1+1,color='red')
plt.xlim([5,8])
plt.grid()
plt.show()

direv = np.diff(y2)
plt.plot(x2[0:-1],direv)
plt.plot(x2,y2+2,color='red')
plt.xlim([5,8])
plt.grid()
plt.show()