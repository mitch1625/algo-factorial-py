def factorial(num):
	answer = 1

	for x in range(1,num+1): # range(a,b) -> a is implicit and b is explicit. 
		answer *= x
	return answer

