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

#
# is_empty() 链表是否为空
# length() 链表长度
# travel() 遍历整个链表
# add(item) 链表头部添加元素
# append(item) 链表尾部添加元素
# insert(pos, item) 指定位置添加元素
# remove(item) 删除节点
# search(item) 查找节点是否存在



#
# '''
# # # ------------------------------------------------------------
# # # # 1、创建节点 + 链表 + 函数是否为空
# # # # # is_empty()  链表是否为空
# # # ------------------------------------------------------------
# '''
#
# # is_empty() 链表是否为空
# # length() 链表长度
# # travel() 遍历整个链表
# # add(item) 链表头部添加元素
# # append(item) 链表尾部添加元素
# # insert(pos, item) 指定位置添加元素
# # remove(item) 删除节点
# # search(item) 查找节点是否存在
#
#
# class SingleNode(object):
#     def __init__(self, item = None):
#         self._item = item
#         self._next = None
#
# class SingleLinkList(object):
#     def __init__(self, item = None):
#         self._head = item
#
#     def is_empty(self):
#         return self._head is None
#     # pass
#
# def node_is_empty():
#     node = SingleLinkList()
#     print(node.is_empty())
#
# if __name__ == '__main__':
#     node_is_empty()











'''
# # ------------------------------------------------------------
# # # 2、链表尾部添加元素
# # # # is_empty()          链表是否为空
# # # # append(item)        链表尾部添加元素
# # ------------------------------------------------------------
'''
#
# length() 链表长度
# travel() 遍历整个链表
# add(item) 链表头部添加元素
# append(item) 链表尾部添加元素
# insert(pos, item) 指定位置添加元素
# remove(item) 删除节点
# search(item) 查找节点是否存在
#
#
# class SingleNode(object):
#     def __init__(self, item = None):
#         self.item = item
#         self.next = None
#
# class SingleLinkList(object):
#     def __init__(self, item = None):
#         self._head = item
#
#     def is_empty(self):
#         '''
#         链表是否为空
#         :return:
#         '''
#         return self._head is None
#
#
#     def append(self, item):
#         '''
#         链表尾部添加元素
#         :return:
#         '''
#         node = SingleNode(item)
#
#         # null
#         if self.is_empty():
#             self._head = node
#         # not null
#         else:
#             cur = self._head
#             while cur.next is not None:
#                 cur = cur.next
#             # find the last one node
#             cur.next = node
#
#             # while True:
#             #     if cur.next is None:
#             #         cur.next = node
#             #         break
#             #     cur = cur.next
#
#     # pass
#
# class node_test():
#     def __init__(self):
#         pass
#     def node_is_empty(self):
#         node = SingleLinkList()
#         print(node.is_empty())
#
#     def node_append(self):
#         node = SingleLinkList()
#         print(node.is_empty())
#
#         node.append(1)
#         print(node.is_empty())
#
#         node.append(2)
#         node.append(3)
#         print(node.is_empty())
#
# if __name__ == '__main__':
#     # node_is_empty()
#     node = node_test()
#     node.node_append()
#     pass
#













