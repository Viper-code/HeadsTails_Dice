#Please enter roll, dice or flip, coin and nothing else!
import random 
import time

Dice = random.randint(1,6)
f_coin = random.randint(1,2)

start = input('please type roll to roll a dice, enter "filp" to flip a coin, enter "num" to get a random number: ')
if start.lower() == 'roll':
    print('  Rolling...... ')
    time.sleep(2)
    print('You got a ' + str(Dice))
elif start.lower() == 'flip':
    print('   Flipping.......')
    time.sleep(2)
    if f_coin == 1:
        time.sleep(1)
        print('You got HEADS')
    if f_coin == 2:
        time.sleep(1)
        print('you go TAILS')
elif start.lower() =='num':
    
input('Please enter Exit ')

    
