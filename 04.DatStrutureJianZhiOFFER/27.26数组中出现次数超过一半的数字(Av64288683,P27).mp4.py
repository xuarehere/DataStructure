# -*- coding:utf-8 -*-


'''
27.26数组中出现次数超过一半的数字(Av64288683,P27).mp4
## 21.数组中出现次数超过一半的数字[^本题考点 数组]

**数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。例如输入一个长度为9的数组{1,2,3,2,2,2,5,4,2}。由于数字2在数组中出现了5次，超过数组长度的一半，因此输出2。如果不存在则输出0。**


'''


# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        '''
        import copy
        # alistTemp = alist
        alistTemp = copy.deepcopy(numbers)
        saveList = []
        while alistTemp:
            if saveList == []:
                saveList.append(alistTemp.pop(0))
            elif saveList[0] != alistTemp[0]:
                saveList.pop(0)
                alistTemp.pop(0)
            else:
                saveList.append(alistTemp.pop(0))
        if saveList == []:
            return  0
        else:
            # print(saveList)
            count =0
            for ele in numbers:
                if  ele == saveList[0]:
                    count +=1
                    if count > len(numbers)//2:
                        return ele
            return 0
        '''
        numsCount = {}
        numLen = len(numbers)
        for num in numbers:
            if num in numsCount:
                numsCount[num] += 1
            else:
                numsCount[num] = 1
             #如果说字典中某个键 大于 我们这个数组长度的一半，那么就返回这个键， 数组长度的一半 可以用 >> 1右移以为来实现，右移以为相当于 是除以2.
            if numsCount[num] > (numLen >> 1):
                return num
        return 0