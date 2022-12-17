def translation_count(num):
    if not isinstance(num, int) or num < 0:
        return

    str_num = str(num)
    length = len(str_num)
    counts = [0] * length

    for i in range(length - 1, -1, -1):
        if i == length - 1:
            counts[i] = 1
            continue

        count = counts[i + 1]
        value = (ord(str_num[i]) - ord('0')) * 10 + (ord(str_num[i + 1]) - ord('0'))
        if i == length - 2:
            count += 1 if 10 <= value <= 25 else 0
        else:
            count += counts[i + 2] if 10 <= value <= 25 else 0
        counts[i] = count
    return counts[0]




class Solution:
    def numDecodings(self, s: str) -> int:
        #动态规划：时间复杂度O(n),空间复杂度O(n)

        size = len(s)
        #特判
        if size == 0:
            return 0
        dp = [0]*(size+1)
        dp[0] = 1
        for i in range(1,size+1):
            t = int(s[i-1])
            if t>=1 and t<=9:
                dp[i] += dp[i-1] #最后一个数字解密成一个字母
            if i >=2:#下面这种情况至少要有两个字符
                t = int(s[i-2])*10 + int(s[i-1])
                if t>=10 and t<=26:
                    dp[i] += dp[i-2]#最后两个数字解密成一个一个字母
        return dp[-1]
#
# 作者：chuan-12
# 链接：https://leetcode-cn.com/problems/decode-ways/solution/dong-tai-gui-hua-by-chuan-12/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

if __name__ == "__main__":
    print(translation_count(12258))

    a= Solution()
    s = '12258'
    a.numDecodings(s)

