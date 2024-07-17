number = input("Enter a number: ")
count = 0

if(int(number)%2==0):
    print(str(number) + " is not a prime number")
else:
    if(int(number)==1):
        print(str(number) + " is a prime number")
    else:
        for i in range(1, int(number)):
            if(int(number)%i==0):
                count+=1

        if(int(count)==1):
            print(str(number) + " is a prime number")
        else:
            print(str(number) + " is not a prime number")
