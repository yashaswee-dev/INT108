import random

def getInput(): #Function to take User Input
    usrMinInput = int(input("Enter minimum Range : "))
    usrMaxInput = int(input("Enter maximum Range : "))
    return [usrMinInput,usrMaxInput]

def randomRange(min,max):
    return random.random() * (max-min) + min

def displayOutput(range):
    min = range[0]
    max = range[1]
    print("Random number between",min,"&",max,"is",int(randomRange(min,max+1)))

def rollDice():
    displayOutput([1,6])

rollDice()