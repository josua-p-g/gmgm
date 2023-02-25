import random
from os import system, name
import time,sys
artifact = False
knock = 0

def tprint(text):
  for character in text:
    sys.stdout.write(character)
    sys.stdout.flush()
    time.sleep(0.05)
   
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def tspace():
   print('\n\n\n')

def death():
   print(eyes_closed)
   for i in range(10):
     sys.stdout.write("""\n                                    """)
     sys.stdout.flush()
     time.sleep(.5)
   sys.stdout.write("Game Over...")
   sys.stdout.flush()
   time.sleep(2)
   print('')
   quit()

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
   hit = ['attacked','walloped','clobbered','smacked','smited','dang near dismantled','acted unkindly towards']
   u_a = Player.attack + weplst[0].attack
   o_a = opp.attack + weplst[1].attack
   u_d = Player.defend + weplst[0].defend
   o_d = opp.defend + weplst[1].defend
   tspace()
   print(Player.name, "grabs the", weplst[0].name,",", opp.name, "picks up the", weplst[1].name,'..')
   time.sleep(1)
   input('Press enter to begin fight...')
   round = [[Player.name, u_d, u_a, o_d, opp.name,Player.attack,fist],[opp.name,o_d,o_a, u_d,Player.name,opp.attack,fist_reverse]]
   while True:
      for i in round:
       clear()
       hitpoint = int(random.randint(i[5],i[2]))
       print(i[6])
       print("\n",i[0] , "has", random.choice(hit) , i[4] , "for" , hitpoint , "damage.\n")
       i[3] = i[3] - hitpoint
       
       if i[3] <= 0:
         time.sleep(.5)
         tprint("\n"+ i[4] + " has died.\n")
         time.sleep(1)
         if i[4] == Player.name:
           time.sleep(1.5)
           clear()
           death()
         else:
             input("Press enter to continue..")
             return False 
       else:
         input("Press enter to continue..")
         continue


fist = """
                                     ▌  
 ,,                            ▄▄    ▓
 ▀▀▀▀▀▀▀▓▓▄╦                    "█▓, ▓
          `▀▀▀▀▀▓▓▓▓▓▄▄▄▄╦,,      '▀  
                       `Γ"▀▀▀▀▀▓▓▓▓▄▄ 
                                    █µ
                                  ▐ █▌
      `⌂⌐,                       ∩j▌█▌
╓╗▄▄▓▓▓▓██▄▄                    j▄j▌█W
Γ"`        ▀▓▓▄╦, ,             J█j██⌐
             "███▀▀▀▓▓▓▓█▄, ▄─   █µ██⌐
               `T▀▀▀█▀  `Å▀▀▀╖   ▓▌██⌐
                    "▀█▓▄▄,,  `  ╫▌█▀ 
                       Å███▀▀▀▓▓▓▀▀"                         
                          "▀▀▀▀Γ     ▓
                                ╓█Γ  █
                              ╓▓▀    █
                              ""     █
"""

fist_reverse = """                                       
▌                                         
▓▌   ╥█                                    
▓▌  ▄█                                     
  "▀                 ,,╓╦▄▄▄▄▄▓▓▓▓▓▓▄▄▄▄▄▄
    ╓▓▓▓▓▓▓▓▓▓▓▓▀▀▀▀▀▀▀▀▀Γ"`             :└
µ  .█Ü                                     
▌  ▐█                                      
▌  █▌   `▄                  `φ┐            
W ▐█    .`▓ ,'              ▄▓▓▄╦,         
 █▌     "██▓             .▓▌  ""▀▀▓▓▄▄╓   
⌐)█    ,w▀▓█▀            ╓█▀          "▀▀▀N
⌐▓█,,   ╓█▀        ╓▄▄▄▓▓▀`                
  ╙▀▀▀▀██`     .▄▓▀▀└                      
       █▌    .▄█▀                          
▓µ     ╙█▓▄╦▄█▀                            
█▌  ▀▓    ""┘                              
█▌   ▀█µ                                   
█▌    "▀                                   
"""
                                                                                                                                                                                                   
