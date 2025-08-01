# a bomb game where the participant have to pay some amount to play. 
# all he has to do is to guess the box which has no bomb among 5 boxes
#if the guess is right he will get double amount.
import random
Boxes=[1,2,3,4,5]
entry_fee=5
n=1000   #no.of players
gain_amount=entry_fee*n
given_amount=0
for i in range(n):
    bomb=random.choice(Boxes)
    open=random.choice(Boxes)
    if bomb==open:
       given_amount=0
    else:
        given_amount+=10
if(gain_amount>given_amount):
    print("you got profit by ", gain_amount - given_amount)
elif (gain_amount<given_amount):
    print("you got loss by ", given_amount - gain_amount)
else:
    print("you got no profit no loss")
