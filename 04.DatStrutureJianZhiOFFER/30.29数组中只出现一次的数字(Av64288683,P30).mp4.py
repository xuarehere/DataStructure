# -*- coding:utf-8 -*-
'''
30.29数组中只出现一次的数字(Av64288683,P30).mp4

## 22.数组中只出现一次的数字[^数组]



**一个整型数组里除了两个数字之外，其他的数字都出现了偶数次。请写程序找出这两个只出现一次的数字。**

解法1：排序后，后进行检查
查找思路


解法二
抵消思路
采用两个队列，进行处理



解法3：见 对应的 md 文档
抵消思路
采用异或的方式

'''

'''
解法1：排序后，后进行检查
'''
# -*- coding:utf-8 -*-
class Solution:
	# 返回[a,b] 其中ab是出现一次的两个数字
	def FindNumsAppearOnce(self, array):
		# write code here
		import copy
		l = len(array)
		if l == 2:
			if array[0] != array[1]:
				return array
		elif l < 2:
			return None

		arrayTmp = copy.deepcopy(array)

		# for i in range()
		for j in range(0, l - 1):
			count = 0
			for i in range(0, l - 1):
				if arrayTmp[i] > arrayTmp[i + 1]:
					arrayTmp[i], arrayTmp[i + 1] = arrayTmp[i + 1], arrayTmp[i]
					count += 1

			if count == 0:
				break

		print(arrayTmp)
		i = 0
		while len(arrayTmp) != 2:
			if len(arrayTmp) < 2:
				return None
			if arrayTmp[i] == arrayTmp[i + 1]:
				arrayTmp.pop(i)
				arrayTmp.pop(i)
			else:
				i += 1

		return arrayTmp



'''
解法二
采用两个队列，进行处理
'''


def FindNumsAppearOnce( array):
	# write code here
	import copy
	l = len(array)
	if l == 2:
		if array[0] != array[1]:
			return array
	elif l < 2:
		return None

	arrayTmp = copy.deepcopy(array)
	ret = []
	retIndex = 0
	while arrayTmp:
		ret.append(arrayTmp.pop(0))

		retIndex = 0
		print(ret)
		print(arrayTmp)
		print("".center(50, "-"))
		while retIndex < len(ret) and (arrayTmp !=[]) :
			if ret[retIndex] == arrayTmp[0]:
				ret.pop(retIndex)
				arrayTmp.pop(0)
				retIndex =0
			else:
				retIndex +=1
	return ret
#
# '''
# 用例:
# [2,4,3,6,3,2,5,5]
#
# 对应输出应该为:
#
# "4,6"
#
# '''
# array = [2,4,3,6,3,2,5,5]
#
# print( "==>", FindNumsAppearOnce( array) )

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        import copy
        l = len(array)
        if l == 2:
            if array[0] != array[1]:
                return array
        elif l < 2:
            return None

        arrayTmp = copy.deepcopy(array)
        ret = []
        retIndex = 0
        while arrayTmp:
            ret.append(arrayTmp.pop(0))

            retIndex = 0
            print(ret)
            print(arrayTmp)
            print("".center(50, "-"))
            while retIndex < len(ret) and (arrayTmp !=[]) :
                if ret[retIndex] == arrayTmp[0]:
                    ret.pop(retIndex)
                    arrayTmp.pop(0)
                    retIndex =0
                else:
                    retIndex +=1
        return ret

'''
解法3

1、所有的数字，彼此之间进行异或。结果是两个相异的数字A,B异或的
2、mask用来辨别结果中两个数。找到A，B中最大的那个数的二进制中，最高位的位置，创建两个数的mask
3、用mask对原来的数组，进行查找A，B。用mask，对原来的数字进行分组，分别进行异或，找到A，B数字
'''

# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        #如果两个数相同那么两个数的异或操作为0
        #数组的长度如果小于2，那么就就不会有数字出现了偶数次。
        if len(array) < 2:
            return None

        # 变量赋值 两个数的异或为none
        twoNumXor = None
        # 遍历 数组中的数字
        for num in array:
            #判断 如果 两个数的数字异或的结果为0 的话，
            if twoNumXor == None:
                #那么 此时就让 两个数异或中的一个数 为此时遍历出来的那个数。
                twoNumXor = num
            #如果数 这个数不为 空 的话
            else:
                #那么就让这个 两个数异或的结果的值 （或者当 异或的值为空的时候，我们赋给的值 与 此时遍历数组中的数得到的 num 来异或。
                twoNumXor = twoNumXor ^ num
        # 变量  计数 为 0
        count = 0
        # 当异或的 结果 为偶数时
        while twoNumXor % 2 == 0 :
            #那么我们就给它 除以2 ，每除一次2 就记录一次，直到 结果不为 奇数 为止。
            twoNumXor  = twoNumXor >> 1  # 右移以为 相当于 除以2
            count += 1
        # 以上是用来计数  判断 这个 二进制数中 第一个1 是在哪一位上。
        # 我们在这个结果中 找到 第一个为1 的位的位置，记为 第 n 位，那么 现在我们以第n 位 是不是 1

        mask = 1 << count   #向左 移 位 count 位。

        # 为标准 把原 数组中的数字分成两个子数组，第一个数组中每个数字的第n 位 都是1，
		# 而 第 二个子 数组中的 每个数字的第 n 位 都是 0.
		# 由于我们的分配的标准是 数字中的某一位是0 还是1 ，
		# 那么数字相同的数肯定被分到了 同一组，那么每个 子数组中 都会包含一个 只 出现一次的数字，
		# 而 其他数字都出现了两次，这个时候，分别把 子数组中的 所有的数 异或，那么 最后的结果 就是 那个 出现一次的数。

        firstNum = None
        secondNum = None

        for num in array:
            if mask & num == 0:
                if firstNum == None:
                    firstNum = num
                else:
                    firstNum = firstNum ^ num
            else:
                if secondNum == None:
                    secondNum = num
                else:
                    secondNum = secondNum ^ num

        return firstNum,secondNum
if __name__ == '__main__':
    print(3^3)