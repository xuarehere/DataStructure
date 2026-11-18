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
# # # 1、双向链表
# # # #
# # ------------------------------------------------------------
'''
# class Node(object):
#     """双向链表节点"""
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#         self.prev = None
#
# class DLinkList(object):
#     def __init__(self):
#         self._head = None
#
#         # is_empty()
#         # # 链表是否为空
#         # length()
#         # # 链表长度
#         # travel()
#         # # 遍历链表
#         # add(item)
#         # # 链表头部添加
#         # append(item)
#         # # 链表尾部添加
#         # insert(pos, item)
#         # # 指定位置添加
#         # remove(item)
#         # # 删除节点
#         # search(item)
#         # # 查找节点是否存在
#





'''
# # ------------------------------------------------------------
# # # 1、双向链表
# # # # is_empty        链表是否为空
# # ------------------------------------------------------------
'''
# class Node(object):
#     """双向链表节点"""
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#         self.prev = None
#
# class DLinkList(object):
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         '''
#         # 链表是否为空
#         :return:
#         '''
#         return self._head is None
#
#         # length()
#         # # 链表长度
#         # travel()
#         # # 遍历链表
#         # add(item)
#         # # 链表头部添加
#         # append(item)
#         # # 链表尾部添加
#         # insert(pos, item)
#         # # 指定位置添加
#         # remove(item)
#         # # 删除节点
#         # search(item)
#         # # 查找节点是否存在


'''
# # ------------------------------------------------------------
# # # 1、双向链表
# # # # is_empty        链表是否为空
# # # # add             链表头部添加
# # ------------------------------------------------------------
'''
#
#
# class Node(object):
#     """双向链表节点"""
#
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#         self.prev = None
#
#
# class DLinkList(object):
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         '''
#         # 链表是否为空
#         :return:
#         '''
#         return self._head is None
#
#
#         # length()
#         # # 链表长度
#         # travel()
#         # # 遍历链表
#     def add(self, item):
#         '''
#         # 链表头部添加
#         :param item:
#         :return:
#         '''
#         node = Node(item)
#         if self.is_empty():
#             self._head = node
#             node.prev = self._head
#             node.next = None
#         else:
#             node.next = self._head
#             self._head.prev = node
#
#             self._head = node
#             node.prev = self._head
#         # append(item)
#         # # 链表尾部添加
#         # insert(pos, item)
#         # # 指定位置添加
#         # remove(item)
#         # # 删除节点
#         # search(item)
#         # # 查找节点是否存在
#
# def test_Is_empty_Add():
#     print("the function is to test the funtion of is_empyt and add")
#     dlink = DLinkList()
#     print( dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#
# if __name__ =="__main__":
#     # pass
#     test_Is_empty_Add()


'''
# # ------------------------------------------------------------
# # # 3、双向链表
# # # # is_empty        链表是否为空
# # # # add             链表头部添加
# # # # travel          遍历链表
# # ------------------------------------------------------------
'''
#
#
# class Node(object):
#     """双向链表节点"""
#
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#         self.prev = None
#
#
# class DLinkList(object):
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         '''
#         # 链表是否为空
#         :return:
#         '''
#         return self._head is None
#
#         # length()
#         # # 链表长度
#     def travel(self):
#         """
#         # # 遍历链表
#         :return:
#         """
#         cur = self._head
#         while cur is not None:
#             print(cur.item, end=" ")
#             cur = cur.next
#
#     def add(self, item):
#         '''
#         # 链表头部添加
#         :param item:
#         :return:
#         '''
#         node = Node(item)
#         if self.is_empty():
#             self._head = node
#             node.prev = self._head
#             node.next = None
#         else:
#             node.next = self._head
#             self._head.prev = node
#
#             self._head = node
#             node.prev = self._head
#         # append(item)
#         # # 链表尾部添加
#         # insert(pos, item)
#         # # 指定位置添加
#         # remove(item)
#         # # 删除节点
#         # search(item)
#         # # 查找节点是否存在
#
#
# def test_Is_empty_Add():
#     print("the function is to test the funtion of is_empyt and add")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
# def test_Travel():
#     print("the function is to test the funtion of travel()")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#
# if __name__ == "__main__":
#     # pass
#     # test_Is_empty_Add()
#     test_Travel()





















'''
# # ------------------------------------------------------------
# # # 4、双向链表
# # # # is_empty        链表是否为空
# # # # length          链表长度
# # # # add             链表头部添加
# # # # travel          遍历链表
# # ------------------------------------------------------------
'''


