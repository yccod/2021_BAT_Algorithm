# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    
    def FindFirstCommonNode(self, pHead1, pHead2):
        '''
        第一个参数给比较短的那个链表
        第二个参数给比较长的那个链表
        的三个参数是比较短的那个链表头
        第四个参数是比较长的那个链表头
        '''
        def findequal(shortPointer,longPointer,shortHead,longHead):
            k = 0
            #寻找链表长度之间的差值
            while longPointer:
                longPointer = longPointer.next
                k +=1
                #先让长的那个走k步
            shortPointer = shortHead
            longPointer = longHead
            for i in range(k):
                longPointer = longPointer.next
            while shortPointer != longPointer:
                shortPointer = shortPointer.next
                longPointer = longPointer.next
            return longPointer    
        # write code here
        pTmp1 = pHead1
        pTmp2 = pHead2
        
        while pTmp1 and pTmp2:
            #当两个链表相等时
            if pTmp1 == pTmp2:
                return pTmp1
            pTmp1 = pTmp1.next
            pTmp2 = pTmp2.next
            
        if pTmp1:
            return findequal(pTmp2,pTmp1,pHead2,pHead1)
            '''
            k = 0
            # 寻找出链表长度之间的差值
            while pTmp1:
                pTmp1 = pTmp1.next
                k +=1
                
             先让长的那个走k步
             pTmp1 = pHead1
             for i in range(k):
                 pTmp1 = pTmp1.next
                 
            while pTmp1 != pTmp2:
                pTmp1 = pTmp1.next
                pTmp2 = pTmp2.next
            return pTmp1
            '''
        if pTmp2:
            return findequal(pTmp1,pTmp2,pHead1,pHead2)
            '''
            k = 0
            # 寻找出链表长度之间的差值
            while pTmp2:
                pTmp2 = pTmp2.next
                k +=1
                
             先让长的那个走k步
             pTmp2 = pHead2
             for i in range(k):
                 pTmp2 = pTmp2.next
                 
            while pTmp1 != pTmp2:
                pTmp1 = pTmp1.next
                pTmp2 = pTmp2.next
            return pTmp1
            '''

            
            
        
        




