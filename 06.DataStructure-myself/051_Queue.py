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
# '''
# # # ------------------------------------------------------------
# # # # 1,2、队列
# # # # # Queue() 创建一个空的队列
# # # # # is_empty() 判断一个队列是否为空
# # # ------------------------------------------------------------
# '''
#
# # Queue() 创建一个空的队列
# # enqueue(item) 往队列中添加一个item元素
# # dequeue() 从队列头部删除一个元素
# # is_empty() 判断一个队列是否为空
# # size() 返回队列的大小
#
# class Queue():
#     def __init__(self):
#         self.item = []
#
#     def is_empty(self):
#         return self.item ==[]
#
# def test_Is_empty():
#     queue = Queue()
#     print(queue.is_empty())
#
# if __name__ == "__main__":
#     test_Is_empty()

















'''
# # ------------------------------------------------------------
# # # 3、队列
# # # # Queue()             创建一个空的队列 
# # # # enqueue(item)       往队列中添加一个item元素
# # # # is_empty()          判断一个队列是否为空
# # ------------------------------------------------------------
'''
#
# # Queue() 创建一个空的队列
# # enqueue(item) 往队列中添加一个item元素
# # dequeue() 从队列头部删除一个元素
# # is_empty() 判断一个队列是否为空
# # size() 返回队列的大小
#
# class Queue():
#     def __init__(self):
#         self.item = []  # self.item[0] 是关部，  self.item[ len(self.item)-1]是尾部
#     def enqueue(self, item):
#         """
#          往队列中添加一个item元素
#         :param item:
#         :return:
#         """
#         self.item.append(item)
#
#
#     def is_empty(self):
#         return self.item ==[]
#
# def test_Is_empty():
#     queue = Queue()
#     print(queue.is_empty())
#
# def test_Enqueue():
#     queue = Queue()
#     print(queue.is_empty())
#     queue.enqueue(0)
#     print(queue.is_empty())
#     queue.enqueue(1)
#     queue.enqueue(2)
#     print(queue.is_empty())
#     return queue
#
# if __name__ == "__main__":
#     # test_Is_empty()
#     test_Enqueue()










'''
# # ------------------------------------------------------------
# # # 4、队列
# # # # Queue()             创建一个空的队列 
# # # # enqueue(item)       往队列中添加一个item元素
# # # # dequeue()           从队列头部删除一个元素
# # # # is_empty()          判断一个队列是否为空
# # ------------------------------------------------------------
'''
#
# # Queue() 创建一个空的队列
# # enqueue(item) 往队列中添加一个item元素
# # dequeue() 从队列头部删除一个元素
# # is_empty() 判断一个队列是否为空
# # size() 返回队列的大小
#
# class Queue():
#     def __init__(self):
#         self.item = []  # self.item[0] 是关部，  self.item[ len(self.item)-1]是尾部
#     def enqueue(self, item):
#         """
#          往队列中添加一个item元素
#         :param item:
#         :return:
#         """
#         self.item.append(item)
#
#     def dequeue(self):
#         """
#          从队列头部删除一个元素
#         :return:
#         """
#         try:
#             return self.item.pop(0)
#         except:
#             return None
#
#     def is_empty(self):
#         return self.item ==[]
#
# def test_Is_empty():
#     queue = Queue()
#     print(queue.is_empty())
#
# def test_Enqueue():
#     queue = Queue()
#     print(queue.is_empty())
#     queue.enqueue(0)
#     print(queue.is_empty())
#     queue.enqueue(1)
#     queue.enqueue(2)
#     print(queue.is_empty())
#     return queue
#
# def test_Dequeue():
#     queue = test_Enqueue()
#     print(queue.dequeue())
#
#     print(queue.dequeue())
#     print(queue.dequeue())
#     print(queue.dequeue())
#
# if __name__ == "__main__":
#     # test_Is_empty()
#     # test_Enqueue()
#     test_Dequeue()




















'''
# # ------------------------------------------------------------
# # # 5、队列
# # # # Queue()             创建一个空的队列 
# # # # enqueue(item)       往队列中添加一个item元素
# # # # dequeue()           从队列头部删除一个元素
# # # # is_empty()          判断一个队列是否为空
# # # # size()              返回队列的大小
# # ------------------------------------------------------------
'''

# Queue() 创建一个空的队列
# enqueue(item) 往队列中添加一个item元素
# dequeue() 从队列头部删除一个元素
# is_empty() 判断一个队列是否为空
# size() 返回队列的大小

class Queue():
    def __init__(self):
        self.item = []  # self.item[0] 是关部，  self.item[ len(self.item)-1]是尾部
    def enqueue(self, item):
        """
         往队列中添加一个item元素
        :param item:
        :return:
        """
        self.item.append(item)

    def dequeue(self):
        """
         从队列头部删除一个元素
        :return:
        """
        try:
            return self.item.pop(0)
        except:
            return None

    def is_empty(self):
        return self.item ==[]

    def size(self):
        """
        返回队列的大小
        :return:
        """
        return len(self.item)

def test_Is_empty():
    queue = Queue()
    print(queue.is_empty())

def test_Enqueue():
    queue = Queue()
    print(queue.is_empty())
    queue.enqueue(0)
    print(queue.is_empty())
    queue.enqueue(1)
    queue.enqueue(2)
    print(queue.is_empty())
    return queue

def test_Dequeue():
    queue = test_Enqueue()
    print(queue.dequeue())

    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())

def test_Size():
    queue = test_Enqueue()
    print(queue.size())

if __name__ == "__main__":
    # test_Is_empty()
    # test_Enqueue()
    # test_Dequeue()
    test_Size()