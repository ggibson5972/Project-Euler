import math
#function to determine if the current number is prime
def isprime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

#counting function to address the issue of finding the 10001st prime
def term(number):
    t = 0
    count = 0
    while count != number:
        t += 1
        #if prime function determines the number to be prime, increase the count number by 1
        if isprime(t) == True:
            count += 1
    print t

term(10001)
