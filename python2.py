### Condiitonals ###
x = 10
if x > 5:
	print ("A")		# will print if x > 5		# indentation scope 
	print ("B")		# will print if x > 5 
else:
	print ("C")		

score =  93
if score > 90:
	print ("A")
if score > 80: 
	print ("B")
if score > 70:
	print ("C")
else:
	print ("F")
# A, B, C are printed 

score =  93
if score > 90:
	print ("A")
elif score > 80: 
	print ("B")
elif score > 70:
	print ("C")
else:
	print ("F")
# only A is printed 
# elif --> else + if 

# total 100 people 
# 50 boys 
# 50 girls 
# 20 boys wearing black shirt 
# 10 girls wearing black shirt 

# 50 boys raise hand 
# how many people wearing black shirt --> 30

### using else if ... 
# 50 boys go home 
# how many ppl wearing black shirt --> 10 (only girls )

### Function ###

number = 90
if number % 2 == 1: 
	print ("odd")
if number % 2  == 0:		# why use double equation
	print ("even")
# even 

## converting ^ to a function... 

def oddEven(number): 				# def, funtion name, input  # no space in between odd and even, don't capitalize first letter, Camel case to separate words 
	if number % 2 == 1: 
		print ("odd")
	if number % 2  == 0:		
		print ("even")

oddEven (98)						# don't indent 
oddEven (17)						# don't indent
oddEven (83)						# don't indent 

# def functionName (___):
	#if ... == ...:
		#print (...)
	#if ... == ...:
		#print (...)

#functionName ()
#functionName ()

# 1. Absolute Value 
# Write a function absoluteVal(number), that takes in a possibly-negative integer, and prints out the absolute value of the number 

def absoluteVal(number):
	if number > 0:
		print (number)
	if number < 0:
		print (number - (number*2))
	if number == 0:
		print (0)

absoluteVal (7)			# 7
absoluteVal (-1)		# 1
absoluteVal (0)			# 0

# print(abs(-15))			# will give 15 


# 2. Egg Carton 
# 12 eggs goes in a carton. Write a funtion eggCarton(eggs) 
# takes in a number of eggs and print out how many extra eggs are needed to make the carton full 

def eggCarton(eggs): 
	if 12 - eggs > 0:
		print (12 - eggs)
	if eggs == 12:
		print ("0")

eggCarton (2)			# 10
eggCarton (12)			# 0 

#Extra problems 

# isDivisible(x, y)
def isDivisible(x, y):
	if x == int:
		print ("true")
	if y == int: 
		print ("true")
	if x % y == 0: 
		print ("true")
	else:
		print ("false")

isDivisible (2, 1)		# true 
isDivisible (7, 6)		# false

# nearestOdd(x)
def nearestOdd (x):
	if x % 2 == 1: 
		print (x)
	else:
		print (x + 1)
# which may be a float?  what does this mean?

nearestOdd (5)		# 5
nearestOdd (6)		# 7

def nearestOdd (x):
	if x % 2 == 1: 
		print (x)
	if x % 2 == 0:
		print (x + 1)

nearestOdd (5)		# 5
nearestOdd (6)		# 7

#Legal Triangle(s1, s2, s3)
def legalTriangle(s1, s2, s3):
	if s1 + s2 > s3: 
		print ("legal")
	else: 
		print ("illegal")
	

legalTriangle (5, 7, 9)		# legal 
legalTriangle (5, 9, 9)		# legal 
legalTriangle (9, 5, 9)		# legal
legalTriangle (1, 2, 6)		# illegal

# kthDigit(x, K)
# Given two integers, x and k, return the kth digit of x, counting from the right. 
	# kthDigit (789, 0) returns 0
	# kthDigit (789, 1) returns 8 
	# kthDigit (789, 2) returns 7
	# kthDigit (789, 3) returns 0 
	# kthDigit (-789, 0) returns 9

def kthDigit(x, k):
	if k == 0:
		print (x % 10)
	if k == 1: 
		print ((x % 100 - (x % 100) % 10)/10)

kthDigit (11, 0) 			# 1
kthDigit (789, 1)			# 8

# isPerfectCube(X)
# True if perfect cube where x = y ** 3

def isPerfectCube(number):
	if round(number ** (1/3)) ** 3 == number: 		# why use type?
		print (True)					# Boolean should not be in quotation marks, capitalize the T and F 
	else: 
		print (False)

isPerfectCube(27)			
isPerfectCube(4)

print(7/2)


## Going over it in class ##

print(abs(-15))			# 15


def absVal2(number):
	print((number < 0) * (-number) + (number >= 0) * number)

absVal2(-5)
absVal2(5)
absVal2(0)

def absVal3(number):
	if number < 0:
		print (-number)
	else: 
		print (number)


word = "123"
#print(-word)		# error, cannot use - sing with strings
print (word + word)	# can only use + and * with strings 
print (word * 3)


def eggCarton(eggs):
	print (12 - eggs)

eggCarton(12)		# 0 
eggCarton(8)		# 4


def isDivisble(x, y):
	if x % y == 0:
		print ("True")
	else:
		print ("False")


def isDivisible2(x, y): 
	print(x % y == 0)		# Boolean? we know its Boolean by the numer 0?

isDivisible2(6, 3)	# True
isDivisible2(6, 4)	# False


def nearestOdd(x):			# x may be a float 
	number = int(x)
	if number % 2 == 0:
		print (number + 1)
	else:
		print (number)

nearestOdd(4)		# 5
nearestOdd(6.4)		# 7
nearestOdd(4.0)		# 5


def legalTriangle(a, b, c):
	num = max(a, b, c)		# find the max number from a, b, c
	print (num < (a + b + c - num))

legalTriangle(2, 2, 3)			# True 


print(3 / 1)		# as float
print(3 // 1)		# as whole number integer


def isPerfectCube(x):
	if round(x ** (1/3)) ** 3 == x:
		print ("True")
	else:
		print ("False")

isPerfectCube(1000)		# True 

print (1.2 + 2.2)		# 3.40000000004?

a = 1.2 + 2.2
print(a)
b = round(a*10)
c = b/10
print(c)








