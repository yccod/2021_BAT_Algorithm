# -*- coding: utf-8 -*-
'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Here are few examples.
[1,3,5,6], 5 → 2
[1,3,5,6], 2 → 1
[1,3,5,6], 7 → 4
[1,3,5,6], 0 → 0
分析:题目要求时间复杂度O(log(n))，同时涉及有序数组中查找，使用标准二分查找即可实现。
'''
class Solution:
    '''
    @param A:a list of integers
    @param target :an integer to be inserted
    @return : an integer
    '''
    def searchInsert(self,A,target):
        if len(A) == 0:
            return 0
        start ,end = 0,len(A)-1
        while start+1<end:
             mid=(start+end)//2
             if A[mid]>=target:
                 end=mid
             else:
                 start=mid
        if A[start]>=target:
            return start
        if A[end]>=target:
            return end
        return len(A)
                 