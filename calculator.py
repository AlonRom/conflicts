#!/usr/bin/python3
# Program make a simple calculator that can add, subtract, multiply and divide using functions# This function adds two numbers 
def add(x, y):
   #dummy implementation
   return 1920

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   #dummy implementation
   return 1920

# This function divides two numbers
def divide(x, y):
   #dummy implementation
   return 1920
   
=======
# This function adds two numbers 
def add(x, y):
   return x + y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4):")

print("Invalid input ",choice)

n1 = int(input("A="))
n2 = int(input("B="))

print(n1,"-",n2,"=", subtract(n1,n2))
=======
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))
else:
   print("Invalid input ",choice)
