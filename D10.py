import random
D10 = range(1,10)
roll = input ("Type 'roll' to roll the dice:" )
if roll == 'roll':
    print (random.choice(D10))
