import os
s = input().split()
fo = open('qqk.py','w')
txt = 'def jf(x):return '+s[0]
fo.write(txt)
fo.close()
fo=open('tem.txt','w')
fo.write(s[1]+' '+s[2])
fo.close()
os.system('python fn.py')