'''
# # ------------------------------------------------------------
# # # 3、遍历整个链表
# # # # is_empty()          链表是否为空
# # # # append(item)        链表尾部添加元素
# # # # travel()            遍历整个链表

# # ------------------------------------------------------------
'''
# # is_empty() 链表是否为空
# # length() 链表长度
# # travel() 遍历整个链表
# # add(item) 链表头部添加元素
# # append(item) 链表尾部添加元素
# # insert(pos, item) 指定位置添加元素
# # remove(item) 删除节点
# # search(item) 查找节点是否存在
#
#
# class SingleNode(object):
#     def __init__(self, item = None):
#         self.item = item
#         self.next = None
#
# class SingleLinkList(object):
#     def __init__(self, item = None):
#         self._head = item
#
#     def is_empty(self):
#         '''
#         链表是否为空
#         :return:
#         '''
#         return self._head is None
#
#     def travel(self):
#         '''
#         遍历整个链表
#         :return:
#         '''
#         if self.is_empty():
#             return
#
#         cur = self._head
#         while cur is not None:
#             print(cur.item, end=' ')
#             cur = cur.next
#         print("")
#
#
#
#
#     def append(self, item):
#         '''
#         链表尾部添加元素
#         :return:
#         '''
#         node = SingleNode(item)
#
#         # null
#         if self.is_empty():
#             self._head = node
#         # not null
#         else:
#             cur = self._head
#             while cur.next is not None:
#                 cur = cur.next
#             # find the last one node
#             cur.next = node
#
#
#             # while True:
#             #     if cur.next is None:
#             #         cur.next = node
#             #         break
#             #     cur = cur.next
#
#     # pass
#
# class node_test():
#     def __init__(self):
#         pass
#     def node_is_empty(self):
#         node = SingleLinkList()
#         print(node.is_empty())
#
#     def node_append(self):
#         node = SingleLinkList()
#         print(node.is_empty())
#
#         node.append(1)
#         print(node.is_empty())
#
#         node.append(2)
#         node.append(3)
#         print(node.is_empty())
#
#     def node_travel(self):
#
#         node = SingleLinkList()
#         print("node.travel   ========>")
#         node.travel()
#         print("node.travel   ========>end")
#         print(node.is_empty())
#
#         node.append(1)
#         node.append(2)
#         node.append(3)
#         print(node.is_empty())
#
#         print("node.travel   ========>")
#         node.travel()
#         print("node.travel   ========>end")
#
# if __name__ == '__main__':
#     # node_is_empty()
#     node = node_test()
#     # node.node_is_empty()
#     # node.node_append()
#     # node.node_travel()
#
#     pass
#
#
#







'''
# # ------------------------------------------------------------
# # # 4、链表长度
# # # # is_empty()          链表是否为空
# # # # length()            链表长度
# # # # append(item)        链表尾部添加元素
# # # # travel()            遍历整个链表

# # ------------------------------------------------------------
'''
#
#
# # is_empty() 链表是否为空
# # length() 链表长度
# # travel() 遍历整个链表
# # add(item) 链表头部添加元素
# # append(item) 链表尾部添加元素
# # insert(pos, item) 指定位置添加元素
# # remove(item) 删除节点
# # search(item) 查找节点是否存在
#
#
# class SingleNode(object):
#     def __init__(self, item=None):
#         self.item = item
#         self.next = None
#
#
# class SingleLinkList(object):
#     def __init__(self, item=None):
#         self._head = item
#
#     def is_empty(self):
#         '''
#         链表是否为空
#         :return:
#         '''
#         return self._head is None
#
#     def length(self):
#         count =0
#         if self.is_empty():
#             pass
#         else:
#             cur = self._head
#             while cur.next is not None:
#                 count +=1
#                 cur = cur.next
#             count +=1
#         return count
#
#     def travel(self):
#         '''
#         遍历整个链表
#         :return:
#         '''
#         if self.is_empty():
#             return
#
#         cur = self._head
#         while cur is not None:
#             print(cur.item, end=' ')
#             cur = cur.next
#         print("")
#
#     def append(self, item):
#         '''
#         链表尾部添加元素
#         :return:
#         '''
#         node = SingleNode(item)
#
#         # null
#         if self.is_empty():
#             self._head = node
#         # not null
#         else:
#             cur = self._head
#             while cur.next is not None:
#                 cur = cur.next
#             # find the last one node
#             cur.next = node
#
#             # while True:
#             #     if cur.next is None:
#             #         cur.next = node
#             #         break
#             #     cur = cur.next
#
#     # pass
#
#
# class node_test():
#     def __init__(self):
#         pass
#
#     def node_is_empty(self):
#         node = SingleLinkList()
#         print(node.is_empty())
#
#     def node_length(self):
#         node = SingleLinkList()
#         print("node.length   ========>")
#         node.travel()
#         print(node.is_empty())
#         print("node.length():       ", node.length())
#
#         node.append(1)
#         node.append(2)
#         node.append(3)
#         print("node.length():       ", node.length())
#         print("node.length   ========>end")
#
#         pass
#
#     def node_append(self):
#         node = SingleLinkList()
#         print(node.is_empty())
#
#         node.append(1)
#         print(node.is_empty())
#
#         node.append(2)
#         node.append(3)
#         print(node.is_empty())
#
#     def node_travel(self):
#         node = SingleLinkList()
#         print("node.travel   ========>")
#         node.travel()
#         print("node.travel   ========>end")
#         print(node.is_empty())
#
#         node.append(1)
#         node.append(2)
#         node.append(3)
#         print(node.is_empty())
#
#         print("node.travel   ========>")
#         node.travel()
#         print("node.travel   ========>end")
#
#
# if __name__ == '__main__':
#     # node_is_empty()
#     node = node_test()
#     # node.node_is_empty()
#     # node.node_append()
#     # node.node_travel()
#     node.node_length()
#
#     pass
#









