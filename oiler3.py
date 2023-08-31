factors = []

def keepDividingBy2(x):
    y = 2
    while y < x:
        while x % y == 0:
            x /= y
            factors.append(y)
        y += 1
    #print(x)
    factors.append(x)
    print(max(factors))

keepDividingBy2(600851475143)
#print(factors)