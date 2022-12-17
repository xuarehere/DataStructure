# -*- coding:utf-8 -*-

class ShellSort():
	def shellSort(self, alist):
		import math
		n = len(alist)
		# 初始步长
		# gap = (n / 2)  # 一直报错
		# gap = int(n / 2)		# 一直报错
		gap = (n // 2)  # 一直报错
		# gap = math.floor(gap)
		# print(gap, type(gap), type(n))
		# print(type(gap)==type(n))
		while gap > 0:
			# 按步长进行插入排序
			for i in range(gap, n):
				j = i
			# 插入排序
			# while j >= gap and alist[j - gap] > alist[j]:
			while alist[j - gap] > alist[j]:
				alist[j - gap], alist[j] = alist[j], alist[j - gap]
				j -= gap
				# 得到新的步长
			gap = gap // 2

	def shellSortTest(self):
		alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
		self.shellSort(alist)
		print(alist)

if __name__ == '__main__':

	# shellSort = ShellSort()
	# print("shellSort.shellSortTest():\n",  shellSort.shellSortTest() )
	pass


def shellSort(alist):
	gap = len(alist) // 2
	while gap < 1 :
		for i in range(gap, len(alist)):
			j = i
			while j < len(alist):
				if alist[j] < alist[j - gap]:
					alist[j], alist[j - gap] = alist[j - gap], alist[j]
					j = j +gap
		gap = gap//2
	return  alist

def shellSort20200323(alist):
	n = len((alist))
	j = 0
	gap = n//2

	while gap > 0:
		for i in range(gap, n):
			j = i
			# 插入排序
			while j >= gap and alist[j - gap] > alist[j]:
				alist[j - gap], alist[j] = alist[j], alist[j - gap]
				j -= gap
		gap //=2
	return alist



alist = [54,26,93,17,77,31,44,55,20]
shellSort(alist)
print("alist:\n", alist)
print("shellSort(alist):\n",shellSort(alist) )

print("shellSort20200323(alist)):\n", shellSort20200323(alist))