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
# # # 1、创建节点
# # # #
# # ------------------------------------------------------------
'''

#
# class Node(object):
#     """节点"""
#     def __init__(self, item):
#         self.item = item
#         self.next = None

# is_empty() 判断链表是否为空
# length() 返回链表的长度
# travel() 遍历
# add(item) 在头部添加一个节点
# append(item) 在尾部添加一个节点
# insert(pos, item) 在指定位置pos添加节点
# remove(item) 删除一个节点
# search(item) 查找节点是否存在
















'''
# # ------------------------------------------------------------
# # # 2、创建节点
# # # # is_empty() 判断链表是否为空
# # ------------------------------------------------------------
'''
#
#
# class Node(object):
#     """节点"""
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
# class Circulation_node(object):
#     def __init__(self):
#         self._head =None
#     def is_empty(self):
#         """
#         判断链表是否为空
#         """
#         # if self._head is None:
#         #     return True
#         return self._head is None
#
# # length() 返回链表的长度
# # travel() 遍历
# # add(item) 在头部添加一个节点
# # append(item) 在尾部添加一个节点
# # insert(pos, item) 在指定位置pos添加节点
# # remove(item) 删除一个节点
# # search(item) 查找节点是否存在













'''
# # ------------------------------------------------------------
# # # 2、链表
# # # # is_empty() 判断链表是否为空
# # # # length() 返回链表的长度
# # ------------------------------------------------------------
'''
#
#
# class Node(object):
#     """节点"""
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
# class Circulation_node(object):
#     def __init__(self):
#         self._head =None
#     def is_empty(self):
#         """
#         判断链表是否为空
#         """
#         # if self._head is None:
#         #     return True
#         return self._head is None
#
# # length() 返回链表的长度
# # travel() 遍历
#     def add(self, item):
#         """
#         在头部添加一个节点
#         :param item:
#         :return:
#         """
#         node = Node(item)
#         if self.is_empty():
#             self._head = node
#             node.next = self._head
#         else:
#             cur = self._head
#             while cur.next is not self._head:
#                 # find the last one node
#                 cur = cur.next
#             cur.next = node
#             self._head = node
#
# # append(item) 在尾部添加一个节点
# # insert(pos, item) 在指定位置pos添加节点
# # remove(item) 删除一个节点
# # search(item) 查找节点是否存在
#
#
# if __name__ =="__main__":
#     circle_node = Circulation_node()
#     print(circle_node.is_empty())
#
#     circle_node.add(1)
#     print(circle_node.is_empty())
#
#     circle_node.add(2)
#     print(circle_node.is_empty())




















'''
# # ------------------------------------------------------------
# # # 2、链表
# # # # is_empty() 判断链表是否为空
# # # # length() 返回链表的长度
# # # # travel() 遍历
# # ------------------------------------------------------------
'''
#
#
# class Node(object):
#     """节点"""
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
# class Circulation_node(object):
#     def __init__(self):
#         self._head =None
#     def is_empty(self):
#         """
#         判断链表是否为空
#         """
#         # if self._head is None:
#         #     return True
#         return self._head is None
#
# # length() 返回链表的长度
#     def travel(self):
#         """
#         遍历
#         :return:
#         """
#         if self.is_empty():
#             return
#         else:
#             cur = self._head
#             while cur.next is not  self._head:
#                 print(cur.item, end=" ")
#                 cur = cur.next
#             print(cur.item)
#
#
#     def add(self, item):
#         """
#         在头部添加一个节点
#         :param item:
#         :return:
#         """
#         node = Node(item)
#         cur = self._head
#         if self.is_empty():
#             self._head = node
#             node.next = self._head
#         else:
#             while cur.next is not self._head:
#                 # find the last one node
#                 cur = cur.next
#             cur.next = node
#             node.next = self._head
#             self._head = node
#
# # append(item) 在尾部添加一个节点
# # insert(pos, item) 在指定位置pos添加节点
# # remove(item) 删除一个节点
# # search(item) 查找节点是否存在
#
#
# if __name__ =="__main__":
#     circle_node = Circulation_node()
#     circle_node.travel()
#     print("---------")
#     print(circle_node.is_empty())
#
#     circle_node.add(1)
#     print(circle_node.is_empty())
#
#     circle_node.add(2)
#     print(circle_node.is_empty())
#
#     circle_node.add(3)
#     print(circle_node.is_empty())
#
#     circle_node.travel()




























'''
# # ------------------------------------------------------------
# # # 4、链表
# # # # is_empty() 判断链表是否为空
# # # # length() 返回链表的长度
# # # # travel() 遍历
# # # # length() 返回链表的长度
# # ------------------------------------------------------------
'''

#
# class Node(object):
#     """节点"""
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
# class Circulation_node(object):
#     def __init__(self):
#         self._head =None
#     def is_empty(self):
#         """
#         判断链表是否为空
#         """
#         # if self._head is None:
#         #     return True
#         return self._head is None
#
#     def length(self):
#         """
#         返回链表的长度
#         :return:
#         """
#         cur = self._head
#         count = 0
#         if self.is_empty():
#             pass
#         else:
#             count =1        # point to the head node
#             while cur.next is not self._head:
#                     count +=1
#                     cur = cur.next
#         return count
#
#
#
#         #
#         # while True:
#         #     if cur.next is not self._head:
#         #         count +=1
#         #         cur = cur.next
#         #     else:
#         #         break
#         # return count
#
#     def travel(self):
#         """
#         遍历
#         :return:
#         """
#         if self.is_empty():
#             return
#         else:
#             cur = self._head
#             while cur.next is not  self._head:
#                 print(cur.item, end=" ")
#                 cur = cur.next
#             print(cur.item)
#
#
#     def add(self, item):
#         """
#         在头部添加一个节点
#         :param item:
#         :return:
#         """
#         node = Node(item)
#         cur = self._head
#         if self.is_empty():
#             self._head = node
#             node.next = self._head
#         else:
#             while cur.next is not self._head:
#                 # find the last one node
#                 cur = cur.next
#             cur.next = node
#             node.next = self._head
#             self._head = node
#
# # append(item) 在尾部添加一个节点
# # insert(pos, item) 在指定位置pos添加节点
# # remove(item) 删除一个节点
# # search(item) 查找节点是否存在
#
#
# if __name__ =="__main__":
#     circle_node = Circulation_node()
#     circle_node.travel()
#     print(circle_node.length())
#     print("---------")
#     print(circle_node.is_empty())
#
#     circle_node.add(1)
#     print(circle_node.is_empty())
#
#     circle_node.add(2)
#     print(circle_node.is_empty())
#
#     circle_node.add(3)
#     print(circle_node.is_empty())
#
#     circle_node.travel()
#
#     print(circle_node.length() )
























'''
# # ------------------------------------------------------------
# # # 5、链表
# # # # is_empty() 判断链表是否为空
# # # # length() 返回链表的长度
# # # # travel() 遍历
# # # # length() 返回链表的长度
# # # # append(item) 在尾部添加一个节点
# # ------------------------------------------------------------
'''

#
# class Node(object):
#     """节点"""
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
# class Circulation_node(object):
#     def __init__(self):
#         self._head =None
#     def is_empty(self):
#         """
#         判断链表是否为空
#         """
#         # if self._head is None:
#         #     return True
#         return self._head is None
#
#     def length(self):
#         """
#         返回链表的长度
#         :return:
#         """
#         cur = self._head
#         count = 0
#         if self.is_empty():
#             pass
#         else:
#             count =1        # point to the head node
#             while cur.next is not self._head:
#                     count +=1
#                     cur = cur.next
#         return count
#
#
#
#         #
#         # while True:
#         #     if cur.next is not self._head:
#         #         count +=1
#         #         cur = cur.next
#         #     else:
#         #         break
#         # return count
#
#     def travel(self):
#         """
#         遍历
#         :return:
#         """
#         if self.is_empty():
#             return
#         else:
#             cur = self._head
#             while cur.next is not  self._head:
#                 print(cur.item, end=" ")
#                 cur = cur.next
#             print(cur.item)
#
#
#     def add(self, item):
#         """
#         在头部添加一个节点
#         :param item:
#         :return:
#         """
#         node = Node(item)
#         cur = self._head
#         if self.is_empty():
#             self._head = node
#             node.next = self._head
#         else:
#             while cur.next is not self._head:
#                 # find the last one node
#                 cur = cur.next
#             cur.next = node
#             node.next = self._head
#             self._head = node
#
#     def append(self, item):
#         """
#         在尾部添加一个节点
#         :param item:
#         :return:
#         """
#         cur = self._head
#         node = Node(item)
#         if self.is_empty():
#             self._head = node
#             node.next = self._head
#         else:
#             while cur.next is not self._head:
#                 cur = cur.next
#             # cur.next ==self._head
#             node.next = cur.next
#             cur.next = node
#
# # insert(pos, item) 在指定位置pos添加节点
# # remove(item) 删除一个节点
# # search(item) 查找节点是否存在
#
#
# if __name__ =="__main__":
#     circle_node = Circulation_node()
#     circle_node.travel()
#     print(circle_node.length())
#     print("---------")
#     print(circle_node.is_empty())
#
#     circle_node.append(4)
#     circle_node.travel()
#
#     circle_node.add(1)
#     print(circle_node.is_empty())
#
#     circle_node.add(2)
#     print(circle_node.is_empty())
#
#     circle_node.add(3)
#     print(circle_node.is_empty())
#
#     circle_node.travel()
#
#     print("circle_node.length() :   ", circle_node.length() )
#
#     print("==========append")
#     circle_node.append(5)
#     circle_node.travel()
#     circle_node.append(6)
#     circle_node.travel()



















'''
# # ------------------------------------------------------------
# # # 6、链表
# # # # is_empty() 判断链表是否为空
# # # # length() 返回链表的长度
# # # # travel() 遍历
# # # # length() 返回链表的长度
# # # # append() 在尾部添加一个节点
# # # # insert   在指定位置pos添加节点
# # ------------------------------------------------------------
'''

#
# class Node(object):
#     """节点"""
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
# class Circulation_node(object):
#     def __init__(self):
#         self._head =None
#     def is_empty(self):
#         """
#         判断链表是否为空
#         """
#         # if self._head is None:
#         #     return True
#         return self._head is None
#
#     def length(self):
#         """
#         返回链表的长度
#         :return:
#         """
#         cur = self._head
#         count = 0
#         if self.is_empty():
#             pass
#         else:
#             count =1        # point to the head node
#             while cur.next is not self._head:
#                 count +=1
#                 cur = cur.next
#         return count
#
#
#
#         #
#         # while True:
#         #     if cur.next is not self._head:
#         #         count +=1
#         #         cur = cur.next
#         #     else:
#         #         break
#         # return count
#
#     def travel(self):
#         """
#         遍历
#         :return:
#         """
#         if self.is_empty():
#             return
#         else:
#             cur = self._head
#             while cur.next is not  self._head:
#                 print(cur.item, end=" ")
#                 cur = cur.next
#             print(cur.item)
#
#
#     def add(self, item):
#         """
#         在头部添加一个节点
#         :param item:
#         :return:
#         """
#         node = Node(item)
#         cur = self._head
#         if self.is_empty():
#             self._head = node
#             node.next = self._head
#         else:
#             while cur.next is not self._head:
#                 # find the last one node
#                 cur = cur.next
#             cur.next = node
#             node.next = self._head
#             self._head = node
#
#     def append(self, item):
#         """
#         在尾部添加一个节点
#         :param item:
#         :return:
#         """
#         cur = self._head
#         node = Node(item)
#         if self.is_empty():
#             self._head = node
#             node.next = self._head
#             '''
#             # 以下的方式，node.next 最后的指向是 None， 而不是 self._head
#             # 因此，以下的方式是错误的
#             node.next = self._head = None
#             self._head = node
#             '''
#
#         else:
#             # 移到链表尾部
#             while cur.next is not self._head:
#                 cur = cur.next
#             # 将尾节点指向node
#             node.next = cur.next
#             # 将node指向头节点_head
#             cur.next = node
#
#     def insert(self, pos, item):
#         """
#         在指定位置pos添加节点
#         :param pos:
#         :param item:
#         :return:
#         """
#
#         # while cur.next is self._head:
#         if pos <= 0:
#             self.add(item)
#         elif pos > (self.length()-1):
#             self.append(item)
#         else:
#             cur = self._head
#             node = Node(item)
#             # pre =None
#             count = 0
#             '''
#             第一种写法
#              while True:
#                 if count is (pos-1):
#                     node.next = cur.next
#                     cur.next = node
#                     break
#                 else:
#                     cur = cur.next
#                     count +=1
#
#                     if cur.next is self._head:
#                         break
#
#             '''
#             # 简洁的写法
#             # 移动到指定位置的前一个位置
#             while count < (pos-1):
#                 count += 1
#                 cur = cur.next
#             node.next = cur.next
#             cur.next = node
#
#
# # remove(item) 删除一个节点
# # search(item) 查找节点是否存在
#
#
# if __name__ =="__main__":
#     circle_node = Circulation_node()
#     circle_node.travel()
#     print(circle_node.length())
#     print("---------")
#     print(circle_node.is_empty())
#
#     circle_node.append(4)
#     circle_node.travel()
#
#     circle_node.add(1)
#     print(circle_node.is_empty())
#
#     circle_node.add(2)
#     print(circle_node.is_empty())
#
#     circle_node.add(3)
#     print(circle_node.is_empty())
#
#     circle_node.travel()
#
#     print("circle_node.length() :   ", circle_node.length() )
#
#     print("==========append")
#     circle_node.append(5)
#     circle_node.travel()
#     circle_node.append(6)
#     circle_node.travel()        # 3 2 1 4 5 6
#
#     circle_node.insert(0, 111)  # 111 3 2 1 4 5 6
#     circle_node.travel()
#
#     circle_node.insert(6, 666)      # 111 3 2 1 4 5 666 6
#     circle_node.travel()
#
#     circle_node.insert(9, 8888)     # 111 3 2 1 4 5 666 6 8888
#     circle_node.travel()
#














