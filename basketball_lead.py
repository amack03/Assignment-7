import math

pa = float(input("How many points ahead is one team ahead: "))
pa -= 3
hb = str(input('Does the team ahead have the ball? (y/n): '))

if hb == 'y':
    pa += 0.5
elif hb == 'n':
    pa -= 0.5

spa = pa ** 2
sl = int(input('How many seconds are left in the game: '))

r = ((spa/sl)*100)
r = round(r, 2)

if spa > sl:
    print('Lead is safe.')
    print(f'{r}% percent safe, {pa} safety point margin')
else:
    print('Lead is NOT safe.')
    print(f'{r}% percent safe, {pa} safety point margin')

#In a 2022 NBA game, the Dallas Mavericks did the impossible and came back from a large deficient with not much time remaining to tie the game and go on to win in overtime. How likely was it that the NY Nicks would win based upon safe lead calculation? 
#116.35% percent safe, 5.5 safety point margin