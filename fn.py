from qqk import jf
with open('tem.txt','r') as fo:
	s = fo.read()
s = s.split()
ans = 0
k = float(s[0])
while k<float(s[1]):
	ans+=0.0001*jf(k)
	k+=0.0001
print(f'{ans:.3f}')