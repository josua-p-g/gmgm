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


def weapon_choice(w):
  options = [i for i in w.keys()]
  while True:
    for k,v in w.items():
      print(k,"-",v.name)
    weapon_choice_raw = input()
    try:
      weapon_choice = int(weapon_choice_raw)
    except ValueError:
      print("\n'" + weapon_choice_raw + "' is not a valid number, please type 1 or 2: ")
      continue
    if weapon_choice not in range(1,3):
      print("\n'" + weapon_choice_raw + "' is not a valid choice. Please type 1 or 2: ")
      continue
    else:
      clear()
      print('valid')
      break

  options.remove(weapon_choice)
  weapon_list = [w[weapon_choice], w[options[0]]]
  return weapon_list

def battle(weplst):
   user_weapon = weplst[0]
   opp_weapon = weplst[1]
   print('user', user_weapon)
   print('\nopponent', opp_weapon)



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
   attack = 10
   defend = 10
class Walker:
   name = 'walker'
   attack = 10
   defend = 10
class Cane:
   name = 'cane'
   attack = 10
   defend = 10
class HotGlue:
   name = 'hot glue gun'
   attack = 10
   defend = 10

class BiscuitBarrel:
   name = "Biscuit Barrel"
   def arrive():
      weapons = {1:Cane, 2:Pan}
      clear()
      location_keys.remove(loc_choice)
      print(location_keys)
      print('you walk in and see Betty. Its on sight. you notice a cane in the corner, and a frying pan on a table. which do you choose?')
      battle(weapon_choice(weapons))

class JolenesFabrics:
   name = "Jolene's Fabrics"
   def arrive():
      weapons = {1:Walker, 2:HotGlue}
      clear()
      location_keys.remove(loc_choice)
      print(location_keys)
      print('there that broad, francine, you see a woman with a walker meandering past, and a hot glue gun on the counter. do you pick one up?')
      battle(weapon_choice(weapons))

class SunnyvaleRetirement:
   name = "Sunnyvale Retirement"
   def arrive():
      if len(location_keys) ==1:
        clear()
        location_keys.clear()
        print(location_keys)
        print('boss level')
      else:
         clear()
         print('\ncant come here yet. please make another selection')

location_dict = {1:BiscuitBarrel, 2:JolenesFabrics, 3:SunnyvaleRetirement}
location_keys = [i for i in location_dict.keys()]

# print('''
#        _________    ____    ____      _________    ____    ____ 
#       /  ____   |  |    \  /    |    /  ____   |  |    \  /    |
#      |  |    |__|  |     \/     |   |  |    |__|  |     \/     |
#      |  |   ____   |            |   |  |   ____   |            |
#      |  |  |_   |  |   |\  /|   |   |  |  |_   |  |   |\  /|   |
#      |  |____|  |  |   | \/ |   |   |  |____|  |  |   | \/ |   |
#       \_________|  |___|    |___|    \_________|  |___|    |___|

#                 Welcome to GrandMaster Grand Ma v0.0

#                Please enter the name of your fighter:
#           ''')

# Player.name = input()
# clear()
# tspace()

# //////graphic of eyes opening

# tprint('Welcome, ' + Player.name)
# time.sleep(1)
# tprint(', dawn is only 3 hours away..')
# time.sleep(.5)
# clear()
# time.sleep(.5)
# print('''\nYou've just awoken in a place, there's also things. Somthing has happened. You need
# to do something about it. There's two choices of places to go, each with a different opponent
# and choice of weapon. Or maybe just a cane. Maybe if you keep the cane the entire time it will
# unlock a secret later.. or maybe you can come back here later, and remeber the cane has some
# thing hidden in it that you forgot because of dementia.Maybe you should just take the cane now. 
# How about we just pick a place to go first, then you and your first opponent can pick a weapon
# each?\n''')

while len(location_keys) > 0:
    print('\n')
    for k in location_keys:
      print(k ,  "-" , location_dict[k].name)
    if len(location_keys) > 1:
      print("Where to? Type " + ", ".join(map(str,location_keys[:-1])) + " or " + str(location_keys[-1]) + ":")
    else:
      print("Where to? Type " + str(location_keys[-1]) + ":")
    loc_choice_raw = input()
    try:
        loc_choice = int(loc_choice_raw)
    except ValueError:
        print("\n'" , loc_choice , "' is not a valid number, please type " + ", ".join(map(str,location_keys[:-1])) + " or " + str(location_keys[-1]) + ":")
        continue
    if loc_choice not in location_keys:
        print("\n'" , loc_choice , "' is not a valid choice. Please type " + ", ".join(map(str,location_keys[:-1])) + " or " + str(location_keys[-1]) + ":")
        continue
    else:
        print(location_keys)
        arena = location_dict[loc_choice]
        arena.arrive()
        continue



