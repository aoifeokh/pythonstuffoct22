mark = int(input("Enter your mark: "))

#no else
"""if mark >= 65:
    print("Pass")

if mark < 65:
    print("Fail")"""

#with else
"""if mark >= 65:
    print("Pass")
else:
    print("Fail")"""

#multiple boundaries
if mark >= 87:
    print("Distinction")
elif mark >= 75:
    print("Merit")
elif mark >= 60:
    print("Pass")
else mark < 60:
    print("Fail")
