import math
#counts the number of divisors in the triangular number
def divisors(n):
    factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            factors += 2
        else:
            continue
    return factors

x = 1
#iterates to get to the next trianguler number
for y in xrange(2,1000000):
    x += y
    #throws triangular number to the divisors() funtion to count the number of divisors
    if divisors(x) >= 500:
        print x
        break