eyes_open="""
                  ,▄▓██████████▓▄,                                   ,▄▓██████████▓▄,         
                ▄█▀▀"       `▀▀████▓▄                             ▄▓████▀▀:       "▀▀█▄       
              .▀"                "▀████▄                       ▄████▀?                "▀,     
                                    '▀███▄,                 ╓▓███▀`                     `     
                       ,▄«4ⁿⁿ=«w▄,     `▀▀██▄             ▄██▀▀      ,▄∞«=ⁿⁿæw▄,              
                    x^∞;~,\)┐┐' ┐,"ªw,                           ,æ^",¿  ¿┌Ç^¿*;ÅY╕           
           '─,~.`~─▄▄▄█▓████████▓█▄ µ \,                       ,^ | ▄█▓████████▓█▄Ωå⌐',┌',-`  
              `"~=██▀▀"  ▌ ████▀██▀██▌╒                         µ▌██▀█████'█ }  "▀▀██=^"`     
               ^┌^Q██▄   ▌ █▀████▀ ▌ ▀█▄                      '▄█▀ $ ▀██████ █   ▄██"~─~      
                 `⌐▄▀██▓▄ ▀▄"▀▀▀,▄▀    ▀█,                   ┌█▀    ▀▄`▀▀▀"▄▀ ▄▓██▀Σ-`        
                    ┌`╒▀▀▀███████▄▄▓Φ~ ,▄█                   █▄, *π▓▄▄███████▀▀▀,`⌐-          
                         A²╒▐▐▐  U~                                 '▐  ⌐⌐µµ\Y `              """

eyes_closed = """                                                                                                                                                                                                       
                  ╓▄▄▓██████████████▓▄▄,                     ╓▄▄▓██████████████▓▄▄,                       
              ▄▓█▀▀▀▀▀'"'```'"'"▀▀▀▀▀████▓                τ████▀▀▀▀▀▀"'""'''"'"▀▀▀▀▀█▓▄                   
            -▀                                                                        `▀                  
                                                                                                          
                     ,▄∞=ⁿ^ⁿⁿ«w▄,                                   ╓▄«=ⁿ^ⁿⁿ«w▄,                          
                  ╓^"            '▀«╥                           ▄^▀             "V,                       
          \      ^                   "V,                     ╓^`                   τ     ,                
           ,~╖,                         \                  ,"                       . ,∞"                 
            `"*ª█▓;                                                               ▄▓▀ª^"                  
              ─⌐^▄▀█▓▄╦                 ,,                 ,,                ,▄▄█▀▀"~─                    
                 ¬"╓^▄▀▀███▓▓▓▓▓▓▓███▀▀" ".               "└ "▀▀███▓▓▓▓▓▓▓████▀▄v;*-`                     
                    ` :^,"Å▐ ÜÅΓ`                                `^7 µÜ┤▐ ,\ <^                           
"""

def death():
   print(eyes_closed)
   for i in range(10):
     sys.stdout.write("""\n                                    """)
     sys.stdout.flush()
     time.sleep(.5)
   sys.stdout.write("Game Over...")
   sys.stdout.flush()
   time.sleep(2)
   print('')
   quit()

class Player:
    name = ''
    attack = 99
    defend = 2
class Betty:
    name = 'Betty'
    attack = 22
    defend = 28
class Francine:
    name = 'Francine'
    attack = 32
    defend = 18
class Gerdie:
    name = 'Gerdie'
    attack = 30
    defend = 30

class Pan:
   name = 'frying pan'
   attack = 52
   defend = 17
class BirchLog:
   name = 'birch log center piece'
   attack = 15
   defend = 54
class Cane:
   name = 'cane'
   attack = 9
   defend = 60
class HotGlue:
   name = 'hot glue gun'
   attack = 41
   defend = 28

class BiscuitBarrel:
   name = "Biscuit Barrel"
   def arrive():
      weapons = {1:Cane, 2:Pan}
      opponent = Betty
      clear()
      location_keys.remove(loc_choice)
      tspace()
      print('you walk in and see Betty. It   input()s on sight. you notice a cane in the corner, and a frying pan on a table. which do you choose?\n')
      battle(weapon_choice(weapons),opponent)
      clear()
      print('\n\n\nSnarky comment about something..\n')
class JolenesFabrics:
   name = "Jolene's Fabrics"
   def arrive():
      weapons = {1:BirchLog, 2:HotGlue}
      opponent = Francine
      clear()
      location_keys.remove(loc_choice)
      tspace()
      print('there that broad, francine, you see a woman with a walker meandering past, and a hot glue gun on the counter. do you pick one up?\n')
      battle(weapon_choice(weapons),opponent)
      clear()
      print('\n\n\n you leave, slightly worse for the wear, and head to your LeSabre..\n')
