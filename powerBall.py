#Morgan Baughman
#01/09/18
#powerBall.py - Pick Powerball numbers that have the greatest chance of winning.

from random import*

data = {}
data['numbersW'] = [0,0,0,0,0]
data['numbersR'] = [0]
data['whiteBalls'] = []
data['redBalls'] = []


for i in range(0,5):
    white = int(input('Enter the last winning numbers:'))
    data['whiteBalls'].append(white)
        
for num in range(0,1):
    latest = int(input('Enter the powerball #:'))
    data['redBalls'].append(latest)


for num in range(0,5):
    for num in range(0,5):
        data['numbersW'][num] = randint(1,69)
            
    for num in range(0,1):
        data['numbersR'][num] = randint(1,latest-1)
            
            
            
def matching():
    for num in data['whiteBalls']:
        if num in data['numbersW']:
            data['numbersW'][num] = randint(1,69)
print(data['numbersW'][:],data['numbersR'][:])
print(data['whiteBalls'])
print(data['redBalls'])
