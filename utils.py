def fact(n):
	m=1
	for i in range(1, n+1):
		m*=i
	return m
def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a > b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)

