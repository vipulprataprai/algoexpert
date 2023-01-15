#Complexity :: Time = O(n) Space = O(d) {d is the greatest depth of the special array in the array} 
def productSum(array, multiplier =1):
    # Write your code here.
    # I am leating git
    #Cheers to learning. First step is important.
	sum = 0
	for element in array:
		if type(element) is list:
			sum += productSum(element, multiplier + 1)
		else:
			sum += element
	return sum * multiplier
