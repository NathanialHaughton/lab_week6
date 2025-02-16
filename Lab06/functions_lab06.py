# Importing the random library to use for the dice later
import random

# Defining the save game function
def save_game(result):
    # Opening the save file in append mode
    with open("save.txt", "a") as file:
        # Writing the result to the save file
        file.write(result + "\n")

# Defining the load game function
def load_game():
    try:
        # Opening the save file in read mode
        with open("save.txt", "r") as file:
            # Reading all lines from the save file
            lines = file.readlines()
            # Returning the last line if there are any lines, otherwise returning a message indicating no saved game
            return lines[-1].strip() if lines else "No previous game saved."
    except FileNotFoundError:
        # Handling the case where the save file is not found
        return "No previous game saved."

# The line below will print when you import function.py into main.py
# print("Inside function.py")

# Defining the function to use loot (Lab 4: Question 4)
def use_loot(belt, health_points):
    good_loot_options = ["Health Potion", "Leather Boots"]
    bad_loot_options = ["Poison Potion"]

    # Notifying the player about the monster in the distance and the need to use the first item
    print("    |    !!You see a monster in the distance! So you quickly use your first item:")
    first_item = belt.pop(0)
    if first_item in good_loot_options:
        # Increasing health points if the first item is good loot
        health_points = min(20, (health_points + 2))
        print("    |    You used " + first_item + " to up your health to " + str(health_points))
    elif first_item in bad_loot_options:
        # Decreasing health points if the first item is bad loot
        health_points = max(0, (health_points - 2))
        print("    |    You used " + first_item + " to hurt your health to " + str(health_points))
    else:
        # Informing the player if the first item is not helpful
        print("    |    You used " + first_item + " but it's not helpful")
    return belt, health_points

# Defining the function to collect loot (Lab 4: Question 3)
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
    print(ascii_image3)
    # Rolling for loot selection
    loot_roll = random.choice(range(1, len(loot_options) + 1))
    # Popping the selected loot item from the options
    loot = loot_options.pop(loot_roll - 1)
    # Adding the selected loot item to the belt
    belt.append(loot)
    print("    |    Your belt: ", belt)
    return loot_options, belt

# Defining the hero's attack function
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
    print(ascii_image)
    print("    |    Player's weapon (" + str(combat_strength) + ") ---> Monster (" + str(m_health_points) + ")")
    if combat_strength >= m_health_points:
        # Informing that the player was strong enough to kill the monster in one blow
        m_health_points = 0
        print("    |    You have killed the monster")
    else:
        # Informing that the player only damaged the monster
        m_health_points -= combat_strength
        print("    |    You have reduced the monster's health to: " + str(m_health_points))
    return m_health_points

# Defining the monster's attack function
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
    print(ascii_image2)
    print("    |    Monster's Claw (" + str(m_combat_strength) + ") ---> Player (" + str(health_points) + ")")
    if m_combat_strength >= health_points:
        # Informing that the monster was strong enough to kill the player in one blow
        health_points = 0
        print("    |    Player is dead")
    else:
        # Informing that the monster only damaged the player
        health_points -= m_combat_strength
        print("    |    The monster has reduced Player's health to: " + str(health_points))
    return health_points

# Defining the recursion function for inception dream (Lab 5: Question 7)
# You can choose to go crazy, but it will reduce your health points by 5
def inception_dream(num_dream_lvls):
    num_dream_lvls = int(num_dream_lvls)
    # Base Case: Checking if the player is in the deepest dream level
    if num_dream_lvls == 1:
        print("    |    You are in the deepest dream level now")
        print("    |", end="    ")
        input("Start to go back to real life? (Press Enter)")
        print("    |    You start to regress back through your dreams to real life.")
        return 2

    # Recursive Case: Reducing the dream levels and calling the function recursively
    else:
        return 1 + int(inception_dream(num_dream_lvls - 1))
