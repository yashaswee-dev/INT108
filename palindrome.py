def getInput(): #Function to take User Input
    usrInput = input("Enter a String to test : ")
    return usrInput

def isPalindrome(testCase):
    testCase = testCase.upper()
    index = 0
    length = len(testCase)
    while index<length:
        if(testCase[index]!=testCase[length-index-1]):
            return False
        index+=1
    return True

def displayOutput(testCase, result): #Display function to handle Outputs to the Console
    if(result): #Checking result from 'isPalindrome' Function
        print(testCase,"is a Palindrome String")
    else:
        print(testCase,"is NOT a Palindrome String")    

#Main Program Flow
testCase = getInput()
displayOutput(testCase,isPalindrome(testCase))