'''
# # ------------------------------------------------------------
# # # 7、链表
# # # # is_empty() 判断链表是否为空
# # # # length() 返回链表的长度
# # # # travel() 遍历
# # # # length() 返回链表的长度
# # # # append() 在尾部添加一个节点
# # # # insert   在指定位置pos添加节点
# # # # remove   删除一个节点
# # ------------------------------------------------------------
'''

#
# class Node(object):
#     """节点"""
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
# class Circulation_node(object):
#     def __init__(self):
#         self._head =None
#     def is_empty(self):
#         """
#         判断链表是否为空
#         """
#         # if self._head is None:
#         #     return True
#         return self._head is None
#
#     def length(self):
#         """
#         返回链表的长度
#         :return:
#         """
#         cur = self._head
#         count = 0
#         if self.is_empty():
#             pass
#         else:
#             count =1        # point to the head node
#             while cur.next is not self._head:
#                 count +=1
#                 cur = cur.next
#         return count
#
#
#
#         #
#         # while True:
#         #     if cur.next is not self._head:
#         #         count +=1
#         #         cur = cur.next
#         #     else:
#         #         break
#         # return count
#
#     def travel(self):
#         """
#         遍历
#         :return:
#         """
#         if self.is_empty():
#             return
#         else:
#             cur = self._head
#             while cur.next is not  self._head:
#                 print(cur.item, end=" ")
#                 cur = cur.next
#             print(cur.item)
#
#
#     def add(self, item):
#         """
#         在头部添加一个节点
#         :param item:
#         :return:
#         """
#         node = Node(item)
#         cur = self._head
#         if self.is_empty():
#             self._head = node
#             node.next = self._head
#         else:
#             while cur.next is not self._head:
#                 # find the last one node
#                 cur = cur.next
#             cur.next = node
#             node.next = self._head
#             self._head = node
#
#     def append(self, item):
#         """
#         在尾部添加一个节点
#         :param item:
#         :return:
#         """
#         cur = self._head
#         node = Node(item)
#         if self.is_empty():
#             self._head = node
#             node.next = self._head
#             '''
#             # 以下的方式，node.next 最后的指向是 None， 而不是 self._head
#             # 因此，以下的方式是错误的
#             node.next = self._head = None
#             self._head = node
#             '''
#
#         else:
#             # 移到链表尾部
#             while cur.next is not self._head:
#                 cur = cur.next
#             # 将尾节点指向node
#             node.next = cur.next
#             # 将node指向头节点_head
#             cur.next = node
#
#     def insert(self, pos, item):
#         """
#         在指定位置pos添加节点
#         :param pos:
#         :param item:
#         :return:
#         """
#
#         # while cur.next is self._head:
#         if pos <= 0:
#             self.add(item)
#         elif pos > (self.length()-1):
#             self.append(item)
#         else:
#             cur = self._head
#             node = Node(item)
#             # pre =None
#             count = 0
#             '''
#             第一种写法
#              while True:
#                 if count is (pos-1):
#                     node.next = cur.next
#                     cur.next = node
#                     break
#                 else:
#                     cur = cur.next
#                     count +=1
#
#                     if cur.next is self._head:
#                         break
#
#             '''
#             # 简洁的写法
#             # 移动到指定位置的前一个位置
#             while count < (pos-1):
#                 count += 1
#                 cur = cur.next
#             node.next = cur.next
#             cur.next = node
#
#
#     def remove(self, item):
#         '''
#         删除一个节点
#         :return:
#         '''
#         cur = self._head
#         pre = None
#         if self.is_empty():
#             return
#         elif cur.item is item:
#             # 首节点就是我们要找的
#             if cur.next is self._head:
#                 # 只有一个节点的情况
#                 self._head = None
#             else:
#                 # 多个节点的情况
#                 pre = cur.next      # 记录第二个节点
#                 while cur.next is not self._head:
#                     cur = cur.next
#                 cur.next = pre
#                 self._head = pre
#
#             # # 多个节点
#             # pre = self._head  # 首节点
#             # while (cur.next is not self._head) and (pre is not None):
#             #     cur = cur.next
#             # cur.next
#         else:
#             # 查找的节点不在首节点
#             while (cur.next is not self._head) :
#                 if cur.item is item:
#                     # 删除
#                     pre.next = cur.next
#                     return
#                 else:
#                     # 继续向前步进查找
#                     pre = cur
#                     cur = cur.next
#             # cur 指向尾节点
#             if cur.item is item:
#                 # 尾部删除
#                 pre.next = cur.next
#
#
#
#
# # search(item) 查找节点是否存在
#
#
# if __name__ =="__main__":
#     circle_node = Circulation_node()
#     circle_node.travel()
#     print(circle_node.length())
#     print("---------")
#     print(circle_node.is_empty())
#
#     circle_node.append(4)
#     circle_node.travel()
#
#
#     circle_node.add(1)
#     print(circle_node.is_empty())
#
#     circle_node.add(2)
#     print(circle_node.is_empty())
#
#     circle_node.add(3)
#     print(circle_node.is_empty())
#
#     circle_node.travel()
#
#     print("circle_node.length() :   ", circle_node.length() )
#
#     print("==========append")
#     circle_node.append(5)
#     circle_node.travel()
#     circle_node.append(6)
#     circle_node.travel()        # 3 2 1 4 5 6
#
#     circle_node.insert(0, 111)  # 111 3 2 1 4 5 6
#     circle_node.travel()
#
#     circle_node.insert(6, 666)      # 111 3 2 1 4 5 666 6
#     circle_node.travel()
#
#     circle_node.insert(9, 8888)     # 111 3 2 1 4 5 666 6 8888
#     circle_node.travel()
#
#     circle_node.remove(8888)
#     circle_node.travel()




























