#https://www.reddit.com/r/dailyprogrammer/comments/8s0cy1/20180618_challenge_364_easy_create_a_dice_roller/
from random import randint

input = ['5d12', '6d4', '1d2', '1d8', '3d6', '4d20', '100d100']

for i in input:
    total = 0
    rolls = ''
    d = i.split('d')
    amount = int(d[0])
    faces = int(d[1])
    for a in range(0, amount):
        rint = randint(1, faces)
        total += rint
        rolls += str(rint) + ' '
    print(f'{total}: {rolls}')