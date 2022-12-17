# -*- coding:utf-8 -*-

class MergeSort:
	'''
	def mergeSort(self, alist):
		# split a list
		# def splitList(alist):
		if len(alist) <=1:
			return alist
		n = len(alist) //2
		left = self.mergeSort(alist[:n])
		right = self.mergeSort(alist[n:])

		# merge a list and sort
		lIndex, rIndex = 0, 0
		retList = []
		while lIndex < len(left) and rIndex < len(right):
			if left[lIndex] < right[rIndex]:
				retList.append(left[lIndex])
				lIndex +=1
			else:
				retList.append(right[rIndex])
				rIndex +=1
		print('-'.center(60,'-'))
		print("After while, retList:", retList)
		retList += left[lIndex:]
		retList += right[rIndex:]
		print("retList:", retList)

		return retList
	'''
	def mergeSort1(self, alist):
		# split a list
		# def splitList(alist):
		if len(alist) <=1:
			return alist
		n = len(alist) //2
		left = self.mergeSort1(alist[:n])
		right = self.mergeSort1(alist[n:])

		def mergeList(left, right):
			# merge a list and sort
			lIndex, rIndex = 0, 0
			retList = []
			while lIndex < len(left) and rIndex < len(right):
				if left[lIndex] < right[rIndex]:
					retList.append(left[lIndex])
					lIndex +=1
				else:
					retList.append(right[rIndex])
					rIndex +=1
			print('-'.center(60,'-'))
			print("After while, retList:", retList)
			retList += left[lIndex:]
			retList += right[rIndex:]
			print("retList:", retList)

			return retList

		retList = mergeList(left, right)
		# return  mergeList(left, right)

		return retList


	def test(self):
		# alist = [54,26,93,17,77,31,44,55,20]
		alist = [6, 5, 3, 1, 8, 7, 2 ,4]
		sorted_alist = self.mergeSort1(alist)
		print("sorted_alist", sorted_alist)


if __name__ == '__main__':
    test = MergeSort()
    test.test()


    pass

