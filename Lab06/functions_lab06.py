# Importing the random library to use for the dice later
import random
import os
# Checking if the line below is printing when importing function.py into main.py
# print("Inside function.py")

# Lab 4: Question 4
# Defining a function that is using loot to modify health points
def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]  # Items that increase health
    bad_loot_options = ["Poison Potion"]  # Items that decrease health

    print("    |    !!You are seeing a monster in the distance! So you are quickly using your first item:")
    first_item = belt.pop(0)  # Remove and use the first item in the belt
    if first_item in good_loot_options:
        health_points = min(20, (health_points + 2))  # Increase health but cap at 20
        print("    |    You are using " + first_item + " to increase your health to " + str(health_points))
    elif first_item in bad_loot_options:
        health_points = max(0, (health_points - 2))  # Decrease health but not below 0
        print("    |    You are using " + first_item + " to decrease your health to " + str(health_points))
    else:
        print("    |    You are using " + first_item + " but it is not helpful")
    return belt, health_points

# Lab 4: Question 3 
# Defining a function that is collecting loot and adding it to the belt
def collect_loot(loot_options, belt):
    ascii_image3 = """
                      @@@ @@                
             *# ,        @              
           @           @                
                @@@@@@@@                
               @   @ @% @*              
            @     @   ,    &@           
          @                   @         
         @                     @        
        @                       @       
        @                       @       
        @*                     @        
          @                  @@         
              @@@@@@@@@@@@          
              """
    print(ascii_image3)  # Display ASCII image
    loot_roll = random.choice(range(1, len(loot_options) + 1))  # Randomly select loot
    loot = loot_options.pop(loot_roll - 1)  # Remove loot from the options
    belt.append(loot)  # Add loot to the belt
    print("    |    Your belt: ", belt)
    return loot_options, belt

# Defining a function that is handling the hero's attack
def hero_attacks(combat_strength, m_health_points):
    ascii_image = """
                                @@   @@ 
                                @    @  
                                @   @   
               @@@@@@          @@  @    
            @@       @@        @ @@     
           @%         @     @@@ @       
            @        @@     @@@@@     
               @@@@@        @@       
               @    @@@@                
          @@@ @@                        
       @@     @                          
   @@*       @                          
   @        @@                          
           @@                                                    
         @   @@@@@@@                    
        @            @                   
      @              @                   

  """
    print(ascii_image)  # Display ASCII image
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        m_health_points = 0  # Monster dies
        print("    |    You are killing the monster")
    else:
        m_health_points -= combat_strength  # Reduce monster health
        print("    |    You are reducing the monster's health to: " + str(m_health_points))
    return m_health_points

# Defining a function that is handling the monster's attack
def monster_attacks(m_combat_strength, health_points):
    ascii_image2 = """                                                                 
           @@@@ @                            
      (     @*&@  ,                          
    @               %                        
     &#(@(@%@@@@@*   /                       
      @@@@@.                                 
               @       /                    
                %         @                  
            ,(@(*/           %              
               @ (  .@#                 @   
                          @           .@@. @
                   @         ,              
                      @       @ .@          
                             @              
                          *(*  *      
             """
    print(ascii_image2)  # Display ASCII image
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        health_points = 0  # Player dies
        print("    |    Player is dead")
    else:
        health_points -= m_combat_strength  # Reduce player's health
        print("    |    The monster is reducing Player's health to: " + str(health_points))
    return health_points

# Lab 5: Question 7
# Defining a recursive function that is handling dream levels
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    # Checking the base case
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You are starting to regress back through your dreams to real life.")
        return 2

    # Checking the recursive case
    else:
        return 1 + int(inception_dream(num_dream_lvls - 1))

# Lab 6: Save and Load Game Functions
# Defining a function that is saving the game result to a file
def save_game_result(num_stars):
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Getting the folder of the current script
    file_path = os.path.join(script_dir, "save.txt")  # Saving the file in the same folder

    with open(file_path, "a") as file:
        if num_stars >= 3:
            file.write(f"Hero has killed a monster and gained {num_stars} stars.\n")
        else:
            file.write("Monster has killed the hero previously.\n")

# Defining a function that is loading the last game result
def load_last_game():
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Getting the folder of the current script
    file_path = os.path.join(script_dir, "save.txt")  # Loading the file from the same folder

    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if lines:
                last_game = lines[-1].strip()
                print("Previous Game:", last_game)
                return last_game
    except FileNotFoundError:
        return None
    return None

def apply_game_result(last_game):
    """
    Apply changes based on the previous game result.
    If the hero won with more than 3 stars, increase monster's combat strength by +1.
    If the monster won, increase hero's combat strength by +1.
    Otherwise, no change.
    Returns updated (hero_combat_strength, monster_combat_strength).
    """
    hero_combat_strength = 1
    monster_combat_strength = 1

    if last_game:
        if "Hero" in last_game and "stars" in last_game:
            stars = int(last_game.split()[-2])  # Extract number of stars
            if stars > 3:
                monster_combat_strength += 1
        elif "Monster" in last_game:
            hero_combat_strength += 1

    return hero_combat_strength, monster_combat_strength
