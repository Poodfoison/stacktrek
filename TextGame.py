print("L O S T\n\n")

name = input("What is your name? ")

health = 10

play = input("Do you want to play? ").lower()
if (play == "yes") or (play == "y"):
    print(f"\nYou are staring with {health} health.")
    print(f"Let's play!\n")
    print(f"You are lost in the woods which direction would you want to go Left or Right (left/right)? ")
    choice = input()
    if choice == "left":
        print(f"\nNow you follow a path and reach to a lake... Do you swim across or go around (across/around)? ")
        answer = input()

        if answer == "around":
            print("\nYou went around and reached the other side of the lake.")

        elif answer == "across":
            print("\nYou managed to swim across, but were bitten my a swarm of piranha but managed to escape.")
            print("You lose 5 health.")
            health -= 5

        print(f"\nYou notice a house and a river. Which do you go to (river/house)? ")
        answer = input()

        if answer == "house":
            print(f"\nYou go to the house and are greeted by the owner... He is angry and doesn't like you then he hits you with a stick.")
            print(f"You lose 5 health.")
            health -= 5
            if health <= 0:
                print(f"\nYou now have 0 health and you lost the game...")
                print(f"\nGame Over!")

            else:
                print(f"\nYou have survived... You win!")

        else:
            print(f"\nYou fell in the river and drowned...")
            print(f"\nGame Over!")

    else:
        print(f"\nYou enter a cave and get eaten by a bear...")
        print(f"\nGame Over!")
else:
    print(f"\nExiting...")
    print()