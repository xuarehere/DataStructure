# -*- coding:utf-8 -*-

'''
12.11调整数组顺序使奇数位于偶数前面(Av64288683,P12).mp4




## 9. 调整数组顺序使奇数位于偶数前面       [^本题知识点 *数组*]

**输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，。**
偶数和偶数之间的相对位置不变

题目描述
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。


用例:
[1,2,3,4,5,6,7]

对应输出应该为:

[1,3,5,7,2,4,6]

'''


class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        while array:
            if array[0] % 2 == 0 :
                even.append(array.pop(0))
            else:
                odd.append(array.pop(0))
        while even:
            odd.append(even.pop(0))
        return odd


def sort(array):
    l = len(array)
    for i in range(0, l-1):
        for j in range(0, l-1 -i ):
            # if array[j] > array[j+1]:
            if array[j] % 2==0 and  array[j+1]%2 !=0:
                array[j],  array[j+1] = array[j+1],  array[j]
    return array



a = [1,2,3,4,5,6,7]
print(sort(a))


