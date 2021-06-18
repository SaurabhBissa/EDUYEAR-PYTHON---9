# Assignment for For Loops

# 1. From range n to m, print all the numbers divisible by 5 and 7 both

# 2. Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
# Given:

# number_of_terms = 5

# So series will become 2 + 22 + 222 + 2222 + 22222

# Expected output:

# 24690

# Hint: 'a'*2 = 'aa'



# Assignment for While Loops

# 3. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print the sum of all numbers. (Use while loop)

# 4.  Write a loop to find the factorial of any number
# The factorial (symbol: !) means to multiply all whole numbers from our chosen number down to 1.

# For example: calculate the factorial of 5

# 5! = 5 × 4 × 3 × 2 × 1 = 120
# Expected output:

# 120


# 5. input: python language is best programming language
# output: P-y-T-h-O-n l-A-n-G-u-A-g-E I-s b-E-s-T P-r-O-g-R-a-M-m-I-n-G L-a-N-g-U-a-G-e


""" 1. From range n to m, print all the numbers divisible by 5 and 7 both
n, m=1, 100
for x in range(n,m):
	if (x%5==0):
		if (x%7==0):
			print(x," divisible by both")"""


""" 2. Find the sum of the series 2 +22 + 222 + 2222 + .. n terms
number_or_terms = int(input("Enter a number : "))
num = cop = 2
sm = 0
for x in range(number_or_terms):
	sm = sm + num
	num = num*10+cop
print(sm)"""

""" 3. Take integer inputs from user until he/she presses q ( Ask to press q to quit after every integer input ). Print the sum of all numbers. (Use while loop)
print("Press q to quit")
sm = 0
while True:
	n = input("Enter number : ")
	if n == 'q':
		break
	n = int(n)
	sm += n
print("sum is : ",sm)"""

""" 4.  Write a loop to find the factorial of any number
n = int(input("ENter an number : "))
fact = 1
while n > 0:
	fact = n * fact
	n -=1
print("Factorial is : ",fact)"""

# 5. input: python language is best programming language
# output: P-y-T-h-O-n l-A-n-G-u-A-g-E I-s b-E-s-T P-r-O-g-R-a-M-m-I-n-G L-a-N-g-U-a-G-e
# st = input("Enter a string : ") 
# st = "python language is best programming language"
# n = 0
# while n < len(st):
# 	if n%2==1:
# 		print(st[n], end='-')
# 		if st[n]==' ':
# 			print()
# 	else:
# 		print(st[n].upper(), end='-')
# 	n += 1
# print("\nString : ",st)

st = 'python is a good programming language'
# p-y-t-h-o-n
# i-s
# a
# g-o-o-d
# p-r-o-g-r-a-m-m-i-n-g
# l-a-n-g-u-a-g-e
for i in range(len(st)):
	end_val = '-'
	if st[i] == ' ':
		end_val = '\n'
	if i == len(st)-1:
		end_val = ''
	elif st[i+1] == ' ':
		end_val = ''

	# print(st[i].upper(), end=end_val)
	if i%2 == 0:
		print(st[i].upper(), end=end_val)
	else:
		print(st[i].lower(), end=end_val)

