# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        '''
        k 如果比我们的链表长度还要大的话，我们直接返回None
        k 如果小于链表的长度，我们可以定义两个变量，这两个变量中间间隔k
        '''
        firstPoint = head
        secondPoint = head
        for i in range(k):
            if firstPoint == None:
                return None
            firstPoint = firstPoint.next
        while firstPoint !=None:
            firstPoint = firstPoint.next
            secondPoint = secondPoint.next
        return secondPoint