'''
Created on Dec 1, 2018

@author: zhaod
'''

# fa.py: build internal fa
import sys
import re

dfa = True
fa = []
ss = 0 # start state
stn = None  # num of states
terms = []  # list of terminal states
symbs = None   # array of symbols
eps = False
eps_symb = '@'

# fa is the actual finite automata
# for i in range(0,stnum):
#     fa[i] is the ith vertex data
#     fa[i][0] gives status of ith vertex
#     fa[i][1] gives the ith adjacency list

def read_fa(filename):
    f = open(filename,'r')
    line = f.readline()
    # get first digit of line 0
    r1 = re.compile(R"\s*(\d+).*")
    m1 = r1.search(line)
    global stn  # the number of states
    stn = int(m1.group(1))
    
    global symbs # all symbs in string
    # @ = espilon handled as special case
    symbs = f.readline()
    # stn many ints on separate lines,
    #  giving the status of each state
    #  1 = start, 2 = term, 3 = start and term
    # stp is the status list for each state
    stp = f.readline() # each state status
    ssn = 0  # num of start states (must be 1)
    tn  = 0  # num of term states (at least 1)
    for i in range(0,stn):
        fa.append((int(stp[i]), []))
        if stp[i] == '1' or stp[i] == '3':
            global ss
            ss = i
            ssn = ssn + 1
        if stp[i] == '2' or stp[i] == '3':
            terms.append(i)
            tn = tn + 1
    if ssn != 1:
        sys.stdout.write("ERR, != 1 start st")
    if tn < 1:
        sys.stdout.write("ERR, 0 term states")
            
    # now work on transition data
    r2 = re.compile(R"\s*(\d+)\s+(\S)\s+(\d+)")
    for line in f:
        # read tail_state symb head_state
        m2 = r2.search(line)
        st1 = int(m2.group(1))
        st2 = int(m2.group(3))
        sym = m2.group(2)
        if sym == eps_symb: # check for eps
            global eps
            eps = True
        #  append onto the adjacency list
        fa[st1][1].append( (sym, st2) )
    global dfa
    dfa = check_dfa()
    
def check_dfa():
    for i in range(0,stn):
        for ch in symbs: # string of all symbs
            t = lookup(i, ch)
            if t != None and len(t) >= 2:
                return False
    return True
                  
def lookup(state, symb):
    ret = []
    if state < 0 or state >= len(fa):
        return None
    elif len(fa[state][1]) == 0:
        return None
    else:
        t = len(fa[state][1])
        for i in range(0,t):
            if fa[state][1][i][0] == symb:
                ret.append(fa[state][1][i][1])
        return ret

def get_start_state():
    return ss

def terminals():
    return terms

def is_terminal(state):
    if fa[state][0] == 2 or fa[state][0] == 3:
        return True
    return False

def is_dfa():
    return dfa
    
def printfa():
    if eps:
        sys.stdout.write("NFA with epsilon: ")
    elif dfa:
        sys.stdout.write("DFA: ")
    else:
        sys.stdout.write("NFA: ")
    sys.stdout.write("States " + str(stn) +
         ", Symbols: " + symbs + "\n")
    for i in range(0,stn):
        if i < 10:
            sys.stdout.write(" " + str(i))
        else:
            sys.stdout.write(str(i))
        if i == ss:
            sys.stdout.write("s")
        else:
            sys.stdout.write(" ")
        if is_terminal(i):
            sys.stdout.write("t:")
        else:
            sys.stdout.write(" :")
        print(fa[i])