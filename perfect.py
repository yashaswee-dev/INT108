def getInput(): #Function to take User Input
    usrInput = int(input("Enter an integer to test : "))
    return usrInput

def isPerfect(testcase): #Function to test if the given testCase is Perfect or NOT
    sum = 1 #Sum Variable to store ongoing sum
    factor = 2
    while factor<=(testCase/2):
        if(testCase%factor==0): #To Check if the factor divides the testCase completely
            sum+=factor
        factor+=1
    return sum==testCase #Checking if the Ongoing Sum equals the TestCase

def displayOutput(testCase, result): #Display function to handle Outputs to the Console
    if(result): #Checking result from 'isPerfect' Function
        print(testCase,"is a Perfect Number")
    else:
        print(testCase,"is NOT a Perfect Number")    

#Main Program Flow
testCase = getInput()
displayOutput(testCase,isPerfect(testCase))