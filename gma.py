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

def tspace(num):
   for i in range(num):
     print('\n')

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
      clear()
      tspace(6)
      print("'",  weapon_choice_raw + "' is not a valid number, please type 1 or 2: \n\n")
      continue
    if weapon_choice not in range(1,3):
      clear()
      tspace(6)
      print("'", weapon_choice_raw + "' is not a valid choice. Please type 1 or 2: \n\n")
      continue
    else:
      clear()
      break
  options.remove(weapon_choice)
  weapon_list = [w[weapon_choice], w[options[0]]]
  return weapon_list

def battle(weplst,opp):
   hit_verb = ['attacked','walloped','clobbered','smacked','smited','dang near dismantled','acted unkindly towards']
   u_a = Player.attack + weplst[0].attack
   o_a = opp.attack + weplst[1].attack
   u_d = Player.defend + weplst[0].defend
   o_d = opp.defend + weplst[1].defend
   tspace(6)
   print(Player.name, "grabs the", weplst[0].name,",", opp.name, "picks up the", weplst[1].name,'..\n')
   time.sleep(1)
   input('Press enter to begin fight...')
   round = [[Player.name, u_d, u_a, o_d, opp.name,Player.attack,fist],[opp.name,o_d,o_a, u_d,Player.name,opp.attack,fist_reverse]]
   while True:
      for i in round:
       clear()
       hitpoint = int(random.randint(i[5],i[2]))
       print(i[6])
       print("\n\n",i[0] , "has", random.choice(hit_verb) , i[4] , "for" , hitpoint , "damage.\n")
       i[3] = i[3] - hitpoint
       
       if i[3] <= 0:
         time.sleep(.5)
         tprint("\n\n\n"+ i[4] + " has fallen.\n")
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

class Player:
    name = ''
    attack = 40
    defend = 25
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
    attack = 39
    defend = 86

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
class DustMop:
   name = 'dust mop'
   attack = 30
   defend = 50
class Bottle:
   name = 'whiskey bottle'
   attack = 50
   defend = 30
class Artifact:
   name = 'pistol'
   attack = 101
   defend = 11

class BiscuitBarrel:
   name = "Biscuit Barrel"
   def arrive():
      weapons = {1:Cane, 2:Pan}
      opponent = Betty
      clear()
      location_keys.remove(loc_choice)
      tspace(2)
      print("""You kick open the door to the Biscuit Barrel, the smells of coffee and bacon\n"""
            """hammerfist you in the face, but the breakfast buffet won't satiate you this time.\n"""
            """Betty is seated by herself, her cane leaned against her table.\n"""
            """Her Sunrise Scrambler sits sizzling before her.\n"""
            """Neither one of you wait for the bell.""")
      print("\n\n\nPlease choose your weapon:\n\n")
      battle(weapon_choice(weapons),opponent)
      clear()
      opps_down = 3 - len(location_keys)
      print("""\n\n"""
            """"I always said Betty would do well to skip breakfast", you quip while turning\n"""
            """the ignition to the LeSabre.""", opps_down, """down,""", len(location_keys) , """to go.\n\n\n\n\n\n\n""")
class JolenesFabrics:
   name = "Jolene's Fabrics"
   def arrive():
      weapons = {1:BirchLog, 2:HotGlue}
      opponent = Francine
      clear()
      location_keys.remove(loc_choice)
      tspace(2)
      print(""" You walk into the unlocked back door to the fabric store. Francine is there\n"""
            """ preparing for her shift. "Them grandkids of yourn don't know how to act and\n"""
            """ I guess you're the one that taught 'em" you say as you cross the hall to the\n"""
            """ employee room. There's a nice birch log centerpiece on the table someone was\n"""
            """ hot gluing burlap to. "One of you'uns gotta tote this whoopin, guess that's\n"""
            """ gonna be you,too" """)
      print('\n\n\nPlease choose your weapon:\n\n')
      battle(weapon_choice(weapons),opponent)
      clear()
      print('\n\n\n You hotglue your wounds closed and, slightly worse for the wear, head to your LeSabre..\n\n\n')
