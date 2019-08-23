import math
n=13
r=[]
def s(c,n):
	u=sum(i**2 for i in c)
	if u==n: return len(c)
	c.append(int(math.sqrt(n-u)))
	return s(c,n)
print(s(r,n))