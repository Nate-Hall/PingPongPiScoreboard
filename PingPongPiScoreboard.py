import time
import cmd

playerScore = [0, 0]
served = 0
serving = 0

def mainLoop(i = 0):
    while True:
        x = input("Waiting for input: ")
        if(x != False):
            if(x == 'q'):
                addPoint(0, 1)
                time.sleep(0.1)
            if(x == 'w'):
                addPoint(1, 1)
                time.sleep(0.1)
            if(x == 't'):
                break
            print(playerScore)
            print(str(serving))

        if(checkWinner() != False):
            print("The winner is player " + str(checkWinner()) + "!")
            print(playerScore)
            resetGame()
        
def addPoint(playerID = 0, amount = 1):
    global served
    global serving
    
    if(served == 0):
        serving = playerID
        served = 1
    else:    
        playerScore[playerID] += amount
        
        if(playerScore[playerID] < 0):
           playerScore[playerID] = 0

        combined = playerScore[0] + playerScore[1]
        if((combined < 20 and combined % 2 == 0) or combined > 20):
            if(serving == 0):
                serving = 1
            else:
                serving = 0

def resetGame():
    global served
    
    playerScore[:] = [0, 0]
    served = 0

def checkWinner():
    if(playerScore[0] >= 11 or playerScore[1] >= 11):
        dif = playerScore[0] - playerScore[1]
        if(dif >= 2 or dif <= -2):
            if(playerScore[0] > playerScore[1]):
                ret = 1
            else:
                ret = 2
        else:
            ret = False
    else:
        ret = False

    return ret
        
    
mainLoop()
