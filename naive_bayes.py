import csv
import random
import math
#load du lieu de tien hanh training
def loadCsv(filename):
	lines = csv.reader(open(filename, "rb"))
	dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [str(x) for x in dataset[i]]
	return dataset
filename = 'attack_log.csv'
dataset = loadCsv(filename)
print('Loaded data file {0} with {1} row').format(filename, len(dataset))

#tach du lieu thanh train data va test data
def splitDataset(dataset, splitRatio):
   trainSize = int(len(dataset) * splitRatio)
   trainSet = []
   copy = list(dataset)

   while len(trainSet) < trainSize:
       index = random.randrange(len(copy))
       trainSet.append(copy.pop(index))
   return [trainSet, copy]
filename = 'attack_log.csv'
dataset = loadCsv(filename)
print('Loaded data file {0} with {1} row').format(filename, len(dataset))
splitRatio = 0.25
train, test = splitDataset(dataset, splitRatio)
print ('Split {0} rows into train with {1} and test with {2}').format(len(dataset), train, test)

def separateByClass(dataset):
   separate = {}
   for i in range(len(dataset)):
       vector = dataset[i]
       if (vector[-1] not in separate):
           separate[vector[-1]] = []
       separate[vector[-1]].append(vector)
   return separate
filename = 'attack_log.csv'
dataset = loadCsv(filename)
separated = separateByClass(dataset)
print ('Sperated instance : {0}').format(separated)

def mean(numbers):
	return sum(numbers)/float(len(numbers))

def stdev(numbers):
  avg = mean(numbers)
  variance = sum([pow(x - avg,2) for x in number])/float(len(numbers) -1)
  return math.sqrt(variance)
# with open ("attack_log.csv") as f:

  