mark = int(input("Enter your mark: "))

#no else - ex1
"""if mark >= 65:
    print("Pass")

if mark < 65:
    print("Fail")"""

#with else - ex2
"""if mark >= 65:
    print("Pass")
else:
    print("Fail")"""

#multiple boundaries - ex3
if mark >= 87:
    print("Distinction")
elif mark >= 75:
    print("Merit")
elif mark >= 60:
    print("Pass")
else:
    print("Fail")
