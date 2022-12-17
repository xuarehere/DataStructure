# -*- coding:utf-8 -*-
'''
42.41数据流中的中位数-封装(Av64288683,P42).mp4


题目描述
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，使用GetMedian()方法获取当前读取数据的中位数。


'''

#
# # -*- coding:utf-8 -*-
# class Solution:
# 	def __init__(self):
# 		# self.data = self.sort(data)
# 		self.data = []
#
# 	'''
# 	def sort(x):
# 		if not x:
# 			return []
# 		length = len(x)
#
# 		for i in range(0, length -1):
# 			count = 0
# 			for j in range(0, length -1 - i):
# 				if x[j] > x[j+1]:
# 					x[j], x[j+1] =x[j+1], x[j]
# 					count +=1
# 			if count ==0:
# 				break
# 		return x
#
# 	'''
#
# 	def Insert(self, num):
# 		# write code here
# 		if not self.data:
# 			self.data.append(num)
#
# 		else:
# 			for i in range(len(self.data)):
# 				if self.data[i] > num:
# 					self.data.insert(i, num)
# 					return
#
# 			self.data.append(num)
#
# 	def GetMedian(self, data):
# 		# write code here
# 		if not self.data:
# 			return None
# 		length = len(self.data)
# 		if length % 2 == 1:
# 			return self.data[length // 2]
# 		else:
# 			return (self.data[length // 2] + self.data[length // 2 - 1]) / 2.0


# -*- coding:utf-8 -*-
class Solution:
	def __init__(self):
		self.data = []

	def Insert(self, num):
		# write code here
		self.data.append(num)

	def GetMedian(self, data):
		# write code here
		if not self.data:
			return None

		import copy
		dataTmp = copy.deepcopy(self.data)
		dataTmp.sort()
		dataLen = len(dataTmp)
		if dataLen % 2 == 1:
			return dataTmp[dataLen // 2]
		else:
			return (dataTmp[dataLen // 2] + dataTmp[dataLen // 2 + 1]) / 2.0

if __name__ == '__main__':
    s = Solution()
    s.Insert(5)
    print(s.GetMedian())

    s.Insert(2)
    print(s.GetMedian())

    s.Insert()
    print(s.GetMedian())