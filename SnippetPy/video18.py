#Snippet Codes for Python
#Video 18: Fibonacci Sequence

i = int(raw_input('Write the n-th term in Fibonacci sequence: \n'))
fib = []
fib.append(1)
fib.append(1)
j = 0
while j < i:
	fib.append(fib[j]+fib[j+1])
	j = j + 1
print 'The Fibonacci sequence: ',fib




