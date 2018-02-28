#probability of getting exactly one head if flip coin 3 times

def flip(p):
    # one head other tail 
    return 3 * p * (1 -p) * (1 -p)
print (flip(0.5)) 
