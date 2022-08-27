def getInput(): #Function to take User Input
    usrInput = int(input("Enter an integer to test : "))
    return usrInput

def isArmstrong(testCase): #Function to test if the given testCase is Perfect or NOT
    sum = 0 #Sum Variable to store ongoing sum
    length = len(str(testCase)) #length variable to store the length of the integer
    for digit in str(testCase):
        sum+=(int(digit)**length)
    return sum==testCase

def displayOutput(testCase, result): #Display function to handle Outputs to the Console
    if(result): #Checking result from 'isArmstrong' Function
        print(testCase,"is an Armstrong Number")
    else:
        print(testCase,"is NOT an Armstrong Number")    

#Main Program Flow
testCase = getInput()
displayOutput(testCase,isArmstrong(testCase))