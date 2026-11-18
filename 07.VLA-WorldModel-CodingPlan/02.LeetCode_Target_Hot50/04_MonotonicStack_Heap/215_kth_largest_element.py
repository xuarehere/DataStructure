"""
LeetCode 215. 数组中的第 K 个最大元素 (Kth Largest Element in an Array)
知识点: 快速选择 (QuickSelect) 分治思想 / 最小堆 (Min-Heap)
对应 06 底座: 064_Quicksort.py (基准数划分 Partition 思想)
求职对应场景:
- LLM 生成采样 Top-K 过滤与高分截断
- 目标检测 / 轨迹生成中的非极大值抑制 (NMS) 分数排序
"""

import random
import heapq

class Solution:
    def findKthLargest_quickselect(self, nums: list[int], k: int) -> int:
        """
        基于快速排序 Partition 思想的快速选择算法:
        找第 k 大的元素，相当于升序排序后下标为 target_idx = len(nums) - k 的元素。
        
        时间复杂度: 期望 O(N)，最坏 O(N^2)（通过随机化基准 pivot 避免退化）
        空间复杂度: O(log N) 递归调用栈
        """
        target_idx = len(nums) - k
        
        def quickselect(left: int, right: int) -> int:
            if left >= right:
                return nums[left]
                
            # 随机选取 pivot 交换到 left，避免最坏恶化情况
            pivot_idx = random.randint(left, right)
            nums[left], nums[pivot_idx] = nums[pivot_idx], nums[left]
            
            pivot = nums[left]
            i, j = left, right
            
            # 对应 064_Quicksort.py 中的标准双指针填坑/划分思想
            while i < j:
                while i < j and nums[j] >= pivot:
                    j -= 1
                nums[i] = nums[j]
                
                while i < j and nums[i] <= pivot:
                    i += 1
                nums[j] = nums[i]
                
            nums[i] = pivot
            
            # 根据基准点最终落点 i 进行单侧剪枝
            if i == target_idx:
                return nums[i]
            elif i < target_idx:
                return quickselect(i + 1, right)
            else:
                return quickselect(left, i - 1)
                
        return quickselect(0, len(nums) - 1)

    def findKthLargest_heap(self, nums: list[int], k: int) -> int:
        """
        最小堆解法 (维护容量为 k 的小顶堆):
        时间复杂度: O(N log k)
        空间复杂度: O(k)
        """
        min_heap = []
        for x in nums:
            heapq.heappush(min_heap, x)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        return min_heap[0]


if __name__ == "__main__":
    sol = Solution()
    
    nums1 = [3, 2, 1, 5, 6, 4]
    k1 = 2
    res_qs1 = sol.findKthLargest_quickselect(list(nums1), k1)
    res_heap1 = sol.findKthLargest_heap(nums1, k1)
    print(f"用例 1: QuickSelect 结果={res_qs1}, Heap 结果={res_heap1}, 预期=5")
    assert res_qs1 == 5 and res_heap1 == 5
    
    nums2 = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k2 = 4
    res_qs2 = sol.findKthLargest_quickselect(list(nums2), k2)
    res_heap2 = sol.findKthLargest_heap(nums2, k2)
    print(f"用例 2: QuickSelect 结果={res_qs2}, Heap 结果={res_heap2}, 预期=4")
    assert res_qs2 == 4 and res_heap2 == 4
    
    print("\n✅ LeetCode 215 / 快速选择与小顶堆算法全部通过！")
