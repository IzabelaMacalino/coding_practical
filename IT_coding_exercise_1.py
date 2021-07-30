# Writa a program that ask the user to enter the mass
# of an object in kilograms and then calculates 
# and display mass of the object in pounds.

# Data given (conversion rate): 1 kg = 2.205 lb
One_kg_to_lb = 2.205


# input()funtion for getting input in kilograms from the user.Float()fanction converts a number stored in a string or integer into a floating point number.

userInput = float(input("Please enter the number to convert to pounds: "))

# multipication the user input with conversion rate of kilograms

userKilgramsToPounds = userInput * One_kg_to_lb

# print() method to show messges, value and result

print( "result" ,userInput, "converted to pounds is", userKilgramsToPounds)
