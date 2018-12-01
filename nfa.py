'''
Created on Dec 1, 2018

@author: zhaod
'''

# nfa.py: simulate an nfa
import auto
import sys

def is_term(s):  # s set, contains term?
    if not s:
        return False
    else:
        for x in s:
            if auto.is_terminal(x):
                return True
        return False

def eps_cl(s): # s a set, epsilon closure
    # could use s for b, save one list
    t = list(s) # list t is stack or queue
    b = set(t)  # set of "black" states
    while len(t) != 0:
        u = t.pop() # remove end elt
        # use @ for epsilon
        r = auto.lookup(u,auto.eps_symb)
        if r != None:
            for v in r:
                if not (v in  b):
                    b.add(v) # add
                    t.append(v) # push
    return b
    
auto.read_fa("dfa.auto")
auto.printfa()
sys.stdout.write("\n")
#################################################################
f = open("dfa.input",'r')
instr = f.readline()
ss = auto.get_start_state()
x = []
x.append(auto.get_start_state())
s1 = set(x)
s1 = eps_cl(s1) # start state
sys.stdout.write("Start:\n   " +
       str(list(s1)) + "\n")
i = 0
while instr[i] != '$':
    s2 = set()
    for y in s1:
        s = auto.lookup(y, instr[i])
        if not s:
            s = set()
        else:
            s = set(s)
        s2 = s2 | s  # as sets, union
    # now got set, need epsilon closure
    s2 = eps_cl(s2)
    sys.stdout.write(instr[i] + ": " +
          str(list(s2)))
    if is_term(s2):
        sys.stdout.write(" term ")
    sys.stdout.write("\n")
    s1 = s2
    i = i + 1 # next instr