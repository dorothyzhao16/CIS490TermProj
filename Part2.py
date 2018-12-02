#Yiyuan Dorothy Zhao and Myra Zaidi
#CIS490 Term Project Part 2: Fall 2018

from tkinter import *
class DFA:

    currState = None

    def __init__ (self, states, alphabet, transFunct, startState, finalState): #M = (Q, sigma, transition function, q0, F)
        self.states = states
        self.alphabet = alphabet
        self.transFunct = transFunct
        self.startState = startState
        self.finalState = finalState
        self.currState = startState #start at q0
        return

   
    def transToStateWithInput(self, inputVal):
        if ((self.currState, inputVal) not in self.transFunct.keys()): #if given string not in dict, keep current state at none
            self.currState = None
            return

        self.currState = self.transFunct[(self.currState, inputVal)] #else update current state to transition to state with input
        return

   
    def inFinalState(self):
        return self.currState in finalState
    def goToStartState(self):
        self.currState = self.startState
        return


    def inputRun(self, inputList): #run with input
        self.goToStartState()
        for i in inputList: #for input in the list
            self.transToStateWithInput(i) #use the function to put input in list
            continue

        return self.inFinalState() #returns the current state in programmed final state
    pass

#################################################################
states = {0, 1, 2, 3} #q0, q1, q2, q3
alphabet = {'a', 'b'} #set of all strings in {a, b}*

transFunct = dict() #place transition functions into dictionary

transFunct[(0, 'a')] = 1 #from q0, a goes to q1
transFunct[(0, 'b')] = 3 #from q0, b goes to q3

transFunct[(1, 'a')] = 3 #from q1, a goes to q3
transFunct[(1, 'b')] = 2 #from q1, b goes to q2 (final state)

transFunct[(2, 'a')] = 2 #loop in final state
transFunct[(2, 'b')] = 2 #loop in final state

transFunct[(3, 'a')] = 3 #loop in trap state
transFunct[(3, 'b')] = 3 #loop in trap state

startState = 0 #start at q0
finalState = {2} #q2 is final state
#################################################################

userDFA = DFA(states, alphabet, transFunct, startState, finalState) #DFA to be created and tested using user-given string


def showResult():
    inputString = list(e1.get())
    print("Result: %s\n" % (userDFA.inputRun(inputString)))

master = Tk()
Label(master, text="Enter a string for the DFA:").grid(row=0)

e1 = Entry(master, bd = 5)
e1.grid(row=0, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=showResult).grid(row=3, column=1, sticky=W, pady=4)

mainloop()

showResult()
