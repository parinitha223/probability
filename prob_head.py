# code to plot the graph of probability of getting a head in tossing a coin
import random
import matplotlib.pyplot as plt
coin = ["head", "tail"]
no_of_tosses = 0
An = 0                               # Count of heads    
x = []                               # Number of tosses
y = []                               # Probability of head (An/n)
n=100000
# Simulate n tosses
for i in range(n):
    outcome = random.choice(coin)
    no_of_tosses += 1
    if (outcome == "head"):
        An += 1
    x.append(no_of_tosses)             #adding each toss count to x
    y.append(An / no_of_tosses)        # adding Probability of head (An/n) for each toss to y

# Plot the graph
plt.plot(x, y, linewidth=0.7)  
plt.grid(True)
plt.title("Running Probability of Getting 'Head' in Coin Tosses")
plt.xlabel("Number of Tosses ")
plt.ylabel("An/n (Probability of Head)")
plt.axhline(y=0.5, color='green', linestyle='dotted', label='Theoretical Probability (0.5)')
plt.legend()
plt.xlim(0, 100000)
plt.tight_layout()
plt.show()