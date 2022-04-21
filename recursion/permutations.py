#Solution 1 
#Time Complexity = O(n!*n^2) {Upper Bound} | O(n!*n) {Lower bound}
#Space Complexity = O(n!*n)
def getPermutations(array):
	permutations = []
	getPerHelper(array,[],permutations)
	return permutations

	
def getPerHelper(array, currentperm, permutations):
	if not len(array) and len(currentperm):
		permutations.append(currentperm)
	else:
		for i in range(len(array)):
			newarray = array[:i] + array[i+1:]
			newperm = currentperm + [array[i]]
			getPerHelper(newarray,newperm,permutations)
      
#Solution 2
#Time Complexity = O(n!*n)
#Space Complexity = O(n!*n)

def getPermutations(array):
	permutations = []
	getHelp(0, array, permutations)
	return permutations

	
			
def getHelp(i,array,permutations):
	if i == len(array)-1:
		permutations.append(array[:])
	else:
		for j in range(i,len(array)):
			swap(array,i,j)
			getHelp(i+1,array,permutations)
			swap(array,i,j)
	
def swap(array,i,j):
	array[i],array[j] = array[j],array[i]
