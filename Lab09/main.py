import random  # Importing the random library to use for the dice rolls later
import function  # Importing all the functions from another file

# Defining two Dice
small_dice_options = list(range(1, 7))  # Defining max combat strength as 6
big_dice_options = list(range(1, 21))  # Defining max health points as 20

# Defining the number of stars to award the player
num_stars = 0
input_valid = False

# Looping to get valid input for Hero Combat Strength
i = 0
while not input_valid and i in range(5):  # Allowing up to 5 attempts
    try:
        combat_strength = input("Enter your combat Strength (1-6): ")  # Asking player to input combat strength
        if not combat_strength.isnumeric():  # Checking if input is a number
            raise ValueError("Player needs to enter integer numbers for Combat Strength")
        combat_strength = int(combat_strength)
        if combat_strength not in range(1, 7):  # Validating input range
            raise ValueError("Entering a valid integer between 1 and 6 only")
        input_valid = True  # Setting flag to true if input is valid
    except ValueError as e:
        print(e)  # Printing error message
        i += 1  # Incrementing attempt count

# Looping to get valid input for Monster Combat Strength
m_input_valid = False
while not m_input_valid and i in range(5):  # Allowing up to 5 attempts
    try:
        m_combat_strength = input("Enter the monster's combat Strength (1-6): ")  # Asking for monster combat strength
        if not m_combat_strength.isnumeric():  # Checking if input is a number
            raise ValueError("Monster needs to enter integer numbers for Combat Strength")
        m_combat_strength = int(m_combat_strength)
        if m_combat_strength not in range(1, 7):  # Validating input range
            raise ValueError("Entering a valid integer between 1 and 6 only")
        m_input_valid = True  # Setting flag to true if input is valid
    except ValueError as e:
        print(e)  # Printing error message
        i += 1  # Incrementing attempt count

if input_valid and m_input_valid:
    # Rolling for player health points
    input("Rolling the dice for your health points (Press enter)")  # Prompting player to roll dice
    health_points = random.choice(big_dice_options)  # Randomly selecting health points
    print("Player is rolling " + str(health_points) + " health points")  # Displaying rolled health points

# Rolling for monster combat strength
input("Rolling the dice for the monster's combat strength (Press enter)")  # Prompting player to roll dice
m_combat_strength = random.choice(small_dice_options)  # Randomly selecting monster combat strength
print("Player is rolling " + str(m_combat_strength) + " combat strength for the monster")  # Displaying rolled combat strength

# Rolling for monster health points
input("Rolling the dice for the monster's health points (Press enter)")  # Prompting player to roll dice
m_health_points = random.choice(big_dice_options)  # Randomly selecting monster health points
print("Player is rolling " + str(m_health_points) + " health points for the monster")  # Displaying rolled health points

# Looping while the monster and the player are alive
while m_health_points > 0 and health_points > 0:
    # Starting the fight sequence
    # Determining who attacks first
    input("Rolling to see who attacks first (Press Enter)")  # Prompting player to roll dice
    attack_roll = random.choice(small_dice_options)  # Rolling to determine first attacker
    if not (attack_roll % 2 == 0):  # Checking if odd (hero attacks first)
        input("You are striking (Press enter)")  # Prompting hero to attack
        # Hero is attacking first
        m_health_points = function.hero_attacks(combat_strength, m_health_points)  # Reducing monster health
        if m_health_points != 0:  # Checking if monster is still alive
            input("The monster is striking (Press enter)!!!")  # Prompting monster attack
            try:
                health_points = function.monster_attacks(m_combat_strength, health_points)  # Reducing hero health
            except Exception as e:
                print("Error is occurring in monster attack:", e)  # Printing error if occurs
                break
    else:
        # Monster is attacking first
        input("The Monster is striking (Press enter)")  # Prompting monster attack
        try:
            health_points = function.monster_attacks(m_combat_strength, health_points)  # Reducing hero health
        except Exception as e:
            print("Error is occurring in monster attack:", e)  # Printing error if occurs
            break
        if health_points != 0:  # Checking if hero is still alive
            input("The hero is striking!! (Press enter)")  # Prompting hero to attack back
            # Hero is attacking back
            m_health_points = function.hero_attacks(combat_strength, m_health_points)  # Reducing monster health
