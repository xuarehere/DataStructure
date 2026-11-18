"""
LeetCode 142. 环形链表 II (Linked List Cycle II - 寻找入环点)
知识点: 快慢双指针 (Floyd 判圈算法)、数学推导
直接复用 06 底座: 032_CirculationNode.py (循环链表成环机制)
求职对应场景:
- 计算图有向环检测与死锁定位
- 状态机死循环防护机制
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        """
        Floyd 判圈算法 + 入环点数学推导:
        设链表头到环入口距离为 a，环入口到快慢指针相遇点距离为 b，相遇点再走 c 步回到环入口 (环长 L = b + c)。
        快指针速度为慢指针 2 倍:
            fast 步数 = a + n(b + c) + b
            slow 步数 = a + b
            2(a + b) = a + n(b + c) + b
            => a = (n - 1)(b + c) + c = (n - 1)L + c
        结论: 当快慢指针在相遇点重合时，让一个指针回到 head，另一个保持在相遇点，
        两者以相同速度 (每次 1 步) 前进，再次相遇的节点即为【环入口】！
        
        时间复杂度: O(N)
        空间复杂度: O(1)
        """
        if not head or not head.next:
            return None
            
        slow = head
        fast = head
        
        # 1. 寻找相遇点
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # 无环
            
        # 2. 寻找入环点: 一个从 head 出发，一个从相遇点出发
        ptr1 = head
        ptr2 = slow
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            
        return ptr1


if __name__ == "__main__":
    sol = Solution()
    
    # 构造测试环: 3 -> 2 -> 0 -> -4 -> 接入节点 2 (val=2)
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # 环入口在 node2
    
    entry = sol.detectCycle(node1)
    print(f"检测到入环节点的值: {entry.val if entry else None}")
    assert entry == node2
    
    # 无环测试: 1 -> 2
    no_cycle_1 = ListNode(1)
    no_cycle_2 = ListNode(2)
    no_cycle_1.next = no_cycle_2
    assert sol.detectCycle(no_cycle_1) is None
    
    print("✅ LeetCode 142 / 环形链表 II 入环点检测测试全部通过！")
