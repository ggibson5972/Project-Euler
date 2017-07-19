result = 0
#iterate from 1 to 1000
for i in range(1000):
    #determine if i is a multiple of 3 or 5
    if ((i % 3 == 0) or (i % 5 == 0)):
        #if i is a multiple of 3 or 5, add to sum (result)
        result += i
print result
