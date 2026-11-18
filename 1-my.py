"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # dummy = ListNode(-1)
        # tail = dummy
        # l1 = list1
        # l2 = list2
        # while l1 and l2:
        #     if l1.val <= l2.val:
        #         tail.next = l1
        #         l1 = l1.next
        #     else:
        #         tail.next = l2
        #         l2 = l2.next

        #     tail = tail.next

        # tail.next = l1 if l1 else l2
        # return dummy.next       
        dummy = ListNode(-1)
        l1 = list1
        l2 = list2
        merge = dummy

        
        while l1 and l2:
            # 合并
            new_node = ListNode(-1)
            ## 1号小于等于
            if l1.val <= l2.val:
                new_node.val = l1.val
                merge.next = new_node

                l1 = l1.next
                
            else:
                new_node.val = l2.val
                merge.next = new_node
                l2 = l2.next
            new_node.next = new_node
            merge.next = new_node
        if l1:
            merge.next = l1
        else :
            merge.next = l2
        return dummy.next
        

        
""