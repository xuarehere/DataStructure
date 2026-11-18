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
# # # 1、节点实现
# # # #
# # ------------------------------------------------------------
'''
#
#
# class SingleNode(object):
#     """单链表的结点"""
#     def __init__(self,item):
#         # _item存放数据元素
#         self.item = item
#         # _next是下一个节点的标识
#         self.next = None









# '''
# # # ------------------------------------------------------------
# # # # 2、单向链表
# # # # # is_empty 是否为空
# # # ------------------------------------------------------------
# '''

# class SingleNode(object):
#     """单链表的结点"""
#     def __init__(self,item):
#         # _item存放数据元素
#         self.item = item
#         # _next是下一个节点的标识
#         self.next = None


# class SingleLinkList(object):
#     def __init__(self):
#         self._head = None

#     def is_empty(self):
#         # 链表是否为空
#         return self._head is None

#     def length(self):
#         # 链表长度
#         pass

#     def travel(self):
#         # 遍历整个链表
#         pass

#     def add(item):
#         # 链表头部添加元素
#         pass

#     def append(item):
#         # 链表尾部添加元素
#         pass

#     def insert(pos, item):
#         # 指定位置添加元素
#         pass

#     def remove(item):
#         # 删除节点
#         pass

#     def search(item):
#         # 查找节点是否存在
#         pass

# if __name__ == "__main__":
#     ll = SingleLinkList()
#     print(ll.is_empty())













'''
# # ------------------------------------------------------------
# # # 3、单向链表
# # # # is_empty 是否为空  is_empty
# # ------------------------------------------------------------
'''
#
# class SingleNode(object):
#     """单链表的结点"""
#     def __init__(self,item):
#         # _item存放数据元素
#         self.item = item
#         # _next是下一个节点的标识
#         self.next = None
#
#
# class SingleLinkList(object):
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         # 链表是否为空
#         return self._head is None
#
#     def length(self):
#         # 链表长度
#         pass
#
#     def travel(self):
#         # 遍历整个链表
#         pass
#
#     def add(self, item):
#         # 链表头部添加元素
#         # node = SingleNode(item)
#         # node.next = self._head
#         pass
#
#     def append(self, item):
#         # 链表尾部添加元素
#         node = SingleNode(item)
#         if self._head is None:
#             self._head = node
#             # return
#         else:
#             cur = self._head
#             while True:
#                 if cur.next is None:
#                     cur.next = node
#                     break
#
#
#
#         # pass
#
#     def insert(pos, item):
#         # 指定位置添加元素
#         pass
#
#     def remove(item):
#         # 删除节点
#         pass
#
#     def search(item):
#         # 查找节点是否存在
#         pass
#
# if __name__ == "__main__":
#     ll = SingleLinkList()
#     print(ll.is_empty())
#
#     ll.append(1)
#     print(ll.is_empty())
#
#     ll.append(2)
#     print(ll.is_empty())























'''
# # ------------------------------------------------------------
# # # 3、单向链表
# # # # is_empty 是否为空
# # # # append   添加元素
# # # # travel   遍历元素
# # ------------------------------------------------------------
'''
#
# class SingleNode(object):
#     """单链表的结点"""
#     def __init__(self,item):
#         # _item存放数据元素
#         self.item = item
#         # _next是下一个节点的标识
#         self.next = None
#
#
# class SingleLinkList(object):
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         # 链表是否为空
#         return self._head is None
#
#     def length(self):
#         # 链表长度
#         pass
#
#     def travel(self):
#         # 遍历整个链表
#         # if self._head is None:
#         #    return
#         # else:
#         #     cur = self._head
#         #     while cur is not None:
#         #         print(cur.item)
#         #         cur = cur.next
#         cur = self._head
#         while cur is not None:
#             print(cur.item)
#             cur = cur.next
#         # pass
#
#     def add(self, item):
#         # 链表头部添加元素
#         # node = SingleNode(item)
#         # node.next = self._head
#         pass
#
#     def append(self, item):
#         # 链表尾部添加元素
#         node = SingleNode(item)
#         if self._head is None:
#             self._head = node
#             # return
#         else:
#             cur = self._head
#             while True:
#                 if cur.next is None:
#                     cur.next = node
#                     break
#
#
#
#         # pass
#
#     def insert(pos, item):
#         # 指定位置添加元素
#         pass
#
#     def remove(item):
#         # 删除节点
#         pass
#
#     def search(item):
#         # 查找节点是否存在
#         pass
#
# if __name__ == "__main__":
#     ll = SingleLinkList()
#     ll.travel()
#     print("===================")
#     print(ll.is_empty())
#
#     ll.append(1)
#     print(ll.is_empty())
#
#     ll.append(2)
#     print(ll.is_empty())
#
#     ll.travel()
















