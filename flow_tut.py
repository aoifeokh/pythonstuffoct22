a = int(input("enter an integer: "))

b = int(input("enter a 2nd integer: "))

c = int(input("enter a 3rd integer: "))

if a > b:
    if a > c:
        print(a)
    else: 
        print(c)
elif b > c:
    print(b)

else:
    print(c)
