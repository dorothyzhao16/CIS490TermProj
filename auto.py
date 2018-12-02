'''
Created on Dec 1, 2018

@author: zhaod
'''

import sys
import re

dfa = True
fa = [] #finite automata

numStates = None  #number of states
finals = []  #list of final states
tf = None   #array of transition functions

ss = 0 #start state

epsilonSymbol = 'E' #E represents epsilon
epsilon = False

def readFA(filename):
    f = open(filename,'r')
    line = f.readline()     #gets firs line 0, first digit

    patt = re.compile(R"\s*(\d+).*") #compiles pattern into pattern objects
    pattSearch = patt.search(line) #searches first line
    
    global numStates  #global number of states
    numStates = int(pattSearch.group(1))
    
    global tf #all transition functions in the string
    tf = f.readline()

    status = f.readline() #status list of each state: 1 represents start state, 2 represents terminal state, 3 represents start and terminal state
    ssn = 0  #number of start states
    fn  = 0  #number of final states 
    
    for n in range(0,numStates):
        
        fa.append((int(status[n]), []))
        
        if status[n] == '1' or status[n] == '3':
            global ss
            ss = n
            ssn = ssn + 1 #number of start states incremented
        if status[n] == '2' or status[n] == '3':
            finals.append(n)
            fn = fn + 1
            
    if ssn != 1:
        sys.stdout.write("Cannot be more than one start state")
        
    if fn < 1:
        sys.stdout.write("Need at least one final state")
            
    #transition functions read here
    r2 = re.compile(R"\s*(\d+)\s+(\S)\s+(\d+)")
    for line in f:         #reads tail_state symb head_state
        m2 = r2.search(line)
        st1 = int(m2.group(1))
        st2 = int(m2.group(3))
        sym = m2.group(2)
        if sym == epsilonSymbol: #checks for epsilon
            global epsilon
            epsilon = True
        # appends onto adjacency list
        fa[st1][1].append( (sym, st2) )
    global dfa
    dfa = checkDFA()
    
    
    
def checkDFA():
    for n in range(0,numStates):
        for ch in tf: #go through each symbol in transition functions
            check = lookup(n, ch) #looks up if state is usable
            if check != None and len(check)>=2:
                return False
    return True
           
                  
def lookup(state, symbol):
    retFA = [] #variable to be returned with state and symbol
    if state < 0 or state >= len(fa):
        return None
    elif len(fa[state][1]) == 0:
        return None
    else:
        t = len(fa[state][1])
        for i in range(0,t):
            if fa[state][1][i][0] == symbol:
                retFA.append(fa[state][1][i][1])
        return retFA


def getStartState():
    return ss

def finalStates():
    return finals

def isFinal(state):
    if fa[state][0] == 2 or fa[state][0] == 3:
        return True
    return False

def is_dfa():
    return dfa
    
def printFinAuto(): #prints the finite automata, in this case epsilon-NFA
    if epsilon:
        sys.stdout.write("-------------------epsilon-NFA-------------------")
    elif dfa:
        sys.stdout.write("DFA: ")
    else:
        sys.stdout.write("NFA: ")
    
    sys.stdout.write("\nThe epsilon-NFA has " + str(numStates) + " states, and" + " the transition functions are " + tf + "\n")
    
    for i in range(0,numStates):
        if i < 10:
            sys.stdout.write(" " + str(i))
        else:
            sys.stdout.write(str(i))
                     
        if isFinal(i):
            sys.stdout.write("t: ")
        else:
            if i == ss:
                sys.stdout.write("s: ")
            else:
                sys.stdout.write(": ")
            
        print(fa[i])
