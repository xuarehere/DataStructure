# -*- coding:utf-8 -*-
# 49.48连续子数组的最大和(Av64288683,P49).mp4
'''
连续的数字中，连续相加的数字的和是   最大的
题目描述
HZ偶尔会拿些专业问题来忽悠那些非计算机专业的同学。今天测试组开完会后,他又发话了:在古老的一维模式识别中,常常需要计算连续子向量的最大和,当向量全为正数的时候,问题很好解决。但是,如果向量中包含负数,是否应该包含某个负数,并期望旁边的正数会弥补它呢？例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)。给一个数组，返回它的最大连续子序列的和，你会不会被他忽悠住？(子向量的长度至少是1)

分析：
这个题目的理解上存在一定的问题，不是很懂。



用例:
例子1
[1,-2,3,10,-4,7,2,-5]

对应输出应该为:

18

例子2:
{6,-3,-2,7,-15,1,2,2},
连续子向量的最大和为8


用例:
[-2,-8,-1,-5,-9]

对应输出应该为:

-1


分析：
情况1：全是正数
情况2：全是负数
情况3：有正有负
       前面累计为负的数，丢弃
思路1：
    情况1：全是正数，全部相加
    情况2：全是负数， 取负数中，最大的那个的
    情况3：有正有负，如果是正数，一定相加；如果是负数，该数以及前面某一位置相加的值大于等于0

    在实现过程中，
    一个记录过去最大，
    一个记录当前最大

思路2：
    暴力解法
    区间从1，到最大，进行求子向量求和

'''


# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        maxNum = array[0]
        tmpNum = 0
        for i in array:
            print("i , tmpNum, maxNum", i, tmpNum, maxNum)
            # if tmpNum + i < i:
            if tmpNum + i < i:
                tmpNum = i
            else:
                tmpNum += i
            if maxNum < tmpNum:
                maxNum = tmpNum
        return maxNum

'''

优化解法1
'''
# -*- coding:utf-8 -*-
class Solution1:
    def FindGreatestSumOfSubArray(self, array):
        maxNum = array[0]
        tmpNum = 0
        for i in array:
            print("i , tmpNum, maxNum", i, tmpNum, maxNum)
            # if tmpNum + i < i:
            if tmpNum < 0:
                tmpNum = i
            else:
                tmpNum += i
            if maxNum < tmpNum:
                maxNum = tmpNum
        return maxNum

if __name__ == '__main__':
    test = Solution()
    # ret = test.rectCover(3)
    # print( ret)
    # [1, -2, 3, 10, -4, 7, 2, -5]
    # print(test.FindGreatestSumOfSubArray([1, -2, 3, 10, -4, 7, 2, -5]) )
    # print(test.FindGreatestSumOfSubArray([6,-3,-2,7,-15,1,30,2]))


'''
做的不对

'''


# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return None

        arrLen = len(array)
        arrSum = []
        sumMax = array[0]

        for j in range(0, arrLen):
            for i in range(j, arrLen + 1):
                if i < arrLen:
                    if sumMax < array[i]:
                        sumMax = array[i]
                        continue
                tmpSum = sum(array[j:i])
                arrSum.append(tmpSum)
                if arrSum[-1] > sumMax:
                    sumMax = arrSum[-1]

        return sumMax


'''
暴力解法

'''
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if not array:
            return None
        arraySum = []
        arrayLen = len(array)
        for j in range(1, arrayLen + 1):
            gap = j
            for i in range(arrayLen):
                end = i + gap
                if end >= arrayLen:
                    end = arrayLen
                arraySum.append(sum(array[i:end]))
        arraySum.sort()
        return arraySum[-1]


a = [2,8,1,5,9]
s = Solution()

print( s.FindGreatestSumOfSubArray(a))
