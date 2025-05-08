import time

filename = 'bag.csv'
def main():
    # to test the code more efficeintly
    while True:
        test_input = input("Find a spot?\n")
        if test_input == "Front":
            front_desk()
            break
        elif test_input == "Night":
            night()
            break
        elif test_input == "Moon":
            choices_fullmoon()
            break
        elif test_input == "Witch":
            witch()


        print("\n\nCuriosity Killed the Cat") 
        # to make each line appear one by one
        input("")
        text = "You're in a bustling tavern. You take up a spot in the corner."
        anim_print(text)
        input("")
        text = "You overhear that your fellow monster hunters have been going missing."
        anim_print(text)
        input("")
        text = "You've decided to investigate the cause."
        anim_print(text)
        input("")
        text = "After asking around, eveything seems to trace back to one secluded town..."
        anim_print(text)
        input("")
        text = "Day 1: Checking In"
        anim_print(text)
        input("")
        text = "It's been a long day of traveling and you find a small inn to stay in. \nSo far, the town is pretty unassuming other than the occasional glare cast your way.\n\nThe front desk clerk greets you: 'What d'ya need?'"
        anim_print(text)
        input("")
        front_desk()
        input("")
        text = "Pulling out your gold pouch you find you only have enough to stay 4 more days.\nYou hand over the full amount to the desk clerk and he gives you a rusted copper key to a room on the second floor." \
        "\nThere is a small window at the end of the hall on the second floor. The moon shines brightly. It'll probably be full tomorrow.\n" \
        "You set your bag down and lay down. As the night goes on, you hear noises from outside.\n"
        anim_print(text)
        night()
        text = "\nDay 2: Investigation"
        anim_print(text)
        input("")
        text = "Feeling well rested, you're ready to start your search.\n" \
        "Coming into town you noticed three main suspects: The Apothecary, The Lumberjack, and The Night Guard."
        anim_print(text)
        input("")
        choices_fullmoon()
        text = "That was a busy day. It's gotten late. Best head back to the inn."
        anim_print(text)
        prompt_msg = (" Once you get back to the room you can check your bag.\n")
        anim_print(prompt_msg)
        choice = input("\n1. To check your bag\n"
        "2. Skip\n\n")
        if choice == "1":
            display_inventory(filename)
        elif choice == "2":
            print("")
            text = "You decided not to check your bag tonight."
        else:
            print("Invalid input. Please try again")

        text = "\nYou sleep\n"
        anim_print(text)
        text = "\nDay 3: Investigation"
        anim_print(text)
        input("")
        text = "You awaken ready to continue your search."
        anim_print(text)
        input("")
        choices()
        break
def display_inventory(filename):
    with open(filename) as file:
            for line in file:
                item, use = line.rstrip().split(',')
                print(f"{item} - {use}")

def anim_print(text):
    """Works like print, but animates the display of each character
    
    :param text: Text to print
    "type text: str
    """
    for charcter in text:
        print(charcter, end="", flush=True)
        time.sleep(0.00)
    print()
def front_desk():
    # creates a loop so if there is an invalid imput it asks again
    prompt_msg = ("How do you reply?")
    anim_print(prompt_msg)
    while True:
        choice = input(("1. I need a room for a few nights.\n"
        "2. I've heard there's a monster in this town\n\n"))

        if choice == "1":
            text = "\nThe desk clerk's wrinkled hands sift through a large, worn ledger. Sunken eyes scan the ink filled, yellowed pages.\nHis bony finger stops " \
            "on an empty line. He grabs a feather pen from an ink well. Hand hovering over the page, he replies:\n'There's a room for one open. It'll cost you 10 gold per night.'"
            anim_print(text)
            break
        elif choice == "2":
            text = "\nAll of a sudden, the atmosphere feels more tense. The desk clerk's bony finger traces over rows in a worn ledger. \nIt stops on a blank line and the clerk looks up at you with his sunken eyes."\
            "\nHe replies: 'There's a room for one open. It'll cost you 15 gold per night'"
            anim_print(text)
            break
        else:
            print("Invalid input. Please try again")
def night():
    prompt_msg = ("What do you do?")
    anim_print(prompt_msg)
    while True:
        choice = input(("1. Get up and look out the window.\n"
        "2. Get up and check the hallway\n"
        "3. Go back to sleep.\n\n"))

        if choice == "1":
            text = "\nYou fling open the curtains, letting moonlight pour in. As you turn to go back to bed, a blur catches your eye. A bat perhaps?\n" \
            "Taking a closer look out of the window, you can't find the bat. However, you do spot a night guard on patrol.\n" \
            "You go back to sleep after a few minutes."
            anim_print(text)
            break
        elif choice == "2":
            text = "\nYou light a candle and open the door. Sticking your head out into the hallway, you hear a scurrying noise somewhere further down.\n" \
            "As you approach, it vanishes. However, left behind is a silver bullet casing. Perhaps left over from a previous hunter?\n" \
            "You return to your room and sleep."
            anim_print(text)
            break
        elif choice == "3":
            break
        else:
            print("Invalid input. Please try again")