'''
# # ------------------------------------------------------------
# # # 4、单向链表
# # # # is_empty 是否为空
# # # # append   添加元素
# # # # travel   遍历元素
# # ------------------------------------------------------------
'''
# class SingleNode(object):
#     """单链表的结点"""
#     def __init__(self,item):
#         # _item存放数据元素
#         self.item = item
#         # _next是下一个节点的标识
#         self.next = None
#
#
# class SingleLinkList(object):
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         # 链表是否为空
#         return self._head is None
#
#     def length(self):
#         # 链表长度
#         count = 0
#         cur = self._head
#         while cur is not None:
#             count +=1
#             cur = cur.next
#         return count
#
#         # pass
#
#     def travel(self):
#         # 遍历整个链表
#         # if self._head is None:
#         #    return
#         # else:
#         #     cur = self._head
#         #     while cur is not None:
#         #         print(cur.item)
#         #         cur = cur.next
#         cur = self._head
#         while cur is not None:
#             print(cur.item)
#             cur = cur.next
#         # pass
#
#     def add(self, item):
#         # 链表头部添加元素
#         # node = SingleNode(item)
#         # node.next = self._head
#         pass
#
#     def append(self, item):
#         # 链表尾部添加元素
#         node = SingleNode(item)
#         if self.is_empty():
#             self._head = node
#             # return
#         else:
#             # cur = self._head
#             # while True:
#             #     if cur.next is None:
#             #         cur.next = node
#             #         break
#             #     cur = cur.next
#
#             cur = self._head
#             while cur.next is not None:
#                 cur = cur.next
#             cur.next = node
#
#
#
#         # pass
#
#     def insert(pos, item):
#         # 指定位置添加元素
#         pass
#
#     def remove(item):
#         # 删除节点
#         pass
#
#     def search(item):
#         # 查找节点是否存在
#         pass
#
# if __name__ == "__main__":
#     ll = SingleLinkList()
#     ll.travel()
#     print("===================")
#     print(ll.is_empty())
#
#     ll.append(1)
#     print(ll.is_empty())
#
#     ll.append(2)
#     print(ll.is_empty())
#
#     ll.travel()
#
#     print("===================")
#     ll.append(3)
#     ll.append(4)
#
#     ll.travel()
#
#     print(ll.length() )




















'''
# # ------------------------------------------------------------
# # # 5、单向链表
# # # # is_empty 是否为空
# # # # append   添加元素
# # # # travel   遍历元素
# # # # add      链表头部添加元素
# # ------------------------------------------------------------
'''
# class SingleNode(object):
#     """单链表的结点"""
#     def __init__(self,item):
#         # _item存放数据元素
#         self.item = item
#         # _next是下一个节点的标识
#         self.next = None
#
#
# class SingleLinkList(object):
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         # 链表是否为空
#         return self._head is None
#
#     def length(self):
#         # 链表长度
#         count = 0
#         cur = self._head
#         while cur is not None:
#             count +=1
#             cur = cur.next
#         return count
#
#         # pass
#
#     def travel(self):
#         # 遍历整个链表
#         # if self._head is None:
#         #    return
#         # else:
#         #     cur = self._head
#         #     while cur is not None:
#         #         print(cur.item)
#         #         cur = cur.next
#         cur = self._head
#         while cur is not None:
#             print(cur.item)
#             cur = cur.next
#         # pass
#
#     def add(self, item):
#         # 链表头部添加元素
#         node = SingleNode(item)
#         node.next = self._head
#         self._head = node
#         # pass
#
#     def append(self, item):
#         # 链表尾部添加元素
#         node = SingleNode(item)
#         if self.is_empty():
#             self._head = node
#             # return
#         else:
#             # cur = self._head
#             # while True:
#             #     if cur.next is None:
#             #         cur.next = node
#             #         break
#             #     cur = cur.next
#
#             cur = self._head
#             while cur.next is not None:
#                 cur = cur.next
#             cur.next = node
#
#
#
#         # pass
#
#     def insert(pos, item):
#         # 指定位置添加元素
#         pass
#
#     def remove(item):
#         # 删除节点
#         pass
#
#     def search(item):
#         # 查找节点是否存在
#         pass
#
# if __name__ == "__main__":
#     ll = SingleLinkList()
#     ll.travel()
#     print("===================")
#     print(ll.is_empty())
#
#     ll.append(1)
#     print(ll.is_empty())
#
#     ll.append(2)
#     print(ll.is_empty())
#
#     ll.travel()
#
#     print("===================")
#     ll.append(3)
#     ll.append(4)
#
#     ll.travel()
#
#     print(ll.length() )
#
#     print("===================add")
#     ll.add(10)
#     ll.add(20)
#     ll.travel()























