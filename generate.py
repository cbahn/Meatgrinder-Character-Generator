import random
from escpos.printer import Usb

def character_name():
    return "Sam" 
    
def character_title(biggest_stat):
    return " the "+biggest_stat

def get_stats():
    strength = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    dexterity = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    charisma = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    wisdom = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    intelligence = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    constitution = random.randint(1,6) + random.randint(1,6) + random.randint(1,6)
    HP = int(constitution/3.0) + random.randint(1,4)
    to_return = "STR:{0: >2}   WIS:{1: >2}\n".format(strength, wisdom)
    to_return += "DEX:{0: >2}   INT:{1: >2}\n".format(dexterity, intelligence)
    to_return += "CHA:{0: >2}   CON:{1: >2}\n".format(charisma, constitution)
    to_return += "HP: {0: >2}\n".format(HP)
    
    return to_return #[strength, dexterity, charisma, wisdom, intelligence, constitution]
    
def personality():
    options = ["sweet", "bitter", "dry", "moist", "bland", "saucy", "spicy", "hot",
     "salty", "greasy", "sour", "crunchy", "creamy", "minty", "tart", "zesty", "cheesy",
      "flakey", "nutty"]
    return random.choice(options)
    
def occupation():
    options = ["farmer", "baker", "mason", "dancer", "jester", "cabbage seller", "weaver", "shepherd", 
    "barkeep", "innkeeper", "floutist", "milk maid", "noble man", "lumberjack", "elf"]
    return random.choice(options)
    
def lame_weapon():
    options = ["rolling pin", "sewing needle", "lantern", "pine branch", "rat on a string", 
    "large boot", "old sock", "moldy cheese", "chicken (live)", "chicken (dead)", "chicken (rubber)",
    "stick", "pointy stick", "three forks", "lute", "dinner plate", "basket", "bottle", "hamm",
    "sack of potatoes", "tangled net", "syphilis", "jar of bees", "unusual sweater"]
    return random.choice(options)    
    
def occupational_object():
    return "rolling pin"    
    
def random_object():
    return "jar with an eyeball"
    
def starting_gold(total = 0):
    if random.randint(0, 9) == 0:
        return total
    else:
        return starting_gold(total +1) 
        
def printer_print(in_text):
    try:
        p = Usb(0x0416, 0x5011) #, 0, profile="TM-T88III")
        p.text(in_text)
        p.text("\n")
    except:
        print("Connection to printer failed. \n")
        print(in_text)
        print("\n")
    
def print_header():
    try:
        printer_print(" MEATGRINDER! MEATGRINDER! ")
    except:
        print("Connection to printer failed.")

                                                                 
    
def print_character():
    print_header()
    to_print = (character_name())
    to_print += ('\n'+personality())
    to_print += ('\n'+occupation())
    to_print += ('\n'+"Gold: {0}".format(starting_gold()))
    to_print += ('\n'+lame_weapon())
    to_print += ('\n'+occupational_object())
    to_print += ('\n'+random_object())
    to_print += ('\n'+get_stats())
    to_print += ("\n\n\n")
    printer_print(to_print)
    
print_character()