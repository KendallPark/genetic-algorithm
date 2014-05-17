# Kendall Park
# This will run a very, very long time.

from GeneticAlgorithm import *
from time import time
from AverageDev import avgDev

def experiment(incr, trials, sets, reps):
	i = 8
	while i < trials:
		i += 1
		j = 0
		trialTime = 0.0
		while j < sets:
			j += 1
			size = i*incr
			V = [random.randint(1,size) for n in range(size)]
			W = [random.randint(1,size) for n in range(size)]
			MAX = random.randint(1,size*4)
			k = 0
			setTime = 0
			weights = []
			while k < reps:
				k += 1
				t1 = time()
				winner = knapsack(V, W, MAX, 100, 100, 10*size, 0.9)
				t2 = time()
				setTime += t2-t1
				#print winner
				weights += [evaluateAnswer(winner, V, W, MAX)]
				#print answer
			print "Trial "+str(i)+" Set: "+str(j)
			print "Volumes: " + str(V)
			print "Weights: " + str(W)
			print "Max Volume: " + str(MAX)
			print "Weights Found: " + str(weights)
			print avgDev(weights)
			print "Average Time: "+str(setTime/reps)
			print ""
			trialTime += setTime/reps
		print "Set "+str(i)+" avg time :"+str(trialTime/trials)
		print ""
		
def evaluateAnswer(gene, V, W, MAX):
	volume = 0
	weight = 0
	for j in range(len(gene)):
			if gene[j] == 1:
				volume += V[j]
				weight += W[j]
	if volume > MAX:
		print "ERROR!!! VOLUME IS GREATER THAN MAX VOLUME!"
	return weight
			
experiment(10, 10, 10, 10)
