#Use the keyword def to declare the function input_numbers() 
def input_numbers():
# ask user to input two numbers
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
 #The function return statement determines the value to be returned.    
    return a, b

#Create two arguments
x, y = input_numbers()

while True:
#  check that y value is without zero.
    if y != 0:
# division input numbers without 0 
        print(f"{x} / {y} is {x/y}")
        break
# If the y value is zero, we print a warning
# message and repeat the input cycle again.  
    else:

        print("Cannot divide by zero")
        x, y = input_numbers()
