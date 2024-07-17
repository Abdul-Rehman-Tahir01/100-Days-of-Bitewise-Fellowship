string = input("Enter a string: ")

if(string == string[::-1]):
    print(str(string) + " is a palindrome")
else:
    print(str(string) + " is not a palindrome")