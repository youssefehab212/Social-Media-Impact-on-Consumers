import math
import numpy as np
import pandas as pd

## import samples from excel file
df1 = pd.read_excel('Sample1.xlsx')
Sample=np.array(df1)

# Calculate mean for each sample and total mean
means = np.empty(8)
for i in range(8):
    means[i]=np.mean(Sample[:,i])

Totalmean=np.mean(Sample)

k=8
n=30

################ Calculate SSA ##########
SSA=0

for i in range(k):
    SSA += pow(means[i]-Totalmean,2)
    
SSA = SSA*n
print("SSA = %.3f" % SSA)

############### Calculate SSE ###########
SSE=0
for i in range(k):
    for j in range(n):
        SSE += pow(Sample[j][i]-means[i],2)
        
print("SSE = %.3f" % SSE)

########### Calculate SST #########

SST = SSA + SSE
print("SST = %.3f" % SST)

######## ANOVA table values #####

dfTreatment = k-1
dfError = n-k
dfTotal = n-1
MSTreatment = SST/dfTreatment
MSError = SSE/dfError
F = MSTreatment/MSError 

print("df Treatment = %d" % dfTreatment)
print("df Error = %d" % dfError)
print("df Total = %d" % dfTotal)
print("MS Treatment = %.3f" % MSTreatment)
print("MS Error = %.3f" % MSError)
print("F = %.3f" % F)







