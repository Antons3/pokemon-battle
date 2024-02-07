
print("")
print("                                  ,'\\")
print("    _.----.        ____         ,'  _\   ___    ___     ____")
print("_,-'       `.     |    |  /`.   \,-'    |   \  /   |   |    \  |`.")
print("\      __    \    '-.  | /   `.  ___    |    \/    |   '-.   \ |  |")
print(" \.    \ \   |  __  |  |/    ,','_  `.  |          | __  |    \|  |")
print("   \    \/   /,' _`.|      ,' / / / /   |          ,' _`.|     |  |")
print("    \     ,-'/  /   \    ,'   | \/ / ,`.|         /  /   \  |     |")
print("     \    \ |   \_/  |   `-.  \    `'  /|  |    ||   \_/  | |\    |")
print("      \    \ \      /       `-.`.___,-' |  |\  /| \      /  | |   |")
print("       \    \ `.__,'|  |`-._    `|      |__| \/ |  `.__,'|  | |   |")
print("        \_.-'       |__|    `-._ |              '-.|     '-.| |   |")
print("                                `'                            '-._|")
print("")
print("Pokemon Battle")
print("")

import json
import random

# read Pokemon file into dictionary
pokemons_file = open('pokemons.json') # opening JSON file
pokemons = json.load(pokemons_file) # returns JSON object as a dictionary
pokemons_file.close() # Closing file

print(pokemons[0])

while True:
    print("1. Show pokemon by index")
    print("2. Top 10 strongest pokemons")
    print("3. Top 10 weakest pokemons")
    print("4. Battle of 2 pokemons")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        # https://www.w3schools.com/python/python_dictionaries_access.asp
        number = int(input("Enter number: ")) - 1
        print(pokemons[number])
    elif choice == '2':
        # https://www.w3schools.com/python/python_lists_sort.asp
        sortedh = sorted(pokemons, key=lambda x: int(x["attack"]), reverse=True)
        print("Top 10 strongest: ", sortedh[:10])
    elif choice == '3':
        # https://www.w3schools.com/python/python_lists_sort.asp
        sortedh = sorted(pokemons, key=lambda x: int(x["attack"]))
        print("Top 10 weakest: ", sortedh[:10])
    elif choice == '4':
        # Battle
        # https://www.w3schools.com/python/ref_random_choice.asp - random choice
        # Computer choosing one random Pokemon from list
        # Player choosing by entering Pokemon index
        # Damage is calculated by: (attack of Pokemon 2) - (defense of Pokemon 1) + (random from 5 to 20), and vice-versa
        # Player reaching 0 health - lost
        number = int(input("Enter number: ")) - 1
        pok1 = pokemons[number]
        import random
        pok2 = random.choice(pokemons)
        print("Your Pokemon: " + pok1["name"])
        print("Your Pokemons hp: ", pok1["total"])
        print("Computer's pokemon: " + pok2["name"])
        print("Computer's pokemon hp: ", pok2["total"])
        print("Are you ready to fight?")
        hp1 = pok1["total"]
        hp2 = pok2["total"]
        ready = input("1 - Yes, 2 - No: ")
        if ready == '1':
            print("you attack first")
            import random
            random_number = random.randint(5, 20)
            
            damage1 = pok1["attack"] - pok2["defense"] + random_number
            if damage1 < 0:
                damage1 = 0
            print("Damage: ", damage1)
            hp2 = hp2 - damage1
            if hp2 > 0:
                print("Enemy hp: ", hp2)
                print("Enemy's attack...")
                import random
                random_number = random.randint(5, 20)
                damage2 = pok2["attack"] - pok1["defense"] + random_number
                if damage2 < 0:
                    damage2 = 0
                print("Damage: ", damage2)
                hp1 = hp1 - damage2
                if hp1 > 0:
                    print("Your Hp:", hp1)
                    pass
                elif hp1 < 0:
                    print("You loose!")
            else:
                print("You Win!")        
                


    elif choice == '5':
        print("Exiting")
        break
    else:
        print("Invalid choice, choose from 1 to 5")

    print("==========================")


