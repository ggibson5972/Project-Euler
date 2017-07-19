import math
#initiate first, second, and third fib numbers
curr = 1
prev = 1
prev2 = 0
total = 0

#loop to find new fib numbers
while curr <= 4000000:
    curr = prev + prev2
    if curr % 2 == 0:
        total = total + curr
    #shift numbers to next label
    prev2 = prev
    prev = curr
print total
