import math

r = float(input('Enter the radius of the circle :'))
area= math.pi * r * r

print("Area of the circle is : %.2f" %area)

filename = input("Input the Filename: ")
f_extens = filename.split(".")
print("The extension of the filename is : " + repr(f_extens[-1]))
