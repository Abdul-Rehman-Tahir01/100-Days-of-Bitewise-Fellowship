def longest_palindrome(string):
    if len(string) == 0:
        return ""
    if len(string) == 1:
        return string

    longest = string[0]

    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if(substring == substring[::-1] and len(substring)>len(longest)):
                longest = substring

    return longest

# Test cases
print(longest_palindrome("string"))
print(longest_palindrome("babad"))
print(longest_palindrome("cbbd"))
print(longest_palindrome("racecar"))