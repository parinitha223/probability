# checking the number of even and odd outcomes on rolling a dice for n times
import random
dice=[1,2,3,4,5,6]
even=0
odd=0
n=100
for i in range(n):
    outcome=random.choice(dice)
    if(outcome%2==0):
        even+=1
    else:
        odd+=1
print("no of even outcomes :",even)
print("no of odd outcomes :",odd)