class BennysBingo():
   name = "Benny's Bingo"
   def arrive():
      global knock,artifact
      if len(location_keys) == 1:
        weapons = {1:DustMop,2:Bottle}
        clear()
        location_keys.clear()
        if artifact == True:
          tspace(2)
          print("""You walk into darkened Bingo Parlor, empty save the louring silhouette of Gerdie at the bar.\n"""
                """Gerdie looks up, " """, Player.name ,"""you broke my door, I know it was you. You were looking for me."\n\n"""
                """"I was looking for you, but I found something else.." you reply as you set the\n"""
                """contents of your pocket onto the table in front of you. The old Venetian blinds slice\n"""
                """dusty rays of light onto the table, where glints the stainless slide of a Colt Delta Elite.\n\n"""
                """"That's mine, you stole it!" Gerdie starts towards you, eyes never leaving the Colt.\n\n"""
                """"That's right, I took it, and I'm here to take the rest" you say as you pick up the pistol.\n""")
          input("Press enter to continue")
          clear()
          tspace(2)
          print("""Gerdie stops dead in her tracks. "Is this about the kids fighting again?" she asks.\n\n"""
                """"It's not about what they were doing, it's about what they were saying.. you told them."\n\n"""
                """"No I didn't, and even if I did, it's been fifty some years..."\n\n"""
                """"You talked."\n\n"""
                """\"No one is looking for you,""", Player.name, """, you're a good woman, you wouldn't do this."\n\n"""
                """\"What is a good woman? Who gets to decide that? Does everyone get a vote? What about HIM? That man?\n"""
                """  What would HE say? One resounding 'nay' on a mail-in ballot from an unmarked grave in the desert.\n"""
                """  Or maybe there's a count.. A tally of all the bad and good you've done in your life, the needle ever swinging\n"""
                """  back and forth across center for 89 years? Can you get too far into the red? Because one day\n"""
                """  the needle stops swinging."\n\n"""
                """Gerdie lookes on in silence, fixated on the 10 millimeter aperture in front of her.\n\n"""
                """"I just hope I've swung the needle far enough to make up for this..."\n""")
          time.sleep(3)
          input("Press enter to continue")
          clear()
        else:
           tspace(2)
           print(""" Gerdie's car is out front as you wheel the LeSabre perfectly into the first spot past the handicap parking.\n"""
                 """ Stale smoke and the sounds of penny slots lend this place the only bit of charm it has. The place is empty,\n"""
                 """ except for the louring silhouette of Gerdie at the bar.\n\n"""
                 """ "Them yougins of yourn fight as dirty as you do," you say, stepping past an butt pocked dust mop.\n\n"""
                 """ "And yours loses as bad as you do" she fires back as she circumnavigates the counter where her"""
                 """ hair-of-the-dog hooch sits sweating."""
                 )
           print('\n\n\nPlease choose your weapon:\n\n')
           while True:
            for k,v in weapons.items():
              print(k,"-",v.name)
            weapon_choice_raw = input()
            try:
              weapon_choice = int(weapon_choice_raw)
            except ValueError:
              clear()
              tspace(6)
              print("'",  weapon_choice_raw + "' is not a valid number, please type 1 or 2: \n\n")
              continue
            if weapon_choice not in range(1,3):
             clear()
             tspace(6)
             print("'", weapon_choice_raw + "' is not a valid choice. Please type 1 or 2: \n\n")
             continue
            else:
              clear()
              break
           final_weapons = [weapons[weapon_choice],Artifact]
           clear()
           tspace(3)
           print("As you reach for a weapon Gerdie slides a loaded pistol from the jacket hanging by the door...\n\n")
           time.sleep(2)
           input('Press enter to continue..')
           clear()
           battle(final_weapons,Gerdie)
           clear()
           tspace(3)
           input("It's finally over, press Enter to go home...")
           clear()

      else:
         if knock == 3:
          clear()
          string_knock = "\n\n\nWHOOPS! The dang door broke! Well, since it's already open, there's no damage\nin taking a look around. There's no one here but there's a coat hanging on the coat rack.\nYou examine the coat's pockets and find a pistol.. \n\n"
          print(string_knock)
          tspace(3)
          while True:
            takegun = input("Do you take the pistol? Y/N :")
            if takegun.lower() == "y":
              artifact = True
              clear()
              print("\n\n\nYou take the pistol and slide out through the broken door back to your LeSabre\n\n\n\n\n")
              break
            elif takegun.lower() == "n":
              clear()
              print("\n\n\nYou leave the gun where it was and slide back through the broken door to your LeSabre\n\n\n\n\n")
              break
            else:
              clear()
              print(string_knock , "\n\n\n\n" ,  takegun , "' is not a valid choice.\n")
              continue
          knock += 1
         elif knock == 4:
            clear()
            tprint("\n\nYou pull back up to the scene of your B&E. Gerdie is standing there with the police.\n"
                   "'That's her!' she cries. Your fingerprints are everywhere.\n"
                   "They draw their weapons. You close your eyes..")
            time.sleep(1.5)
            clear()
            death()

         else:  
           clear()
           print("\n\n\n\nThis place doesn't appear to be open yet. I'll try back later\n\n\n\n\n\n\n\n")
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

