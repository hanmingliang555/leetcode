# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> optional[ListNode]:
        # 特判：如果其中一个链表为空，绝对不可能相交
        if not headA or not headB:
            return None
            
        pA = headA
        pB = headB
        
        # 只要两人还没相遇（指向同一个节点），就继续走
        while pA != pB:
            # pA 如果走到头了（None），就重置到链表 B 的头节点；否则正常走一步
            pA = pA.next if pA else headB
            
            # pB 如果走到头了（None），就重置到链表 A 的头节点；否则正常走一步
            pB = pB.next if pB else headA
            
        # 循环结束时，只有两种情况：
        # 1. pA == pB 且不为 None，说明他们在交点相遇了！返回 pA 即可。
        # 2. pA == pB 且都为 None，说明他们俩各自把两条路都走完了还没相遇，不相交，返回 None。
        return pA