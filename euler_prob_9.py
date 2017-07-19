for a in range(1,1000):
    #b can only be whatever the difference is between 1000 and a
    for b in range(a, 1000 - a):
        #c can only be whatever the difference is between 1000 and a and b
        c = 1000 - b - a
        if c < b:
            break
        if c ** 2 == a ** 2 + b ** 2:
            print(a, b, c)
            print a * b * c
