#printing the sample space of the event when we roll the dice and toss the coin at the same time
import random
dice=[1,2,3,4,5,6]    #virtual dice
coin=['h','t']        #virtual coin
for i in dice:
    for j in coin:
        print(str(i)+j)        #printing each element of sample space
