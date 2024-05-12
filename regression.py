import math
import numpy as np
import pandas as pd

def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

## import samples from excel file
df1 = pd.read_excel(r'Sample2.xlsx')
Sample=np.array(df1)
n=300 # sample size
k=1 # number of independent variables

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

## Calculate standard error

SSE=0
for i in range(n):
    SSE += pow(Sample[i][1] - (a + b*Sample[i][0]),2)

print("SSE = %d" % SSE)
Se=math.sqrt(SSE/(n-k-1))

## Calculate variance-covariance matrix

X=Sample
for i in range(n):
    X[i][1]=Sample[i][0]
    X[i][0]=1
    

X_transpose = transpose(X)

result=np.dot(X_transpose,X)
C = np.linalg.inv(result)
C*=pow(Se,2)

## Calculate R-Squared

R2=(Sxy**2)/(Sxx*Syy)

print("Se^2 = %d" % pow(Se,2))
print("Variance-Covariance matrix")
print(C)

print("Variance of a = %.3f" % C[0][0])
print("Variance of b = %.3f" % C[1][1])
print("Covariance of (a,b) = %.3f" % C[0][1])
print("R-squared = %.3f" % R2)

print("Sxx = %d" % Sxx)
print("Syy = %d" % Syy)
print("Sxy = %d" % Sxy)
print("Y = %.2f + %.4fx" % (a,b))

