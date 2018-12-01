'''
Created on Dec 1, 2018

@author: zhaod
'''
# dfa.py: simulate a dfa; 1 = start, 2 = terminal, 3 = start and terminal
import auto
import sys

auto.read_fa("dfa.auto")
auto.printfa()
sys.stdout.write("\n")
f = open("dfa.input",'r')
instr = f.readline()
sys.stdout.write("Input: " + instr + "\n")
sys.stdout.write("Simulation Run ...\n")
s1 = auto.get_start_state()
for ch in instr:
    if ch != '$':
        s2 = auto.lookup(s1, ch)[0]
        sys.stdout.write(str(s1) + " " + 
          ch + " " + str(s2))
        if auto.is_terminal(s2):
            sys.stdout.write(" term")
        sys.stdout.write("\n")
        s1 = s2
    else:
        break