# class Node(object):
#     """双向链表节点"""
#
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#         self.prev = None
#
#
# class DLinkList(object):
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         '''
#         # 链表是否为空
#         :return:
#         '''
#         return self._head is None
#
#     def length(self):
#         '''
#         # # 链表长度
#         :return:
#         '''
#         count = 0
#         cur = self._head
#         while cur is not None:
#             count +=1
#             cur = cur.next
#         return count
#
#
#     def travel(self):
#         """
#         # # 遍历链表
#         :return:
#         """
#         cur = self._head
#         while cur is not None:
#             print(cur.item, end=" ")
#             cur = cur.next
#
#     def add(self, item):
#         '''
#         # 链表头部添加
#         :param item:
#         :return:
#         '''
#         node = Node(item)
#         if self.is_empty():
#             #             # 如果是空链表，将_head指向node
#             self._head = node
#             # node.prev = self._head
#             node.next = None
#         else:
#             # 非空
#             node.next = self._head
#             # 将_head的头节点的prev指向node
#             self._head.prev = node
#
#             self._head = node
#
#     # append(item)
#     # # 链表尾部添加
#     # insert(pos, item)
#     # # 指定位置添加
#     # remove(item)
#     # # 删除节点
#     # search(item)
#     # # 查找节点是否存在
#
#
# def test_Is_empty_Add():
#     print("the function is to test the funtion of is_empyt and add")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
# def test_Travel():
#     print("the function is to test the funtion of travel()")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#
# def test_Length():
#     print("the function is to test the funtion of is_empyt and add")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#     print("length:", dlink.length())
#
# if __name__ == "__main__":
#     # pass
#     # test_Is_empty_Add()
#     # test_Travel()
#     test_Length()














'''
# # ------------------------------------------------------------
# # # 5、双向链表
# # # # is_empty        链表是否为空
# # # # length          链表长度
# # # # add             链表头部添加
# # # # travel          遍历链表
# # # # append          链表尾部添加
# # ------------------------------------------------------------
'''
#
#
# class Node(object):
#     """双向链表节点"""
#
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#         self.prev = None
#
#
# class DLinkList(object):
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         '''
#         # 链表是否为空
#         :return:
#         '''
#         return self._head is None
#
#     def length(self):
#         '''
#         # # 链表长度
#         :return:
#         '''
#         count = 0
#         cur = self._head
#         while cur is not None:
#             count +=1
#             cur = cur.next
#         return count
#
#
#     def travel(self):
#         """
#         # # 遍历链表
#         :return:
#         """
#         cur = self._head
#         while cur is not None:
#             print(cur.item, end=" ")
#             cur = cur.next
#
#     def add(self, item):
#         '''
#         # 链表头部添加
#         :param item:
#         :return:
#         '''
#         node = Node(item)
#         if self.is_empty():
#             #             # 如果是空链表，将_head指向node
#             self._head = node
#             # node.prev = self._head
#             node.next = None
#         else:
#             # 非空
#             node.next = self._head
#             # 将_head的头节点的prev指向node
#             self._head.prev = node
#
#             self._head = node
#
#     def append(self, item):
#         """
#         链表尾部添加
#         :param item:
#         :return:
#         """
#         node = Node(item)
#         if self.is_empty():
#             # 如果是空链表，将_head指向node
#             self._head = node
#         else:
#             # 移动到链表尾部
#             cur = self._head
#
#             while cur.next is not None:
#                 cur = cur.next
#             # 将尾节点cur的next指向node
#             node.prev = cur
#             # 将node的prev指向cur
#             cur.next = node
#
#
#
#     # insert(pos, item)
#     # # 指定位置添加
#     # remove(item)
#     # # 删除节点
#     # search(item)
#     # # 查找节点是否存在
#
#
# def test_Is_empty_Add():
#     print("the function is to test the funtion of is_empyt and add")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
# def test_Travel():
#     print("the function is to test the funtion of travel()")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#
# def test_Length():
#     print("the function is to test the funtion of is_empyt and add")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#     print("length:", dlink.length())
#
# def test_Append():
#     print("the function is to test the funtion of append()")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.append(0)
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#     print("length:", dlink.length())
#
#     dlink.append(5)
#     dlink.travel()
#     print("length:", dlink.length())
#
# if __name__ == "__main__":
#     # pass
#     # test_Is_empty_Add()
#     # test_Travel()
#     # test_Length()
#     test_Append()




















