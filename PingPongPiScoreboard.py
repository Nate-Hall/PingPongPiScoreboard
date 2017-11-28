import time
import cmd
import pygame

playerScore = [0, 0]
served = 0
serving = 0

pygame.init()
pygame.joystick.init()
for i in range(pygame.joystick.get_count()):
    pygame.joystick.Joystick(i).init()

def checkButtons():
    for event in pygame.event.get(): # User did something
        
        # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
        if event.type == pygame.JOYBUTTONDOWN:
            if(checkWinner() != False):
                resetGame()
            elif event.dict['button'] == 0:
                addPoint(event.dict['joy'], 1)

def getScores():
    return playerScore

def getServer():
    if(served == 1):
        return serving
    else:
        return -1
        
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