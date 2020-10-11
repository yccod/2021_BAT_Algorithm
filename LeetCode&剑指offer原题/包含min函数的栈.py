# -*- coding: utf-8 -*-
class Solution1:
    def __init__(self):
        self.stack = []
        self.minValue = []
    def push(self,node):
        self.stack.append(node)
        if self.minValue:
            if self.minValue[-1] > node:
                self.minValue.append(node)
            else:
                self.minValue.append(self.minValue[-1])
        else:
            self.minValue.append(node)
    def pop(self):
        if self.stack:
            self.minValue.pop()
            return self.stack.pop()
        else:
            return None
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None
    def min(self):
        if self.minValue:
            return self.minValue[-1]
        else:
            return None




'''
Solution2
'''
class Solution2:
    def __init__(self):
        self.stack = []
        self.minValue = []
    def push(self,node):
        self.stack.append(node)
        if self.minValue:
            if self.minValue[-1] >= node:
                self.minValue.append(node)
#            else:
#                self.minValue.append(self.minValue[-1])
        else:
            self.minValue.append(node)
    def pop(self):
        if self.stack:
            temp = self.stack.pop()
            if temp == self.minValue[-1]: 
                self.minValue.pop()
            return temp
        else:
            return None
    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return None
    def min(self):
        if self.minValue:
            return self.minValue[-1]
        else:
            return None

