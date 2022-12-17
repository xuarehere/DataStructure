# -*- coding:utf-8 -*-
"""
303. 区域和检索 - 数组不可变
难度
简单

179

收藏

分享
切换为英文
关注
反馈
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。


"""


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        # 先创建列表空间
        '''
        self.sums = [0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            self.sums[i] = self.sums[i-1] + nums[i-1]
        '''
        # 利用append实现动态计算累加值，动态添加至列表
        self.sums = [0]
        for i in range(len(nums)):
            self.sums.append(nums[i] + self.sums[i])
        print(self.nums)
        print(self.sums)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j + 1] - self.sums[i]


# 作者：yu - fa - tang - you - dian - tian
# 链接：https: // leetcode - cn.com / problems / range - sum - query - immutable / solution / 303
# pythondong - tai - ji - suan - lei - jia - li - yong - huan - cun /
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

#
# class NumArray:
#
#     def __init__(self, nums):
#         self.list = nums
#         if not self.list:
#             return self.list
#
#         self.sumList = [0] * len(self.list)
#         print(self.sumList)
#         for i in range(0, len(self.list)):
#             if i == 0:
#                 self.sumList[i] = self.list[i]
#             else:
#                 self.sumList[i] = self.sumList[i - 1] + self.list[i]
#
#         print(self.list)
#         print(self.sumList)
#     def sumRange(self, i, j) :
#         if i == 0:
#             return self.sumList[j]
#         else:
#             return self.sumList[j] - self.sumList[i - 1]


if __name__ == '__main__':
    nums = [-2, 0, 3, -5, 2, -1]
    a = NumArray(nums)
    i,j = 0,2
    # print( a.sumRange(i,j))


"""
# 作者：yu-fa-tang-you-dian-tian
# 链接：https://leetcode-cn.com/problems/range-sum-query-immutable/solution/303pythondong-tai-ji-suan-lei-jia-li-yong-huan-cun/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""