'''
# # ------------------------------------------------------------
# # # 6、单向链表
# # # # is_empty 是否为空
# # # # append   添加元素
# # # # travel   遍历元素
# # # # add      链表头部添加元素
# # # # insert   指定位置添加元素
# # ------------------------------------------------------------
'''
# class SingleNode(object):
#     """单链表的结点"""
#     def __init__(self,item):
#         # _item存放数据元素
#         self.item = item
#         # _next是下一个节点的标识
#         self.next = None
#
#
# class SingleLinkList(object):
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         # 链表是否为空
#         return self._head is None
#
#     def length(self):
#         # 链表长度
#         count = 0
#         cur = self._head
#         while cur is not None:
#             count +=1
#             cur = cur.next
#         return count
#
#         # pass
#
#     def travel(self):
#         # 遍历整个链表
#         # if self._head is None:
#         #    return
#         # else:
#         #     cur = self._head
#         #     while cur is not None:
#         #         print(cur.item)
#         #         cur = cur.next
#         cur = self._head
#         while cur is not None:
#             print(cur.item, end=" ")
#             cur = cur.next
#         # pass
#
#     def add(self, item):
#         # 链表头部添加元素
#         node = SingleNode(item)
#         node.next = self._head
#         self._head = node
#         # pass
#
#     def append(self, item):
#         # 链表尾部添加元素
#         node = SingleNode(item)
#         if self.is_empty():
#             self._head = node
#             # return
#         else:
#             # cur = self._head
#             # while True:
#             #     if cur.next is None:
#             #         cur.next = node
#             #         break
#             #     cur = cur.next
#
#             cur = self._head
#             while cur.next is not None:
#                 cur = cur.next
#             cur.next = node
#
#
#
#         # pass
#
#     # def insert(self, pos, item):
#     #     # 指定位置添加元素     只能正向添加元素，即pos只能是正
#     #     # try:
#     #     node = SingleNode(item)
#     #     cur = self._head
#     #     if pos == 0:
#     #         node.next = cur
#     #         self._head = node
#     #     else:
#     #     # cur = self._head
#     #         count =0
#     #         while count < pos-1:
#     #             cur = cur.next
#     #             count += 1
#     #         node.next = cur.next
#     #         cur.next = node
#     #     # pass
#     def insert(self, pos, item):
#         # 指定位置添加元素     只能正向添加元素，即pos只能是正
#         # try:
#         node = SingleNode(item)
#         cur = self._head
#         if pos ==0:
#             self.add(item)
#             return
#
#         if pos < 0:
#             pos = self.length() + pos   # Convert to positive number
#         # elif pos ==0:
#         #     self.add(item)
#             # node.next = cur
#             # self._head = node
#         # else:
#             # cur = self._head
#         count = 0
#         while count < pos - 1:
#             cur = cur.next
#             count += 1
#         node.next = cur.next
#         cur.next = node
#         # pass
#
#     def remove(item):
#         # 删除节点
#         pass
#
#     def search(item):
#         # 查找节点是否存在
#         pass
#
# if __name__ == "__main__":
#     ll = SingleLinkList()
#     ll.travel()
#     print("===================")
#     print(ll.is_empty())
#
#     ll.append(1)
#     print(ll.is_empty())
#
#     ll.append(2)
#     print(ll.is_empty())
#
#     ll.travel()
#
#     print("===================")
#     ll.append(3)
#     ll.append(4)
#
#     ll.travel()
#
#     print(ll.length() )
#
#     print("===================add")
#     ll.add(10)
#     ll.add(20)
#     ll.travel()
#
#     print("ll.length():", ll.length())
#
#     print("===================insert")
#     ll.travel()
#     print()
#     ll.insert(0, 100)
#     ll.travel()
#     print()
#     ll.insert(2,200)
#     ll.travel()
#     print("ll.length():", ll.length())
#     ll.insert(8, 200)
#     ll.travel()
#     print()
#     ll.insert(-2, 200)
#     ll.travel()

























