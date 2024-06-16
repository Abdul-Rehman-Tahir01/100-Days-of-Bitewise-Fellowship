sentence = input("Input a sentence: \n")
words = sentence.split()

reversed_sentence = ' '.join(words[::-1])
print(reversed_sentence)