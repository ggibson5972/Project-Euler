#initiate list of primes
primes = []
#limit iteration to 3-digit numbers
for i in range(100,1000,1):
    for j in range(100,1000,1):
        x = i * j
        #save product as a string
        x = str(x)
        #determine if x is a palindrome
        if x == x[::-1]:
            primes.append(int(x))
#find max number in list of primes
t = max(primes)
print t
