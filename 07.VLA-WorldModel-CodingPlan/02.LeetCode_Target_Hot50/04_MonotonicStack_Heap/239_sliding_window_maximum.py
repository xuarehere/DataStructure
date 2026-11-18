"""
LeetCode 239. 滑动窗口最大值 (Sliding Window Maximum)
知识点: 单调双端队列 (Monotonic Deque)
对应 06 底座: 052_Deque.py (双端队列的基础思想)
求职对应场景:
- 智驾传感器点云 / 图像时序滑动窗口极值统计
- 流式信号峰值检波与动作序列平滑滤波
"""

from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        """
        单调双端队列解法:
        维护一个存储【元素下标】的双端队列 q:
        1. 保持队列中下标对应的数值严格单调递减:
           当新元素 nums[i] >= 队尾元素 nums[q[-1]] 时，队尾元素永远不可能成为后续窗口的最大值，直接 pop() 弹出。
        2. 检查队首下标是否已经滑出当前窗口 [i - k + 1, i]，若滑出则 popleft() 弹出。
        3. 当窗口形成 (i >= k - 1) 时，队首 nums[q[0]] 即为当前窗口最大值。
        
        时间复杂度: O(N) 每个元素最多入队一次、出队一次
        空间复杂度: O(k) 队列最多存储 k 个下标
        """
        if not nums or k == 0:
            return []
            
        q = deque() # 存储下标
        res = []
        
        for i, val in enumerate(nums):
            # 1. 保持单调递减性质 (队尾比当前小的全弹出)
            while q and nums[q[-1]] < val:
                q.pop()
                
            q.append(i)
            
            # 2. 检查队首是否已经过期滑出窗口
            if q[0] <= i - k:
                q.popleft()
                
            # 3. 记录窗口最大值
            if i >= k - 1:
                res.append(nums[q[0]])
                
        return res


if __name__ == "__main__":
    sol = Solution()
    
    # 示例用例 1
    nums1 = [1, 3, -1, -3, 5, 3, 6, 7]
    k1 = 3
    expected1 = [3, 3, 5, 5, 6, 7]
    res1 = sol.maxSlidingWindow(nums1, k1)
    print(f"用例 1 输出: {res1}, 预期: {expected1}")
    assert res1 == expected1
    
    # 示例用例 2: 窗口大小为 1
    nums2 = [1]
    k2 = 1
    assert sol.maxSlidingWindow(nums2, k2) == [1]
    
    # 示例用例 3: 严格递减数组
    nums3 = [9, 8, 7, 6, 5]
    k3 = 2
    assert sol.maxSlidingWindow(nums3, k3) == [9, 8, 7, 6]
    
    print("\n✅ LeetCode 239 / 单调双端队列滑动窗口最大值测试全部通过！")
