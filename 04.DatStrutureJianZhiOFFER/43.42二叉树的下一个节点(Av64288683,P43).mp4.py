# -*- coding:utf-8 -*-
# 43.42二叉树的下一个节点(Av64288683,P43).mp4

'''
题目描述
	给定一个二叉树和其中的一个结点，请找出中序遍历顺序的下一个结点并且返回。注意，树中的结点不仅包含左右子结点，同时包含指向父结点的指针。

这个题目有点奇怪，只有节点

不会原因分析：：
1、看到这个的时候，没有认真分析题目，导致一种一个做不出来
2、另外一个原因是因为对二叉树的不熟悉，许多题目看到的时候，感觉就已经做不错来了

思路：
1、输入的节点，它上有父节点，下有子节点的情况
2、输入的节点是叶结点，它上有父节点，下没有子节点


# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here


'''

'''
下面代码没有通过

问题出在那里
已经发现，下面代码的BUG出现在哪儿，下面

'''
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here

        '''
        根节点
        给定节点是父节点的左子树： 返回的下一个节点是父节点
        给定节点是父节点的右子树： 返回的是父节点的父节点

        :param pNode:
        :return:
        '''
        # 1.寻找右子树, 如果存在就一直找到右子树的最左边就是下一个节点 *\
        # 2.没有右子树, 就寿找他的父节点, 一直找到它是父节点的左子树, 打印父节点
        if pNode.right:
                tmpNode = pNode.right
                while tmpNode.left:
                    tpmNode = tmpNode.left
                return tmpNode
        else:
            tmpNode = pNode
            while tmpNode.next:
                if tmpNode.next.left == tmpNode:
                    return tmpNode.next
                tmpNode = tmpNode.next
            return None






'''
修复上面的bug
以下是通过的代码


'''
# -*- coding:utf-8 -*-
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None
class Solution:
    def GetNext(self, pNode):
        # write code here

        '''
        根节点
        给定节点是父节点的左子树： 返回的下一个节点是父节点
        给定节点是父节点的右子树： 返回的是父节点的父节点

        :param pNode:
        :return:
        '''
        # 1.寻找右子树, 如果存在就一直找到右子树的最左边就是下一个节点 *\
        # 2.没有右子财, 就寿找他的父节点, 一直找到它是父节点的左子树, 打印父节点
        if pNode.right:
                tmpNode = pNode.right
                while tmpNode.left:
                    tmpNode = tmpNode.left
                return tmpNode
        else:
            tmpNode = pNode
            while tmpNode.next:
                if tmpNode.next.left == tmpNode:
                    return tmpNode.next
                tmpNode = tmpNode.next
            return None
