string = input("Enter a string: ")

vowels = "aeiouAEIOU"
count = 0

for i in string:
    if i in vowels:
        count += 1


print("The number of vowels is: " + str(count))
