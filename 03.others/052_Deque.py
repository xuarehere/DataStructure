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







class Deque(object):
    """双端队列"""
    def __init__(self):
        self.items = []

    def is_empty(self):
        """判断队列是否为空"""
        return self.items == []

    def add_front(self, item):
        """在队头添加元素"""
        self.items.insert(0,item)

    def add_rear(self, item):
        """在队尾添加元素"""
        self.items.append(item)

    def remove_front(self):
        """从队头删除元素"""
        return self.items.pop(0)

    def remove_rear(self):
        """从队尾删除元素"""
        return self.items.pop()

    def size(self):
        """返回队列大小"""
        return len(self.items)
    def get_deque(self):
        return self.items

if __name__ == "__main__":
    deque = Deque()
    deque.add_front(1)  # 1
    deque.add_front(2)  # 2 1
    deque.add_rear(3)   # 2 1 3
    deque.add_rear(4)   # 2 1 3 4

    print( deque.get_deque() )
    print( deque.size() )    # 4
    print( deque.remove_front() )
    print(deque.get_deque())
    print(  deque.remove_front()  )
    print(  deque.remove_rear() )
    print(  deque.remove_rear() )