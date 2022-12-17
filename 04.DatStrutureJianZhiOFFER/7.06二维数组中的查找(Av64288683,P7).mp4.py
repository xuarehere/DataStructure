# -*- coding:utf-8 -*-
'''
7.06二维数组中的查找(Av64288683,P7).mp4


**在一个二维数组中（每个一维数组的长度相同），每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。**

加快搜索的话，考虑采用二分法搜索算法，加快速度

'''




# array 二维列表
def Find( target, array):
	# write code here
	row = len(array)
	line = len(array[0])
	print(row, line)

	for i in range(row - 1, 0, -1):
		j = line - 1
		if target > array[i - 1][0] and target <= array[i][j]:
			while j >= 0:
				if target == array[i][j]:
					return True
				else:
					j -= 1

	j = line - 1
	i = 0
	while j >= 0:
		if target == array[i][j]:
			return True
		else:
			j -= 1
	return False

# 用例:
# 7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]
print( Find(7,[
	[1,2,8,9],
	[2,4,9,12],[4,7,10,13],[6,8,11,15]]))


