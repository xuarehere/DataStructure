# -*- coding:utf-8 -*-
'''
15.14栈的压入弹出序列(Av64288683,P15).mp4


## 10.栈的压入，弹出序列  [^本题考点 *栈*]

**
输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。
假设压入栈的所有数字均不相等。例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，
但4,3,5,1,2就不可能是该压栈序列的弹出序列。（注意：这两个序列的长度是相等的）
**

1,2,3,			4,5
4,5,			3,2,1

4,3,5,1,2

'''


def IsPopOrder(pushV, popV):
	'''
	以下的代码是有问题的
	:param pushV:
	:param popV:
	:return:
	'''
	# write code here
	'''
	1,2,3,4,5
	4,5,3,2,1
	'''

	pushPop = []

	while pushV:
		if pushV[0] == popV[-1]:
			pushV.pop(0)
			popV.pop(-1)

		else:
			pushPop.append(pushV.pop(-1))

			if pushPop[-1] == popV[-1] and pushPop != []:
				pushPop.pop(-1)
				popV.pop(-1)

	return popV == []


# pushV = [1, 2, 3, 4, 5]
# popV  = [4, 5, 3, 2, 1]
#
# pushV = [1,2,3,4,5]
# popV = [3,5,4,2,1]
# print( IsPopOrder(pushV, popV) )
#



# -*- coding:utf-8 -*-
class Solution:
	def IsPopOrder(self, pushV, popV):
		'''
		通过的代码
		:param pushV:
		:param popV:
		:return:
		'''
		# write code here
		'''
		1,2,3,4,5
		4,5,3,2,1
		'''
		if pushV == [] or popV == []:
			return None

		pushPop = []

		while pushV:
			# 只操作 pushV 栈
			# 正常的逆序操作
			if pushV[0] == popV[-1]:
				pushV.pop(0)
				popV.pop(-1)

			# 非常的逆序操作
			else:

				pushPop.append(pushV.pop(-1))
				while pushPop and pushPop[-1] == popV[-1]:
					if pushPop[-1] == popV[-1]:
						pushPop.pop(-1)
						popV.pop(-1)

		return popV == []

pushV = [1,2,3,4,5]
popV = [3,5,4,2,1]
# pushV = [1,2,3,4,5]
# popV = [4,5,3,2,1]
a = Solution()
print( a.IsPopOrder(pushV, popV) )