'''
# # ------------------------------------------------------------
# # # 7、单向链表
# # # # is_empty 是否为空
# # # # append   添加元素
# # # # travel   遍历元素
# # # # add      链表头部添加元素
# # # # insert   指定位置添加元素
# # # # remove   删除节点
# # ------------------------------------------------------------
'''
# class SingleNode(object):
#     """单链表的结点"""
#     def __init__(self,item):
#         # _item存放数据元素
#         self.item = item
#         # _next是下一个节点的标识
#         self.next = None
#
#
# class SingleLinkList(object):
#     def __init__(self):
#         self._head = None
#
#     def is_empty(self):
#         # 链表是否为空
#         return self._head is None
#
#     def length(self):
#         # 链表长度
#         count = 0
#         cur = self._head
#         while cur is not None:
#             count +=1
#             cur = cur.next
#         return count
#
#         # pass
#
#     def travel(self):
#         # 遍历整个链表
#         # if self._head is None:
#         #    return
#         # else:
#         #     cur = self._head
#         #     while cur is not None:
#         #         print(cur.item)
#         #         cur = cur.next
#         cur = self._head
#         while cur is not None:
#             print(cur.item, end=" ")
#             cur = cur.next
#         # pass
#
#     def add(self, item):
#         # 链表头部添加元素
#         node = SingleNode(item)
#         node.next = self._head
#         self._head = node
#         # pass
#
#     def append(self, item):
#         # 链表尾部添加元素
#         node = SingleNode(item)
#         if self.is_empty():
#             self._head = node
#             # return
#         else:
#             # cur = self._head
#             # while True:
#             #     if cur.next is None:
#             #         cur.next = node
#             #         break
#             #     cur = cur.next
#
#             cur = self._head
#             while cur.next is not None:
#                 cur = cur.next
#             cur.next = node
#
#
#
#         # pass
#
#     # def insert(self, pos, item):
#     #     # 指定位置添加元素     只能正向添加元素，即pos只能是正
#     #     # try:
#     #     node = SingleNode(item)
#     #     cur = self._head
#     #     if pos == 0:
#     #         node.next = cur
#     #         self._head = node
#     #     else:
#     #     # cur = self._head
#     #         count =0
#     #         while count < pos-1:
#     #             cur = cur.next
#     #             count += 1
#     #         node.next = cur.next
#     #         cur.next = node
#     #     # pass
#     def insert(self, pos, item):
#         # 指定位置添加元素     只能正向添加元素，即pos只能是正
#         # try:
#         node = SingleNode(item)
#         cur = self._head
#         if pos ==0:
#             self.add(item)
#             return
#
#         if pos < 0:
#             pos = self.length() + pos   # Convert to positive number
#         # elif pos ==0:
#         #     self.add(item)
#             # node.next = cur
#             # self._head = node
#         # else:
#             # cur = self._head
#         count = 0
#         while count < pos - 1:
#             cur = cur.next
#             count += 1
#         node.next = cur.next
#         cur.next = node
#         # pass
#
#     def remove(self, item):
#         # 删除节点
#         '''
#         对于逻辑问题比较复杂的
#         1、考虑一般情况
#         2、划分为两大类：一般情况 + 特殊情况
#         3、将特殊情况在一般情况或特殊情况中，继续细分
#         对比  remove 函数与完全注释的 remove 函数
#         :param item:
#         :return:
#         '''
#         cur = self._head
#         pre = None
#
#         if cur.item is item:
#             # the head is the element we are looking for
#             self._head = cur.next
#             return
#         elif cur is None:
#             return
#         else:
#             # if cur.next is not None:
#             while cur.next is not None:
#                 if cur.item is item:
#                     # delete item
#                     pre.next = cur.next
#                     break
#                 else:
#                     pre = cur
#                     cur = cur.next
#
#             if cur.item is item:
#                 # the last one
#                 pre.next = cur.next
#
#     '''
#     def remove(self,item):
#             """删除节点"""
#             cur = self._head
#             pre = None
#             while cur != None:
#                 # 找到了指定元素
#                 if cur.item == item:
#                     # 如果第一个就是删除的节点
#                     if not pre:
#                         # 将头指针指向头节点的后一个节点
#                         self._head = cur.next
#                     else:
#                         # 将删除位置前一个节点的next指向删除位置的后一个节点
#                         pre.next = cur.next
#                     break
#                 else:
#                     # 继续按链表后移节点
#                     pre = cur
#                     cur = cur.next
#     '''
#     def search(item):
#         # 查找节点是否存在
#         pass
#
# if __name__ == "__main__":
#     ll = SingleLinkList()
#     ll.travel()
#     print("===================")
#     print(ll.is_empty())
#
#     ll.append(1)
#     print(ll.is_empty())
#
#     ll.append(2)
#     print(ll.is_empty())
#
#     ll.travel()
#
#     print("===================")
#     ll.append(3)
#     ll.append(4)
#
#     ll.travel()
#
#     print(ll.length() )
#
#     print("===================add")
#     ll.add(10)
#     ll.add(20)
#     ll.travel()
#
#     print("ll.length():", ll.length())
#
#     print("===================insert")
#     ll.travel()
#     print()
#     ll.insert(0, 100)
#     ll.travel()
#     print()
#     ll.insert(2,200)
#     ll.travel()
#     print("ll.length():", ll.length())
#     ll.insert(8, 800)
#     ll.travel()
#     print()
#     ll.insert(-2, 200)
#     ll.travel()
#     print()
#
#     print("ll.length():", ll.length())
#     print("ll.remove(800)")
#     ll.remove(800)
#     ll.travel()
#     print()
#     print("ll.remove(999)")
#     ll.remove(999)
#     ll.travel()
#     print()
#     print("ll.remove(100)")
#     ll.remove(100)
#     ll.travel()
#     print()
#     print("ll.remove(1)")
#     ll.remove(1)
#     ll.travel()
#     print()
























