# -*- coding: utf-8 -*-
'''
队列
'''
class Queue:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)

'''
约瑟夫问题
'''
def hotPotato(namelist,num):
    simqueue=Queue()
    for name in namelist:
        simqueue.enqueue(name)
    print(simqueue.items)
    while simqueue.size()>1:
        for i in range(num):
            simqueue.enqueue(simqueue.dequeue())
        simqueue.dequeue()
        print(simqueue.items)
    return simqueue.dequeue()

'''
双向队列
'''
class Deque:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def addFront(self,item):
        self.items.append(item)
    def addRear(self,item):
        self.items.insert(0,item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def size(self):
        return len(self.items)
        
        
'''
回文检查
'''
def palchecker(aString):
    chardeque=Deque()
    for ch in aString:
        chardeque.addRear(ch)
    stillEqual=True
    while chardeque.size()>1 and stillEqual:
        first=chardeque.removeFront()
        last=chardeque.removeRear()
        if first!=last:
            stillEqual=False
        return stillEqual
        
        