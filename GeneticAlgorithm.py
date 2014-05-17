# Kendall Park
# Filename: GeneticAlgorithm.py

import random

	# 1. [Start] Generate random population of n chromosomes (suitable solutions for the problem)
	# 2. [Fitness] Evaluate the fitness f(x) of each chromosome x in the population
	# 3. [New population] Create a new population by repeating following steps until the new population is complete
		# A. [Selection] Select two parent chromosomes from a population according to their fitness (the better fitness, the bigger chance to be selected)
		# B. [Crossover] With a crossover probability cross over the parents to form a new offspring (children). If no crossover was performed, offspring is an exact copy of parents.
		# C. [Mutation] With a mutation probability mutate new offspring at each locus (position in chromosome).
		# D. [Accepting] Place new offspring in a new population
	# 4. [Replace] Use new generated population for a further run of algorithm
	# 5. [Test] If the end condition is satisfied, stop, and return the best solution in current population
	# 6 [Loop] Go to step 2

def knapsack(V, W, MAX, popSize, mut, maxGen, percent):
	generation = 0
	pop = generate(V, popSize)
	fitness = getFitness(pop, V, W, MAX)
	while(not test(fitness, percent) and generation < maxGen):
		generation += 1
		pop = newPopulation(pop, fitness, mut)
		fitness = getFitness(pop, V, W, MAX)
	#print fitness
	#print generation
	return selectElite(pop, fitness)

def generate(V, popSize):
	length = len(V)
	pop = [[random.randint(0,1) for i in range(length)] for j in range(popSize)]
	#print pop
	return pop
	
def getFitness(pop, V, W, MAX):
	fitness = []
	for i in range(len(pop)):
		weight = 0
		volume = MAX+1
		while (volume > MAX):
			weight = 0
			volume = 0
			ones = []
			for j in range(len(pop[i])):
				if pop[i][j] == 1:
					volume += V[j]
					weight += W[j]
					ones += [j]
			if volume > MAX:
				pop[i][ones[random.randint(0, len(ones)-1)]] = 0
		fitness += [weight]
	#print "Modified Population:"
	#print pop
	#print "Fitness of Population:"
	#print fitness
	return fitness
	

def newPopulation(pop, fit, mut):
	popSize = len(pop)
	newPop = []
	newPop += [selectElite(pop, fit)]
	#print "Elite:"
	#print newPop
	while(len(newPop) < popSize):
		(mate1, mate2) = select(pop, fit)
		newPop += [mutate(crossover(mate1, mate2), mut)]
		
	#print "After Selection"
	#print newPop
	return newPop
	
def selectElite(pop, fit):
	elite = 0
	for i in range(len(fit)):
		if fit[i] > fit[elite]:
			elite = i
	return pop[elite]

def select(pop, fit):
	size = len(pop)
	totalFit = sum(fit)
	lucky = random.randint(0, totalFit)
	tempSum = 0
	mate1 = []
	fit1 = 0
	for i in range(size):
		tempSum += fit[i]
		if tempSum >= lucky:
			mate1 = pop.pop(i)
			fit1 = fit.pop(i)
			break
	tempSum = 0
	lucky = random.randint(0, sum(fit))
	for i in range(len(pop)):
		tempSum += fit[i]
		if tempSum >= lucky:
			mate2 = pop[i]
			pop += [mate1]
			fit += [fit1]
			return (mate1, mate2)

def crossover(mate1, mate2):
	lucky = random.randint(0, len(mate1)-1)
	#print "Lucky: " + str(lucky)
	return mate1[:lucky]+mate2[lucky:]
	
def mutate(gene, mutate):
	for i in range(len(gene)):
		lucky = random.randint(1, mutate)
		if lucky == 1:
			#print "MUTATED!"
			gene[i] = bool(gene[i])^1
	return gene
		
def test(fit, rate):
	maxCount = mode(fit)
	if float(maxCount)/float(len(fit)) >= rate:
		return True
	else:
		return False

def mode(fit):
	values = set(fit)
	maxCount = 0
	for i in values:
		if maxCount < fit.count(i):
			maxCount = fit.count(i)
	return maxCount

volume = [1, 3, 2, 3, 2, 3, 3]
weights = [2, 100, 5, 3, 50, 16, 60]
maxVolume = 6
popSize = 10

#print crossover(volume, weights)

#print mutate([1, 1, 1, 1, 1, 1, 1, 1, 1])

#print "FINAL SOLUTION: " + str(knapsack(volume, weights, maxVolume, popSize))
