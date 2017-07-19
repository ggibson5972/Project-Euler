#open text file with numbers and read lines into list
my_file = open("13file.txt")

#turn each 50-digit number found in 13file.txt into an integer from a string
my_file = map(int, my_file)
#find the sum of all 100 50-digit numbers in file
total = sum(my_file)
print total
