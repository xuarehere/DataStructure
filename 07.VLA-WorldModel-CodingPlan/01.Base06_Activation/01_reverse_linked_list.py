"""
剑指 Offer 24. 反转链表 (对应目录 05: 24_ReverseList)
LeetCode 206. 反转链表
大厂面试基础手撕必考题（双指针迭代法 + 递归法）
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList_iterative(self, head: ListNode) -> ListNode:
        """
        双指针迭代法：
        时间复杂度 O(N)，空间复杂度 O(1)
        """
        prev = None
        curr = head
        while curr:
            next_temp = curr.next  # 保存后继节点
            curr.next = prev       # 反转指向
            prev = curr            # prev 前进一步
            curr = next_temp       # curr 前进一步
        return prev

    def reverseList_recursive(self, head: ListNode) -> ListNode:
        """
        递归法：
        时间复杂度 O(N)，空间复杂度 O(N)（递归栈开销）
        """
        if not head or not head.next:
            return head
        new_head = self.reverseList_recursive(head.next)
        head.next.next = head
        head.next = None
        return new_head


# 辅助测试工具
def build_linked_list(arr: list[int]) -> ListNode:
    dummy = ListNode(0)
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_list(head: ListNode) -> list[int]:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


if __name__ == "__main__":
    sol = Solution()
    
    # 测试迭代法
    l1 = build_linked_list([1, 2, 3, 4, 5])
    rev1 = sol.reverseList_iterative(l1)
    print("双指针迭代反转结果:", to_list(rev1))
    assert to_list(rev1) == [5, 4, 3, 2, 1]
    
    # 测试递归法
    l2 = build_linked_list([10, 20, 30])
    rev2 = sol.reverseList_recursive(l2)
    print("递归反转结果:", to_list(rev2))
    assert to_list(rev2) == [30, 20, 10]
    
    print("✅ 剑指 Offer 24 / 反转链表测试通过！")
