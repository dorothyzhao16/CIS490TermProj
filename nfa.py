#Yiyuan Dorothy Zhao and Myra Zaidi
#CIS490 Term Project Part 2: Fall 2018

from tkinter import *
import auto
import sys

def isFinal(s):  #checks the s set if there is a final state or not
    if not s:
        return False
    else:
        for x in s:
            if auto.isFinal(x):
                return True
        return False


def epsilonClosure(s): #do the epsilon closure for s set
    m = list(s) 
    trap = set(m)  #trap states set
    while len(m) != 0:
        rem = m.pop() #removes end element
        c = auto.lookup(rem,auto.epsilonSymbol) #use auto import lookup function
        
        if c != None:
            for d in c:
                if not (d in trap):
                    trap.add(d) 
                    m.append(d) 
    return trap
#################################################################  
def showDFA():
    auto.readFA("dfa.auto")
    auto.printFinAuto()

    sys.stdout.write("\n")

    f = open("dfa.input",'r')
    instruct = f.readline()

    ss = auto.getStartState()

    t = []
    t.append(ss)

    s1 = set(t)
    s1 = epsilonClosure(s1)

#print("For NFA: 0 = s, 1 = p, 2 = r, 3 = q. \nFor DFA: 0 = spr, 1 = sprq, 2 = prq.\n")
    print("--------------Equivalent DFA Below--------------")

    sys.stdout.write("Start at: " + str(list(s1)) + "\n")
    i = 0
    while instruct[i] != '.':
        s2 = set()
        for n in s1:
            s = auto.lookup(n, instruct[i])
            if not s:
                s = set()
            else:
                s = set(s)
            s2 = s2 | s  #union as sets
    
            #does epsilon closure below
        s2 = epsilonClosure(s2)
        sys.stdout.write(instruct[i] + ": " + str(list(s2)))
    
        if isFinal(s2):
            sys.stdout.write(" accepted ")
    
        sys.stdout.write("\n")
        s1 = s2
    
        i = i + 1 #next instruction, count is increment to go to next
    
master = Tk()
Label(master, text = "For NFA: 0 = s, 1 = p, 2 = r, 3 = q. \nFor DFA: 0 = spr, 1 = sprq, 2 = prq.\n").grid(row = 0)

Button(master, text='Quit', command=master.quit).grid(row = 3, column = 0, sticky = W, pady = 4)
Button(master, text = 'Show', command = showDFA).grid(row = 3, column = 1, sticky = W, pady = 4)

mainloop()
    
