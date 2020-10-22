def getNthFib(n):
	if not(n==0 and n==1):
		n=(n-1)+(n-2)
		return(n)
	else:
		return(n)
	
num=int(input("Nmber"))
getNthFib(num)