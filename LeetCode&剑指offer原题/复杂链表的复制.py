# -*- coding:utf-8 -*-
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        #复制一个一样的node，并且添加到之前的链表的每一个node后面
        if pHead == None:
            return None
        pTmp = pHead
        while pTmp:
            node = RandomListNode(pTmp.label)
            node.next = pTmp.next
            pTmp.next = node
            pTmp = node.next
            
            
        #实现新建的node的random的指向
        pTmp = pHead
        while pTmp:
            if pTmp.random:
                pTmp.next.random = pTmp.random.next
            pTmp = pTmp.next.next
            
        #断开原来的node和新的node之间的连接
        pTmp = pHead
        newHead = pHead.next
        pNewTmp = pHead.next
        while pTmp:
            pTmp.next = pTmp.next.next
            pTmp = pTmp.next
            if pNewTmp.next:
                pNewTmp.next = pNewTmp.next.next
                pNewTmp = pNewTmp.next
        return newHead    
        
            
            
            
            