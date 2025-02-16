# Importing the random library to be used for generating random values later in the game
import random
import os
# Putting all the functions into another file and importing them for use in this game
import functions_lab06

# Attempting to load the last saved game to continue from where it was left off
monster_bonus = 0
try:
    with open("save.txt", "r") as file:
        last_line = file.readlines()[-1].strip()
        print(f"Previous game result: {last_line}")

        # Adjusting the monster's and hero's strength based on previous game results
        if "Hero" in last_line and "stars" in last_line:
            num_stars_previous = int(last_line.split()[-2])
            if num_stars_previous > 3:
                print("Monster is getting stronger this time!")
                monster_bonus = 1
            else:
                monster_bonus = 0
        elif "Monster" in last_line:
            print("Hero is getting stronger this time!")
            hero_bonus = 1
        else:
            monster_bonus = hero_bonus = 0
except FileNotFoundError:
    print("No previous game is found. Starting fresh.")
    monster_bonus = hero_bonus = 0

# Game Flow setup: 
# Defining dice with small and large ranges for the random rolls
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Defining weapons that the hero can use in the game
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Defining loot options that the hero can find during the game
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]
belt = []  # The hero's inventory

# Defining the different powers the monster might have
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Defining the number of stars that the hero will receive at the end of the game
num_stars = 0

# Looping to get valid input for Hero and Monster's Combat Strength
i = 0
input_invalid = True

while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength = input("Enter the monster's combat Strength (1-6): ")

    # Checking if the input values are numeric
    if (not combat_strength.isnumeric()) or (not m_combat_strength.isnumeric()):
        print("    |    One or more invalid inputs. Player needs to be entering integer numbers for Combat Strength    |")
        i += 1
        continue
    elif (int(combat_strength) not in range(1, 7)) or (int(m_combat_strength) not in range(1, 7)):
        print("    |    Entering a valid integer between 1 and 6 only")
        i += 1
        continue
    else:
        input_invalid = False

# Adjusting the combat strength values with any bonuses from previous results
hero_bonus = 0
if not input_invalid:
    combat_strength = int(combat_strength) + hero_bonus
    m_combat_strength = int(m_combat_strength) + monster_bonus

    # Rolling the dice to determine the hero's weapon
    print("    |", end="    ")
    input("Rolling the dice for your weapon (Press enter)")
    ascii_image5 = """
              , %               .           
   *      @./  #         @  &.(         
  @        /@   (      ,    @       # @ 
  @        ..@#% @     @&*#@(         % 
   &   (  @    (   / /   *    @  .   /  
     @ % #         /   .       @ ( @    
                 %   .@*                
               #         .              
             /     # @   *              
                 ,     %                
            @&@           @&@
            """
    print(ascii_image5)

    # Rolling the dice to determine the weapon power
    weapon_roll = random.choice(small_dice_options)
    combat_strength = min(6, (combat_strength + weapon_roll))
    print("    |    The hero's weapon is " + str(weapons[weapon_roll - 1]))

    # Rolling the dice to determine the hero's health points
    print("    |", end="    ")
    input("Rolling the dice for your health points (Press enter)")
    health_points = random.choice(big_dice_options)
    print("    |    Player rolled " + str(health_points) + " health points")

    # Rolling the dice to determine the monster's health points
    print("    |", end="    ")
    input("Rolling the dice for the monster's health points (Press enter)")
    m_health_points = random.choice(big_dice_options)
    print("    |    Monster rolled " + str(m_health_points) + " health points")

    # Collecting loot for the hero to use in battle
    print("    |    !!You are finding a loot bag!! You are looking inside to find 2 items:")
    loot_options, belt = functions_lab06.collect_loot(loot_options, belt)
    loot_options, belt = functions_lab06.collect_loot(loot_options, belt)

    print("    |    Your belt: ", sorted(belt))

    # Using the loot to boost the hero's abilities
    belt, health_points = functions_lab06.use_loot(belt, health_points)

    # Rolling the dice for the monster's magical powers
    print("    |", end="    ")
    input("Rolling for Monster's Magic Power (Press enter)")
    ascii_image4 = """
                @%   @                      
         @     @                         
             &                           
      @      .                           

     @       @                    @     
              @                  @      
      @         @              @  @     
       @            ,@@@@@@@     @      
         @                     @        
            @               @           
                 @@@@@@@                
                                      """
    print(ascii_image4)
    power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])
    m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
    print(f"    |    The monster's combat strength is now {m_combat_strength} using {power_roll} magic power")

    # Looping to get a valid input for how many dream levels the hero wants to go down
    while True:
        print("    |", end="    ")
        num_dream_lvls = input("How many dream levels do you want to go down? (Enter a number 0-3): ")
        if num_dream_lvls.isdigit() and int(num_dream_lvls) in range(4):
            num_dream_lvls = int(num_dream_lvls)
            break
        else:
            print("    |    Invalid input. Please enter a number between 0-3.")

    # If the hero is going down any dream levels, adjusting health points and combat strength
    if num_dream_lvls != 0:
        health_points -= 1
        crazy_level = functions_lab06.inception_dream(num_dream_lvls)
        combat_strength += crazy_level

    # Starting the fight sequence between the hero and the monster
    print("    ------------------------------------------------------------------")
    print("    |    You are meeting the monster. FIGHT!!")
    while m_health_points > 0 and health_points > 0:
        input("Rolling to see who strikes first (Press Enter)")
        attack_roll = random.choice(small_dice_options)

        # Checking who is striking based on the dice roll (even for monster, odd for hero)
        if attack_roll % 2 == 0:
            input("The Monster is striking (Press enter)")
            health_points = functions_lab06.monster_attacks(m_combat_strength, health_points)
        else:
            input("You are striking (Press enter)")
            m_health_points = functions_lab06.hero_attacks(combat_strength, m_health_points)

        # Determining the number of stars based on who wins the fight
        if m_health_points == 0:
            num_stars = 3
        elif health_points == 0:
            num_stars = 1
        else:
            num_stars = 2

    # Saving the game result after the fight
    if health_points > 0:
        result = f"Hero has killed a monster and gained {num_stars} stars."
    else:
        result = "Monster has killed the hero previously."

    # Get the directory of the current script
    script_dir = os.getcwd()

    # Create the full path to save.txt in the same directory as the script
    save_path = os.path.join(script_dir, "save.txt")

    # Now use save_path to open and save the file
    with open(save_path, "a") as file:
        file.write(result + "\n")

    print(f"Game Over! {result}")

    # Final Score Display
    tries = 0
    input_invalid = True
    while input_invalid and tries < 5:
        hero_name = input("Enter your Hero's name (in two words): ")
        name = hero_name.split()
        if len(name) != 2 or not name[0].isalpha() or not name[1].isalpha():
            print("    |    Please enter a valid alphabetical name with two parts.")
            tries += 1
        else:
            short_name = name[0][:2] + name[1][0]
            print(f"    |    I'm going to call you {short_name} for short")
            input_invalid = False

    if not input_invalid:
        stars_display = "*" * num_stars
        print(f"    |    Hero {short_name} is getting <{stars_display}> stars")
