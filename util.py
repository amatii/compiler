pair={"[":"]","{":"}","(":")"}
opCode={"+":"ADD","-":"SUB","*":"MUL","\\":"DIV"}
opRel={">":"bgt",">=":"bge","<":"blt","<=":"ble","==":"beq","!=":"bnq"}
TEMP_VARIABLE_CORE="temp+for+internalUse"

def Parenthesize(x,y=None):
    if y==None:
        return "("+str(x)+")"
    else:
        return "("+str(x) + "," + str(y) +")"

class Random_variable_gen():
    def __init__(self):
        def _counter():
            for i in range(1,10000000):
                yield i
            else:
                print("tooooo many temp variables")
        self.a=_counter()
        self._current=self.next()
        
    def next(self):
        self._current=TEMP_VARIABLE_CORE+str(next(self.a))
        return self._current
    
    def get_current_random_variable(self):
        return self._current        

def add_to_both(live_left,live_right,inst):
        try:live_left.add(int(inst.x[1:-1]))
        except:pass
        try:live_left.add(int(inst.y[1:-1]))
        except:pass
        try:live_right.add(int(inst.x[1:-1]))
        except:pass
        try:live_right.add(int(inst.y[1:-1]))
        except:pass        
def split_live(live_left,live_right,inst):
        try:live_left.add(int(inst.x[1:-1]))
        except:pass
        try:live_right.add(int(inst.y[1:-1]))
        except:pass
def remove_SSA_number_all(SSA_number,live,live_left,live_right):
        try:live.remove(SSA_number)
        except:pass
        try:live_left.remove(SSA_number)
        except:pass
        try:live_right.remove(SSA_number)
        except:pass

def remove_loops(G_reverse,reverse=False):
        try:
            reverse_edges=nx.find_cycle(G_reverse, orientation='original')
            while len(reverse_edges)>0:
                reverse_edges=nx.find_cycle(G_reverse, orientation='original')
                print(reverse_edges)
                for e in reverse_edges:
                    if not reverse:
                        if e[0]<e[1]:
                            G_reverse.remove_edge(e[0],e[1])
                    if reverse:
                        if e[0]>e[1]:
                            G_reverse.remove_edge(e[0],e[1])
        except:
            print("no loop found!")
        return G_reverse

if __name__ == '__main__':
	#test Random_variable_gen:
	b=Random_variable_gen()
	print(b.next())
	print(b.next(),b.get_current_random_variable())  

