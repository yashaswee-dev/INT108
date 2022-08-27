def getInput(): #Function to take User Input
    usrInput = int(input("Enter Integer : "))
    return usrInput

def getFactorial(testCase):
    sum = 1 #sum Variable to store the ongoing sum
    num = 1 #num Variable to store the ongoing number
    while num<=testCase:
        sum*=num
        num+=1 #incrementing the number count
    return sum

def displayOutput(testCase, result): #Display function to handle Outputs to the Console
    print("Factorial of",testCase,"=",result)

testCase = getInput()
displayOutput(testCase,getFactorial(testCase))