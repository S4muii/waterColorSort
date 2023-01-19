import random
import itertools
import math
from   pprint import pprint
import copy 

# from numpy import *


#can WIN this
# random.seed(34324)
#the recursion hell - fixed
# random.seed(6522)
# numOfPermutations = math.perm(numOfEmptyStacks+numOfFullStacks , 2)

def printListOfStacks(): 
    for i in listOfStacks: print(i)


def isListFull(aList):
      return len(aList) == MaximumNumOfBallsPerStack
 
def isListEmpty(aList):
    return len(aList) == 0

def doTransfer(srcStack,dstStack):
    dstStack.append(srcStack.pop())
    

def transferItem(srcStack,dstStack):
    '''
        takes a src and a DST stack and does the Transfer
        returns:
            0 everything went smooth
            -1 this path is a dead end , homie
    '''
    #check the srcStackFirst
    if isListEmpty(srcStack)   : return -1     #"srcStack Cannot be empty"
    if isListFull(dstStack)    : return -1     #"DstStack is FULL"
    if not isListEmpty(dstStack):
        
        #check if the last item in DST matches the the last item in SRC
         if not srcStack[-1] == dstStack[-1] : 
             return -1# "last item in SRC doesn't meet last item in DST"
         
         doTransfer(srcStack, dstStack)
         return 0
    else:
        doTransfer(srcStack, dstStack)
        return 0
        

def gameWon():
    global didIwinYetUGH
    #for each stack . if all items are the same or if there's no items at all return true
    #the list has a Bool value for each stack . if that bool value is true then this stack has passed the test
    #Need to make sure that every bool value is equal true
    
    if didIwinYetUGH:
        return didIwinYetUGH
    
    #0 means that there was no items - 1 means that there was a bunch of items and all of em were True
    allItemsMatching = [len(set(stack)) in [0,1] for stack in listOfStacks]
    if set(allItemsMatching) == {True}:
        print("GAMEWONNNNN ,Decisions Made:\n{{{" )
        print(*moves,"}}}}",sep="\n")
        didIwinYetUGH=True
    else:
        didIwinYetUGH=False
    
    return didIwinYetUGH
        
        

def solveGame():


    #ensure that those lists are taken from the global vars 
    global listOfStacks,OriginallistOfStacks,trials,maxNumOfTrials,listOfPermutations
    global recursionDepth,maxRecursionDepth,stuckNoMoves,MaxstuckNoMoves
    
    #BASE CASE - if the game is won in that branch then return out of the function already . game is over
    while True:
        if not gameWon():
            if trials < maxNumOfTrials:
     
                recursionDepth+=1
                i=random.choice(listOfPermutations)
                    
                #second base case - if game is lost in that branch then just try out a new completely different random branch.
                if len(moves) >= maxMoves or recursionDepth >= maxRecursionDepth or stuckNoMoves >= MaxstuckNoMoves:
                    trials +=1
                    recursionDepth=0
                    moves.clear()
                    listOfStacks = copy.deepcopy(OriginallistOfStacks)
                    print("reseting the listOfStacks to the original value and moves as well")
                    continue
                
                #HACKS . couple of hacks to speed up the progress
                
                #Don't allow reversing the last move - Unproductive
                if len(moves)>0:
                    if i[1] is moves[-1][0] and i[0] is moves[-1][1]:
                        print("curr_src,curr_dst is prev_dst,prev_src")
                        stuckNoMoves+=1
                        continue
                    
                #if the srcStack has 3 or 4 of matching elements then don't do it - Unproductive as well 
                if len(set(i[0]))==1 and len(i[0])>=3:
                    stuckNoMoves+=1
                    print("all items in the srcStack is matching and it's either 3 or 4 items in length PS: Stack is ",i[0])
                    continue
                
                #if you get stuck for 5 iterations not sure what to do then you lose
                
                #successful
                if transferItem(i[0],i[1]) == 0:
                    moves.append([i[0],i[1]])
                    print("[*] Operation between",listOfStacks.index(i[0]),"->",listOfStacks.index(i[1]))
                    printListOfStacks()
                else:
                    stuckNoMoves+=1
            else:
                break
        else:
            break
            
    print("Game won here's how" if didIwinYetUGH else "Game is not solvable or needs to change the parameters probably")
            
                
        





seed=random.randint(1, 100000)
#random one 
random.seed(89259)
print("seed is ,",seed)

#constants
MaximumNumOfBallsPerStack=4
didIwinYetUGH = False
maxMoves = 100
maxNumOfTrials = 100
maxRecursionDepth = 100
stuckNoMoves = 0
MaxstuckNoMoves= 100

#vars
listOfStacks,listOfBalls,numOfFullStacks,numOfEmptyStacks = [],[],4,1
moves,trials,recursionDepth = [],0,0



# I need to create random 4 stacks . one is empty . three are filled with random values
#from 1->4 cause it's only 4 items in each . and the rules are simple
#I can only add a number to a stack . if it's not full . or if it has no elemets
#or if the last element is the same as the one that I wanna move . otherwise the move should fail
#once I moved an item there I have to remove it from my stack

#populate the listOfBalls 
for i in range(numOfFullStacks):
    listOfBalls +=  [i+1]*MaximumNumOfBallsPerStack
random.shuffle(listOfBalls)


#Create The stacks

#fullItemedStacks 
listOfStacks += [[listOfBalls.pop() for j in range(MaximumNumOfBallsPerStack)] for i in range(numOfFullStacks)]
#one Empty stack appeneded
listOfStacks += [[] for i in range(numOfEmptyStacks)]
#list of permutations
listOfPermutations = list(itertools.permutations(listOfStacks,2))


OriginallistOfStacks = copy.deepcopy(listOfStacks)
printListOfStacks()



solveGame()



