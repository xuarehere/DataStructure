# -*- coding:utf-8 -*-
'''
4.03数组的概念(Av64288683,P4).mp4( 数组中出现次数超过一半的数字)

## 21.数组中出现次数超过一半的数字[^本题考点 数组]

**数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。
由于数字2在数组中出现了 5 次，超过数组长度的一半，因此输出2。如果不存在则输出0。**

用字典





有pop  ， 没有解决
用队列


'''

# pop  有问题


def MoreThanHalfNum_Solution( alist):
	import copy
	n = len(alist)
	# alistTemp = alist
	alistTemp = copy.deepcopy(alist)
	saveList = []
	while alistTemp:
		if saveList == []:
			saveList.append(alistTemp.pop(0))
		elif saveList[0] != alistTemp[0]:
			saveList.pop(0)
			alistTemp.pop(0)
		else:
			saveList.append(alistTemp.pop(0))
	if saveList == []:
		return  0
	else:
		print(saveList)
		count =0
		for ele in alist:
			if  ele == saveList[0]:
				count +=1
				if count > len(alist)//2:
					return ele
		return 0





	return saveList
	# print(saveList)

	print(alist)
alist = [1,2,3,2,2]
# alist = [1,2,3,2,2,2,5,4,2,9,1,27,9,4,5,6,2,2,2]
# alist = [1,2,3,2,2,2,5,4,2]
print(MoreThanHalfNum_Solution(  alist ) )
