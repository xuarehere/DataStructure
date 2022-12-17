# # -*- coding:utf-8 -*-
# '''
# 最后的中间值替换，即边界值需要花点时间分析一下
#
# '''
#
# #
# # def quickSort(alist):
# #
# #
# # 	low = 0
# # 	# mid = 0
# # 	midValue = alist[0]
# # 	high = len(alist) -1
# #
# # 	while low < high:
# # 		# while low < high:
# # 		while  midValue <= alist[high]:
# # 			high -=1
# # 		alist[low] = alist[high]
# #
# #
# # 		while alist[low] < midValue:
# # 			low += 1
# # 		alist[high] = alist[low]
# # 	# print(low,high)
# # 	alist[low] = midValue
# #
# # 	return alist
# #
# #
# # # [20, 26, 44, 17, 31, 77, 54, 55, 93]
# # alist = [54,26,93,17,77,31,44,55,20]
# # # quickSort(alist,0,len(alist)-1)
# # alist =quickSort(alist)
# #
# # print(alist)
# #
# #
#
#
#
# def quickSort(alist, start, end):
# 	if start >= end:
# 		return  alist
# 	low = start
# 	high = end
# 	midValue = alist[low]
# 	while low < high:
# 		while low < high and midValue <= alist[high]:
# 			high -=1
# 		alist[low] = alist[high]
#
# 		while low < high and  alist[low] < midValue:
# 			low +=1
# 		alist[high] = alist[low]
#
# 	alist[low] = midValue
# 	alist = quickSort(alist,start, low-1)               # 这里，stat 与 end 如果分别为0， len（alist） 就错误
# 	alist = quickSort(alist, low+1, end)
# 	return alist
#
#
#
#
#
# # [20, 26, 44, 17, 31, 77, 54, 55, 93]
# alist = [54,26,93,17,77,31,44,55,20]
# print(alist)
#
# alist = quickSort(alist,0,len(alist)-1)
# # alist =quickSort(alist)
#
# print(alist)




def quickSort1(alist, start, end ):
	# # print('===>')
	# if not alist:
	# 	return None
	# elif start >= end:
	if start >= end:
		return alist

	lIndex = start
	rIndex = end
	# rIndex = len(alist) -1
	midValue = alist[lIndex]

	while lIndex < rIndex:
		while lIndex < rIndex and  midValue <= alist[rIndex]:
			rIndex -=1
		alist[lIndex] = alist[rIndex]

		while  lIndex < rIndex and  alist[lIndex] <  midValue:
			lIndex +=1
		alist[rIndex] = alist[lIndex]

	alist[lIndex] = midValue
	# quickSort(alist,0, len(  alist[lIndex]) -1)
	alist = quickSort1( alist, start,    lIndex - 1 )
	alist = quickSort1( alist, lIndex+1, end        )

	return alist


# [20, 26, 44, 17, 31, 77, 54, 55, 93]
alist = [54,26,93,17,77,31,44,55,20]
print('-'.center(40, '-'))
print(alist)
alist = quickSort1(alist,0,len(alist)-1)
# alist =quickSort(alist)

print(alist)