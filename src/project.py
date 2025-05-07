import time

def main():
    # to test the code more efficeintly
    while True:
        test_input = input("Find a spot?\n")
        if test_input == "Front":
            front_desk()
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
        text = "Eveything seems to trace back to one secluded town..."
        anim_print(text)
        input("")
        text = "Day 1: Checking In"
        anim_print(text)
        input("")
        text = "It's been a long day of traveling and you find a small hotel to stay in. \nSo far, the town is pretty unassuming other than the occasional glares cast your way.\n\nThe front desk clerk greets you: 'How may I be of service?'"
        anim_print(text)
        input("")
        front_desk()


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
            "He replies:\nThere's a room for one open. It'll cost you 10 gold per night"
            anim_print(text)
            break
        else:
            print("Invalid input. Please try again")


if __name__ == "__main__":
    main()