'''
# # ------------------------------------------------------------
# # # 6、双向链表
# # # # is_empty        链表是否为空
# # # # length          链表长度
# # # # add             链表头部添加
# # # # travel          遍历链表
# # # # append          链表尾部添加
# # # # insert          指定位置添加
# # ------------------------------------------------------------
'''
#
#
# class Node(object):
#     """双向链表节点"""
#
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#         self.prev = None
#
#
# class DLinkList(object):
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         '''
#         # 链表是否为空
#         :return:
#         '''
#         return self._head is None
#
#     def length(self):
#         '''
#         # # 链表长度
#         :return:
#         '''
#         count = 0
#         cur = self._head
#         while cur is not None:
#             count +=1
#             cur = cur.next
#         return count
#
#
#     def travel(self):
#         """
#         # # 遍历链表
#         :return:
#         """
#         cur = self._head
#         while cur is not None:
#             print(cur.item, end=" ")
#             cur = cur.next
#
#     def add(self, item):
#         '''
#         # 链表头部添加
#         :param item:
#         :return:
#         '''
#         node = Node(item)
#         if self.is_empty():
#             #             # 如果是空链表，将_head指向node
#             self._head = node
#             # node.prev = self._head
#             node.next = None
#         else:
#             # 非空
#             node.next = self._head
#             # 将_head的头节点的prev指向node
#             self._head.prev = node
#
#             self._head = node
#
#     def append(self, item):
#         """
#         链表尾部添加
#         :param item:
#         :return:
#         """
#         node = Node(item)
#         if self.is_empty():
#             # 如果是空链表，将_head指向node
#             self._head = node
#         else:
#             # 移动到链表尾部
#             cur = self._head
#
#             while cur.next is not None:
#                 cur = cur.next
#             # 将尾节点cur的next指向node
#             node.prev = cur
#             # 将node的prev指向cur
#             cur.next = node
#
#
#     def insert(self, pos, item):
#         """
#         指定位置添加
#         :param pos:
#         :param item:
#         :return:
#         """
#         node = Node(item)
#         if self.is_empty() or (pos <= 0):
#             self.add(item)
#         elif pos >= ( self.length()):
#             # 最后的位置
#             self.append(item)
#         else:
#             # 中间的位置
#             cur_pos =0      # 当前的位置
#             cur = self._head
#             # while cur.next is not None:
#             #     cur = cur.next
#             #     cur_pos +=1
#             while cur_pos < (pos-1):
#                 cur_pos +=1
#                 cur = cur.next
#
#             # pos位置的节点
#             node.next = cur.next
#             cur.next.prev = node
#             # pos 上一位置的节点
#             node.prev = cur
#             cur.next = node
#
#     # remove(item)
#     # 删除节点
#     # search(item)
#     # # 查找节点是否存在
#
#
# def test_Is_empty_Add():
#     print("the function is to test the funtion of is_empyt and add")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
# def test_Travel():
#     print("the function is to test the funtion of travel()")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#
# def test_Length():
#     print("the function is to test the funtion of is_empyt and add")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#     print("length:", dlink.length())
#
# def test_Append():
#     print("the function is to test the funtion of append()")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.append(0)
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#     print("length:", dlink.length())
#
#     dlink.append(5)
#     dlink.travel()
#     print("length:", dlink.length())
#
# def test_Insert():
#     print("the function is to test the funtion of append()")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.insert(0, 11)
#     dlink.travel()
#
#     dlink.append(0)
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#     print("length:", dlink.length())
#
#     dlink.append(5)
#     dlink.travel()
#     print("length:", dlink.length())
#
#     dlink.insert(-11, 44)
#     dlink.travel()
#
#     print()
#     dlink.insert(0, 55)
#     dlink.travel()
#
#     print()
#     dlink.insert(2, 99)
#     dlink.travel()
#
#     print()
#     dlink.insert(10, 111)
#     dlink.travel()
#
#
# if __name__ == "__main__":
#     # pass
#     # test_Is_empty_Add()
#     # test_Travel()
#     # test_Length()
#     # test_Append()
#     test_Insert()











