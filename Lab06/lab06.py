# Importing the random library to use for rolling dice later
import random

# Importing all the functions from another file
import functions_lab06

# Defining two Dice, one small (1-6) and one big (1-20)
small_dice_options = list(range(1, 7))
big_dice_options = list(range(1, 21))

# Defining the available Weapons that the hero can use
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]

# Defining the possible Loot items that the hero can collect
loot_options = ["Health Potion", "Poison Potion", "Secret Note", "Leather Boots", "Flimsy Gloves"]

# Initializing an empty belt to store collected loot items
belt = []

# Defining the Monster's special powers and their effects on combat strength
monster_powers = {
    "Fire Magic": 2,
    "Freeze Time": 4,
    "Super Hearing": 6
}

# Initializing the number of stars to award the player at the end
num_stars = 0

# Loading previous game results to determine any carry-over effects
previous_game_result = functions_lab06.load_last_game()

# Applying the results from the previous game to adjust combat strength
combat_strength, m_combat_strength = functions_lab06.apply_game_result(previous_game_result)

# Initializing a loop counter and validation flag for input
i = 0
input_invalid = True

# Asking the player to enter their combat strength and the monster’s combat strength
while input_invalid and i in range(5):
    print("    ------------------------------------------------------------------")
    print("    |", end="    ")
    combat_strength_input = input("Enter your combat Strength (1-6): ")
    print("    |", end="    ")
    m_combat_strength_input = input("Enter the monster's combat Strength (1-6): ")

    # Checking if inputs are numeric
    if not (combat_strength_input.isnumeric() and m_combat_strength_input.isnumeric()):
        print("    |    One or more invalid inputs. Enter integer numbers for Combat Strength")
        i += 1
        continue

    # Converting inputs to integers
    combat_strength = int(combat_strength_input)
    m_combat_strength = int(m_combat_strength_input)

    # Validating if inputs are within the allowed range (1-6)
    if combat_strength not in range(1, 7) or m_combat_strength not in range(1, 7):
        print("    |    Enter a valid integer between 1 and 6 only")
        i += 1
        continue

    input_invalid = False

# Prompting the player to roll a dice for their weapon selection
print("    |", end="    ")
input("Roll the dice for your weapon (Press enter)")

# Displaying an ASCII image for visual effect
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

# Rolling the dice to determine the hero's weapon
weapon_roll = random.choice(small_dice_options)

# Updating combat strength based on the weapon roll
combat_strength = min(6, (combat_strength + weapon_roll))
print("    |    The hero's weapon is " + str(weapons[weapon_roll - 1]))

# Prompting the player to roll a dice for their health points
print("    |", end="    ")
input("Roll the dice for your health points (Press enter)")

# Rolling the dice to determine the player's starting health points
health_points = random.choice(big_dice_options)
print("    |    Player rolled " + str(health_points) + " health points")

# Prompting the player to roll a dice for the monster's health points
print("    |", end="    ")
input("Roll the dice for the monster's health points (Press enter)")

# Rolling the dice to determine the monster's starting health points
m_health_points = random.choice(big_dice_options)
print("    |    Monster rolled " + str(m_health_points) + " health points")

# Collecting loot twice and adding it to the belt
loot_options, belt = functions_lab06.collect_loot(loot_options, belt)
loot_options, belt = functions_lab06.collect_loot(loot_options, belt)

# Sorting the belt items for better organization
belt.sort()
print("    |    Your belt: ", belt)

# Using loot items (if applicable)
belt, health_points = functions_lab06.use_loot(belt, health_points)

# Rolling a dice to determine the monster's special power
print("    |", end="    ")
input("Roll for Monster's Magic Power (Press enter)")
power_roll = random.choice(["Fire Magic", "Freeze Time", "Super Hearing"])

# Increasing the monster's combat strength based on the power rolled
m_combat_strength += min(6, m_combat_strength + monster_powers[power_roll])
print("    |    The monster's combat strength is now " + str(m_combat_strength))

# Asking the player how many dream levels they want to descend into
while True:
    num_dream_lvls = input("How many dream levels do you want to go down? (Enter a number 0-3) ")
    if num_dream_lvls.isnumeric() and 0 <= int(num_dream_lvls) <= 3:
        num_dream_lvls = int(num_dream_lvls)
        break
    print("    |    Please enter a valid number between 0 and 3.")

# Adjusting stats if the player chooses to descend into dream levels
if num_dream_lvls != 0:
    health_points -= 1
    crazy_level = functions_lab06.inception_dream(num_dream_lvls)
    combat_strength += crazy_level

# Starting the fight sequence
while m_health_points > 0 and health_points > 0:
    attack_roll = random.choice(small_dice_options)
    
    # Checking if the attack roll is odd
    if attack_roll % 2 == 1:
        # Hero attacks first
        m_health_points = functions_lab06.hero_attacks(combat_strength, m_health_points)
        if m_health_points == 0:
            num_stars = 3
        else:
            # Monster attacks next
            health_points = functions_lab06.monster_attacks(m_combat_strength, health_points)
    else:
        # Monster attacks first
        health_points = functions_lab06.monster_attacks(m_combat_strength, health_points)
        if health_points > 0:
            # Hero attacks next
            m_health_points = functions_lab06.hero_attacks(combat_strength, m_health_points)

# Asking for hero's name and validating input
tries = 0
input_invalid = True

while input_invalid and tries in range(5):
    print("    |", end="    ")
    hero_name = input("Enter your Hero's name (in two words)")
    name = hero_name.split()

    if len(name) != 2 or not name[0].isalpha() or not name[1].isalpha():
        print("    |    Please enter a valid two-part alphabetical name")
        tries += 1
    else:
        short_name = name[0][:2] + name[1][0]
        print("    |    I'm going to call you " + short_name + " for short")
        input_invalid = False

# Displaying the final score with stars
if not input_invalid:
    stars_display = "*" * num_stars
    print("    |    Hero " + short_name + " gets <" + stars_display + "> stars")

# Saving the game result for future reference
functions_lab06.save_game_result(num_stars)
