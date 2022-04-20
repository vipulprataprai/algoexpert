
#Solution 1
#Time Complexity = O(2^n){at each level the function will split in 2 and maximum it will go to
#n levels} and Space = O(n) {because of the at most n calls on the stack}
def getNthFib(n):
  if n == 1:
    return 0
  if n == 2:
    return 1
  return getNthFib(n-1) + getNthFib(n-2)

#Solution 2
#Time Complexity = O(n){n calls as the calls prior are resolved and part of memoize} and Space = O(n) {max length of memoize}
def getNthFib(n, memoize = {1:0,2:1}):
	if n in memoize:
		return memoize[n]
	else:
		memoize[n] = getNthFib(n-1) + getNthFib(n-2)
		return memoize[n]

#Solution 3
#Time Complexity = O(n) Space = O(1)
def getNthFib(n):
  a = 0
  b = 1
  if n = 1:
    return 0
  if n = 2:
    return 1
  else:
    for i in range(1,n-1):
      c = a+b
      a = b
      b = c
    return b  
