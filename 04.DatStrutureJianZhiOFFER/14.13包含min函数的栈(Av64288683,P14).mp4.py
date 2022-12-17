# -*- coding:utf-8 -*-

'''
14.13包含min函数的栈(Av64288683,P14).mp4


## 4.包含min 函数的栈[^本题考点 *栈*]

**定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。**

'''

# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.minValue = []
    # 给栈中推进去数值，推进去元素node，添加函数
    def push(self, node):
        self.stack.append(node)
        #如果最小值列表里有值
        if self.minValue:
            #如果最小值列表里的最后一个值 大于 node 这个值，说明node这个值小，
            # 那么就放进最小值列表中；
            if self.minValue[-1] > node:
                self.minValue.append(node)
             #如果列表里面的最后一个值，小于node值，那么就说明node这个值大；那么就添加上次添加进来的那个小的值，与栈中的数据长度保持一致；
            else:
                self.minValue.append(self.minValue[-1])
        #如果最小值列表里面没有值，就在最小值列表里添加node
        else:
            self.minValue.append(node)
    #给栈中做删除操作
    def pop(self):
        #如果说栈中是空值得话那么就返回none，说明没有在栈中压值进来，没有最小值
        if self.stack == []:
            return None
        #栈的长度与最小值的栈的长度要相同，所以最小值列表也需要删除一个
        self.minValue.pop()
        #有值得话，就需要删除一个，删除做pop 操作；返回我们删除的那个数
        return self.stack.pop()
    #栈顶
    def top(self):
        #如果栈里没有数值的话，就返回一个空
        if not self.stack:
            return None
        #否则栈里有数，那么就返回栈顶的那个数
        return self.stack[-1]
   	#取出最小值，那么就是我们minvalue 中的最后一个值为最小值
    def min(self):
        #如果为空的话，就说明没有值，返回none
        if self.minValue == []:
            return None
        return self.minValue[-1]
test = Solution()
test.push(4)
test.push(3)
test.push(10)
test.push(5)

print()