'''
In Jon Erickson's book "Hacking - the Art of Exploitation" 
the following problem is found in the introduction: 

"Use each of the numbers 1, 3 , 4, and 6 exactly once 
with any of the four basic math operations (addition, subtraction, 
multiplication, and division) to total 24. Each number must be 
used once and only once, and you may define the order of operations."

We solve this by brute force in python.
'''

import itertools


# Operation Codes
# 0 is + (addition)
# 1 is - (subtration)
# 2 is * (multiplication)
# 3 is / (division)
# The return value is None when division by zero occurs.
def singleOperation(operationCode, x, y):
	if operationCode == 0:
		return x + y
	if operationCode == 1:
		return x - y
	if operationCode == 2:
		return x * y
	if operationCode == 3:
		if y == 0:
			return None
		else:
			return x / y


# numberList is just a nonempty list of integers of length n 
# operationCodes is a list of length n-1 and whose elements are in the set {0, 1, 2, 3}
# operationOrders is a permutaion of {0,...,n-2} and hence is also a list of length n-1
# The return value is None when division by zero occurs.
def multipleOperations(numberList, operationCodes, operationOrders):
	if len(numberList) == 1:
		return numberList[0]
	
	i = operationOrders[0]
	numberList[i] = singleOperation(operationCodes[i], numberList[i], numberList[i + 1])
	if numberList[i] == None:
		return None

	del numberList[i + 1]
	del operationCodes[i]
	del operationOrders[0]

	for j in range(0, len(operationOrders)):
		if operationOrders[j] > i:
			operationOrders[j] -= 1

	return multipleOperations(numberList, operationCodes, operationOrders)



allNumberLists = list(itertools.permutations([1, 3, 4, 6]))
allOperationCodes = list(itertools.product(range(0,4), repeat=3))
allOperationOrders = list(itertools.permutations([0, 1, 2]))


for i in range(len(allNumberLists)):
	for j in range(len(allOperationCodes)):
		for k in range(len(allOperationOrders)):
			if multipleOperations(list(allNumberLists[i]), list(allOperationCodes[j]), list(allOperationOrders[k])) == 24:
				print(allNumberLists[i])
				print(allOperationCodes[j])
				print(allOperationOrders[k])