Player.name = input()
clear()

tprint('Welcome, ' + Player.name)
time.sleep(1)
tprint(', dawn is only 3 hours away..')
time.sleep(.5)
print(eyes_closed)
time.sleep(2.2)
clear()
print('Welcome, ' + Player.name + ', dawn is only 3 hours away..')
print(eyes_open)
time.sleep(2.7)

clear()

print("""\n
You wake with a start. It's your phone. A message from your grandson. 
The other kids at school have been picking on him again.
You sit up and kick around for your slippers.
You know the bullies.. well, specifically, you know their grandmas..
You lost the North Idaho Kumite to Gerdie back in '43, with her two sisters
placing 3rd and 4th. It seems like it's high time for a rematch.
You know the places they frequent, and the LeSabre is gassed up.\n
""")

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
        tspace(4)
        print("'" , loc_choice_raw , "' is not a number.\n")
        continue
    if loc_choice not in location_keys:
        clear()
        tspace(4)
        print("'" , loc_choice_raw , "' is not a valid choice.\n")
        continue
    else:
        arena = location_dict[loc_choice]
        arena.arrive()
        continue
tspace(3)
print("""
                                ,╓╖╖╔╔µ╗mææ@@@@@@@▄▄@@@@@@@@ææ╗╗╗╖╖╖,                               
                              ,@▒██████████████████████████████████▓▓▒W                             
                             Æ▓████████████████████████████████████████▒µ                           
                           ,╫████████████████████████████████████████████@                          
                      ╓▄▄▓▄▒██████████████████████████████████████████████▓▄▄▄╖                     
                     └████▒████████████████████████████████████████████████▒████                    
                       .@▒▒██████████████▌▌▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓█████████████████▒▒µ                      
                      ▄▒╫▒▒▒▒▒╫▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒╫╫▓╫╫▓                     
                     ╒▓▓▒▒Ñ▒▒▒▒░░░░░░░░░░▒å▒▒∞░░░░░╨RR▒ÑÑ▒Ñ▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒╫▓▓▓                    
                     ▓████▓███▓██████████▓▓███████████████▓▓███████████████▓███▓▌                   
                     ███████████████████▓███████████████████████████████████████▓                   
                    ╫███████████████████████████████████████████████████████████▓⌐                  
                    ╫▓▓███▓▓▓▓█▌▀▀▀▀▀▀▀▀▀████████████████████▀▀▀▀▀▀▀▓██████████▓▓µ                  
                    ▓▓▓▒▒▒▒▒▒▒▒▀▓▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▓▀▒▒▒▒▒▒▒▒▓▓▓M                  
                    ▓██▓▓▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▓▓██⌐                  
                    ▐██▓▓▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒╫▓▓██                   
                     ████▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓███▌                   
                     █████▓▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀Å▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▓█████▌                   
                     ███████████████████████████████████████████████████████████▌                   
                     ████████░░░░░░╙╙░░╙╙╙╙╙╙╙╙╙╙╙╙╙ÅÅ░▒▒▒▒▀▀▀▀▀▀▀▀█████████████▌                   
                     ████████▒▒░░░░░░                            ````░▒▒████████M                   
                     `███████▒░░░                                     ░▒▓███████                    
                         ``╙╙"``                                       ````                         
""")
tprint("\n\nThe treeline on the far side of County Road 55 is baked in a cadmium glow as you pull\nthe LeSabre westward onto the blacktop. The gas gauge dipping towards 'E'")
time.sleep(1)
print('\n\nGame Over...')