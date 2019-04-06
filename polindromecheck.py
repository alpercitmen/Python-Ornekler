#Python Program to check string is a polindrome or not

def reverse(s):
    return s[::-1]

def isPolindrome(s):
    rev = reverse(s)
    if (s == rev):
        return True
    return False

s = input("Enter String: ")
answer = isPolindrome(s)

if answer == 1:
    print("Yes it is a polindrome")
else:
    print("No it is not a polindrome")
