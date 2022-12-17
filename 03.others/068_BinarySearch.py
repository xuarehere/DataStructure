# -*- coding:utf-8 -*-

#
# def binary_search(alist, item):
# 	if alist ==None:
# 		return None
# 	if len(alist ) > 0 :
# 		midIndex = len(alist) // 2
# 		if alist[midIndex] == item:
# 			return  True
# 		if item < alist[midIndex]:
# 			return  binary_search(alist[:midIndex], item)
# 		else:
# 			return  binary_search(alist[midIndex+1:], item)
# 	return False
#
# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(binary_search(testlist, 3))
# print(binary_search(testlist, 13))
#




#
# def binary_searchNoRe(alist, item):
# 	'''操作数组'''
# 	if alist ==None:
# 		return None
#
# 	while len(alist ) > 0 :
# 		midIndex = len(alist) // 2
# 		if alist[midIndex] == item:
# 			return  True
# 		if item < alist[midIndex]:
# 			alist = alist[:midIndex]
# 			# return  binary_search(alist[:midIndex], item)
# 		else:
# 			alist = alist[midIndex +1:]
# 			# return  binary_search(alist[midIndex+1:], item)
# 	return False
#
# testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
# print(binary_searchNoRe(testlist, 3))
# print(binary_searchNoRe(testlist, 13))




def binary_searchNoRe1(alist, item):
	'''不操作数组'''
	if alist ==None:
		return None
	start = 0
	end   = len(alist )
	while start < end:
		midIndex = (start + end )// 2
		if alist[midIndex] == item:
			return  True
		if item < alist[midIndex]:
			end = midIndex

		else:
			start = midIndex +1
	return False

testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(binary_searchNoRe1(testlist, 3))
print(binary_searchNoRe1(testlist, 13))



