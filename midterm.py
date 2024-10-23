# CSIT 104: Python Programming I
# Project Title: The Mysterious Cave Adventure
# Author: [Nicole Molina]
# Summary: A text-based adventure game where the player navigates a cave through choices, leading to multiple endings.

def start_game():
    print("You wake up to find yourself in a cold, dark cave.")
    print("The air is damp, and the faint echo of dripping water fills your ears.")
    print("You have no memory of how you got here.")
    print("As you get up and dust yourself off, you notice two paths ahead:\n")
    print("1. To your left, a narrow tunnel leads deeper into darkness.")
    print("2. To your right, a wider passage seems to have some light coming from it.")

    choice = input("Do you go left or right? (Type 'left' or 'right'): ").strip().lower()

    if choice == 'left':
        narrow_tunnel()
    elif choice == 'right':
        wide_passage()
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
        start_game()  

def narrow_tunnel():
    print("\nYou bravely step into the narrow tunnel.")
    print("The cold air sends shivers down your spine, and you can hear the water rushing closer.")
    
    choice = input("Do you follow the sound of water or turn back? (Type 'follow' or 'turn back'): ").strip().lower()
    
    if choice == 'follow':
        water_end()
    elif choice == 'turn back':
        start_game()
    else:
        print("Invalid choice. Please type 'follow' or 'turn back'.")
        narrow_tunnel()  

def wide_passage():
    print("\nYou walk towards the wider passage, drawn by the light and whispers.")
    print("As you move closer, the whispers become clearer, sounding almost human.")

    choice = input("Do you approach the source of the light or retreat? (Type 'approach' or 'retreat'): ").strip().lower()
    
    if choice == 'approach':
        whisper_end()
    elif choice == 'retreat':
        start_game()
    else:
        print("Invalid choice. Please type 'approach' or 'retreat'.")
        wide_passage()  

def water_end():
    print("\nYou follow the sound of rushing water and find a beautiful underground river.")
    print("You decide to take a swim and feel rejuvenated. However, you are swept away by the current.")
    print("Ending: You become one with the river, never to be seen again.")

def whisper_end():
    print("\nAs you approach the light, you find a group of friendly cave dwellers.")
    print("They welcome you and offer to guide you out of the cave.")
    print("Ending: You leave the cave safely and make new friends.")

def main():
    while True:
        start_game()
        play_again = input("\nDo you want to play again? (yes or no): ").strip().lower()
        if play_again != 'yes':
            print("Thank you for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
