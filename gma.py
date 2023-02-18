from random import random
from os import system, name
import time,sys
 
def tprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  
def tinput(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
  value = input()  
  return value
 
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def tspace():
   print('\n\n\n')

class Player:
    name = ''
    attack = 10
    defend = 10
class Betty:
    name = 'Betty'
    attack = 10
    defend = 10
class Francine:
    name = 'Francine'
    attack = 10
    defend = 10
class Gerdie:
    name = 'Gerdie'
    attack = 10
    defend = 10

class Pan:
   name = 'frying pan'
class Walker:
   name = 'walker'
class Cane:
   name = 'cane'

locations_dict = {1:'Biscuit Barrel', 2:'''Jolene's Fabrics'''}
location_keys = [i for i in locations_dict.keys()]



print('''
       _________    ____    ____      _________    ____    ____ 
      /  ____   |  |    \  /    |    /  ____   |  |    \  /    |
     |  |    |__|  |     \/     |   |  |    |__|  |     \/     |
     |  |   ____   |            |   |  |   ____   |            |
     |  |  |_   |  |   |\  /|   |   |  |  |_   |  |   |\  /|   |
     |  |____|  |  |   | \/ |   |   |  |____|  |  |   | \/ |   |
      \_________|  |___|    |___|    \_________|  |___|    |___|

                Welcome to GrandMaster Grand Ma v0.0

               Please enter the name of your fighter:
          ''')

Player.name = input()
clear()
tspace()

# //////graphic of eyes opening

tprint('Welcome, ' + Player.name)
print('''\nYou've just awoken in a place, there's also things. Somthing has happened. You need
to do something about it. There's two choices of places to go, each with a different opponent
and choice of weapon. Or maybe just a cane. Maybe if you keep the cane the entire time it will
unlock a secret later.. or maybe you can come back here later, and remeber the cane has some
thing hidden in it that you forgot because of dementia.Maybe you should just take the cane now. 
How about we just pick a place to go first, then you and your first opponent can pick a weapon
each?\n''')
for k,v in locations_dict.items():
   print(k,v)
firstchoice = int(input())

print(firstchoice)
print(location_keys)

while True:
   if firstchoice in location_keys:
      print('ok')
      break
   else:
      print('nah')
      firstchoice = input()
      break