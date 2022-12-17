# -*- coding:utf-8 -*-


'''
41.40数据流中的中位数(Av64288683,P41).mp4


题目描述
如何得到一个数据流中的中位数？如果从数据流中读出奇数个数值，那么中位数就是所有数值排序之后位于中间的数值。
如果从数据流中读出偶数个数值，那么中位数就是所有数值排序之后中间两个数的平均值。我们使用Insert()方法读取数据流，
使用GetMedian()方法获取当前读取数据的中位数。


思路：
不是很这傻逼题目要干嘛

输入输出什么都定义不清楚

'''


'''
没有搞懂到底想做什么，这个题目

下面的代码有BUG
'''
# -*- coding:utf-8 -*-
class Solution:
	def __init__(self):
		# self.data = self.sort(data)
		self.data = []

	'''
	def sort(x):
		if not x:
			return []
		length = len(x)

		for i in range(0, length -1):
			count = 0
			for j in range(0, length -1 - i):
				if x[j] > x[j+1]:
					x[j], x[j+1] =x[j+1], x[j]
					count +=1
			if count ==0:
				break
		return x

	'''

	def Insert(self, num):
		# write code here
		if not self.data:
			self.data.append(num)

		else:
			# self.data.append(num)
			# self.data.sort()

			#下面方式是错的
			for i in range(len(self.data)):
				if self.data[i]>num:
					self.data.insert(i, num)
					break


	def GetMedian(self, data):
		# write code here
		if not self.data:
			return None
		length = len(self.data)
		if length % 2 == 1:
			return self.data[length // 2]
		else:
			return (self.data[length//2] + self.data[length//2 - 1]) / 2.0

##  上面的测试用例
'''
用例:
[5,2,3,4,1,6,7,0,8]

对应输出应该为:

"5.00 3.50 3.00 3.50 3.00 3.50 4.00 3.50 4.00 "

你的输出为:

"5.00 3.50 3.00 3.50 3.00 3.00 3.00 2.50 2.50 "
'''


'''
解决上面的BUG并且通过的代码如下：

'''


# -*- coding:utf-8 -*-
class Solution1:
	def __init__(self):
		# self.data = self.sort(data)
		self.data = []

	'''
	def sort(x):
		if not x:
			return []
		length = len(x)

		for i in range(0, length -1):
			count = 0
			for j in range(0, length -1 - i):
				if x[j] > x[j+1]:
					x[j], x[j+1] =x[j+1], x[j]
					count +=1
			if count ==0:
				break
		return x

	'''

	def Insert(self, num):
		# write code here
		if not self.data:
			self.data.append(num)

		else:
			for i in range(len(self.data)):
				if self.data[i] > num:
					self.data.insert(i, num)
					return

			self.data.append(num)

	def GetMedian(self, data):
		# write code here
		if not self.data:
			return None
		length = len(self.data)
		if length % 2 == 1:
			return self.data[length // 2]
		else:
			return (self.data[length // 2] + self.data[length // 2 - 1]) / 2.0




'''
通过的解法2：
'''

class Solution2:
    def __init__(self):
        self.data=[]
    def Insert(self, num):
        # write code here
        self.data.append(num)
        self.data.sort()
    def GetMedian(self,data):
        # write code here
        length=len(self.data)
        if length%2==0:
            return (self.data[length//2]+self.data[length//2-1])/2.0
        else:
            return self.data[int(length//2)]

'''
用例:
[5,2,3,4,1,6,7,0,8]

对应输出应该为:

"5.00 3.50 3.00 3.50 3.00 3.50 4.00 3.50 4.00 "

'''
a = Solution()
alist = [5,2,3,4,1,6,7,0,8]
for i in  range(len(alist)):
	print(f"{i}".center(60, '-'))
	print(f"Insert data:{alist[i]}, Return:", a.Insert(alist[i]) )
	print(f"data:{a.data}")

	print("Median:\n")
	print(a.GetMedian(1) )





