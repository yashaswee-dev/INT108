def getInput(): #Function to take User Input
    usrInput = int(input("Enter Integer : "))
    return usrInput

def generateFibonacci(terms):
    termsList = [0,1]
    previous2nd=0
    previous1st=1
    index = 2
    while index<terms:
        term = previous1st+previous2nd
        termsList.append(term)
        previous2nd = previous1st
        previous1st = term
        index+=1
    return termsList

def displayOutput(sequence):
    print("List of first",len(sequence),"Terms are as follows:")
    for term in sequence:
        print(term)

cases = getInput()
displayOutput(generateFibonacci(cases))