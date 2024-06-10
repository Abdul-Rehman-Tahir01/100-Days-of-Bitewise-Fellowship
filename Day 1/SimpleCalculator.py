num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

while True:
    operation = input("\nEnter operation (+, -, *, /): ")
    
    if(operation == '+'):
        sum = float(num1) + float(num2)
        print("The result is: " + str(sum))
        break

    elif(operation == '-'):
        difference = float(num1) - float(num2)
        print("The result is: " + str(difference))
        break

    elif(operation == '*'):
        product = float(num1) * float(num2)
        print("The result is: " + str(product))
        break

    elif(operation == '/'):
        quotient = float(num1) / float(num2)
        print("The result is: " + str(quotient))
        break

    else:
        print("Invalid operation")