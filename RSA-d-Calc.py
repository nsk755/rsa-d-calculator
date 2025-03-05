e = int(input("was ist der wert von e: "))
phi = int(input("was ist der wert von phi: "))
for d in range(1000):
    result = (e * d) % phi
    if result == 1:
        print(d)
        break

