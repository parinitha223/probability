import random
coin=['h','t']
n=0             #no of tosses
heads=0         #count for no of heads
print("probability of head:")
print("n\toutcome\theads\tprobability")
for i in range(10):
    n+=1
    outcome=random.choice(coin)
    if(outcome=='h'):
        heads+=1
    print(n,'\t',outcome,'\t',heads,'\t',(heads/n))