n = 600851475143
i = 2
while i ** 2 < n:
    if n % i == 0:
        n = n / i
    i += 1
print n
