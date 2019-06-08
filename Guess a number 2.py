# Random Number 
# Jayesh Maniar
# Seed random number
import random
# random number rn between 1 and 10
rn = random.randint(1,10)

gn = 0

while rn != gn: 
    # input guess gn
    gn = int(input('choose a number: '))
    if gn == rn:
        print('correct')
        break
    else:
        if gn > rn:
            print('Too high, guess again')
        else:
            print('Too low, guess again')
        
        