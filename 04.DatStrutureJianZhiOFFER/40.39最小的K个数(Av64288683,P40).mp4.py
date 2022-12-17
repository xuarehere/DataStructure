# -*- coding:utf-8 -*-
'''
40.39最小的K个数(Av64288683,P40).mp4


题目描述
输入n个整数，找出其中最小的K个数。例如输入4,5,1,6,2,7,3,8这8个数字，则最小的4个数字是1,2,3,4,。

思路：
先排序，后返回
'''


# -*- coding:utf-8 -*-
class Solution:
	def GetLeastNumbers_Solution(self, tinput, k):
		# write code here
		if not tinput or k > len(tinput):
			return []

		length = len(tinput)

		for i in range(0, length):
			count = 0
			for j in range(0, length - 1 - i):
				if tinput[j] > tinput[j + 1]:
					tinput[j], tinput[j + 1] = tinput[j + 1], tinput[j]
					count += 1
			if count == 0:
				break
		return tinput[:k]
