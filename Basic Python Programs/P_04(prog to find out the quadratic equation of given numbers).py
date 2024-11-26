# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("The Quadratic Equation is:" ,a,"x+",b,'y+',c,"=0")
# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)

print('The solution are',sol1, "and" ,sol2)
