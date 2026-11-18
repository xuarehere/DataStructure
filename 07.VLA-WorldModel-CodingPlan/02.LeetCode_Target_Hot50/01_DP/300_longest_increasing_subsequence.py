"""
LeetCode 300. 最长递增子序列 (Longest Increasing Subsequence, LIS)
智驾轨迹规划、时间序列最优子结构经典 DP 问题
包含两种解法：
1. 经典动态规划 O(N^2)
2. 贪心 + 二分查找 O(N log N)
"""

import bisect

class Solution:
    def lengthOfLIS_dp(self, nums: list[int]) -> int:
        """
        动态规划解法:
        状态定义: dp[i] 表示以 nums[i] 结尾的最长递增子序列长度
        状态转移: dp[i] = max(dp[j] + 1) for all j < i if nums[j] < nums[i]
        时间复杂度: O(N^2)
        空间复杂度: O(N)
        """
        if not nums:
            return 0
        n = len(nums)
        dp = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS_greedy_binary_search(self, nums: list[int]) -> int:
        """
        贪心 + 二分查找（耐心排序 Patience Sorting）:
        维护 tails 数组，tails[k] 表示长度为 k+1 的所有递增子序列中，末尾元素的最小值。
        时间复杂度: O(N log N)
        空间复杂度: O(N)
        """
        tails = []
        for x in nums:
            # 找到 x 在 tails 中第一个大于等于 x 的位置
            idx = bisect.bisect_left(tails, x)
            if idx < len(tails):
                tails[idx] = x  # 贪心更新更小的结尾
            else:
                tails.append(x) # 可以扩展子序列长度
        return len(tails)


if __name__ == "__main__":
    sol = Solution()
    test_cases = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
        ([7, 7, 7, 7, 7], 1),
    ]
    
    for arr, expected in test_cases:
        res_dp = sol.lengthOfLIS_dp(arr)
        res_greedy = sol.lengthOfLIS_greedy_binary_search(arr)
        print(f"输入: {arr}")
        print(f"  -> DP 解法结果: {res_dp}, 贪心+二分结果: {res_greedy}, 期望: {expected}")
        assert res_dp == expected and res_greedy == expected
        
    print("\n✅ LeetCode 300 / LIS 动态规划与二分算法全部验证通过！")