def choices_fullmoon():
    prompt_msg = ("Who do you want to investigate today?")
    anim_print(prompt_msg)
    while True:
        choice = input(("1. The Apothecary.\n"
        "2. The Lumberjack\n"
        "3. The Night Guard.\n\n"))

        if choice == "1":
            witch()
            break
        elif choice == "2":
            werewolf_full()
            break
        elif choice == "3":
            vampire()
            break
        else:
            print("Invalid input. Please try again")

def choices():
    prompt_msg = ("Who do you want to investigate today?")
    anim_print(prompt_msg)
    while True:
        choice = input(("1. The Apothecary.\n"
        "2. The Lumberjack\n"
        "3. The Night Guard.\n\n"))

        if choice == "1":
            witch()
            break
        elif choice == "2":
            werewolf()
            break
        elif choice == "3":
            vampire()
            break
        else:
            print("Invalid input. Please try again")
def witch():
    text = ("You enter the shop. It's filled with shelves of bottles and jars. Various plants hang from pots and the scent of strong spices lingers in the air.\n"
    "In the back of the shop is a small counter. Several smaller plants adorn it along with a sleeping black cat and copper bell.\n")
    anim_print(text)
    prompt_msg = ("What do you do?")
    anim_print(prompt_msg)
    while True:
        choice = input(("\n1. Ring the bell.\n"
        "2. Investigate the plants.\n"
        "3. Investigate the jars.\n\n"))
        if choice == "1":
            text = "\nbell"
            anim_print(text)
            if question_witch():
                break
        elif choice == "2":
            text = "\nplants"
            anim_print(text)
        elif choice == "3":
            text = "\njars"
            anim_print(text)
        else:
            print("Invalid input. Please try again")

def question_witch():
    text = ("\nThe cat awakens from its nap and leaps gracefully off the counter. It dissapears behind a doorway shielded by a curtain. \nMoments later the Apothecary emerges, large book in hand.\n"
    "She has long, dark, raven hair that's half tied up. Her dress flows around her, reminiscent of robes, but with shorter sleeves.\n"
    "She greets you: 'How may I help you?'\n")
    anim_print(text)
    input("")
    prompt_msg = ("How do you reply?")
    anim_print(prompt_msg)
    while True:
        choice = input(("\n1. What's the book?'.\n"
        "2. What do you sell?\n"
        "3. Do you know about any monsters in town?\n"
        "4. Thank her and leave.\n\n"))
        if choice == "1":
            text = "\nbook"
            anim_print(text) 
        elif choice == "2":
            text = "\nsell"
            anim_print(text)
        elif choice == "3":
            text = "\nmonsters"
            anim_print(text)
        elif choice == "4":
            text = "\nyou leave\n"
            anim_print(text)
            new_item = "Mysterious Page"
            new_use = "Spell OoOOoOO"
            add_item(filename, new_item, new_use)
            return True
        else:
            print("Invalid input. Please try again")

def werewolf_full():
    text = ("\nYou wake up and try to find the Lumberjack. After hours of searching you cant find him\n"
    "He doesn't seem to be here...odd.\n")
    anim_print(text)
    prompt_msg = ("What do you do?")
    anim_print(prompt_msg)
    while True:
        choice = input(("\n1. Ask Little Girl\n"
        "2. Ask Old Man\n"
        "3. Ask Young Couple\n"
        "4. Ready to Continue\n\n"))
        if choice == "1":
            text = "\ngirl"
            anim_print(text)
        elif choice == "2":
            text = "\nold guy"
            anim_print(text)
        elif choice == "3":
            text = "\ncouple"
            anim_print(text)
        elif choice == "4":
            if question_werewolf_full():
                break
        else:
            print("Invalid input. Please try again")
def question_werewolf_full():
    text = ("Night it starting to fall. You have some suspicions of the Lumberjack's whereabouts.\n")
    anim_print(text)
    prompt_msg = ("What do you do?")
    anim_print(prompt_msg)
    while True:
        choice = input(("\n1. Check the town again\n"
        "2. Check the forest\n"
        "3. Go back to the Inn\n\n"))
        if choice == "1":
            text = "\nnope"
            anim_print(text)
        elif choice == "2":
            text = "\nuh oh"
            anim_print(text)
        elif choice == "3":
            text = "\ncoward"
            return True
        else:
            print("Invalid input. Please try again")

def werewolf():
    print("yep")
def question_werewolf():
    print("yep")
def vampire():
    print("yep")
def question_vampire():
    print("yep")


def add_item(filename, new_item, new_use):
    content = [f"{new_item},{new_use}\n"]
    with open(filename, 'a') as file:
        file.writelines(content)

if __name__ == "__main__":
    main()