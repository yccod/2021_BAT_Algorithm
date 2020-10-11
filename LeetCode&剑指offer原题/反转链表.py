# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        '''
        1.将现有的头换成尾，尾部的next为空
        2.将从第二个node开始，循环将next指向前一个
        3.需要一直有一个指针指向还没有翻转的链表的头部
        '''
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead
        
        leftPointer = pHead
        midPointer = pHead.next
        rightPointer = midPointer.next
        leftPointer.next = None
        
        
        while rightPointer != None:
            midPointer.next = leftPointer
            leftPointer = midPointer
            midPointer = rightPointer
            rightPointer = rightPointer.next
        
        midPointer.next = leftPointer
        return midPointer
        
        