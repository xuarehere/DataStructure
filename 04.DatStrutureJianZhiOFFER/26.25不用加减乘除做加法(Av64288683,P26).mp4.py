# -*- coding:utf-8 -*-
'''
26.25不用加减乘除做加法(Av64288683,P26).mp4

## 20.不用加减乘除做加法[^本题考点 *按位运算*]

**写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。**

感觉考得可能性不大，后面再重新复习吧
'''


# -*- coding:utf-8 -*-
class Solution:
	def Add(self, num1, num2):
		# write code here
		# if num1 < 0:
		# 	num1 = num1 & 0xffffffff
		# if num2 < 0:
		# 	num2 = num2 & 0xffffffff
		noFlag = num1 ^ num2
		flage = (num1 & num2) << 1
		tmp1 = 0
		tmp2 = 0
		count = 1

		while flage:
			tmp1 = noFlag ^ flage
			tmp2 = (noFlag & flage) << 1

			tmp1 = tmp1 & 0xffffffff

			noFlag = tmp1
			flage = tmp2
			count += 1
		return noFlag if noFlag <= 0x7ffffff else ~(noFlag ^ 0xFFFFFFFF)
