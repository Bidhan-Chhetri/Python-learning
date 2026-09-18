# Day 2 of python programming

# Declare a first name variable and assign a value to it

firstName = 'Bidhan'

# Decalre a last name variable and assing a value to it

lastName = 'Chhetri'

# Declare a full name varibale and assign a value to it

fullName = 'Bidhan Chhetri'

# Declare a country variable and assign a value to it

country = 'Nepal'

# Declare a city variable and assign a value to it

city = 'Rupandehi'

# Declare an age variable and assign a value to it

age = 18 

# Decalare a year variable and assign a value to it

year = 2026

# Decalre a variable is_married and assign a value to it

is_married = False

# Decalre a variable is_true and assign a value to it

is_true = True

# Decalre a variable is_light_on and assign a value to it

is_light_on = "Yes"

# Decalre a multiple variable on one line

name, age, country, city  = "Aswin", 18, "Nepal", "Rupandehi"

# Check the data type of all your variable usign built in function type()

print(type(1))
print(type(1.54))
print(type("Bidhan"))
print(type(2j + 3 +4j - 3j + 4))
print(type([1, "Bidhan", 1.5])) 
print(type({'Name': 'Bidhan', 'Age': '18'}))  
print(type((9.8, 3.4, 34.23)))  
print(type({1.5, 'Bidhan', 10}))    

# Using len() built-in function, find the length of your first name

print(len(firstName))

# Compare the length of first name and last name

print(len(firstName), len(lastName))

# Declare 5 as num_one and 4 as num_two

num_one, num_two = 5, 4

# Add num_one and num_two and assign the value to variable total

total = num_one + num_two

# Subtract num_two from num_one and assign value to a variable diff

diff = num_one - num_two

# Multiply num_two and num_one and assing the value to a variable product

product = num_two * num_one

# Divide num_one by num_two and assign the value to a variable division

division = num_one / num_two

# Use a modulus division to find num_two divided vy num_one and assing the value to a variable remainder

remainder = num_one % num_two

# Calculate num_one to the power of num_two and assign the value to a variable exp

exp = num_one ** num_two

# Find floor division of num_one by num_two and assign the value to a variable floor_division

floor_division = num_one // num_two

# Calculate the area of circle and assign the value to a variable name of area_of_circle

pi = 3.14
radius = float(input("Enter the radius of the circle : "))

area_of_circle = pi * (radius ** 2)

print(f"The Area Of Circle is {area_of_circle}.")

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names

firstName = input("Enter the first name : ")
lastName = input("Enter the last name : ")
country = input("Enter the country : ")
city = input("Enter the city : ")
age = int(input("Enter the age : "))

print(f"My name is {firstName} {lastName}. I live in {city}, {country}. My age is {age}.")