'''
# # ------------------------------------------------------------
# # # 7、双向链表
# # # # is_empty        链表是否为空
# # # # length          链表长度
# # # # add             链表头部添加
# # # # travel          遍历链表
# # # # append          链表尾部添加
# # # # insert          指定位置添加
# # # # remove          删除节点
# # ------------------------------------------------------------
'''
#
#
# class Node(object):
#     """双向链表节点"""
#
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#         self.prev = None
#
#
# class DLinkList(object):
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         '''
#         # 链表是否为空
#         :return:
#         '''
#         return self._head is None
#
#     def length(self):
#         '''
#         # # 链表长度
#         :return:
#         '''
#         count = 0
#         cur = self._head
#         while cur is not None:
#             count +=1
#             cur = cur.next
#         return count
#
#
#     def travel(self):
#         """
#         # # 遍历链表
#         :return:
#         """
#         cur = self._head
#         while cur is not None:
#             print(cur.item, end=" ")
#             cur = cur.next
#
#     def add(self, item):
#         '''
#         # 链表头部添加
#         :param item:
#         :return:
#         '''
#         node = Node(item)
#         if self.is_empty():
#             #             # 如果是空链表，将_head指向node
#             self._head = node
#             # node.prev = self._head
#             node.next = None
#         else:
#             # 非空
#             node.next = self._head
#             # 将_head的头节点的prev指向node
#             self._head.prev = node
#
#             self._head = node
#
#     def append(self, item):
#         """
#         链表尾部添加
#         :param item:
#         :return:
#         """
#         node = Node(item)
#         if self.is_empty():
#             # 如果是空链表，将_head指向node
#             self._head = node
#         else:
#             # 移动到链表尾部
#             cur = self._head
#
#             while cur.next is not None:
#                 cur = cur.next
#             # 将尾节点cur的next指向node
#             node.prev = cur
#             # 将node的prev指向cur
#             cur.next = node
#
#
#     def insert(self, pos, item):
#         """
#         指定位置添加
#         :param pos:
#         :param item:
#         :return:
#         """
#         node = Node(item)
#         if self.is_empty() or (pos <= 0):
#             self.add(item)
#         elif pos >= ( self.length()):
#             # 最后的位置
#             self.append(item)
#         else:
#             # 中间的位置
#             cur_pos =0      # 当前的位置
#             cur = self._head
#             # while cur.next is not None:
#             #     cur = cur.next
#             #     cur_pos +=1
#             while cur_pos < (pos-1):
#                 cur_pos +=1
#                 cur = cur.next
#
#             # pos位置的节点
#             node.next = cur.next
#             cur.next.prev = node
#             # pos 上一位置的节点
#             node.prev = cur
#             cur.next = node
#
#     def remove(self, item):
#         """
#         # 删除节点
#         :param item:
#         :return:
#         """
#         cur = self._head
#         pre = None
#         if self.is_empty() or (cur.next is None):
#             # 空链表     或者      只有一个节点链表
#             self._head = None
#             # return
#
#         elif cur.item is item:
#             # 首节点
#             # 将_head指向第二个节点
#             self._head = cur.next
#             # 将第二个节点的prev设置为None
#             cur.next.prev = None
#             # return
#         else:
#             #　非首节点，链表不存在的情况
#             while cur is not None:
#                 if cur.item is item:
#                     pre.next = cur.next
#                     if cur.next is None:
#                         # 最后一个节点
#                         pass
#                     else:
#                         cur.next.prev = pre
#                     break
#                 else:
#                     pre = cur
#                     cur = cur.next
#
#
#
#
#
#     # search(item)
#     # # 查找节点是否存在
#
#
# def test_Is_empty_Add():
#     print("the function is to test the funtion of is_empyt and add")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
# def test_Travel():
#     print("the function is to test the funtion of travel()")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#
# def test_Length():
#     print("the function is to test the funtion of is_empyt and add")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#     print("length:", dlink.length())
#
# def test_Append():
#     print("the function is to test the funtion of append()")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.append(0)
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#     print("length:", dlink.length())
#
#     dlink.append(5)
#     dlink.travel()
#     print("length:", dlink.length())
#
# def test_Insert():
#     print("the function is to test the funtion of append()")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#
#     dlink.insert(0, 11)
#     dlink.travel()
#
#     dlink.append(0)
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#     print("length:", dlink.length())
#
#     dlink.append(5)
#     dlink.travel()
#     print("length:", dlink.length())
#
#     dlink.insert(-11, 44)
#     dlink.travel()
#
#     print()
#     dlink.insert(0, 55)
#     dlink.travel()
#
#     print()
#     dlink.insert(2, 99)
#     dlink.travel()
#
#     print()
#     dlink.insert(10, 111)
#     dlink.travel()
#
# def test_Remove():
#     print("the function is to test the funtion of remove()")
#     dlink = DLinkList()
#     print(dlink.is_empty())
#     dlink.remove(11)
#     print("----------------")
#     dlink.insert(0, 11)
#     dlink.travel()
#     dlink.remove(11)
#
#     dlink.append(0)
#     dlink.add(1)
#     print(dlink.is_empty())
#
#     dlink.add(2)
#     print(dlink.is_empty())
#
#     dlink.add(3)
#     dlink.add(4)
#     dlink.travel()
#     print("length:", dlink.length())
#
#     dlink.append(5)
#     dlink.travel()
#     print("length:", dlink.length())
#
#     dlink.insert(-11, 44)
#     dlink.travel()
#
#     print()
#     dlink.insert(0, 55)
#     dlink.travel()
#
#     print()
#     dlink.insert(2, 99)
#     dlink.travel()
#
#     print()
#     dlink.insert(10, 111)   # 55 44 99 4 3 2 1 0 5
#     dlink.travel()
#     print()
#
#     dlink.remove(55)
#     dlink.travel()
#     print()
#
#
# if __name__ == "__main__":
#     # pass
#     # test_Is_empty_Add()
#     # test_Travel()
#     # test_Length()
#     # test_Append()
#     # test_Insert()
#     test_Remove()




















