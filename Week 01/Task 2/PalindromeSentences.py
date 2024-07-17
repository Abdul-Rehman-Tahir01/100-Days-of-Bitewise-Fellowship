sentence = input("Enter a sentence: \n")
listed_sentence = list(sentence)

# To create a reversed listed and formatted sentence
reversed_listed_sentence = []
for i in range(len(listed_sentence) - 1, -1, -1):
    ascii_val = ord(listed_sentence[i])
    if not ((ascii_val>= 65 and ascii_val<=90) or (ascii_val>= 97 and ascii_val<=122)):
        listed_sentence.pop(i)
    else:
        reversed_listed_sentence.append(listed_sentence[i])
    i-=1

# Formatting the sentence
formatted_sentence = ''.join(listed_sentence)
reversed_formatted_sentence = ''.join(reversed_listed_sentence)

# Equating both sentence
if(formatted_sentence.lower() == reversed_formatted_sentence.lower()):
    print(str(sentence) + " is a Palindrome")
else:
    print(str(sentence) + " is not a Palindrome")