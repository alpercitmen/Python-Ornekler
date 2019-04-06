#Python program to check Python Keywords

import keyword

pythonKeywords = keyword.kwlist
getToCheck = str(input("Keyword to check: "))
check = keyword.iskeyword(getToCheck)
if check:
    print(getToCheck + " is a Python Keyword")
else:
    print(getToCheck + " is not a Python Keyword")

print("\nShowing all keywords in python: \n")
print(pythonKeywords)
