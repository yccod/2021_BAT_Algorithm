# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        
        newHead = pHead1 if pHead1.val < pHead2.val else pHead2
        
        pTmp1 = pHead1
        pTmp2 = pHead2
        
        if newHead == pTmp1:
            pTmp1 = pTmp1.next
        else:
            pTmp2 = pTmp2.next
        
        previousPointer = newHead
        
        while pTmp1 and pTmp2:
            if pTmp1.val < pTmp2.val:
                previousPointer.next = pTmp1
                previousPointer = previousPointer.next
                pTmp1 = pTmp1.next
            else:
                previousPointer.next = pTmp2
                previousPointer = previousPointer.next
                pTmp2 = pTmp2.next
        if pTmp1 == None:
             previousPointer.next = pTmp2
        else:
             previousPointer.next = pTmp1
             
        return newHead
        