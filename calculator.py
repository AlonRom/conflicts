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

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4):")

if choice == '1':
   print("should add")

elif choice == '2':
   print("should sub")

elif choice == '3':
   print(x,"*",y,"=", multiply(x,y))

elif choice == '4':
   print("should divide")

else
  print("Invalid input ",choice)
    
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
   
if choice == '1':
  print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
  print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
  print(num1,"*",y,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
    
else:
   print("Invalid input ",choice)
