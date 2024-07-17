terms = input("Enter number of terms: ")

first_term = 0
second_term = 1

if int(terms) > 0 :
    for i in range(int(terms)):
        next_term = first_term + second_term
        first_term = second_term
        second_term = next_term
    print("The " + str(terms) + "th Fibonacci is " + str(first_term), end = ".")
else:
    print("Invalid number of terms")