'''
# # ------------------------------------------------------------
# # # 8、双向链表
# # # # is_empty        链表是否为空
# # # # length          链表长度
# # # # add             链表头部添加
# # # # travel          遍历链表
# # # # append          链表尾部添加
# # # # insert          指定位置添加
# # # # remove          删除节点
# # # # search          查找节点是否存在
# # ------------------------------------------------------------
'''


class Node(object):
    """双向链表节点"""

    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None


class DLinkList(object):
    def __init__(self):
        self._head = None

    def is_empty(self):
        '''
        # 链表是否为空
        :return:
        '''
        return self._head is None

    def length(self):
        '''
        # # 链表长度
        :return:
        '''
        count = 0
        cur = self._head
        while cur is not None:
            count +=1
            cur = cur.next
        return count


    def travel(self):
        """
        # # 遍历链表
        :return:
        """
        cur = self._head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next

    def add(self, item):
        '''
        # 链表头部添加
        :param item:
        :return:
        '''
        node = Node(item)
        if self.is_empty():
            #             # 如果是空链表，将_head指向node
            self._head = node
            # node.prev = self._head
            node.next = None
        else:
            # 非空
            node.next = self._head
            # 将_head的头节点的prev指向node
            self._head.prev = node

            self._head = node

    def append(self, item):
        """
        链表尾部添加
        :param item:
        :return:
        """
        node = Node(item)
        if self.is_empty():
            # 如果是空链表，将_head指向node
            self._head = node
        else:
            # 移动到链表尾部
            cur = self._head

            while cur.next is not None:
                cur = cur.next
            # 将尾节点cur的next指向node
            node.prev = cur
            # 将node的prev指向cur
            cur.next = node


    def insert(self, pos, item):
        """
        指定位置添加
        :param pos:
        :param item:
        :return:
        """
        node = Node(item)
        if self.is_empty() or (pos <= 0):
            self.add(item)
        elif pos >= ( self.length()):
            # 最后的位置
            self.append(item)
        else:
            # 中间的位置
            cur_pos =0      # 当前的位置
            cur = self._head
            # while cur.next is not None:
            #     cur = cur.next
            #     cur_pos +=1
            while cur_pos < (pos-1):
                cur_pos +=1
                cur = cur.next

            # pos位置的节点
            node.next = cur.next
            cur.next.prev = node
            # pos 上一位置的节点
            node.prev = cur
            cur.next = node

    def remove(self, item):
        """
        # 删除节点
        :param item:
        :return:
        """
        cur = self._head
        pre = None
        if self.is_empty() or (cur.next is None):
            # 空链表     或者      只有一个节点链表
            self._head = None
            # return

        elif cur.item is item:
            # 首节点
            # 将_head指向第二个节点
            self._head = cur.next
            # 将第二个节点的prev设置为None
            cur.next.prev = None
            # return
        else:
            #　非首节点，链表不存在的情况
            while cur is not None:
                if cur.item is item:
                    pre.next = cur.next
                    if cur.next is None:
                        # 最后一个节点
                        pass
                    else:
                        cur.next.prev = pre
                    break
                else:
                    pre = cur
                    cur = cur.next





    def search(self, item):
        """
        查找节点是否存在
        :param item:
        :return:
        """
        cur = self._head
        while cur is not None:
            if cur.item is item:
                return True
            else:
                cur = cur.next
        return False

