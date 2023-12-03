x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x % 2 == 0 and y % 2 == 0 and z % 2 == 0:
    print(min(x, y, z))
elif x % 2 == 0 and y % 2 == 0:
    print(z)
elif x % 2 == 0 and z % 2 == 0:
    print(y)
elif x % 2 == 0:
    print(max(y, z))
elif y % 2 == 0 and z % 2 == 0:
    print(x)
elif y % 2 == 0:
    print(max(x, z))
elif z % 2 == 0:
    print(max(x, y))
else:
    print(max(x, y, z))

