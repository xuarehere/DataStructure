# -*- coding:utf-8 -*-

'''
8.07替换空格(Av64288683,P8).mp4


## 5.替换空格[^本题考点 *字符串*]

**请实现一个函数，将一个字符串中的每个空格替换成`“%20”`。例如，当字符串为`We Are Happy`.则经过替换之后的字符串为`We%20Are%20Happy`。**

解决方式一：
	字符串 replace 函数

解决方式二：
	用列表

'''

#
# # s 源字符串
# def replaceSpace(s):
#
#     # write code here
#     return s.replace(' ', '%20')
#
#
# # s 源字符串
# def replaceSpace(s):
# 	# write code here
# 	return s.replace(' ', '%20')

def replaceSpace(s):
    if not s or len(s)==0:
        return None
    retS = ''
    for i in s:
        if i==' ':
            retS +="%20"
        else:
            retS +=i
    return retS

s= 'We Are Happy'
print( replaceSpace(s))
