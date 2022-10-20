temperature = 20
""" #original code
if temperature > 30:
    print("too hot")
    print("aagh")
    if temperature > 50:
        print("AAH")
print("too cold")
"""
#fixed code - ex4
"""
if temperature > 50:
    print("too hot")
    print("aagh")
elif temperature > 30:
    print("aagh")
else:
    print("AAH")
    print("too cold")
"""

#ex5
"""
temperature = -10
if temperature > 30:
    print("too hot")
    print("aagh")

if temperature < 0:
    print("too cold")

if temperature > 0:
    print("perfect")

"""

#ex6
"""
temperature = 40

if temperature > 30:
    print("too hot")
    print("aagh")

if temperature < 0:
    print("too cold")

else:
    print("perfect")
"""

#ex7
temperature = 40

if temperature > 30:
    print("too hot")
    print("aagh")

elif temperature < 0:
    print("too cold")

else:
    print("perfect")
