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
# # # 1、栈
# # # # Stack()         创建一个新的空栈
# # # # is_empty()      判断栈是否为空
# # ------------------------------------------------------------
'''
#
# # Stack() 创建一个新的空栈
# # push(item) 添加一个新的元素item到栈顶
# # pop() 弹出栈顶元素
# # peek() 返回栈顶元素
# # is_empty() 判断栈是否为空
# # size() 返回栈的元素个数
# class Stack():
#     def __init__(self):
#         self.item = []
#
#     def is_empty(self):
#         return self.item == []
#         # 以下的写法都是错误的
#         #   return self.item == None
#         #   return self.item is []
#
# if __name__ =="__main__":
#     stack = Stack()
#     print( stack.is_empty())


















'''
# # ------------------------------------------------------------
# # # 3、栈
# # # # Stack()         创建一个新的空栈
# # # # push(item)      添加一个新的元素item到栈顶
# # # # is_empty()      判断栈是否为空
# # ------------------------------------------------------------
'''
#
# # Stack() 创建一个新的空栈
# # push(item) 添加一个新的元素item到栈顶
# # pop() 弹出栈顶元素
# # peek() 返回栈顶元素
# # is_empty() 判断栈是否为空
# # size() 返回栈的元素个数
# class Stack():
#     def __init__(self):
#         self.item = []
#
#     def push(self, item):
#         """
#         添加一个新的元素item到栈顶
#         :param item:
#         :return:
#         """
#         self.item.insert(0,item)    # 最开始的位置
#
#     def is_empty(self):
#         return self.item == []
#         # 以下的写法都是错误的
#         #   return self.item == None
#         #   return self.item is []
#
# def test_Is_empty():
#     stack = Stack()
#     print( stack.is_empty())
#
# def test_Push():
#     stack = Stack()
#     print("stack.is_empty():", stack.is_empty())
#
#     stack.push(3)
#     stack.push(2)
#     stack.push(1)
#     print("stack.is_empty():", stack.is_empty())
#
# if __name__ =="__main__":
#     # test_Is_empty()
#     test_Push()
#     # pass
#
#









'''
# # ------------------------------------------------------------
# # # 4、栈
# # # # Stack()         创建一个新的空栈
# # # # push(item)      添加一个新的元素item到栈顶
# # # # is_empty()      判断栈是否为空
# # # # pop()           弹出栈顶元素 
# # ------------------------------------------------------------
'''

# Stack() 创建一个新的空栈
# push(item) 添加一个新的元素item到栈顶
# pop() 弹出栈顶元素
# peek() 返回栈顶元素
# is_empty() 判断栈是否为空
# size() 返回栈的元素个数
#
# class Stack():
#     def __init__(self):
#         self.item = []
#
#     def push(self, item):
#         """
#         添加一个新的元素item到栈顶
#         :param item:
#         :return:
#         """
#         self.item.insert(0,item)    # 最开始的位置
#
#     def pop(self):
#         try:
#             return self.item.pop(0)
#         except:
#             return None
#         # pass
#
#     def is_empty(self):
#         return self.item == []
#         # 以下的写法都是错误的
#         #   return self.item == None
#         #   return self.item is []
#
# def test_Is_empty():
#     stack = Stack()
#     print( stack.is_empty())
#
# def test_Push():
#     stack = Stack()
#     print("stack.is_empty():", stack.is_empty())
#
#     stack.push(3)
#     stack.push(2)
#     stack.push(1)
#     print("stack.is_empty():", stack.is_empty())
#
# def test_Pop():
#     stack = Stack()
#     print("stack.is_empty():", stack.is_empty())
#     print(stack.pop())
#     stack.push(3)
#     stack.push(2)
#     stack.push(1)
#     print("stack.is_empty():", stack.is_empty())
#
#     print(stack.pop())
#     print(stack.pop())
#     print(stack.pop())
#     print(stack.pop())
#
# if __name__ =="__main__":
#     # test_Is_empty()
#     # test_Push()
#     test_Pop()
#     pass
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#























'''
# # ------------------------------------------------------------
# # # 4、栈
# # # # Stack()         创建一个新的空栈
# # # # push(item)      添加一个新的元素item到栈顶
# # # # pop()           弹出栈顶元素 
# # # # peek()          返回栈顶元素
# # # # is_empty()      判断栈是否为空
# # ------------------------------------------------------------
'''
#
# # Stack() 创建一个新的空栈
# # push(item) 添加一个新的元素item到栈顶
# # pop() 弹出栈顶元素
# # peek() 返回栈顶元素
# # is_empty() 判断栈是否为空
# # size() 返回栈的元素个数
#
# class Stack():
#     def __init__(self):
#         self.item = []
#
#     def push(self, item):
#         """
#         添加一个新的元素item到栈顶
#         :param item:
#         :return:
#         """
#         self.item.insert(0,item)    # 最开始的位置
#
#     def pop(self):
#         try:
#             return self.item.pop(0)
#         except:
#             return None
#         # pass
#
#     def peek(self):
#         """
#         返回栈顶元素
#         :return:
#         """
#         try:
#             return self.item[0]
#         except:
#             return None
#
#     def is_empty(self):
#         return self.item == []
#         # 以下的写法都是错误的
#         #   return self.item == None
#         #   return self.item is []
#
# def test_Is_empty():
#     stack = Stack()
#     print( stack.is_empty())
#
# def test_Push():
#     stack = Stack()
#     print("stack.is_empty():", stack.is_empty())
#
#     stack.push(3)
#     stack.push(2)
#     stack.push(1)
#     print("stack.is_empty():", stack.is_empty())
#     return stack
#
# def test_Pop():
#     stack = Stack()
#     print("stack.is_empty():", stack.is_empty())
#     print(stack.pop())
#     stack.push(3)
#     stack.push(2)
#     stack.push(1)
#     print("stack.is_empty():", stack.is_empty())
#
#     print(stack.pop())
#     print(stack.pop())
#     print(stack.pop())
#     print(stack.pop())
#
# def test_Peek():
#     stack = test_Push()
#     print(stack.peek())
#
#     stack.push(5)
#     print(stack.peek())
#
#     stack.push(7)
#     print(stack.peek())
#
#
# if __name__ =="__main__":
#     # test_Is_empty()
#     # test_Push()
#     # test_Pop()
#     test_Peek()
#     pass
#
#















'''
# # ------------------------------------------------------------
# # # 6、栈
# # # # Stack()         创建一个新的空栈
# # # # push(item)      添加一个新的元素item到栈顶
# # # # pop()           弹出栈顶元素 
# # # # peek()          返回栈顶元素
# # # # is_empty()      判断栈是否为空
# # # # size() 返回栈的元素个数
# # ------------------------------------------------------------
'''

# Stack() 创建一个新的空栈
# push(item) 添加一个新的元素item到栈顶
# pop() 弹出栈顶元素
# peek() 返回栈顶元素
# is_empty() 判断栈是否为空
# size() 返回栈的元素个数

class Stack():
    def __init__(self):
        self.item = []

    def push(self, item):
        """
        添加一个新的元素item到栈顶
        :param item:
        :return:
        """
        self.item.insert(0,item)    # 最开始的位置

    def pop(self):
        """弹出元素"""
        try:
            return self.item.pop(0)
        except:
            return None
        # pass

    def peek(self):
        """
        返回栈顶元素
        :return:
        """
        try:
            return self.item[0]
        except:
            return None

    def is_empty(self):
        """判断是否为空"""
        return self.item == []
        # 以下的写法都是错误的
        #   return self.item == None
        #   return self.item is []
    def size(self):
        """
        返回栈的元素个数
        :return:
        """
        return len(self.item)

def test_Is_empty():
    stack = Stack()
    print( stack.is_empty())

def test_Push():
    stack = Stack()
    print("stack.is_empty():", stack.is_empty())

    stack.push(3)
    stack.push(2)
    stack.push(1)
    print("stack.is_empty():", stack.is_empty())
    return stack

def test_Pop():
    stack = Stack()
    print("stack.is_empty():", stack.is_empty())
    print(stack.pop())
    stack.push(3)
    stack.push(2)
    stack.push(1)
    print("stack.is_empty():", stack.is_empty())

    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())

def test_Peek():
    stack = test_Push()
    print(stack.peek())

    stack.push(5)
    print(stack.peek())

    stack.push(7)
    print(stack.peek())

def test_Size():
    stack = test_Push()
    print(stack.size())

if __name__ =="__main__":
    # test_Is_empty()
    # test_Push()
    # test_Pop()
    # test_Peek()
    test_Size()
    pass
