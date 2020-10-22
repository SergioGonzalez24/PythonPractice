def getNthFib(n):
	if not(n==0 or n==1):
		for i in (2,n):
			n=(i-1)+(i-2)
		return(n)
	else:
		return(n)
	

getNthFib(2)