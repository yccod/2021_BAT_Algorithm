# -*- coding: utf-8 -*-
'''
Given a sorted linked list, delete all duplicates such that each element appear only once.

For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.

跳过相同的元素，指向再后一个元素。
'''
class Solutuon:
    # @param head ,a ListNode
    # @return a listNode
    def deleteDuplicates(self,head):
        p=head
        while (p!=None and p.next!=None):
            if p.var != p.next.val:
                p=p.next
            else:
                p.next=p.next.next
            return head