def test_Is_empty_Add():
    print("the function is to test the funtion of is_empyt and add")
    dlink = DLinkList()
    print(dlink.is_empty())

    dlink.add(1)
    print(dlink.is_empty())

    dlink.add(2)
    print(dlink.is_empty())

def test_Travel():
    print("the function is to test the funtion of travel()")
    dlink = DLinkList()
    print(dlink.is_empty())

    dlink.add(1)
    print(dlink.is_empty())

    dlink.add(2)
    print(dlink.is_empty())

    dlink.add(3)
    dlink.add(4)
    dlink.travel()

def test_Length():
    print("the function is to test the funtion of is_empyt and add")
    dlink = DLinkList()
    print(dlink.is_empty())

    dlink.add(1)
    print(dlink.is_empty())

    dlink.add(2)
    print(dlink.is_empty())

    dlink.add(3)
    dlink.add(4)
    dlink.travel()
    print("length:", dlink.length())

def test_Append():
    print("the function is to test the funtion of append()")
    dlink = DLinkList()
    print(dlink.is_empty())

    dlink.append(0)
    dlink.add(1)
    print(dlink.is_empty())

    dlink.add(2)
    print(dlink.is_empty())

    dlink.add(3)
    dlink.add(4)
    dlink.travel()
    print("length:", dlink.length())

    dlink.append(5)
    dlink.travel()
    print("length:", dlink.length())

def test_Insert():
    print("the function is to test the funtion of append()")
    dlink = DLinkList()
    print(dlink.is_empty())

    dlink.insert(0, 11)
    dlink.travel()

    dlink.append(0)
    dlink.add(1)
    print(dlink.is_empty())

    dlink.add(2)
    print(dlink.is_empty())

    dlink.add(3)
    dlink.add(4)
    dlink.travel()
    print("length:", dlink.length())

    dlink.append(5)
    dlink.travel()
    print("length:", dlink.length())

    dlink.insert(-11, 44)
    dlink.travel()

    print()
    dlink.insert(0, 55)
    dlink.travel()

    print()
    dlink.insert(2, 99)
    dlink.travel()

    print()
    dlink.insert(10, 111)
    dlink.travel()

def test_Remove():
    print("the function is to test the funtion of remove()")
    dlink = DLinkList()
    print(dlink.is_empty())
    dlink.remove(11)
    print("----------------")
    dlink.insert(0, 11)
    dlink.travel()
    dlink.remove(11)

    dlink.append(0)
    dlink.add(1)
    print(dlink.is_empty())

    dlink.add(2)
    print(dlink.is_empty())

    dlink.add(3)
    dlink.add(4)
    dlink.travel()
    print("length:", dlink.length())

    dlink.append(5)
    dlink.travel()
    print("length:", dlink.length())

    dlink.insert(-11, 44)
    dlink.travel()

    print()
    dlink.insert(0, 55)
    dlink.travel()

    print()
    dlink.insert(2, 99)
    dlink.travel()

    print()
    dlink.insert(10, 111)   # 55 44 99 4 3 2 1 0 5
    dlink.travel()
    print()

    dlink.remove(55)
    dlink.travel()
    print()

def test_Search():
    print("the function is to test the funtion of search()")
    dlink = DLinkList()
    print("dlink.search(111): ", dlink.search(111))

    dlink.append(0)
    dlink.travel()
    print("dlink.search(9999): ", dlink.search(9999))
    print("dlink.search(0): ", dlink.search(0))
    dlink.add(1)
    dlink.add(2)
    dlink.add(3)
    dlink.add(4)
    dlink.travel()

    print("dlink.search(2): ", dlink.search(2))
    print("dlink.search(4): ", dlink.search(4))
    print("dlink.search(55): ", dlink.search(555))

if __name__ == "__main__":
    # pass
    # test_Is_empty_Add()
    # test_Travel()
    # test_Length()
    # test_Append()
    # test_Insert()
    # test_Remove()
    test_Search()