# -*- coding:utf-8 -*-
# 46.45把二叉树打印成多行(Av64288683,P46).mp4

'''
题目描述
从上到下按层打印二叉树，同一层结点从左至右输出。每一层输出一行。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    retList = []

    def Print(self, pRoot):
        # write code here
        if pRoot == None:
            return []
        queue1 = [pRoot]
        queue2 = []
        retList = []

        while queue1 or queue2:
            tmpList = []
            while queue1:
                tmp = queue1[0]
                del queue1[0]
                tmpList.append(tmp.val)
                if tmp.left:
                    queue2.append(tmp.left)
                if tmp.right:
                    queue2.append(tmp.right)
            if tmpList:
                retList.append(tmpList)

            tmpList = []
            while queue2:
                tmp = queue2[0]
                del queue2[0]
                tmpList.append(tmp.val)
                if tmp.left:
                    queue1.append(tmp.left)
                if tmp.right:
                    queue1.append(tmp.right)
            if tmpList:
                retList.append(tmpList)
        return retList

'''
用例:
{8,6,10,5,7,9,11}

对应输出应该为:

[[8],[6,10],[5,7,9,11]]

你的输出为:

[[8],[6,10],[5,7,9,11],[]]
'''
# def createTree():
#     # num = [8,6,10,5,7,9,11]
#     num = [[8], [6, 10], [5, 7, 9, 11]]
#     i = 0
#     node = TreeNode(num[0][0])
#     del num[0]
#
#     for nodeH in num:
#         # if i ==0:
#         #     pass
#         # else :
#         while nodeH:
#             nodeVal= nodeH[0]
#             del nodeH[0]
#             nodeTmp = TreeNode(nodeVal)
#
#         if i % 2 :
#             node.left = nodeTmp
#         else:
#             node.right = nodeTmp
#         i +=1
#     return node
#
# def testPrint(node):
#     test = Solution()
#     retList  = test.Print(node)
#     print( retList)


if __name__ == '__main__':
    # node = createTree()
    # # print(node)
    # # testPrint( node)
    pass

