# -*- coding:utf-8 -*-



def inserSort(alist):
	for i in range(1,len(alist)):
		for j in range(i,0,-1 ):
			if alist[j-1]> alist[j] :
				alist[j-1], alist[j] = alist[j], alist[j-1]
	return alist


'''
优化1
'''

def inserSort20200320(alist):
	for j in range(1, len(alist)):
		for i in range(j,0,-1):
			if alist[i] < alist[i -1]:
				alist[i] , alist[i - 1] = alist[i], alist[i ]
			else:
				break
	return  alist
alist = [54,26,93,17,77,31,44,55,20]
inserSort(alist)
print(alist)

print(inserSort20200320(alist))















'''
另外一种解法
'''



def insertSort(alist):
	if not alist:
		return None
	retList = []

	for ele in alist:
		if retList == []:
			retList.append(ele)
		if ele>= retList[-1]:
			retList.append(ele)
		else:
			retL = len(retList) -1
			while ele < retList[retL]:
				retL -=1
				if retL <0:
					break
			retList.insert(retL+1, ele)

	print( ">>",retList)
	return  retList

alist = [54,26,93,17,77,31,44,55,20]
print("===",alist)
alist = insertSort(alist)
print(alist)




def insertSort(alist):
	if not alist:
		return  None

	l = len(alist)

	for i in range(1, l):
		for j in range(i,0, -1):
			if alist[j] < alist[j-1]:
				alist[j], alist[j - 1]= alist[j-1], alist[j]
	# print("==>")
	print( alist)
	return alist


alist = [54,26,93,17,77,31,44,55,20]
print("===",alist)
alist = insertSort(alist)
print(alist)



