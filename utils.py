def fact(n):
	m=1
	for i in range(1, n+1):
		m*=i
	return m
def gcd(a, b):
    while a*b!=0:
        a=a%b
        return gcd(a, b)
    return max(a, b)
def is_prime(n):
    for i in range(2, (n+2)//2):
        if n%i==0:
            return "NO"
    return "YES"
