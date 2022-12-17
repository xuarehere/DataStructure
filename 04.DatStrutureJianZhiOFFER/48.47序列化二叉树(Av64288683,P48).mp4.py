
# 48.47序列化二叉树(Av64288683,P48).mp4

'''
题目描述
请实现两个函数，分别用来序列化和反序列化二叉树

二叉树的序列化是指：把一棵二叉树按照某种遍历方式的结果以某种格式保存为字符串，从而使得内存中建立起来的二叉树可以持久保存。序列化可以基于先序、中序、后序、层序的二叉树遍历方式来进行修改，序列化的结果是一个字符串，序列化时通过 某种符号表示空节点（#），以 ！ 表示一个结点值的结束（value!）。

二叉树的反序列化是指：根据某种遍历顺序得到的序列化字符串结果str，重构二叉树。




'''
# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        retList = []
        def preOrder(root):
            if root == None:
                retList.append('#')
            # elif root.left == None and root.right == None:
            #     retList.append('!')
            #     return ret
            retList.append( str(root.val) )
            preOrder(root.left)
            preOrder(root.right)
            # return ret
        # preOrder(root)
        return ' '.join(retList)

    def Deserialine(self,s ):
        # write code here
        retList = s.split()
        def dePreOrder():
            if retList == []:
                return None
            rootVal = retList[0]
            del retList[0]
            if rootVal == '#':
                return None
            node = TreeNode( int(rootVal))

            nodeLeft  = dePreOrder()
            nodeRight = dePreOrder()

            node.left = nodeLeft
            node.right = nodeRight
            return node

        pRoot = dePreOrder()
        return pRoot


'''
采用层次遍历法，没有做出来

'''


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self):
        self.rootStr = ''

    def Serialize(self, root):
        # write code here
        if not root:
            return None
        stack1 = [root]
        stack2 = []
        retRootStr = ''
        # 以 ！ 表示一个结点值的结束（value!）。???
        while stack1 or stack2:
            if stack1:
                tmpStr = ''
                while stack1:
                    tmpNode = stack1.pop(0)
                    if tmpNode:
                        tmpStr = tmpStr + str(tmpNode.val)
                    else:
                        tmpStr = tmpStr + '#'
                    # if tmpNpde.left:
                    stack2.append(tmpNode.left)
                    # if tmpNpde.right:
                    stack2.append(tmpNode.right)

                retRootStr += tmpStr + '!'
            if stack2:
                tmpStr = ''
                while stack2:
                    tmpNode = stack2.pop(0)
                    if tmpNode:
                        tmpStr = tmpStr + str(tmpNode.val)
                    else:
                        tmpStr = tmpStr + '#'
                    # if tmpNpde.left:
                    stack1.append(tmpNode.left)
                    # if tmpNpde.right:
                    stack1.append(tmpNode.right)

                retRootStr += tmpStr + '!'

        self.rootStr = retRootStr

    def Deserialize(self, s):
        # write code here
        if not s:
            return None

        sLen = len(s)
        retHead = TreeNode(eval(s[0]))
        count = 1
        retTmp = retHead
        stack1 = [retTmp]
        stack2 = []
        retRootStr = ''
        # 以 ！ 表示一个结点值的结束（value!）。???
        while stack1 or stack2:
            if stack1:
                tmpStr = ''
                while stack1:
                    tmpNode = sLen[count]
                    if tmpNode == '#':
                        newNode = None
                    elif tmpNode != '#' and tmpNode != '!':
                        newNode = TreeNode(eval(s[count]))
                    # if tmpNpde.left:
                    stack2.append(tmpNode.left)
                    # if tmpNpde.right:
                    stack2.append(tmpNode.right)

                retRootStr += tmpStr + '!'
            if stack2:
                tmpStr = ''
                while stack2:
                    tmpNode = stack2.pop(0)
                    if tmpNode:
                        tmpStr = tmpStr + str(tmpNode.val)
                    else:
                        tmpStr = tmpStr + '#'
                    # if tmpNpde.left:
                    stack1.append(tmpNode.left)
                    # if tmpNpde.right:
                    stack1.append(tmpNode.right)

                retRootStr += tmpStr + '!'

        self.rootStr = retRootStr
