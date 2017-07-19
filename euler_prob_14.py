count_list = []
starter = []
for i in range(1,1000000):
    starter.append(i)
    count = 1
    while i > 1:
        if i % 2 == 0:
            #equation to find next number in chain if i is even
            i = i / 2
            #increase length of chain by 1
            count += 1
        else:
            #equation to find next number in chain if i is odd
            i = 3 * i + 1
            #increase length of chain by 1
            count += 1
    #add chain length to count_list list
    count_list.append(count)

#find max in count_list
print starter[count_list.index(max(count_list))]
