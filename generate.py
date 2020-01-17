import random

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
    return ["{} gold".format(starting_gold()), lame_weapon(), occupational_object(), random_object() ]

def print_list( list_of_strings ):
    str = ""
    for i, line in enumerate(list_of_strings):
        if i > 0: # don't put a comma on the first line
            str += ", "
        str += line
    return str

def starting_gold(total = 0):
    if random.randint(0, 9) == 0:
        return total
    else:
        return starting_gold(total +1) 

def center_format(str, pad_character = " ", width = 32):
    if len(str) >= width:
        return str
    
    left_pad_amount = int ((width - len(str)) / 2)
    right_pad_ammount = int(width - len(str) - left_pad_amount)
    
    return pad_character*left_pad_amount + str + pad_character*right_pad_ammount


def header():
    return "~ MEATGRINDER! MEATGRINDER! ~"

def print_character():
    to_print = ""
#    to_print +=  "{}\n".format( header() )
#    to_print += '\n'
    to_print += center_format("{} the {} {}".format( character_name(), personality(), occupation() )) + '\n'
    to_print += "================================\n"
    to_print += "STR:{0: >2}   WIS:{1: >2}\n".format( roll_3d6(), roll_3d6() )
    to_print += "DEX:{0: >2}   INT:{1: >2}\n".format( roll_3d6(), roll_3d6() )
    to_print += "CHA:{0: >2}   CON:{1: >2}\n".format( roll_3d6(), roll_3d6() )
    to_print += "\n"
    to_print += "{}\n".format(print_list( roll_objects() ))
    ## to_print += ("\n\n\n") # Trailing newlines moved to print_receipt.py
    print(to_print)
    
print_character()