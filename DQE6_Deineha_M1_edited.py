# Python DQE6, Module 1, Homework 1, Nataliia Deineha

# Task1
# create list of 100 random numbers from 0 to 1000

# import Random module whs is generate random numbers
print ('Task 1')
import random
# use random.sample ha returns list of items from the range
random_list =random.sample(range(1, 1000),100)
# print result
print(random_list)

# Task2
# sort list from min to max (without using sort())

# use random.sample ha returns list of items from the range
print ('Task 2')
i = 0

print('Not sorted list:', random_list)

for i in range(i, len(random_list)):
    # to compare the first value with the next
    for j in range (i+1, len(random_list)):
        # check if the first value greater than second
        if (random_list[i] > random_list[j]):
            # if the first value greater than second, need to swap
            random_list[i], random_list[j] = random_list[j], random_list[i]

print ("Sorted list:", random_list)


# Task3
# calculate average for even and odd numbers
print ('Task 3')

# create variables
even_list = 0
even_sum = 0
odd_list = 0
odd_sum = 0
for i in random_list:
         # check if the value even
        if  i % 2 ==0:
            # calculate the sum
           even_sum += i
            # calculate the count
           even_list  +=1
# calculate the average= (sum / count) and print the result for even numbers
print ('Even AVG:', even_sum / even_list)

for o in random_list:
         # check if the value odd
        if  o % 2 !=0:
           # calculate the sum
           odd_sum += o
           # calculate the count
           odd_list  +=1
#  calculate the average= (sum / count) and print the result for odd numbers
print ('Odd AVG:', odd_sum / odd_list)