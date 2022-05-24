#A simple CLI calculator

def add(x,y):          #Defining the addition function
    return (x+y)

def subtract(x,y):     #Defining the subtraction function
    return (x-y)

def multiply(x,y):     #Defining the multiplication function
    return (x*y)

def divide(x,y):       #Defining the division function
    return (x/y)

def modulus(x,y):      #Defining the modulus function
    return (x%y)

counter = 0            #Counter varibale for tracking multiple incorrect selections

print("Select Operation to be Performed")

while True:             #looping back to user input after wrong entry by user.
    op_sel=input("Enter [A] to Add, [S] to Subtract, [M] to Multiply, [D] to divide or [MD] to modulus ")       #Operation input from user
    counter = counter + 1

    if op_sel in ("A", "S", "M", "D", "MD"):
    
        num1 = float(input("Enter First Number: "))             #user's numerical input 1
        num2 = float(input("Enter Second Number: "))            #user's numerical input 2

        #performing addition operation
        if op_sel == "A":
            print(num1, "+", num2, "=", add(num1,num2))            
        #performing subtraction operation
        elif op_sel == "S":
            print(num1, "-", num2, "=", subtract(num1,num2))
        #performing multiplication operation    
        elif op_sel == "M":
            print(num1, "*", num2, "=", multiply(num1,num2))
        #performing division operation
        elif op_sel == "D":
            print(num1, "/", num2, "=", divide(num1,num2))
        #performing modulus operation
        elif op_sel == "MD":
            print(num1, "%", num2, "=", modulus(num1,num2))
        break
        
    else:
        if counter < 5:                                 #tracking number of wrong operation entries.
            print("Invalid Input", "Try Again")
        elif counter == 5:                              #exit application after 5 wrong operation entries.
            print("Multiple invalid input", "Exiting Calculator" )  
            break
