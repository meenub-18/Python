# Approach 1) swapping of two variables using a third variable

x = 10
y = 20

temp = x 
x = y
y = temp

print("The value of X:", x)
print("The value of Y:", y)

# Approach 2) swapping of two variables without using a third variable

x = 20
y = 50

x,y = y,x

print("The value of variable x:", x)
print("The value of variable y:", y)

# Approach 3) swapping of two variables by taking input from the user

x = input("Enter the value of x:")
y = input("Enter the value of y:")

x,y = y,x

print("The value of variable x:", x)
print("The value of variable y:", y)

# Approach 4) swapping of two variables using arithmetic operations 

x = 20
y = 30

x = x + y
y = x - y
x = x - y

print("The value of x:", x)
print("The value of y:", y)

# Approach 5) swapping of two variables using the multiplication operator

x = 1000
y = 5000

x = x * y
y = x / y
x = x / y

print("The value of x:", x)
print("The value of y:", y)