'''
# # ------------------------------------------------------------
# # # 7、单向链表
# # # # is_empty 是否为空
# # # # append   添加元素
# # # # travel   遍历元素
# # # # add      链表头部添加元素
# # # # insert   指定位置添加元素
# # # # remove   删除节点
# # # # search   查找节点是否存在
# # ------------------------------------------------------------
'''
# class SingleNode(object):
#     """单链表的结点"""
#     def __init__(self,item):
#         # _item存放数据元素
#         self.item = item
#         # _next是下一个节点的标识
#         self.next = None


# class SingleLinkList(object):
#     def __init__(self):
#         self._head = None

#     def is_empty(self):
#         # 链表是否为空
#         return self._head is None

#     def length(self):
#         # 链表长度
#         count = 0
#         cur = self._head
#         while cur is not None:
#             count +=1
#             cur = cur.next
#         return count

#         # pass

#     def travel(self):
#         # 遍历整个链表
#         # if self._head is None:
#         #    return
#         # else:
#         #     cur = self._head
#         #     while cur is not None:
#         #         print(cur.item)
#         #         cur = cur.next
#         cur = self._head
#         while cur is not None:
#             print(cur.item, end=" ")
#             cur = cur.next
#         # pass

#     def add(self, item):
#         # 链表头部添加元素
#         node = SingleNode(item)
#         node.next = self._head
#         self._head = node
#         # pass

#     def append(self, item):
#         # 链表尾部添加元素
#         node = SingleNode(item)
#         if self.is_empty():
#             self._head = node
#             # return
#         else:
#             # cur = self._head
#             # while True:
#             #     if cur.next is None:
#             #         cur.next = node
#             #         break
#             #     cur = cur.next

#             cur = self._head
#             while cur.next is not None:
#                 cur = cur.next
#             cur.next = node



#         # pass

