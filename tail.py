import random
coin=['h','t']
outcome=random.choice(coin)
while(outcome!='t'):
    print(outcome)
    outcome=random.choice(coin)
print('t')