num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

largest = num1 if (float(num1)>float(num2) and float(num1)>float(num3)) else num2 if ((float(num2)>float(num1) and float(num2)>float(num3))) else num3

print("The largest number is: " + str(largest))