'''
# # ------------------------------------------------------------
# # # 5、链表头部添加元素
# # # # is_empty()          链表是否为空
# # # # length()            链表长度
# # # # append(item)        链表尾部添加元素
# # # # travel()            遍历整个链表
# # # # add(item)           链表头部添加元素
# # ------------------------------------------------------------
'''

#
# # is_empty() 链表是否为空
# # length() 链表长度
# # travel() 遍历整个链表
# # add(item) 链表头部添加元素
# # append(item) 链表尾部添加元素
# # insert(pos, item) 指定位置添加元素
# # remove(item) 删除节点
# # search(item) 查找节点是否存在
#
#
# class SingleNode(object):
#     def __init__(self, item=None):
#         self.item = item
#         self.next = None
#
#
# class SingleLinkList(object):
#     def __init__(self, item=None):
#         self._head = item
#
#     def is_empty(self):
#         '''
#         链表是否为空
#         :return:
#         '''
#         return self._head is None
#
#     def length(self):
#         count =0
#         if self.is_empty():
#             pass
#         else:
#             cur = self._head
#             while cur.next is not None:
#                 count +=1
#                 cur = cur.next
#             count +=1
#         return count
#
#     def travel(self):
#         '''
#         遍历整个链表
#         :return:
#         '''
#         if self.is_empty():
#             return
#
#         cur = self._head
#         while cur is not None:
#             print(cur.item, end=' ')
#             cur = cur.next
#         print("")
#
#     def add(self, item):
#         """
#         # add(item) 链表头部添加元素
#         :return:
#         """
#         node = SingleNode(item)
#         if self.is_empty():
#             self._head = node
#         else:
#             node.next = self._head
#             self._head = node
#
#
#     def append(self, item):
#         '''
#         链表尾部添加元素
#         :return:
#         '''
#         node = SingleNode(item)
#
#         # null
#         if self.is_empty():
#             self._head = node
#         # not null
#         else:
#             cur = self._head
#             while cur.next is not None:
#                 cur = cur.next
#             # find the last one node
#             cur.next = node
#
#             # while True:
#             #     if cur.next is None:
#             #         cur.next = node
#             #         break
#             #     cur = cur.next
#
#     # pass
#
#
# class node_test():
#     def __init__(self):
#         pass
#
#     def node_is_empty(self):
#         node = SingleLinkList()
#         print(node.is_empty())
#
#     def node_length(self):
#         node = SingleLinkList()
#         print("node.length   ========>")
#         node.travel()
#         print(node.is_empty())
#         print("node.length():       ", node.length())
#
#         node.append(1)
#         node.append(2)
#         node.append(3)
#         print("node.length():       ", node.length())
#         print("node.length   ========>end")
#
#         pass
#
#     def node_append(self):
#         node = SingleLinkList()
#         print(node.is_empty())
#
#         node.append(1)
#         print(node.is_empty())
#
#         node.append(2)
#         node.append(3)
#         print(node.is_empty())
#
#     def node_travel(self):
#         node = SingleLinkList()
#         print("node.travel   ========>")
#         node.travel()
#         print("node.travel   ========>end")
#         print(node.is_empty())
#
#         node.append(1)
#         node.append(2)
#         node.append(3)
#         print(node.is_empty())
#
#         print("node.travel   ========>")
#         node.travel()
#         print("node.travel   ========>end")
#
#
#     def node_add(self):
#         node = SingleLinkList()
#         # None
#         node.add(0)
#         print("node.travel   ========>")
#         node.travel()
#         print("node.travel   ========>end")
#
#         node.append(1)
#         node.append(2)
#         node.append(3)
#
#         print("node.travel   ========>")
#         node.travel()
#         print("node.travel   ========>end")
#
#         node.add(33)
#         node.add(22)
#         node.add(11)
#         print("node.travel   ========>")
#         node.travel()
#         print("node.travel   ========>end")
#
# if __name__ == '__main__':
#     # node_is_empty()
#     node = node_test()
#     # node.node_is_empty()
#     # node.node_append()
#     # node.node_travel()
#     # node.node_length()
#     node.node_add()
#     pass










