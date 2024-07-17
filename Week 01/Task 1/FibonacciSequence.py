terms = input("How many terms? ")

FIRST_TERM = 0
SECOND_TERM = 1

for i in range(int(terms)):
    print(str(FIRST_TERM), end=" ")
    nth = FIRST_TERM + SECOND_TERM
    FIRST_TERM = SECOND_TERM
    SECOND_TERM = nth
