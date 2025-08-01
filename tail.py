# printing the outcome when we toss a coin until the tail comes
import random
coin=['h','t']        #virtual coin
outcome=random.choice(coin)        #tossing the coin
while(outcome!='t'):
    print(outcome)
    outcome=random.choice(coin)
print('t')
