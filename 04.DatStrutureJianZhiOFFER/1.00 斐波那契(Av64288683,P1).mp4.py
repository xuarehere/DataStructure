# -*- coding:utf-8 -*-
'''

1.00 斐波那契(Av64288683,P1).mp4
## 6.斐波那契数列

**大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39**


这样一个数列：1、1、2、3、5、8、13、21、34、……
2 = 1+ 1
3 = 2 + 1
5 = 3 + 2
f(n) = f(n-1) + f(n-2)
'''

def feiBoNaQie(n):
	if n < 1:
		return 0
	elif n < 3:
		return 1
	return feiBoNaQie(n-1) + feiBoNaQie(n -2)
	# pass

print( feiBoNaQie(9) )



