
import random
dice=[1,2,3,4,5,6]          #creating virtual dice
n=1000                      #virtual participants
gain_amount=0
given_amount=0
for i in range(n):          #rolling the dice
    outcome=random.choice(dice)
    gain_amount+=4
    given_amount+=outcome
if(gain_amount>given_amount):               #calculating the gain or loss
    print("you got profit by:",gain_amount-given_amount)
else:
    print("you got  by:",given_amount-gain_amount)