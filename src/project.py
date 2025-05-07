import time

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
        text = "It's been a long day of traveling and you find a small hotel to stay in. \nSo far, the town is pretty unassuming other than the occasional glare cast your way.\n\nThe front desk clerk greets you: 'How may I be of service?'"
        anim_print(text)
        input("")
        front_desk()
        text = "Pulling out your gold pouch you find you only have enough to stay 4 more days.\nYou hand over the full amount to the desk clerk and he hands you a rusted copper key to a room on the second floor." \
        "There is a small window at the end of the hall on the second floor. The moon shines brightly. It'll probably be full tomorrow.\n" \
        "You set your bag down and lay down. As the night goes on, you hear noises from outside."
        input("")
        night()
        text = "Day 2: Investigation"
        anim_print(text)
        input("")
        text = "Feeling well rested, you're ready to start your search.\n" \
        "Coming into town you noticed three main suspects: The Apothecary, The Lumberjack, and The Night Guard."
        anim_print(text)
        input("")
        choices_fullmoon()


def anim_print(text):
    """Works like print, but animates the display of each character
    
    :param text: Text to print
    "type text: str
    """
    for charcter in text:
        print(charcter, end="", flush=True)
        time.sleep(0.03)
    print()
def front_desk():
    # creates a loop so if there is an invalid imput it asks again
    prompt_msg = ("How do you reply?")
    anim_print(prompt_msg)
    while True:
        choice = input(("1. I need a room for a few nights.\n"
        "2. I've heard there's a monster in this town\n"))

        if choice == "1":
            text = "\nThe desk clerk's wrinkled hands sift through a large, worn ledger. Sunken eyes scan the ink filled, yellowed pages.\nHis bony finger stops " \
            "on an empty line. He grabs a feather pen from an ink well. Hand hovering over the page, he replies:\nThere's a room for one open. It'll cost you 10 gold per night."
            anim_print(text)
            break
        elif choice == "2":
            text = "\nAll of a sudden, the atmosphere feels more tense. The desk clerk's bony finger traces over rows in a worn ledger. \nIt stops on a blank line and the clerk looks up at you with his sunken eyes."\
            "He replies:\nThere's a room for one open. It'll cost you 15 gold per night"
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
            text = "\nYou fling open the curtains, letting moonlight come pouring in. As you turn to go back to bed, a blur catches your eye. A bat perhaps?\n" \
            "Taking a closer look out of the window, you can't find the bat. However, you do spot a night guard on patrol.\n" \
            "You go back to sleep after a few minutes."
            anim_print(text)
            break
        elif choice == "2":
            text = "\nYou light a candle and open the door. Sticking your head out into the hallway you hear a scurrying noise somewhere further down.\n" \
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
            text = "\nwitch"
            anim_print(text)
            break
        elif choice == "2":
            text = "\nwerewolf"
            anim_print(text)
            break
        elif choice == "3":
            text = "\nvampire"
            anim_print(text)
            break
        else:
            print("Invalid input. Please try again")

if __name__ == "__main__":
    main()