#     # def insert(self, pos, item):
#     #     # 指定位置添加元素     只能正向添加元素，即pos只能是正
#     #     # try:
#     #     node = SingleNode(item)
#     #     cur = self._head
#     #     if pos == 0:
#     #         node.next = cur
#     #         self._head = node
#     #     else:
#     #     # cur = self._head
#     #         count =0
#     #         while count < pos-1:
#     #             cur = cur.next
#     #             count += 1
#     #         node.next = cur.next
#     #         cur.next = node
#     #     # pass
#     def insert(self, pos, item):
#         # 指定位置添加元素     只能正向添加元素，即pos只能是正
#         # try:
#         node = SingleNode(item)
#         cur = self._head
#         if pos ==0:
#             self.add(item)
#             return

#         if pos < 0:
#             pos = self.length() + pos   # Convert to positive number
#         # elif pos ==0:
#         #     self.add(item)
#             # node.next = cur
#             # self._head = node
#         # else:
#             # cur = self._head
#         count = 0
#         while count < pos - 1:
#             cur = cur.next
#             count += 1
#         node.next = cur.next
#         cur.next = node
#         # pass

#     def remove(self, item):
#         # 删除节点
#         '''
#         对于逻辑问题比较复杂的
#         1、考虑一般情况
#         2、划分为两大类：一般情况 + 特殊情况
#         3、将特殊情况在一般情况或特殊情况中，继续细分
#         对比  remove 函数与完全注释的 remove 函数
#         :param item:
#         :return:
#         '''
#         cur = self._head
#         pre = None

#         if cur.item is item:
#             # the head is the element we are looking for
#             self._head = cur.next
#             return
#         elif cur is None:
#             return
#         else:
#             # if cur.next is not None:
#             while cur.next is not None:
#                 if cur.item is item:
#                     # delete item
#                     pre.next = cur.next
#                     break
#                 else:
#                     pre = cur
#                     cur = cur.next

#             if cur.item is item:
#                 # the last one
#                 pre.next = cur.next

#     '''
#     def remove(self,item):
#             """删除节点"""
#             cur = self._head
#             pre = None
#             while cur != None:
#                 # 不是链表
#                 # 找到了指定元素
#                 if cur.item == item:
#                     # 如果第一个就是删除的节点
#                     if not pre:
#                         # 将头指针指向头节点的后一个节点
#                         self._head = cur.next
#                     else:
#                         # 将删除位置前一个节点的next指向删除位置的后一个节点
#                         pre.next = cur.next
#                     break
#                 else:
#                     # 继续按链表后移节点
#                     pre = cur
#                     cur = cur.next
#     '''
#     def search(self, item):
#         # 查找节点是否存在
#         cur = self._head
#         while cur is not None:
#             if cur.item is item:
#                 return  True
#             else:
#                 cur = cur.next

#         return False
#         # pass

# if __name__ == "__main__":
#     ll = SingleLinkList()
#     ll.travel()
#     print("===================")
#     print(ll.is_empty())

#     ll.append(1)
#     print(ll.is_empty())

#     ll.append(2)
#     print(ll.is_empty())

#     ll.travel()

#     print("===================")
#     ll.append(3)
#     ll.append(4)

#     ll.travel()

#     print(ll.length() )

#     print("===================add")
#     ll.add(10)
#     ll.add(20)
#     ll.travel()

#     print("ll.length():", ll.length())

#     print("===================insert")
#     ll.travel()
#     print()
#     ll.insert(0, 100)
#     ll.travel()
#     print()
#     ll.insert(2,200)
#     ll.travel()
#     print("ll.length():", ll.length())
#     ll.insert(8, 800)
#     ll.travel()
#     print()
#     ll.insert(-2, 200)
#     ll.travel()
#     print()

#     print("ll.length():", ll.length())
#     print("ll.remove(800)")
#     ll.remove(800)
#     ll.travel()
#     print()
#     print("ll.remove(999)")
#     ll.remove(999)
#     ll.travel()
#     print()
#     print("ll.remove(100)")
#     ll.remove(100)
#     ll.travel()
#     print()
#     print("ll.remove(1)")
#     ll.remove(1)
#     ll.travel()
#     print()

#     print("------------->ll.search")
#     print("ll.length()",ll.length())
#     ll.travel()
#     print()
#     print(ll.search(20))
#     print(ll.search(10))
#     print(ll.search(4))
#     print(ll.search(100000000))


