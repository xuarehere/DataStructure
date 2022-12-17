# -*- coding:utf-8 -*-
'''

3.02变态跳台阶(Av64288683,P3).mp4

## 8.变态跳台阶

**一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。**

1	1						mo
2	11,	12					2
3	111, 12, 21,3 			4
4,	31,13,4,  				8
	31: 111 1, 12 1, 21 1,
	13: 1 111, 1 12, 1 21,

算法(九)：变态跳台阶_码神岛
https://msd.misuland.com/pd/3053059875815819996

'''

def abnormalfrogJump(n):
	if n < 0:
		return None
	# elif n ==0 :
	# 	return 0
	# elif n == 1:
	# 	return 1
	# return 2*abnormalfrogJump(n-1)
	return 2**(n-1)

print(abnormalfrogJump(4))