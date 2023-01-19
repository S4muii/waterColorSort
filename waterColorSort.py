import random
import itertools
import math
from   pprint import pprint
import copy 
from lolviz import listviz


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
    global didIwinYet
    #for each stack . if all items are the same or if there's no items at all return true
    #the list has a Bool value for each stack . if that bool value is true then this stack has passed the test
    #Need to make sure that every bool value is equal true
    
    if didIwinYet:
        return didIwinYet
    
    #0 means that there was no items - 1 means that there was a bunch of items and all of em were True
    allItemsMatching = [len(set(stack)) in [0,1] for stack in listOfStacks]
    if set(allItemsMatching) == {True}:
        print("GAMEWONNNNN ,Decisions Made:\n{{{" )
        print(*moves,"}}}}",sep="\n")
        didIwinYet=True
    else:
        didIwinYet=False
    
    return didIwinYet
        
        

def solveGame():


    #ensure that those lists are taken from the global vars 
    global listOfStacks,OriginallistOfStacks,trials,maxNumOfTrials,listOfPermutations
    global stuckNoMoves,MaxstuckNoMoves
    
    #BASE CASE - if the game is won in that branch then return out of the function already . game is over
    while True:
        if not gameWon():
            if trials < maxNumOfTrials:
     
                
                newMove=random.choice(listOfPermutations)
                ##HERE you need to trim the viable choices 
                    
                #second base case - if game is lost in that branch then just try out a new completely different random branch.
                if len(moves) >= maxMoves or stuckNoMoves >= MaxstuckNoMoves:
                    trials +=1
                    print( "trials:%06d/%06d"%(trials,maxNumOfTrials-1))
                    stuckNoMoves=0
                    moves.clear()
                    listOfStacks = copy.deepcopy(OriginallistOfStacks)
                    # print("reseting the listOfStacks to the original value and moves as well")
                    continue
                
                #HACKS . couple of hacks to speed up the progress
                
                #Don't allow reversing the last move - Unproductive
                if len(moves)>0:
                    if newMove[DST] is moves[LAST][SRC] and newMove[SRC] is moves[LAST][DST]:
                        stuckNoMoves+=1
                        continue
                    
                #if the srcStack has 3 or 4 of matching elements then don't do it - Unproductive as well 
                if len(set(listOfStacks[newMove[SRC]]))==1 and len(listOfStacks[newMove[SRC]])>=3:
                    stuckNoMoves+=1
                    # print("all items in the srcStack is matching and it's either 3 or 4 items in length PS: Stack is ",i[0])
                    continue
                
                #if you get stuck for 5 iterations not sure what to do then you lose
                
                #successful
                if transferItem(listOfStacks[newMove[SRC]],listOfStacks[newMove[DST]]) == 0:
                    moves.append([newMove[SRC],newMove[DST]])
                    # print("[*] Operation between",listOfStacks.index(i[0]),"->",listOfStacks.index(i[1]))
                    # printListOfStacks()
                else:
                    stuckNoMoves+=1
            else:
                break
        else:
            break
            
    print("Game won" if didIwinYet else "Game is not solvable or needs to change the parameters probably")
            
                
        





seed=random.randint(1, 100000)
#random one 
# random.seed(89259)
# random.seed(92339)
random.seed(seed)
print("seed is ,",seed)

#constants
MaximumNumOfBallsPerStack=4
maxMoves,maxNumOfTrials,MaxstuckNoMoves = 100000,10000,10000
listOfStacks,listOfBalls,numOfFullStacks,numOfEmptyStacks = [],[],12,2
SRC,DST,LAST = 0,1,-1

#vars
moves=[]
stuckNoMoves,trials= 0,0
didIwinYet = False



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
#randomListOfStacks
# listOfStacks += [[listOfBalls.pop() for j in range(MaximumNumOfBallsPerStack)] for i in range(numOfFullStacks)]
#MYlistOfStacks
listOfStacks +=[
    [4,3,2,1],
    [8,7,6,5],
    [4,6,1,5],
    [5,1,2,9],
    [3,11,10,9],
    [3,7,10,3],
    [4,2,11,12],
    [12,9,12,2],
    [9,11,10,8],
    [8,11,7,8],
    [6,6,12,4],
    [1,5,7,10],
    ]
#one Empty stack appeneded
listOfStacks += [[] for i in range(numOfEmptyStacks)]
#list of permutations
listOfPermutations = list(itertools.permutations([i for i in range(numOfFullStacks+numOfEmptyStacks)],2))



OriginallistOfStacks = copy.deepcopy(listOfStacks)
printListOfStacks()



solveGame()



