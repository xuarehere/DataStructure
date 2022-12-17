# -*- coding:utf-8 -*-



# 20200226

'''
# # ------------------------------------------------------------
# # # 1、冒泡排序
# # # #
# # ------------------------------------------------------------
'''
# class BubbleSort():
# 	import  time
# 	def bubbleSort(alist):
# 		# lenList = len(alist)
# 		for j in range(0, len(alist)-1):
# 			for i in range(1, len(alist)):
# 				if alist[i] < alist[i-1]:
# 					alist[i], alist[i-1] = alist[i-1], alist[i]
# 		return  alist
#
# 	#
# 	# def countTime(func):
# 	# 	import time
# 	# 	startTime = time.time()
# 	# 	ret = func()
# 	# 	endTime = time.time()
# 	# 	print(ret, endTime - startTime)
# 	#
#
# 	alist = [54,226,93,17,77,31,44,55,20]
#
# 	startTime = time.time()
# 	bubbleSort(alist)
# 	endTime = time.time()
# 	print(alist, endTime - startTime)
#
#
# 	def bubbleSort1(alist):
# 		# lenList = len(alist)
# 		for j in range(0, len(alist)-1):
# 			count = 0
# 			for i in range(1, len(alist)-j):
# 				if alist[i] < alist[i-1]:
# 					alist[i], alist[i-1] = alist[i-1], alist[i]
# 					count +=1
# 			if count == 0:
# 				break
# 		return  alist
#
# 	alist = [54,226,93,17,77,31,44,55,20]
# 	startTime = time.time()
#
# 	bubbleSort1(alist)
# 	endTime = time.time()
# 	print(alist)
# 	print(alist, endTime - startTime)
#
#
# 	def bubbleSort2(alist):
# 		for i in  range(0, len(alist)-1):
# 			for j in range(i, len(alist)-1):
# 				if alist[j] > alist[j+1]:
# 					alist[j], alist[j+1] = alist[j+1], alist[j]
#

'''
# # ------------------------------------------------------------
# # # 2、希尔排序
# # # #
# # ------------------------------------------------------------
'''
# class ShellSort():
# 	def shellSort(self, alist):
# 		n = len(alist)
# 		# 初始步长
# 		gap = int(n / 2)
# 		print(gap, type(gap), type(n))
# 		print(type(gap)==type(n))
# 		while gap > 0:
# 			# 按步长进行插入排序
# 			for i in range(gap, n):
# 				j = i
# 				# 插入排序
# 				while j >= gap and alist[j - gap] > alist[j]:
# 					alist[j - gap], alist[j] = alist[j], alist[j - gap]
# 					j -= gap
# 			# 得到新的步长
# 			gap = gap / 2
#
# 	def shellSortTest(self):
# 		alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
# 		self.shellSort(alist)
# 		print(alist)
#
# shellSort = ShellSort()
# shellSort.shellSortTest()




'''
# # ------------------------------------------------------------
# # # 3、栈
# # # #
2020 0302

Stack() 创建一个新的空栈
push(item) 添加一个新的元素item到栈顶
pop() 弹出栈顶元素
peek() 返回栈顶元素
is_empty() 判断栈是否为空
size() 返回栈的元素个数
# # ------------------------------------------------------------
'''
#
# class Stack():
# 	def __init__(self):
# 		self.stack = []
#
# 	def push(self,item):
# 		self.stack.append(item)
#
# 	def pop(self):
# 		if self.size() < 1 :
# 			 return None
# 		return self.stack.pop()
#
# 	def peek(self):
# 		if self.size() < 1:
# 			return None
# 		return self.stack[-1]
#
# 	def is_empty(self):
# 		if self.stack == []:
# 			return True
# 		return False
#
# 	def size(self):
# 		return len(self.stack)
#
# if __name__ == "__main__":
#     stack = Stack()
#     stack.push("hello")
#     stack.push("world")
#     stack.push("itcast")
#     print (stack.size())
#     print( stack.peek())
#     print( stack.pop())
#     print (stack.pop())
#     print (stack.pop())



'''
# # ------------------------------------------------------------
# # # 4、队列
# # # #
2020 0302

Queue() 创建一个空的队列
enqueue(item) 往队列中添加一个item元素
dequeue() 从队列头部删除一个元素
is_empty() 判断一个队列是否为空
size() 返回队列的大小
# # ------------------------------------------------------------
'''


class Queue():
    # 创建一个空的队列
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # 往队列中添加一个item元素
        self.queue.append(item)

    def dequeue(self):
        # 从队列头部删除一个元素
        return self.queue.pop(0)

    def is_empty(self):

        # 判断一个队列是否为空
        return self.queue == []

    def size(self):
        # 返回队列的大小
        return len(self.queue)


class Sort():
    def quickSort(self, alist, start, end):
        if start >= end:
            return

        low = start
        high = end
        midValue = alist[low]

        while low < high:
            while low < high and  (midValue <= alist[high]):
                high -=1
            alist[low] = alist[high]

            while low < high and (midValue > alist[low]):
                low += 1
            alist[high] = alist[low]

        alist[low] = midValue
        self.quickSort(alist, start, low-1)
        self.quickSort(alist, low+1, end)
        return alist

    def selectionSort(self,alist):
        if not alist :
            return []
        l = len(alist)

        for j in  range(l-1):
            minIndex = j
            for i in range (j+1, l):
                if alist [ minIndex] > alist[i]:
                    minIndex = i
            if minIndex !=j:
                alist[j], alist[minIndex] = alist[minIndex], alist[j]
        return alist

    def selectionSort0320(self, alist):
        if not alist:
            return None
        for j in  range(0, len(alist)):
            minIndex = j
            for i in range(j+1, len(alist)):
                if alist[minIndex ]> alist[i]:
                    minIndex = i
            if minIndex != j :
                alist[j] = alist[minIndex]
        return  alist


if __name__ == "__main__":
    q = Queue()
    # q.enqueue("hello")
    # q.enqueue("world")
    # q.enqueue("itcast")
    # print( q.size())
    # print( q.dequeue())
    # print( q.dequeue())
    # print( q.dequeue())

    s = Sort()
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]

    # print(  s.quickSort(alist, 0, len(alist)-1))
    print(s.selectionSort(alist))
    print( s.selectionSort0320(alist) )