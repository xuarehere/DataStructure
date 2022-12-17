# -*- coding:utf-8 -*-
'''
10.09旋转数组的最小数字-1(Av64288683,P10).mp4




## 2. 旋转数组的最小数字 [^本题考点 查找]

**把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 输入一个非减排序的数组的一个旋转，
输出旋转数组的最小元素。 例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。**


难点：
1、二分法查找
2、边界问题，什么时候要返回
3、如果有值相等的临界条件

'''
#
# # # -*- coding:utf-8 -*-
#
# class Solution:
#     def minNumberInRotateArray(self, rotateArray):
#         # write code here
#         if len( rotateArray) ==0 :
#             return 0
#         minValue = rotateArray[0]
#         for i in range(1, len(rotateArray)):
#             if minValue > rotateArray[i]:
#                 minValue = rotateArray[i]
#         return minValue

'''
这个解法是有bug的
'''
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        '''
        if len( rotateArray) ==0 :
            return 0
        minValue = rotateArray[0]
        for i in range(1, len(rotateArray)):
            if minValue > rotateArray[i]:
                minValue = rotateArray[i]
        return minValue
        '''

        if not rotateArray:
            return 0
        left = 0
        right = len(rotateArray) - 1
        while left <= right:
            mid = (left + right) >> 1
            # 如果说中间的数的上一个数 > 中间数，那么就说明，我们要找的数就是这个中间的数，返回这个数。
            if rotateArray[mid - 1] > rotateArray[mid]:
                return rotateArray[mid]
            # 如果说中间的数 < 中间数的上一个数，那么就说明，我们要找的数在二分法的左侧，所以右侧取值的索引需要改变为中间的索引-1；因为越往左索引值越小
            elif rotateArray[mid] < rotateArray[right]:
                right = mid - 1
            # 否则就说明，我们要找的数在二分法的右侧，所以左侧取值的索引需要改变为中间的索引+1；因为越往右索引值越小
            else:
                left = mid + 1
        return 0


a = Solution()
alist = [3,4,5,1,2]
alist = [3, 4, 5, 1, 1, 2]
alist = [4,5,6,1,2,2,2,2,2,2,2,2,2,3]

# alist = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]

print(alist)
print( a.minNumberInRotateArray(alist))




'''
下面的代码有bug

'''
# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if not rotateArray:
            return 0

        lIndex = 0
        rIndex = len(rotateArray) - 1

        while lIndex <= rIndex:
            midIndex = (lIndex + rIndex) >> 1
            if rotateArray[midIndex - 1] > rotateArray[midIndex]:
                return rotateArray[midIndex]
            # right
            if rotateArray[lIndex] < rotateArray[midIndex]:
                lIndex = midIndex
                # left
            # else rotateArray[midIndex] < rotateArray[rIndex]:
            else:
                rIndex = midIndex - 1
        # return rotateArray[midIndex]
        return 0

#
# a = Solution()
# alist = [3,4,5,1,2]
# alist = [6501,6828,6963,7036,7422,7674,8146,8468,8704,8717,9170,9359,9719,9895,9896,9913,9962,154,293,334,492,1323,1479,1539,1727,1870,1943,2383,2392,2996,3282,3812,3903,4465,4605,4665,4772,4828,5142,5437,5448,5668,5706,5725,6300,6335]
#
# print(alist)
# print( a.minNumberInRotateArray(alist))
#



