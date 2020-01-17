import random

#initialize item lists

good = open('good.txt').read().splitlines()
bad = open('bad.txt').read().splitlines()
weird = open('weird.txt').read().splitlines()

random.shuffle(good)
random.shuffle(bad)
random.shuffle(weird)

# pop an item off the list. If the list is empty, return a default item.
def pull( item_list, default_item = "stick" ):
    if len(item_list) == 0:
        return default_item
    return item_list.pop(0)

# return a random item. gp, bp, and wp are the relative odds of pulling from good, bad, or weird lists.
def roll_item(gp, bp, wp):
  roll = random.randint(0,gp+bp+wp)
  if roll < gp:
    return pull(good)
  roll -= gp
  if roll < bp:
    return pull(bad)
  return pull(weird)

def character_name():
    if random.randint(0,50) == 0:
        return "Patricia"
    return "Sam" 
    
def character_title(biggest_stat):
    return " the "+biggest_stat


def roll_3d6():
    return random.randint(1,6) + random.randint(1,6) + random.randint(1,6)

#    HP = int(constitution/3.0) + random.randint(1,4)

    
def personality():
    options = ["sweet", "bitter", "dry", "moist", "bland", "saucy", "spicy", "hot",
     "salty", "greasy", "sour", "crunchy", "creamy", "minty", "tart", "zesty", "cheesy",
      "flakey", "nutty"]
    return random.choice(options).capitalize()
    
def occupation():
    options = ["farmer", "baker", "mason", "dancer", "jester", "Cabbage Seller", "weaver", "shepherd", 
    "barkeep", "innkeeper", "floutist", "Milk Maid", "noble", "lumberjack", "elf"]
    return random.choice(options).capitalize()
    
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

def roll_objects():
    my_items = [
        roll_item(94, 5, 1),
        roll_item(45,50, 5),
        roll_item(21,45,34)
        ]
    random.shuffle(my_items)
    return my_items

def print_list( list_of_strings ):
    str = ""
    for i, line in enumerate(list_of_strings):
        if i > 0: # don't put a comma on the first line
            str += ", "
        str += line
    return str

def starting_gold():
    if random.randint(0, 9) == 0:
        return 0
    else:
        return 1 + starting_gold()

def center_format(str, pad_character = " ", width = 32):
    if len(str) >= width:
        return str
    
    left_pad_amount = int ((width - len(str)) / 2)
    right_pad_ammount = int(width - len(str) - left_pad_amount)
    
    return pad_character*left_pad_amount + str + pad_character*right_pad_ammount


def header():
    return "~ MEATGRINDER! MEATGRINDER! ~"

def print_character():

    ### CREATE CHARACTER ###

    stats = {}
    stat_types = ["str","dex","cha","wis","int","con"]
    for stat in stat_types:
        stats[stat] = roll_3d6()

    hp = stats["con"] + random.randint(0,3) - 4

    items = roll_objects()
    
    ### PRINT CHARACTER ###

    to_print = ""
#    to_print +=  "{}\n".format( header() )
#    to_print += '\n'
    to_print += center_format("{} the {} {}".format( character_name(), personality(), occupation() )) + '\n'
    to_print += "================================\n"
    to_print += "STR:{0: >2}   WIS:{1: >2}\n".format(stats["str"],stats["wis"] )
    to_print += "DEX:{0: >2}   INT:{1: >2}\n".format(stats["dex"],stats["int"] )
    to_print += "CHA:{0: >2}   CON:{1: >2}\n".format(stats["cha"],stats["con"] )
    to_print += "\n"
    to_print += "{} gold\n".format( starting_gold() )
    to_print += "{}\n".format(items[0])
    to_print += "{}\n".format(items[1])
    to_print += "{}\n".format(items[2])
    to_print += "HP: {}".format(hp)
    ## to_print += ("\n\n\n") # Trailing newlines moved to print_receipt.py
    print(to_print)

while True:
    print_character()
    input("")