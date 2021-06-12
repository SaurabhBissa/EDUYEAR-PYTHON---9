# variable names

name = "saurabh"
age = 24
salary = 123456.78

print(name, age, salary, sep='@')
print(name, age, salary, sep='')
print(name, age, salary, sep='\n')

print(name, age, salary, end='@')
print()
print(name, age, salary, end='')
print()
print("Name   : ",name)
print("Age    : ",age)
print("Salary : ",salary)

str = "My name is {} ,My age is {} and My salary is {}".format(name,age,salary)
print(str)

str = f"My name is {name} ,My age is {age} and My salary is {salary}".format(name,age,salary)
print(str)