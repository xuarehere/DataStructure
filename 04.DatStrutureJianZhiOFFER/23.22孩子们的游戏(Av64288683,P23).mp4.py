# -*- coding:utf-8 -*-
'''
23.22孩子们的游戏(Av64288683,P23).mp4
## 17.圆圈中最后剩下的数 [^本题考点 *模拟*]

**每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。
其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那个
小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....这样下去....直到剩下最
后一个小朋友,可以不用表演,并且拿到牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,哪个小朋友会得到这份礼品呢？
(注：小朋友的编号是从0到n-1)**


思路1：
看剑指offer书籍
1、用同样长度的列表

思路2：
用环形链表

思路3：
找规律，用递归公式


'''


# -*- coding:utf-8 -*-
class Solution:
	def LastRemaining_Solution(self, n, m):
		# write code here
		if n < 1 or m < 1:
			return -1
		elif n == 1:
			return 1
		alist = []
		tmpN = n
		tmpM = m
		for i in range( tmpN):
			alist.append(i)
		j = 0
		while True:
			j += tmpM - 1
			if len(alist) == 1:
				return alist[0]
			elif j < len(alist):
				alist.pop(j)
			else:
				while j >= len(alist):
					j = j - len(alist)
				alist.pop(j)



print(  Solution().LastRemaining_Solution(8, 3) )
