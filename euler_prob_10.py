#function determines if number is prime
def isprime(num):
    #num**0.5 == sqrt(num)
    limit = int(num ** 0.5)
    for x in xrange(3, limit + 1, 2):
        if num % x == 0:
            return False
    return True

#function that iterates through all numbers from 3 to 2 million and throws the numbers to the isprime() function
def term(max):
    yield 2
    t = 1
    curr = 3
    while curr < max:
        if isprime(curr) == True:
            yield curr
            t += 1
        curr += 2

print sum(term(2000000))