'''
# # ------------------------------------------------------------
# # # 6、指定位置添加元素
# # # # is_empty()          链表是否为空
# # # # length()            链表长度
# # # # append(item)        链表尾部添加元素
# # # # travel()            遍历整个链表
# # # # add(item)           链表头部添加元素
# # # # insert(pos, item)   指定位置添加元素
# # ------------------------------------------------------------
'''
#
#
# # is_empty() 链表是否为空
# # length() 链表长度
# # travel() 遍历整个链表
# # add(item) 链表头部添加元素
# # append(item) 链表尾部添加元素
# # insert(pos, item) 指定位置添加元素
# # remove(item) 删除节点
# # search(item) 查找节点是否存在
#
#
# class SingleNode(object):
#     def __init__(self, item=None):
#         self.item = item
#         self.next = None
#
#
# class SingleLinkList(object):
#     def __init__(self, item=None):
#         self._head = item
#
#     def is_empty(self):
#         '''
#         链表是否为空
#         :return:
#         '''
#         return self._head is None
#
#     def length(self):
#         count =0
#         if self.is_empty():
#             pass
#         else:
#             cur = self._head
#             while cur.next is not None:
#                 count +=1
#                 cur = cur.next
#             count +=1
#         return count
#
#     def travel(self):
#         '''
#         遍历整个链表
#         :return:
#         '''
#         if self.is_empty():
#             return
#
#         cur = self._head
#         while cur is not None:
#             print(cur.item, end=' ')
#             cur = cur.next
#         print("")
#
#     def add(self, item):
#         """
#         # add(item) 链表头部添加元素
#         :return:
#         """
#         node = SingleNode(item)
#         if self.is_empty():
#             self._head = node
#         else:
#             node.next = self._head
#             self._head = node
#
#
#     def append(self, item):
#         '''
#         链表尾部添加元素
#         :return:
#         '''
#         node = SingleNode(item)
#
#         # null
#         if self.is_empty():
#             self._head = node
#         # not null
#         else:
#             cur = self._head
#             while cur.next is not None:
#                 cur = cur.next
#             # find the last one node
#             cur.next = node
#
#             # while True:
#             #     if cur.next is None:
#             #         cur.next = node
#             #         break
#             #     cur = cur.next
#
#
#     def insert(self, pos, item):
#         """
#         指定位置添加元素
#         :param pos:
#         :param item:
#         :return:
#         """
#         index = 0
#         node = SingleNode(item)
#         cur = self._head
#         # 空
#         if self.is_empty():
#             self._head = node
#         # 开头
#         elif pos<=0:
#             node.next = self._head
#             self._head = node
#         # 结束
#         elif pos >=self.length():
#             self.append(item)
#         # 中间
#         else:
#             while pos-1 is not index:
#                 cur = cur.next
#                 index +=1
#             node.next = cur.next
#             cur.next = node
#
#
#         # pass
#
#
#
#
#
# class node_test():
#     def __init__(self):
#         pass
#
#     def node_is_empty(self):
#         node = SingleLinkList()
#         print(node.is_empty())
#
#     def node_length(self):
#         node = SingleLinkList()
#         print("node.length   ========>")
#         node.travel()
#         print(node.is_empty())
#         print("node.length():       ", node.length())
#
#         node.append(1)
#         node.append(2)
#         node.append(3)
#         print("node.length():       ", node.length())
#         print("node.length   ========>end")
#
#         pass
#
#     def node_append(self):
#         node = SingleLinkList()
#         print(node.is_empty())
#
#         node.append(1)
#         print(node.is_empty())
#
#         node.append(2)
#         node.append(3)
#         print(node.is_empty())
#
#     def node_travel(self):
#         node = SingleLinkList()
#         print("node.travel   ========>")
#         node.travel()
#         print("node.travel   ========>end")
#         print(node.is_empty())
#
#         node.append(1)
#         node.append(2)
#         node.append(3)
#         print(node.is_empty())
#
#         print("node.travel   ========>")
#         node.travel()
#         print("node.travel   ========>end")
#
#
#     def node_add(self):
#         node = SingleLinkList()
#         # None
#         node.add(0)
#         print("node.travel   ========>")
#         node.travel()
#         print("node.travel   ========>end")
#
#         node.append(1)
#         node.append(2)
#         node.append(3)
#
#         print("node.travel   ========>")
#         node.travel()
#         print("node.travel   ========>end")
#
#         node.add(33)
#         node.add(22)
#         node.add(11)
#         print("node.travel   ========>")
#         node.travel()
#         print("node.travel   ========>end")
#
#     def node_insert(self):
#         node = SingleLinkList()
#         # 空
#         node.insert(1, 10)
#         node.travel()
#
#         node.append(1)
#         node.append(2)
#         node.append(3)
#         node.travel()
#
#         # 头
#         node.insert(0, 22)
#         node.insert(-10, 11)
#         node.travel()
#
#         # 尾
#         lengh = node.length()
#         node.insert(lengh, 44)
#         node.insert(lengh+10, 55)
#         node.travel()
#
#         # 中间
#         node.insert(3, 333333333)
#         node.travel()
#
#         # pass
#
#
# if __name__ == '__main__':
#     # node_is_empty()
#     node = node_test()
#     # node.node_is_empty()
#     # node.node_append()
#     # node.node_travel()
#     # node.node_length()
#     # node.node_add()
#     node.node_insert()
#     pass
#






