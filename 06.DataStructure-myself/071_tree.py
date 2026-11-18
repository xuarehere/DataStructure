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
# # # 1、二叉树的节点表示以及树的创建
# # # #
# # ------------------------------------------------------------
'''
class Node(object):
    ''''''
    def __init__(self, item, lchild, rchild):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    def __init__(self, root=None):
        self.root  = root

    def add(self, elem):
        node = Node(elem)
        if self.root is  None:
            self.root = elem
        else:
            queue = []
            queue.append(self.root)

            cur = queue.pop(0)  # when poping , the element will be none?
            if cur.lchild is None:
                cur.lchild = node
                return

            elif cur.rchild is None:
                cur.rchild = node
                return
            else:
                queue.append(cur.lchild)
                queue.append(cur.rchild)

