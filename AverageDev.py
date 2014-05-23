# Kendall Park
# Because I'm so sick of computing the average devation by hand #chemlabwin
# TODO: figure out some args coolness in python

import math 

def avgDev(values) :
  sum = 0.0;
  for value in values :
    sum+=value
  mean = sum/len(values)
  
  i = 0
  avgDev = []
  while i < len(values):
    avgDev.append( abs(mean - values[i]) )
    i+=1
  
  sum = 0.0
  for dev in avgDev: 
    sum+=dev
  avgDevMean = sum/len(avgDev)
  
  return "Mean: "+str(mean)+" \nAvg Dev: "+str(avgDevMean)+" \nPercent Dev "+str(avgDevMean/mean*100)+"%"
  
HCl = [-59.9, -59.4, -58.0]

Acetic = [-51.7, -51.5, -50.9]

metal = [24.56, 24.86, 24.60]

Ka = [1.2e-3, 1.6e-3, 1.6e-3]

Ka1 = [5.4e-3, 6.6e-3, 5.9e-3]

Ka2 = [2.3e-10, 2.1e-10, 2.0e-10]

#print avgDev(HCl)
#print avgDev(Acetic)

print avgDev(Ka2)
