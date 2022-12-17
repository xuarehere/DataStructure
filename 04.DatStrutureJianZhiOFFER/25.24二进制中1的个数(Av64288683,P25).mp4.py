# -*- coding:utf-8 -*-
'''
25.24二进制中1的个数(Av64288683,P25).mp4

## 19.二进制中的1的个数

**输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示**

#### `知识点:`

#### 补码

负数如何求补码？分为如下步骤：
1、首先求出负数的原码，如-8的原码为 1000 1000，
2、通过原码求出它的反码，负数的反码就是 除符号为以外，其余的全部求反，如-8 反码为 1111 0111，
3、负数的补码 +1，就是它的补码，如 -8 的补码为 1111 1000
————————————————
版权声明：本文为CSDN博主「love_yqy」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/love_gzd/article/details/85085084

负数求补码_Python_love_gzd的博客-CSDN博客
https://blog.csdn.net/love_gzd/article/details/85085084

原码、反码、补码知识详细讲解（此作者是我找到的讲的最细最明白的一个）_网络_Coding-CSDN博客
https://blog.csdn.net/zl10086111/article/details/80907428


(3种解法)
《简单记记》输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。 - 简书
https://www.jianshu.com/p/436cbea81cad

感觉不考
'''

# -*- coding:utf-8 -*-
class Solution:
    def NumberOf1(self, n):
        # write code here
        count =0
        for i in range(32):
            if n & 1:
                count +=1
            n = n >>1
        return count


n = 5
n = n & 0xff
m = bin(5)
print( n >> 1 )