'''
# # ------------------------------------------------------------
# # # 7、删除节点
# # # # is_empty()          链表是否为空
# # # # length()            链表长度
# # # # append(item)        链表尾部添加元素
# # # # travel()            遍历整个链表
# # # # add(item)           链表头部添加元素
# # # # insert(pos, item)   指定位置添加元素
# # # # remove(item)        删除节点
# # ------------------------------------------------------------
'''


# is_empty() 链表是否为空
# length() 链表长度
# travel() 遍历整个链表
# add(item) 链表头部添加元素
# append(item) 链表尾部添加元素
# insert(pos, item) 指定位置添加元素
# remove(item) 删除节点
# search(item) 查找节点是否存在


class SingleNode(object):
    def __init__(self, item=None):
        self.item = item
        self.next = None


class SingleLinkList(object):

    def __init__(self, item=None):
        self._head = item

    def node_head(self):
        return self._head

    def is_empty(self):
        '''
        链表是否为空
        :return:
        '''
        return self._head is None

    def length(self):
        count =0
        if self.is_empty():
            pass
        else:
            cur = self._head
            while cur.next is not None:
                count +=1
                cur = cur.next
            count +=1
        return count

    def travel(self):
        '''
        遍历整个链表
        :return:
        '''
        if self.is_empty():
            return

        cur = self._head
        while cur is not None:
            print(cur.item, end=' ')
            cur = cur.next
        print("")

    def add(self, item):
        """
        # add(item) 链表头部添加元素
        :return:
        """
        node = SingleNode(item)
        if self.is_empty():
            self._head = node
        else:
            node.next = self._head
            self._head = node


    def append(self, item):
        '''
        链表尾部添加元素
        :return:
        '''
        node = SingleNode(item)

        # null
        if self.is_empty():
            self._head = node
        # not null
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            # find the last one node
            cur.next = node

            # while True:
            #     if cur.next is None:
            #         cur.next = node
            #         break
            #     cur = cur.next


    def insert(self, pos, item):
        """
        指定位置添加元素
        :param pos:
        :param item:
        :return:
        """
        index = 0
        node = SingleNode(item)
        cur = self._head
        # 空
        if self.is_empty():
            self._head = node
        # 开头
        elif pos<=0:
            node.next = self._head
            self._head = node
        # 结束
        elif pos >=self.length():
            self.append(item)
        # 中间
        else:
            while pos-1 is not index:
                cur = cur.next
                index +=1
            node.next = cur.next
            cur.next = node


    def remove(self, item, all=False):
        """

        :param item:
        :param all:     删除所有重复的节点信息
        :return:
        """
        cur = self._head
        if self.is_empty():
            return
        elif cur.item is item:
            # 存在1个 或者是 头节点就是
            self._head = cur.next

        else:
            # 至少2个存在的节点
            cur = self._head
            pre = None
            while cur is not None:
                if cur.item is item:
                    pre.next = cur.next
                # if all == None:
                    # 如果没有设置，那么默认删除第一个
                    return
                pre = cur
                cur = cur.next

        # pass


