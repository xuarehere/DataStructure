#!/usr/bin/env python
# -*- coding:utf-8 -*-
# ------------------------------------------------------------
# 参考资料：
#
#
# ------------------------------------------------------------
# ******************** 中文名称 *******************
# ******************** 中文名称 *******************
# 如：
# ******************** chapter3 科学计算库Numpy *******************

# =====>>>>>>内容概览
# =====>>>>>>内容概览
# 课程英文名称
# 如：
# chapter3_numpy

'''

# 目录结构

'''

# ------------------------------------------------分割线-------------------------------------------------
# ------------------------------------------------分割线-------------------------------------------------
# ------------------------------------------------分割线-------------------------------------------------
'''
# # ------------------------------------------------------------
# # # 1、语法错误，SyntaxError --变量
# # # #
# # ------------------------------------------------------------
'''

def selectionSort(alist):
	maxValue = alist[0]
	for i in range(0, len(alist)):
		maxValue = i
		for j in range(i+1, len(alist)):
			if alist[maxValue] < alist[j]:
				maxValue = j
		if i!= maxValue:
			alist[i], alist[maxValue] = alist[maxValue], alist[i]

alist = [54,226,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)




def selectionSort1(alist):
		# maxValue =0
		for i in range(0, len(alist)-1):
			maxIndex = i
			for j in range(i+1, len(alist)):
				if alist[maxValue] < alist[j]:
					maxValue = j
			if maxIndex != i :
				alist[i], alist[maxIndex] = alist[maxIndex], alist[i]
		return  alist


alist = [54,226,93,17,77,31,44,55,20]
selectionSort(alist)
print(alist)


def selectionSort(alist):
    if not alist:
        return None

    l  = len(alist)

    for j in  range(l):
        minIndex = j
        for i in range(j +1, l):
            if alist[minIndex] > alist[i]:
                minIndex =i
        if minIndex != j :
            alist[j], alist[minIndex] = alist[minIndex], alist[j]

    return alist

print(1111111)
alist = [54, 226, 93, 17, 77, 31, 44, 55, 20]
print(alist)
selectionSort(alist)
print(alist)
print(1111111)


def quick_sort(alist, start, end):
    """快速排序"""

    # 递归的退出条件
    if start >= end:
        return

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[start]

    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则 high 向左移动
        while low < high and alist[high] >= mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]

    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)

    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)


alist = [54,26,93,17,77,31,44,55,20]
quick_sort(alist,0,len(alist)-1)
print(alist)