class BennysBingo():
   name = "Benny's Bingo"
   def arrive():
      global knock,artifact
      if len(location_keys) == 1:
        weapons = {}
        opponent = Gerdie
        clear()
        location_keys.clear()
        if artifact == True:
          print('secret ending (.)(.)')
          print("""You walk into darkened Bingo Parlor, empty save the imposing silhouette of Gerdie at the bar.\n"""
                """"You broke my door, I know it was you. You were looking for me" Gerdie hisses.\n"""
                """"I was looking for you, but I found something else.." you reply as you set the\n"""
                """contents of your pocket onto the table in front of you. Dusty rays of light filter through\n"""
                """the blinds onto the stainless slide of a Colt Delta Elite.\n"""
                """"That's mine, you took it!" Gerdie shrieks and starts towards you.\n"""
                """"That's right, I took it, but I'm not done taking yet" you say as you pick up the pistol.\n""")
          input("Press enter to continue")
          clear()
          print("""You level the pistol at her. She stops dead in her tracks.
                "Give me everything...""")
        else:
           print(location_keys)
           print('boss level')
      else:
         if knock == 3:
          clear()
          print("WHOOPS! The dang door broke! Well, since it's already open, there's no damage\nin taking a look around. There's no one here but there's a coat hanging on the coat rack.\nYou examine the coat's pockets and find a pistol.. \n")
          while True:
            takegun = input("Do you take the pistol? Y/N :")
            if takegun.lower() == "y":
              artifact = True
              clear()
              print("\n\n\nYou take the pistol and slide out through the broken door back to your LeSabre\n")
              break
            elif takegun.lower() == "n":
              clear()
              print("\n\n\nYou leave the gun where it was and slide back through the broken door to your LeSabre\n")
              break
            else:
              clear()
              print("\n", takegun, " is not a valid choice.\n\n")
              continue
          knock += 1
         elif knock == 4:
            clear()
            tprint("You pull back up to the scene of your B&E. Gerdie is standing there with the police.\n'That's her!' she cries. You're fingerprints are everywhere.\nThey draw their weapons,you close your eyes..")
            time.sleep(1.5)
            clear()
            death()

         else:  
           clear()
           print("\n\n\n\nThis place doesn't appear to be open yet. I'll try back later\n\n\n")
           knock += 1
         

location_dict = {1:BiscuitBarrel, 2:JolenesFabrics, 3:BennysBingo}
location_keys = [i for i in location_dict.keys()]

clear()
print('''
       _________    ____    ____      _________    ____    ____ 
      /  ____   |  |    \  /    |    /  ____   |  |    \  /    |
     |  |    |__|  |     \/     |   |  |    |__|  |     \/     |
     |  |   ____   |            |   |  |   ____   |            |
     |  |  |__  |  |   |\  /|   |   |  |  |__  |  |   |\  /|   |
     |  |____|  |  |   | \/ |   |   |  |____|  |  |   | \/ |   |
      \_________|  |___|    |___|    \_________|  |___|    |___|

                   Welcome to GrandMaster Grand Ma

               Please enter the name of your fighter:
          ''')

# Player.name = input()
# clear()

# tprint('Welcome, ' + Player.name)
# time.sleep(1)
# tprint(', dawn is only 3 hours away..')
# time.sleep(.5)
# print(eyes_closed)
# time.sleep(2.2)
# clear()
# print('Welcome, ' + Player.name + ', dawn is only 3 hours away..')
# print(eyes_open)
# time.sleep(2.7)
# clear()
# tspace()
# print("You've awakened in a place, there's some things, something happened, you need to do something about it.\n")



while len(location_keys) > 0:
    for k in location_keys:
      print(k ,  "-" , location_dict[k].name)
    if len(location_keys) > 1:
      print("\nWhere to? Type " + ", ".join(map(str,location_keys[:-1])) + " or " + str(location_keys[-1]) + ": ")
    else:
      print("Where to? Type " + str(location_keys[-1]) + ": ")
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
        arena = location_dict[loc_choice]
        arena.arrive()
        continue

print('sunnnrise')

