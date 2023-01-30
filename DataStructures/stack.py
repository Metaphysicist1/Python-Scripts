import collections 
#import numpy as np



class Stack(object):
    def __init__(self,data:list=[]):
        self.list = data
        self.length = len(self.list) 
        self.log=[] # list for stack logs
        
    def Append(self,value): # adds value to the stack
        self.list.append(value)
        self.log.append(f"Append: Value {value} successfully added to stack")
    
    def peek(self): # returns the peeked value
        return self.list[-1]
    
    def Pop(self): #removes peek element from stack
        self.list.pop()
        self.log.append(f"Pop: Peek Value {self.peek()} successfully removed from stack")
    
    def Print(self):
        print('Stack',*[f'|{i}|' for i in self.list[::-1]],sep='\n')
        print('---','\n')
        self.log.append("Print: stack successfully printed")
    
    
    def Info(self): # tracking all activities and changes in ds
        print("Log Information:",*[f'{i+1}) {self.log[i]}' for i in range(self.length)],sep='\n')
        

# stack = Stack([4,6,92,0,'5'])
# stack.Append(0)
# stack.Append(3)
# stack.Print()
# stack.Pop()
# stack.Print()
# stack.Info()