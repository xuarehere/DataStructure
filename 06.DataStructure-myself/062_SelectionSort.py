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
# # # 1、思想
# # # # 前面有序，后面无序
# # ------------------------------------------------------------
'''
#
# def selection_sort(list):
#     n = len(list)
#     for j in range(n-1):
#         # min value
#         #     min = list[j]
#         count = 0       # checking if the list is order
#         for i in range(j, n):  # 0 __ n-2
#             if( list[j] > list[i] ):
#                 list[j], list[i] = list[i], list[j]
#                 count = 0
#             else:
#                 count += 1
#                 # print(count)
#                 # continue
#         # new_list.append(min)
#         if count >= (n-j):
#             # no charge
#             break       # sort finished
#
#     return list
#     # pass
#
# # alist = [54,226,93,17,77,31,44,55,20]
# # print(alist)
# #
# # print( selection_sort(alist) )
#
# alist1 = [54,226,93,17,77,313,44,55,11]
# alist2 = [11, 17, 44, 54, 55, 77, 93, 226, 313]
# print(selection_sort(alist2 ))
#
#
#







def selection_sort(alist):
    n = len(alist)
    for j in range(n-1):
        min_index = j
        for i in range(j+1, n):
           if alist[min_index] > alist[i]:
               min_index = i
        if j is not min_index:
            alist[min_index], alist[j] = alist[j], alist[min_index]

    return alist
    # pass

# alist = [54,226,93,17,77,31,44,55,20]
# print(alist)
#
# print( selection_sort(alist) )

alist1 = [54,226,93,17,77,313,44,55,11]
alist2 = [11, 17, 44, 54, 55, 77, 93, 226, 313]
print(selection_sort(alist1))
# print(selection_sort(alist2 ))



