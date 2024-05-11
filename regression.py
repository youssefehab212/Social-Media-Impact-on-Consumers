import math
import numpy as np
import pandas as pd

## import samples from excel file
df1 = pd.read_excel('Sample2.xlsx')
Sample=np.array(df1)
n=300

## Calculate sums of squares and products

Sumx=0
Sumy=0
Sumxy=0
Sumxx=0
Sumyy=0

for i in range(n):
    Sumx += Sample[i][0]
    Sumy += Sample[i][1]
    Sumxy += Sample[i][0]*Sample[i][1]
    Sumxx += Sample[i][0]**2
    Sumyy += Sample[i][1]**2
    
## Calculate Sxx Syy and Sxy

Sxx = Sumxx - (Sumx**2)/n
Syy = Sumyy - (Sumy**2)/n
Sxy = Sumxy - (Sumx*Sumy)/n

ymean = Sumy/n
xmean = Sumx/n

## Calculate a and b

b = Sxy/Sxx
a = ymean - b*xmean

print("Sxx = %d" % Sxx)
print("Syy = %d" % Syy)
print("Sxy = %d" % Sxy)
print("Y = %.2f + %.4fx" % (a,b))

