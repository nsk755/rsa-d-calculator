e = input("e = ")
phi = input("phi = ")
for d in range(1000):
    result = (e * d) % phi
    if result == 1:
        print(d)
        break
    