# Regular Expressions
# https://www.py4e.com/lessons/regex

def isPalindrome(s):
    return s == s[::-1]
# Driver code
s = "hello"
ans = isPalindrome(s)
 
if ans:
    print("Yes")
else:
    print("No")