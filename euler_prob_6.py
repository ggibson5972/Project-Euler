#find some of squares of first 100 natural nums
sum = 0
for n in range(101):
    y = n ** 2
    sum = sum + y

#find square of sum of first 10 natural nums
tot = 0
for i in range(101):
    tot = tot + i
squm = tot ** 2

#find difference of sum of squares and square of the sum
diff = squm - sum
print "The result is", diff
