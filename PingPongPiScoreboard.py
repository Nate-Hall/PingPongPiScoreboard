import time
import cmd
import pygame

from PingPongPiEloRanking import *

playerScore = [0, 0]
playerNameNums = [-1, -1]
served = 0
serving = 0
ranked = 0

names = ["Andrew", "Tom", "Nathan"]

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
            elif event.dict['button'] == 1:
                addPoint(event.dict['joy'], -1)
            elif event.dict['button'] == 2:
                if(playerNameNums[0] + 1 < len(names)):
                    playerNameNums[0] += 1
                else:
                    playerNameNums[0] = 0
            elif event.dict['button'] == 3:
                if ranked == 0:
                    ranked = 1
                else:
                    ranked = 0
            elif event.dict['button'] == 4:
                if(playerNameNums[1] + 1 < len(names)):
                    playerNameNums[1] += 1
                else:
                    playerNameNums[1] = 0

def checkForExitPress():
    exitCount = 0
    
    for event in pygame.event.get():
        
        if event.type == pygame.JOYBUTTONDOWN:
            exitCount += 1
    return exitCount

def exitCheck():
    exitCount = 0
    
    for event in pygame.event.get():
        
        if event.type == pygame.JOYBUTTONDOWN:
            exitCount += 1
    if(exitCount >= 2):
        sys.exit()

def getScores():
    return playerScore

def getNames():
    pNames = ["", ""]
    for i in range(len(playerNameNums)):
        if playerNameNums[i] >= 0:
            pNames[i] = names[i] + " (" + str(round(GetElo(names[i]), 0)) + ")"
        else:
            pNames[i] = "Player " + str(i+1)

        if ranked == 1:
            pNames[i] = pNames[i].upper()
    return pNames

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

    if(ranked == 1):
        CalculateElo(playerName[0], playerName[1], playerScore[0], playerScore[1])
    
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