"""
Created on Wed Aug 21 21:11:03 2019

@author: yc

判断括号是否匹配
"""
class Stack:
    def __init__(self):
        self.items=[]
    def isEmpty(self):
        return self.items==[]
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
    

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                s.pop()
        index = index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False



'''
判断符号是否匹配
'''
def parChecker1(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced=False
            else:
                top = s.pop()
            if not matches(top,symbol):
                balanced=False
        index = index+1
    if balanced and s.isEmpty():
        return True
    else:
        return False
def matches(open,close):
    opens = "([{"
    closers = ")]}"
    return opens.index(open) == closers.index(close)



'''
十进制转二进制
'''
def devideBy2(decNumber):
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % 2
        remstack.push(rem)
        decNumber = decNumber//2
    binString=""
    while not remstack.isEmpty():
        binString = binString + str(remstack.pop())
    return binString

'''
十进制转任意(二到十六)进制
'''
def baseConverter(decNumber,base):
    digits = "0123456789ABCDEF"
    remstack = Stack()
    while decNumber > 0:
        rem = decNumber % base
        remstack.push(rem)
        decNumber = decNumber // base
    newString = ""
    while not remstack.isEmpty():
        newString = newString + digits[remstack.pop()]
    return newString

    