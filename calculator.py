import re

def isValid(expression):
    if(re.search('[0-9]', expression) and not re.search('[!?\\&$#@_\\[\\]\\{\\}\\:\\;\\,=]', expression) 
    and not re.search('[a-zA-Z]', expression)):
        return True 
    else:
        return False

def printHelp():
    print("\n- Type a valid calculation, I will give you the answer\n- A valid calculation contains only math symbols and numbers, but no '='\n- Type quit to exit")


print("Welcome to Michelle's Calculator!") 
print("\n- Type a valid calculation, I will give you the answer\n- Type quit to exit\n- Type help for instructions")

while True:
    expression = input("Please enter a math expression: ")
    if expression == "quit":
        break 
    elif expression == "help":
        printHelp()
    elif isValid(expression) == True:
        print(expression + " = " + str(eval(expression)))
    else:
        print("\nERROR - Expression Invalid\nOnly use math symbols and numbers, no '='\n")
    
