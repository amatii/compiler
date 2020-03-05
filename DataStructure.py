from util import *

class Result():
    def __init__(self, kind=None,val=None,address=None,regno=None,real_value=None):
        self.kind = kind
        self.val = val
        self.address = address
        self.regno=regno
        self.real_value=real_value
        
    def __repr__(self):
        return "$"+str(self.kind) + str(self.val) + str(self.address) + str(self.regno) + str(self.real_value) +"$"


class Reg():
    def __init__(self):
        self.num=5
        self.occ= [0]*self.num 
        
    def AllocateReg(self):pass
    def DeAllocateReg(self,i):pass        
    def emit(self,bb,op,x=None,y=None):pass
    def load(self,x,bb): pass #get from the parser_compute

#SSA_code: [SSA_number:,op:,x:,y:,str:]
class SSA_code():
    def __init__(self,SSA_number=0,op=None,x=None,y=None):
        self.SSA_number=SSA_number
        self.op=op
        self.x=x
        self.y=y        
    def __repr__(self):
        return Parenthesize(self.SSA_number)+" "+ str(self.op) +" "+\
                ",".join([str(i) for i in [self.x,self.y] if i is not None and i is not ""])
    def __eq__(self,i):
        # (i) add r1,r2 and (j) add r2,r1 are the same?
        return self.op==i.op and self.x==i.x and self.y==i.y
