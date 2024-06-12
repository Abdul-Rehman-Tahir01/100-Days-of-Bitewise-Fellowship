string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

if(sorted(string1.lower()) == sorted(string2.lower())):
    print(string1 + " and " + string2 + " are anagrams")
else:
    print(string1 + " and " + string2 + " are not anagrams")