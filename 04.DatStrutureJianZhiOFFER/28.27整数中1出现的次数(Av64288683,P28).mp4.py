# -*- coding:utf-8 -*-

'''
28.27整数中1出现的次数(av64288683,p28).mp4


**求出1~13的整数中1出现的次数,并算出100~1300的整数中1出现的次数？为此他特别数了一下1~13中包含1的数字有
1、10、11、12、13因此共出现6次,但是对于后面问题他就没辙了。acmer希望你们帮帮他,并把问题更加普遍化,可以很快的求出
任意非负整数区间中1出现的次数（从1 到 n 中1出现的次数）。**

'''

'''
暴力解法

每一次看最后的一位是不是1，是的话就统计一次


'''
# -*- coding:utf-8 -*-
class solution:
    def numberof1between1andn_solution(self, n):
        # write code here
        sum =0
        for i in range(1, n+1):
            k = i
            while k :
                if (k%10) == 1:
                    sum += 1
                k = k/10
        return sum



'''
解法二

找规律，分析0-9，在一组数中的情况
'''


class solution:
    def numberof1between1andn_solution(self, n):
        # write code here
        #循环的出口是 highvalue = 0
        #我们从最低位开始一个位一个位的来寻找 1 的可能出现的 情况次数。
        # 一开始 精准度为1.高位低位中位 先赋值为1.
        preceise = 1
        highvalue = 1
        lowvalue = 1
        midvalue =1
        #计数 后面的位数。
        count = 0
        #计数 1 的次数和
        sumnum = 0
        #循环的 出口是我们找不到最高位了，那么这个时候就说明，我们遍历到了 这个数字的最高位。
        while highvalue != 0:
            #高位 先将这个数 除以10 得到高位
            highvalue = n // (preceise * 10)
            #中位 先将这个数  与 10 取余。
            midvalue = (n // preceise)%10
            #低位 先将这个数 除以 1 那么低位就是个位后面的，没有就是0.
            lowvalue = n % preceise
            #每遍历一次 向右移一位，那么就是说 精准度要乘以10.
            preceise *= 10
            #如果这个数是0 的话，

            if midvalue == 0:
                #那么它就是高位的值，乘以 10^后面的位数 次方，但是这个时候 对于中位 来说 它是个位，后面没有位，所以是0，
                num = (highvalue)* pow(10,count)
            #如果这个数 大于1 的话，
            elif midvalue > 1:
                #那么它 就是 最高位加1 乘以 10^后面的位数 次方，
                num = (highvalue+1)*pow(10,count)
            else:
                #否则的话 它就是等于1 的情况了，对于等于1 的1情况，又是比较特殊的情况，它需要 最高位 * 它10 的后面位数个数的次方，然后要加上我们低位 的数值再加 1， 原因在上面的分析中已经给出。
                num = highvalue*pow(10,count)+(lowvalue+1)
            #最后 我们1 出现的 次数 就是这 三个 num 的和，。
            sumnum += num
            #没循环一次，这个三个就往左移一次吗，那么这个时候它们 后面的位数也就会 多一位。
            count += 1
        #最后返回这个  次数和。
        return sumnum



'''
解法二：  自己写的，有BUG
'''
# -*- coding:utf-8 -*-
# class Solution:
def NumberOf1Between1AndN_Solution( n):
    # write code here
    '''
    sum =0
    for i in range(1, n+1):
        k = i
        while k :
            if (k%10) ==1:
                sum +=1
            k =k/10
    return sum
    '''

    highValue = 1
    midValue = 1
    lowValue = 1
    count = 0
    sumNum = 0
    percent = 10
    while highValue != 0:

        '''
        highValue = n // pow(10, count )
        midValue  = ( n // pow(10, count-1 ) ) % 10
        lowValue  = n % pow(10, count-1 ) 
        '''
        highValue = n // percent
        midValue = (n // (percent / 10)) % 10
        lowValue = n % (percent / 10)
        percent  *=10

        if midValue == 0:
            num = highValue * pow(10, count)
        elif midValue == 1:
            num = (highValue) * pow(10, count) + (lowValue + 1)
            pass
        else:
            # none of 1 and 0
            num = (highValue + 1) * pow(10, count)

        sumNum += num
    count += 1

    return sumNum


'''
解法二： 几种值得计算方式
'''


# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        '''
        sum =0
        for i in range(1, n+1):
            k = i
            while k :
                if (k%10) ==1:
                    sum +=1
                k =k/10
        return sum
        '''

        highValue = 1
        midValue = 1
        lowValue = 1
        count = 0
        sumNum = 0

        while highValue != 0:

            highValue = n // pow(10, count + 1)
            midValue = (n // pow(10, count)) % 10
            lowValue = n % pow(10, count)

            '''
            # percent = 10 # 初始化的值
            highValue = n // percent
            midValue  = ( n % percent ) // (percent/10)
            lowValue  = ( n % percent ) % (percent/10)
             percent *=10
            '''
            '''
             # percent = 1  # 初始化的值
            highValue = n // (percent * 10)
            midValue  = (n // percent)%10
            lowValue  =  n % percent
            percent *=10
            '''

            if midValue == 0:
                num = highValue * pow(10, count)
            elif midValue == 1:
                num = (highValue) * pow(10, count) + (lowValue + 1)

            else:
                # none of 1 and 0
                num = (highValue + 1) * pow(10, count)

            sumNum += num
            count += 1

        return sumNum
