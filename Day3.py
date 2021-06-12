# DAY 3 : ASSIGNMENT TO PUSH ON GITHUB

# AGE CALCULATOR 
# 1)  calculate Age of a person - User should enter the year of birth and the program should output the age.. eg : entered value is 1990, output age is 30

# 2) Simple Calculator:

# 	- get 2 numbers from the user and print the result of addition, subtraction, multiplication and floor division, decimal division, remainder, power of the input numbers

# 1) Age Calculator
'''year = input("enter year : ")
year = int(year)
age = 2021-year
print("your age is : ",age)'''

# 2) Simple Calculator
num1 = input("Enter 1 number : ")
num2 = input("Enter 2 number : ")
num1 = int(num1)
num2 = int(num2)

addi = num1+num2
sub = num1-num2
mul = num1*num2
dec = num1/num2
flo = num1//num2
rem = num1%num2
pwr = num1**num2

print("addition : ",addi)
print("subtraction : ",sub)
print("multiplication : ",mul)
print("division : ",dec)
print("floor division : ",flo)
print("modulus : ",rem)
print("power : ",pwr)