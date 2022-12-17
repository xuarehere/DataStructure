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


# is_empty() 链表是否为空
# length() 链表长度
# travel() 遍历整个链表
# add(item) 链表头部添加元素
# append(item) 链表尾部添加元素
# insert(pos, item) 指定位置添加元素
# remove(item) 删除节点
# search(item) 查找节点是否存在

class SingleNode:
    def __init__(self, item):
        self.item = item
        self.next = None

class SingleNodeLink:
    def __init__(self):
        self._head = None

    def is_empty(self):
        return self._head is None

    def length(self):
        """链表长度"""
        count = 0
        cur = self._head
        while cur is not None:
            count +=1
            cur = cur.next
        return count

    def travel(self):
        cur = self._head
        while cur is not None:
            print(cur.item, end=" ")
            cur = cur.next
        print()

    def add(self, item):
        """链表头部添加元素"""
        node = SingleNode(item)
        node.next = self._head
        self._head = node

    def append(self, item):
        """链表尾部添加元素"""
        node = SingleNode(item)
        if self.is_empty() is True:
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node
    def insert(self, pos, item):
        """指定位置添加元素"""
        node = SingleNode(item)
        if pos <0:
            pos =0
        elif pos >self.length():
            pos =self.length()

        if (self.is_empty() is True) or (pos is 0):
            node.next = self._head
            self._head = node
        else:
            index = 0
            cur = self._head
            while index< pos -1:
                cur = cur.next
                index +=1
            node.next = cur.next
            cur.next = node
    def remove(self, item):
        """删除节点"""
        cur = self._head
        if self.is_empty():
            return
        # 首个节点或者只有一个节点的时候
        elif cur.item is item:
            self._head = cur.next
        else:
            pre = None
            while cur is not None:
                if cur.item is item:
                    pre.next = cur.next
                    break
                else:
                    pre = cur
                    cur = cur.next

    def search(self, item):
        """查找节点是否存在"""
        if self.is_empty():
            return False
        else:
            cur = self._head
            while cur is not None:
                if cur.item is item:
                    return True
                else:
                    cur = cur.next

class test_node:
    def __init__(self):
        """create node"""
        self.node = SingleNodeLink()

    def is_empty(self):
        print("node.is_empty():", self.node.is_empty())

    def length(self):
        print("None:                 ", self.node.length())
        self.append()
        print("after append:         ", self.node.length())


    def append(self):
        self.is_empty()
        print("self.node.append(1)")
        self.node.append(1)

        print("self.node.append(2)")
        self.node.append(2)
        self.is_empty()

    def travel(self):
        print("None:    ", self.node.travel())
        self.append()
        print("after apped, travel ", self.node.is_empty())
        self.node.travel()

    def add(self):
        print("self.node.is_empty()):    ", self.node.is_empty())
        self.node.add(11)
        self.node.add(22)
        self.node.add(33)
        print("after node add. self.node.is_empty()", self.node.is_empty())
        self.node.travel()

    def insert(self):
        # 空的时候
        # print("空的时候".center(width=20, fillchar='*'))
        # print("空的时候".center(width=40, fillchar='*'))
        print("空的时候".center(40, '*'))
        node_none = SingleNodeLink()
        print("self.node.is_empty()):    ", node_none.is_empty())
        node_none.insert(1, 111)
        node_none.travel()
        #
        print("非空链表".center(40,'*'))
        node_link = SingleNodeLink()
        node_link.append(1)
        node_link.append(2)
        node_link.append(3)
        print("链表内容：")
        node_link.travel()

        print("insert:      node_link.insert(-1, 22)")
        node_link.insert(-1, 22)
        print("链表内容：")
        node_link.travel()

        print("insert:      node_link.insert(0, 11)")
        node_link.insert(0, 11)
        print("链表内容：")
        node_link.travel()

        print("insert:      node_link.insert(2, 2222)")
        node_link.insert(2, 2222)
        print("链表内容：")
        node_link.travel()

        print("insert:      node_link.insert(node_link.length(), 6666)")
        node_link.insert(node_link.length(), 6666)
        print("链表内容：")
        node_link.travel()

        print("insert:      node_link.insert(node_link.length(), 6666)")
        node_link.insert(node_link.length() + 1, 7777)
        print("链表内容：")
        node_link.travel()
    # pass

    def remove(self):
        print("不存在".center(40, "*"))
        self.node.remove(1)
        self.node.remove(12)

        print("一个节点".center(40, "*"))
        node_one = SingleNodeLink()
        node_one.append(1)
        print("===========>查看节点内容")
        node_one.travel()
        node_one.remove(1)
        print("===========>删除后，查看节点内容")
        node_one.travel()

        print("首节点".center(40, "*"))
        node_mul = SingleNodeLink()
        node_mul.append(1)
        node_mul.append(2)
        node_mul.append(3)
        node_mul.append(4)
        node_mul.append(5)
        node_mul.append(6)
        print("===========>查看节点内容")
        node_mul.travel()
        node_mul.remove(1)
        print("===========>删除后，查看节点内容")
        node_mul.travel()

        print("中间节点".center(40, "*"))
        node_remove_center = SingleNodeLink()
        node_remove_center.append(1)
        node_remove_center.append(2)
        node_remove_center.append(3)
        node_remove_center.append(4)
        node_remove_center.append(5)
        node_remove_center.append(6)
        print("===========>查看节点内容")
        node_remove_center.travel()
        node_remove_center.remove(3)
        print("===========>删除后,node_remove_center.remove(3)")
        node_remove_center.travel()

        print("尾巴节点".center(40, "*"))
        node_remove_tail = SingleNodeLink()
        node_remove_tail.append(1)
        node_remove_tail.append(2)
        node_remove_tail.append(3)
        node_remove_tail.append(4)
        node_remove_tail.append(5)
        node_remove_tail.append(6)
        print("===========>查看节点内容")
        node_remove_tail.travel()
        node_remove_tail.remove(6)
        print("===========>删除后,node_remove_tail.remove(3)")
        node_remove_tail.travel()

        pass

    def search(self):
        node_null = SingleNodeLink()
        print("空".center(40, "*"))
        print("node_null.search(1), node_null.search(2)")
        print( node_null.search(1), node_null.search(2))

        print("非空".center(40, "*"))
        self.append()
        self.node.travel()
        print("self.node.search(1), self.node.search(2)")
        print(self.node.search(1), self.node.search(2))


if __name__ == "__main__":
    node = test_node()
    # node.is_empty()
    # node.append()
    # node.travel()
    # node.length()
    # node.add()
    # node.insert()
    # node.remove()
    node.search()


