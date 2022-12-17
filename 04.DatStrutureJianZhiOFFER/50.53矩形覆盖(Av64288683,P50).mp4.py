
''''
50.53矩形覆盖(Av64288683,P50).mp4
题目描述
我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''
# -*- coding:utf-8 -*-
class Solution:
    def rectCover(self, number):
        # write code here
        if number == 0:
            return 0
        if number == 1:
            return 1
        elif number == 2:
            return 2

        a = 1
        b = 2
        for i in range(3, number + 1):
            b = a + b
            a = b - a

        return b


class Solution1:
    def rectCover(self, number):
        # write code here
        if number ==None or number < 0:
            return None
        elif number ==0:
            return 0
        if number == 1:
            return 1
        elif number == 2 :
            return 2
        a = 1
        b = 2
        ret =0
        for i in range(number-2):
            ret = a + b
            a,b = b, ret
        return ret



class Solution2:
    def rectCover(self, number):
        # write code here
        if number ==None or number < 0:
            return None
        elif number ==0:
            return 0
        if number == 1:
            return 1
        elif number == 2 :
            return 2
        a = 1
        b = 2
        for i in range(number-2):
            a,b = b, a + b
        return b



if __name__ == '__main__':
    test = Solution2()
    # ret = test.rectCover(3)
    # print( ret)
    print(test.rectCover(-1), 111)
    print( test.rectCover(3))
    print(test.rectCover(4))
    print(test.rectCover(5))