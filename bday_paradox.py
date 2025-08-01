#Birthday paradox problem
def ne(days,n):         # no. of ways that no two people share a birthday
    r=1
    for i in range(n):
        r=r*(days-i)
    return r
a=[10,20,30,40,50,60,70,80] 
for i in range(len(a)):     # checking the probability in a group of n (10 ,20,...)people 
    n=a[i]                  # group size
    n_s=(365**n)            # total no. of ways to assign birthdays
    n_e=ne(365,n)           # no. of ways that no two people share a birthday
    p_e=100-((n_e)/(n_s))*100       # probability that at least two people share a birthday
    print("n:",a[i],"p:",p_e)       #probability of at least two people sharing a birthday in a group of n people
