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
# # # 1、二叉树   广度优先遍历(层次遍历)
# # # #
# # ------------------------------------------------------------
'''
# class Node(object):
#     ''''''
#     def __init__(self, elem, lchild=None, rchild=None):
#         self.elem = elem
#         self.lchild = lchild
#         self.rchild = rchild
#
# class Tree(object):
#     """树类"""
#     def __init__(self, root=None):
#         self.root = root
#
#     def add(self, elem):
#         """为树添加节点"""
#         node = Node(elem)
#         #如果树是空的，则对根节点赋值
#         if self.root == None:
#             self.root = node
#         else:
#             queue = []
#             queue.append(self.root)
#             #对已有的节点进行层次遍历
#             while queue:
#                 #弹出队列的第一个元素
#                 cur = queue.pop(0)
#                 if cur.lchild == None:
#                     cur.lchild = node
#                     return
#                 elif cur.rchild == None:
#                     cur.rchild = node
#                     return
#                 else:
#                     #如果左右子树都不为空，加入队列继续判断
#                     queue.append(cur.lchild)
#                     queue.append(cur.rchild)
#
#     def breadth_travel(self):
#         if self.root is None:
#             return
#         queue = [self.root]
#         while queue:
#             cur_node = queue.pop(0)
#             print(cur_node.elem)
#             if cur_node.lchild is not None:
#                 queue.append(cur_node.lchild)
#             if cur_node.rchild is not None:
#                 queue.append(cur_node.rchild)
#
#     def preorder(self, node):
#         pass
#
#     def inorder():
#         pass
#
#     def postorder():
#         pass
#
#
# if __name__ =="__main__":
#     tree = Tree()
#     tree.add(1)
#     tree.add(2)
#     tree.add(3)
#     tree.add(3)
#     print(tree.root.elem)
#     print(tree.root.lchild)
#     print(tree.root.rchild)
#     tree.breadth_travel()
#     tree.breadth_travel()
#     # for i in tree.root:
#     #     print(i)
#     # tree.preorder(tree)
#
#





'''
# # ------------------------------------------------------------
# # # 2、二叉树   先序遍历
# # # #
# # ------------------------------------------------------------
'''
# class Node(object):
#     ''''''
#     def __init__(self, elem, lchild=None, rchild=None):
#         self.elem = elem
#         self.lchild = lchild
#         self.rchild = rchild
#
# class Tree(object):
#     """树类"""
#     def __init__(self, root=None):
#         self.root = root
#
#     def add(self, elem):
#         """为树添加节点"""
#         node = Node(elem)
#         #如果树是空的，则对根节点赋值
#         if self.root == None:
#             self.root = node
#         else:
#             queue = []
#             queue.append(self.root)
#             #对已有的节点进行层次遍历
#             while queue:
#                 #弹出队列的第一个元素
#                 cur = queue.pop(0)
#                 if cur.lchild == None:
#                     cur.lchild = node
#                     return
#                 elif cur.rchild == None:
#                     cur.rchild = node
#                     return
#                 else:
#                     #如果左右子树都不为空，加入队列继续判断
#                     queue.append(cur.lchild)
#                     queue.append(cur.rchild)
#
#     def breadth_travel(self):
#         if self.root is None:
#             return
#         queue = [self.root]
#         while queue:
#             cur_node = queue.pop(0)
#             print(cur_node.elem)
#             if cur_node.lchild is not None:
#                 queue.append(cur_node.lchild)
#             if cur_node.rchild is not None:
#                 queue.append(cur_node.rchild)
#
#     def preorder(self, node):
#         """
#         递归实现先序遍历
#         先序
#             根节点->左子树->右子树
#         """
#         if node == None:
#             return
#         print(node.elem, end=" ")
#         self.preorder(node.lchild)
#         self.preorder(node.rchild)
#
# def inorder():
#     pass
#
# def postorder():
#     pass
#
#
# if __name__ =="__main__":
#     tree = Tree()
#     tree.add(1)
#     tree.add(2)
#     tree.add(3)
#     tree.add(4)
#     tree.add(5)
#     tree.add(6)
#     tree.add(7)
#     print(tree.root.elem)
#     tree.breadth_travel()
#     tree.preorder(tree.root)










'''
# # ------------------------------------------------------------
# # # 2、二叉树    中序遍历
# # # #
# # ------------------------------------------------------------
'''
# class Node(object):
#     ''''''
#     def __init__(self, elem, lchild=None, rchild=None):
#         self.elem = elem
#         self.lchild = lchild
#         self.rchild = rchild
#
# class Tree(object):
#     """树类"""
#     def __init__(self, root=None):
#         self.root = root
#
#     def add(self, elem):
#         """为树添加节点"""
#         node = Node(elem)
#         #如果树是空的，则对根节点赋值
#         if self.root == None:
#             self.root = node
#         else:
#             queue = []
#             queue.append(self.root)
#             #对已有的节点进行层次遍历
#             while queue:
#                 #弹出队列的第一个元素
#                 cur = queue.pop(0)
#                 if cur.lchild == None:
#                     cur.lchild = node
#                     return
#                 elif cur.rchild == None:
#                     cur.rchild = node
#                     return
#                 else:
#                     #如果左右子树都不为空，加入队列继续判断
#                     queue.append(cur.lchild)
#                     queue.append(cur.rchild)
#
#     def breadth_travel(self):
#         if self.root is None:
#             return
#         queue = [self.root]
#         while queue:
#             cur_node = queue.pop(0)
#             print(cur_node.elem)
#             if cur_node.lchild is not None:
#                 queue.append(cur_node.lchild)
#             if cur_node.rchild is not None:
#                 queue.append(cur_node.rchild)
#
#     def preorder(self, node):
#         """
#         递归实现先序遍历
#         先序
#             根节点->左子树->右子树
#         """
#         if node == None:
#             return
#         print(node.elem, end=" ")
#         self.preorder(node.lchild)
#         self.preorder(node.rchild)
#
#     def inorder(self, node):
#         if node is None:
#             return
#         self.inorder(node.lchild)
#         print(node.elem, end=" ")
#         self.inorder(node.rchild)
#
#
#     def postorder():
#         pass
#
#
# if __name__ =="__main__":
#     tree = Tree()
#     tree.add(0)
#     tree.add(1)
#     tree.add(2)
#     tree.add(3)
#     tree.add(4)
#     tree.add(5)
#     tree.add(6)
#     tree.add(7)
#     tree.add(8)
#     tree.add(9)
#     print(tree.root.elem)
#     tree.breadth_travel()
#     tree.preorder(tree.root)
#     print()
#     tree.inorder(tree.root)
#













'''
# # ------------------------------------------------------------
# # # 3、二叉树    后序遍历
# # # #
# # ------------------------------------------------------------
'''
class Node(object):
    ''''''
    def __init__(self, elem, lchild=None, rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class Tree(object):
    """树类"""
    def __init__(self, root=None):
        self.root = root

    def add(self, elem):
        """为树添加节点"""
        node = Node(elem)
        #如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = []
            queue.append(self.root)
            #对已有的节点进行层次遍历
            while queue:
                #弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.lchild == None:
                    cur.lchild = node
                    return
                elif cur.rchild == None:
                    cur.rchild = node
                    return
                else:
                    #如果左右子树都不为空，加入队列继续判断
                    queue.append(cur.lchild)
                    queue.append(cur.rchild)

    def breadth_travel(self):
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem)
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)
            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        """
        递归实现先序遍历
        先序
            根节点->左子树->右子树
        """
        if node == None:
            return
        print(node.elem, end=" ")
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=" ")
        self.inorder(node.rchild)


    def postorder(self, node):
        """
        后序遍历 在后序遍历中，我们先递归使用后序遍历访问左子树和右子树，最后访问根节点
        左子树->右子树->根节点
        :param node:
        :return:
        """
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=" ")


if __name__ =="__main__":
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print(tree.root.elem)
    tree.breadth_travel()
    tree.preorder(tree.root)
    print()
    tree.inorder(tree.root)
    print()
    tree.postorder(tree.root)