'''
# # ------------------------------------------------------------
# # # 8、链表
# # # # is_empty() 判断链表是否为空
# # # # length() 返回链表的长度
# # # # travel() 遍历
# # # # length() 返回链表的长度
# # # # append() 在尾部添加一个节点
# # # # insert   在指定位置pos添加节点
# # # # remove   删除一个节点
# # # # search   查找节点是否存在
# # ------------------------------------------------------------
'''


class Node(object):
    """节点"""
    def __init__(self, item):
        self.item = item
        self.next = None

class Circulation_node(object):
    def __init__(self):
        self._head =None
    def is_empty(self):
        """
        判断链表是否为空
        """
        # if self._head is None:
        #     return True
        return self._head is None

    def length(self):
        """
        返回链表的长度
        :return:
        """
        cur = self._head
        count = 0
        if self.is_empty():
            pass
        else:
            count =1        # point to the head node
            while cur.next is not self._head:
                count +=1
                cur = cur.next
        return count



        #
        # while True:
        #     if cur.next is not self._head:
        #         count +=1
        #         cur = cur.next
        #     else:
        #         break
        # return count

    def travel(self):
        """
        遍历
        :return:
        """
        if self.is_empty():
            return
        else:
            cur = self._head
            while cur.next is not  self._head:
                print(cur.item, end=" ")
                cur = cur.next
            print(cur.item)


    def add(self, item):
        """
        在头部添加一个节点
        :param item:
        :return:
        """
        node = Node(item)
        cur = self._head
        if self.is_empty():
            self._head = node
            node.next = self._head
        else:
            while cur.next is not self._head:
                # find the last one node
                cur = cur.next
            cur.next = node
            node.next = self._head
            self._head = node

    def append(self, item):
        """
        在尾部添加一个节点
        :param item:
        :return:
        """
        cur = self._head
        node = Node(item)
        if self.is_empty():
            self._head = node
            node.next = self._head
            '''
            # 以下的方式，node.next 最后的指向是 None， 而不是 self._head
            # 因此，以下的方式是错误的
            node.next = self._head = None
            self._head = node
            '''

        else:
            # 移到链表尾部
            while cur.next is not self._head:
                cur = cur.next
            # 将尾节点指向node
            node.next = cur.next
            # 将node指向头节点_head
            cur.next = node

    def insert(self, pos, item):
        """
        在指定位置pos添加节点
        :param pos:
        :param item:
        :return:
        """

        # while cur.next is self._head:
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            cur = self._head
            node = Node(item)
            # pre =None
            count = 0
            '''
            第一种写法
             while True:
                if count is (pos-1):
                    node.next = cur.next
                    cur.next = node
                    break
                else:
                    cur = cur.next
                    count +=1

                    if cur.next is self._head:
                        break

            '''
            # 简洁的写法
            # 移动到指定位置的前一个位置
            while count < (pos-1):
                count += 1
                cur = cur.next
            node.next = cur.next
            cur.next = node


    def remove(self, item):
        '''
        删除一个节点
        :return:
        '''
        cur = self._head
        pre = None
        if self.is_empty():
            return
        elif cur.item is item:
            # 首节点就是我们要找的
            if cur.next is self._head:
                # 只有一个节点的情况
                self._head = None
            else:
                # 多个节点的情况
                pre = cur.next      # 记录第二个节点
                while cur.next is not self._head:
                    cur = cur.next
                cur.next = pre
                self._head = pre

            # # 多个节点
            # pre = self._head  # 首节点
            # while (cur.next is not self._head) and (pre is not None):
            #     cur = cur.next
            # cur.next
        else:
            # 查找的节点不在首节点
            while (cur.next is not self._head) :
                if cur.item is item:
                    # 删除
                    pre.next = cur.next
                    return
                else:
                    # 继续向前步进查找
                    pre = cur
                    cur = cur.next
            # cur 指向尾节点
            if cur.item is item:
                # 尾部删除
                pre.next = cur.next




    #
    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        cur = self._head
        if cur.item == item:
            return True
        while cur.next != self._head:
            # 先看下一个节点是否是 self._head， 即看是否回到了头部，再向前步进
            cur = cur.next
            if cur.item == item:
                return True
        return False



if __name__ =="__main__":
    circle_node = Circulation_node()
    circle_node.travel()
    print(circle_node.length())
    print("---------")
    print(circle_node.is_empty())

    circle_node.append(4)
    circle_node.travel()



    circle_node.add(1)
    print(circle_node.is_empty())
    print("circle_node.search(4) ", circle_node.search(4))

    circle_node.add(2)
    print(circle_node.is_empty())

    circle_node.add(3)
    print(circle_node.is_empty())

    circle_node.travel()

    print("circle_node.length() :   ", circle_node.length() )

    print("==========append")
    circle_node.append(5)
    circle_node.travel()
    circle_node.append(6)
    circle_node.travel()        # 3 2 1 4 5 6

    circle_node.insert(0, 111)  # 111 3 2 1 4 5 6
    circle_node.travel()

    circle_node.insert(6, 666)      # 111 3 2 1 4 5 666 6
    circle_node.travel()

    circle_node.insert(9, 8888)     # 111 3 2 1 4 5 666 6 8888
    circle_node.travel()

    circle_node.remove(8888)
    circle_node.travel()

    print( circle_node.search(6) )