class node_test():
    def __init__(self):
        pass

    def node_is_empty(self):
        node = SingleLinkList()
        print(node.is_empty())

    def node_length(self):
        node = SingleLinkList()
        print("node.length   ========>")
        node.travel()
        print(node.is_empty())
        print("node.length():       ", node.length())

        node.append(1)
        node.append(2)
        node.append(3)
        print("node.length():       ", node.length())
        print("node.length   ========>end")

        pass

    def node_append(self):
        node = SingleLinkList()
        print(node.is_empty())

        node.append(1)
        print(node.is_empty())

        node.append(2)
        node.append(3)
        print(node.is_empty())

    def node_travel(self):
        node = SingleLinkList()
        print("node.travel   ========>")
        node.travel()
        print("node.travel   ========>end")
        print(node.is_empty())

        node.append(1)
        node.append(2)
        node.append(3)
        print(node.is_empty())

        print("node.travel   ========>")
        node.travel()
        print("node.travel   ========>end")


    def node_add(self):
        node = SingleLinkList()
        # None
        node.add(0)
        print("node.travel   ========>")
        node.travel()
        print("node.travel   ========>end")

        node.append(1)
        node.append(2)
        node.append(3)

        print("node.travel   ========>")
        node.travel()
        print("node.travel   ========>end")

        node.add(33)
        node.add(22)
        node.add(11)
        print("node.travel   ========>")
        node.travel()
        print("node.travel   ========>end")

    def node_insert(self):
        node = SingleLinkList()
        # 空
        node.insert(1, 10)
        node.travel()

        node.append(1)
        node.append(2)
        node.append(3)
        node.travel()

        # 头
        node.insert(0, 22)
        node.insert(-10, 11)
        node.travel()

        # 尾
        lengh = node.length()
        node.insert(lengh, 44)
        node.insert(lengh+10, 55)
        node.travel()

        # 中间
        node.insert(3, 333333333)
        node.travel()

        # pass

    def node_next(self):
        node = SingleLinkList()
        node.append(1)
        node.append(2)
        node.append(3)
        head = node.node_head()
        print(head)
        print(head.item)                # 1
        print(head.next.item)           # 2

    def node_remove(self):
        node = SingleLinkList()
        print("None:\n")
        # none
        node.remove(1)

        print("only one:\n")
        # only one
        node.append(1)
        node.travel()
        node.remove(item=1)
        node.travel()

        print("more than 1\n")
        # more than 1
        node.append(1)
        node.append(2)
        node.travel()
        node.remove(1)
        node.travel()

        print("more than 1\n")
        # # more than 1
        node.append(1)
        node.append(2)
        node.append(3)
        node.remove(3)
        node.remove(2)
        node.remove(1)

        print("not in node:\n")
        # not in node
        node.append(1)
        node.append(2)
        node.append(3)
        node.remove(10)
        node.travel()

        node.append(3)
        node.append(3)
        node.remove(3)
        node.travel()

if __name__ == '__main__':
    # node_is_empty()
    node = node_test()
    # node.node_is_empty()
    # node.node_append()
    # node.node_travel()
    # node.node_length()
    # node.node_add()
    # node.node_insert()
    # node.node_next()
    node.node_remove()
    pass

