# -*- coding:utf-8 -*-
'''
# 2.01青蛙跳台阶(Av64288683,P2).mp4
#
#
# ## 7.青蛙跳台阶
#
# **一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。**
#
1	1						1
2	11,	12					2
3	111, 12, 21 			3
4,	31,13,4,  ==			5
	31: 111 1, 12 1, 21 1,
	13: 1 111, 1 12, 1 21(重),
	4:	22



# ![](C:\Users\Administrator\Desktop\剑指offer\青蛙跳台阶.png)
#剑指Offer算法题-青蛙跳台阶的问题 - 简书
# https://www.jianshu.com/p/965d12083d7f
'''
#
def jumpFloor(number):
	if number < 1:
		return 0
	if number == 1:
		return 1
	if number == 2:
		return 2

	ret = 0
	a = 1
	b = 2
	for i in range(3, number + 1):
		ret = a + b
		a = b
		b = ret
	return ret


def fogJump(n):
	'''
	there is too large for time complexity
	:param n:
	:return:
	'''
	if n < 0:
		return None
	elif n ==0 :
		return 0
	elif n == 1:
		return 1
	elif n == 2:
		return 2
	return fogJump(n-1) + fogJump(n-2)


print(  jumpFloor(10) )
print(  fogJump(10)  )


# -*- coding:utf-8 -*-
class Solution:
	def jumpFloor(self, number):
		# write code here
		n = number
		if n < 0:
			return None
		elif n == 0:
			return 0
		elif n == 1:
			return 1
		elif n == 2:
			return 2
		a = 1
		b = 2
		ret = 0
		for i in range(3, n + 1):
			ret = a + b
			a = b
			b = ret

		return ret