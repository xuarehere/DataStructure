# -*- coding:utf-8 -*-
'''
29.28丑数(Av64288683,P29).mp4



**把只包含质因子2、3和5的数称作丑数（Ugly Number）。例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。求按从小到大的顺序的第N个丑数。**

思路1： 除法。除以丑数的因子，除到底，做出来，时间复杂度太大
思路2: 乘法。空间换时间。生成所有丑数的列表，最后返回对应序号所包含的值就可以了


'''


# -*- coding:utf-8 -*-
class Solution:
	def GetUglyNumber_Solution(self, index):
		# write code here
		if index < 1:
			return None
		elif index == 1:
			return 1
		count = 1
		num = 2
		numTmp = 2
		while index != count:
			numTmp = num
			while (numTmp % 2 == 0) or (numTmp % 3 == 0) or (numTmp % 5 == 0):
				if numTmp % 2 == 0:
					numTmp //= 2

				elif numTmp % 3 == 0:
					numTmp //= 3

				else:
					numTmp //= 5

			if numTmp == 1:
				count += 1
			num += 1

		return num



def GetUglyNumber_Solution( index):
	# write code here
	if index < 1:
		return None
	elif index == 1:
		return 1
	count = 1
	num = 1
	numTmp = 2
	while index != count:
		num += 1
		numTmp = num
		while (numTmp % 2 == 0) or (numTmp % 3 == 0) or (numTmp % 5 == 0):
			if numTmp % 2 == 0:
				numTmp //= 2

			elif numTmp % 3 == 0:
				numTmp //= 3

			else:
				numTmp //= 5

		if numTmp == 1:
			count += 1


	return num

# '''
# print(GetUglyNumber_Solution(1000),end="  ")		# 51200000
# '''
#
# for i in  range(1, 20):
# 	print(i, "\t", end="")
#
# print( )
# for i in range(1, 20):
# 	print(GetUglyNumber_Solution(i),"\t",end="")		# 51200000
#



'''
解法2: 
乘法

步聚1:  1 * 2 =2, 1*3 =3，1*5 =5，那么三个数中比较大小，存放最小 2
步聚2:  2 * 2 =4, 1*3 =3，1*5 =5，那么三个数中比较大小，存放最小 3
步聚3:  2 * 2 =4, 2*3 =6，2*5 =5，那么三个数中比较大小，存放最小 4


'''
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        #首先判断  要找的 丑数 是不是第0个 或者是负数，如果是的话，那么就返回0
        if index <= 0:
            return 0
        #然后判断要找的丑数 是不是第一个，如果是第一个，那么就返回1.
        if index == 1:
            return 1
        #在丑数 这个列表中 给出第一个丑数是1
        numbers = [1]
        #在列表的 一开始  设置三个 指针，也就是 三个指针的 索引位置是0，
        two, three, five = 0, 0, 0
        #丑数的个数 起始为 1
        count = 1
        #循环 当丑数的个数不等于我们要找到 那第 index 个 丑数时，就循环，等于的时候就跳出循环。
        while count != index :
            #给列表中的 2,3,5 这三个指针所在位置的 丑数 分别 乘以2,3,5
            n2, n3, n5 = numbers[two] * 2, numbers[three] * 3, numbers[five] * 5
            #比较这三个丑数的大小
            minValue = min(n2, n3, n5)
            #在丑数列表中，把三个中最小的那个 放进去。
            numbers.append(minValue)
            #每放进去一个，丑数的数量就加1
            count += 1
            #这个是指针移位的，如果说我们比较出来的 三个数中最小的丑数是 2 指针的话，那么2 指针就往前移动一位
            '''
            需要注意下面的移动是 if，而不是  elif；因为当n？产生的值都相等的时候，都要移动.如： minValue =6的时候
            '''
            if minValue == n2:
                two += 1
            #如果是 3 那个指针的话，那么3 这个指针就移一位。
            if minValue == n3:
                three += 1
            #如果是 5 那个指针的话，那么5这个指针就移一位。
            if minValue == n5:
                five += 1
        #最后输出这个丑数列表中的 最后一位，那么就是我们的计数的丑数的个数 -1，就是最后一个丑数的索引值。
        return numbers[count-1]

