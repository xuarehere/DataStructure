class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        dummy = ListNode(-1)
        l1 = list1
        l2 = list2
        merge = dummy

        while l1 and l2:
            new_node = ListNode(-1)
            if l1.val <= l2.val:
                new_node.val = l1.val
                merge.next = new_node   # 1. 搭桥：站在 merge 上，把钩子挂到 new_node
                l1 = l1.next            # 2. l1 施工员往前走一步
            else:
                new_node.val = l2.val
                merge.next = new_node   # 1. 搭桥：站在 merge 上，把钩子挂到 new_node
                l2 = l2.next            # 2. l2 施工员往前走一步
            
            # ✅ 核心修复：桥在上面已经搭好了，这里必须让 merge 本人迈步站到新节点上！
            merge = merge.next          # （写 merge = new_node 效果完全一样）

        if l1:
            merge.next = l1
        else:
            merge.next = l2
        return dummy.next