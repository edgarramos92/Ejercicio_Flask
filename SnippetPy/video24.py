#Snippet Codes for Python
#Video 24: Primes

def primes(n):
        var = []
	var2 = 0
	for i in range(n):
		b = n % (i+2) 
		if b == 0 and n != (i + 2): 
			var2 = var2 
			return 'Es divisible por ',i+2,' no es primo'
  	if var2 == 0 :
		return ' %i es primo'%(n)
print primes(217)


