from random import random
from os import system, name
import time,sys
odometer = 0

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
      break

  options.remove(weapon_choice)
  weapon_list = [w[weapon_choice], w[options[0]]]
  return weapon_list

def battle(weplst,opp):
   user_weapon = weplst[0]
   opp_weapon = weplst[1]
   u_a = Player.attack + weplst[0].attack
   o_a = opp.attack + weplst[1].attack
   u_d = Player.attack + weplst[0].defend
   o_d = opp.defend + weplst[1].defend
   round = [[Player.name, u_d, u_a, o_d, opp.name],[opp.name,o_d,o_a, u_d,Player.name]]
   for i in round:
    
      print(i[0] , " has attacked " , i[4] , " for " , i[2] , " damage.")
      i[3] -= i[2]
      if i[3] <= 0:
         print(i[4] + " has died.")
         if i[4] == Player.name:
            input("Game Over..")
            quit()
         else:
            input("Press enter to continue..")
      
         break 
      else:
         print(u_d, o_d)
         input("Press enter to continue..")
         continue
   print("user health =", u_d)  
   input()
               
     
     
   



class Player:
    name = ''
    attack = 10
    defend = 20
class Betty:
    name = 'Betty'
    attack = 10
    defend = 20
class Francine:
    name = 'Francine'
    attack = 10
    defend = 20
class Gerdie:
    name = 'Gerdie'
    attack = 10
    defend = 20

class Pan:
   name = 'frying pan'
   attack = 50
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
   attack = 50
   defend = 10

class BiscuitBarrel:
   name = "Biscuit Barrel"
   def arrive():
      weapons = {1:Cane, 2:Pan}
      opponent = Betty
      clear()
      location_keys.remove(loc_choice)
      tspace()
      print('you walk in and see Betty. Its on sight. you notice a cane in the corner, and a frying pan on a table. which do you choose?\n')
      battle(weapon_choice(weapons),opponent)
      print('\n\n\nSnarky comment about something..\n')

class JolenesFabrics:
   name = "Jolene's Fabrics"
   def arrive():
      weapons = {1:Walker, 2:HotGlue}
      opponent = Francine
      clear()
      location_keys.remove(loc_choice)
      tspace()
      print('there that broad, francine, you see a woman with a walker meandering past, and a hot glue gun on the counter. do you pick one up?\n')
      battle(weapon_choice(weapons),opponent)
      print('\n\n\n you leave, slightly worse for the wear, and head to your LeSabre..\n')

class SunnyvaleRetirement:
   name = "Sunnyvale Retirement"
   def arrive():
      if len(location_keys) ==1:
        weapons = {}
        opponent = Gerdie
        clear()
        location_keys.clear()
        print(location_keys)
        print('boss level')
 
      else:
         clear()
         print("\n\n\nThis place doesn't appear to be open yet. I'll try back later\n")
         

location_dict = {1:BiscuitBarrel, 2:JolenesFabrics, 3:SunnyvaleRetirement}
location_keys = [i for i in location_dict.keys()]

clear()
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
# tprint('Welcome, ' + Player.name)
# time.sleep(1)
# tprint(', dawn is only 3 hours away..')
# time.sleep(.5)
# clear()
# time.sleep(.5)
# tspace()
clear()
tspace()

# //////graphic of eyes opening

# tprint('Welcome, ' + Player.name)
# time.sleep(1)
# tprint(', dawn is only 3 hours away..')
# time.sleep(.5)
# clear()
# time.sleep(.5)
# tspace()

while len(location_keys) > 0:
    if odometer == 0:
      print("you've awakened in a place, theres's some things, something happened and you need to do something about it. It's your old nemesis, whoe's her face? Gertrude or something silly. I think ihave time before my shows.")
      print('\n')
    else:
       pass
    for k in location_keys:
      print(k ,  "-" , location_dict[k].name)
    if len(location_keys) > 1:
      print("\nWhere to? Type " + ", ".join(map(str,location_keys[:-1])) + " or " + str(location_keys[-1]) + ":")
    else:
      print("Where to? Type " + str(location_keys[-1]) + ":")
    loc_choice_raw = input()
    try:
        loc_choice = int(loc_choice_raw)
    except ValueError:
        clear()
        print("\n\n'",loc_choice_raw , "' is not a number.\n")
        continue
    if loc_choice not in location_keys:
        clear()
        print("\n\n'",loc_choice_raw , "' is not a valid choice.\n")
        continue
    else:
        print(location_keys)
        arena = location_dict[loc_choice]
        arena.arrive()
        odometer += 1
        continue

print('sunnnrise')

