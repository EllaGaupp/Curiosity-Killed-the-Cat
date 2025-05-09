import time
import sys
import random

filename = 'bag.csv'
witch_visit = False
werewolf_visit = False
vampire_visit = False

def main():
    global witch_visit, werewolf_visit, vampire_visit
    # to test the code more efficeintly
    while True:
        print("\n\nCuriosity Killed the Cat") 
        # to make each line appear one by one
        input()
        with open('tavern.txt', 'r') as art:
            text = art.read().replace('\r\n', '\n').replace('\t', '    ')
            print(text) 
        text = "\nYou're in a bustling tavern. You take up a spot in the corner."
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
        with open('clerk.txt', 'r') as art:
            text = art.read().replace('\r\n', '\n').replace('\t', '    ')
            print(text)
        input("")
        front_desk()
        input("")
        text = "Pulling out your gold pouch you find you only have enough to stay 4 more days.\nYou hand over the full amount to the desk clerk and he gives you a rusted copper key to a room on the second floor." 
        anim_print(text)
        input("")
        with open('hallway.txt', 'r') as art:
            text = art.read().replace('\r\n', '\n').replace('\t', '    ')
            print(text) 
        text = "\nThere is a small window at the end of the hall on the second floor. The moon shines brightly. It'll probably be full tomorrow.\n" \
        "You set your bag down and lay down. As the night goes on, you hear noises from outside.\n"
        anim_print(text)
        input("")
        night()
        text = "\nDay 2: Investigation"
        anim_print(text)
        input("")
        text = "Feeling well rested, you're ready to start your search.\n" \
        "Coming into town you noticed three main suspects: The Apothecary, The Lumberjack, and The Night Guard."
        anim_print(text)
        input("")
        witch_visit, werewolf_visit, vampire_visit = choices_fullmoon(
        witch_visit, werewolf_visit, vampire_visit)
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

        text = "\nYou sleep.\n"
        anim_print(text)
        text = "\nDay 3: Investigation"
        anim_print(text)
        input("")
        text = "You awaken ready to continue your search."
        anim_print(text)
        input("")
        witch_visit, werewolf_visit, vampire_visit = choices(
        witch_visit, werewolf_visit, vampire_visit)
        prompt_msg = ("Check your bag?\n")
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
        text = "You've gathered good information. Time to sleep."
        text = "\nDay 4: Investigation"
        anim_print(text)
        input("")
        text = "This is your final day to investigate."
        anim_print(text)
        input("")
        witch_visit, werewolf_visit, vampire_visit = choices(
        witch_visit, werewolf_visit, vampire_visit)
        prompt_msg = ("Check your bag?\n")
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
        text = "With lots to think about, you sleep."
        anim_print(text)
        text = "You've throughly investigated all your suspects."
        anim_print(text)
        prompt_msg = "What would you like to do?\n"
        anim_print(prompt_msg)
        choice = input("1. Choose someone to accuse and eliminate.\n" \
        "2. Leave\n\n")

        if choice == "1":
            final_choice()
        elif choice == "2":
            text = "You leave alive yippie"
            anim_print(text)
        else:
            print("Invalid input. Please try again")
        break

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
            new_item = "Silver Bullet Casing"
            new_use = "perhaps a previous hunter's?"
            add_item(filename, new_item, new_use)
            anim_print(text)
            break
        elif choice == "3":
            break
        else:
            print("Invalid input. Please try again")

def choices_fullmoon(witch_visit, werewolf_visit, vampire_visit):
    prompt_msg = ("Who do you want to investigate today?")
    anim_print(prompt_msg)
    while True:
        choice = input(("1. The Apothecary.\n"
        "2. The Lumberjack\n"
        "3. The Night Guard.\n\n"))

        if choice == "1" and not witch_visit:
            witch_visit = True
            witch()
            break
        elif choice == "2" and not werewolf_visit:
            werewolf_visit = True
            werewolf_full()
            break
        elif choice == "3" and not vampire_visit:
            vampire_visit = True
            vampire()
            break
        else:
            print("Invalid input. Please try again")
    return witch_visit, werewolf_visit, vampire_visit

def choices(witch_visit, werewolf_visit, vampire_visit):
    prompt_msg = ("Who do you want to investigate today?")
    anim_print(prompt_msg)
    while True:
        choice = input(("1. The Apothecary.\n"
        "2. The Lumberjack\n"
        "3. The Night Guard.\n\n"))

        if choice == "1" and witch_visit == False:
            witch()
            witch_visit = True
            break
        elif choice == "2" and werewolf_visit == False:
            werewolf()
            werewolf_visit = True
            break
        elif choice == "3" and vampire_visit == False:
            vampire()
            vampire_visit = True
            break
        elif choice == "1" or "2" or "3":
            visited()
        else:
            print("Invalid input. Please try again")
    return witch_visit, werewolf_visit, vampire_visit

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
            text = "\n*ding*"
            anim_print(text)
            if question_witch():
                break
        elif choice == "2":
            text = "\nYou're to recognize rosemary, basil, mint, and lavender.\n" \
            "However, there are some plants of strange colors tucked away that you can't identify."
            anim_print(text)
        elif choice == "3":
            text = "\nPeering into the nearest jars you see various eyes and limbs.\n" \
            "The closest three jars are labeled as 'Eyes of Toads', 'Legs of Frogs', and 'Tails of Lizards'"
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
            text = "\nJust some medicinal recipes passed down through my family.\n" \
            "If you're sick you tell me your symptoms, I can find a cure for you in here."
            anim_print(text) 
        elif choice == "2":
            text = "\nMostly medicines that I make. However, I'll sell ingredients too.\n" \
            "To outsiders our healing methods may seem a little odd, but eyes of toads work wonders."
            anim_print(text)
        elif choice == "3":
            text = "\nMonsters? In this town? The most monstrous thing I've seen all year\n" \
            "is a wave of bad colds that came through a while back."
            anim_print(text)
        elif choice == "4":
            text = "\nThe Apothecary nods, closes her book, and spins on her heel to return to the back of the shop.\n" \
            "In her haste, a loose page flew out of the book and lands in front of you.\n" \
            "You pick it up to look at later."
            anim_print(text)
            new_item = "Mysterious Page"
            new_use = "it looks more like a spell than recipe"
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
            werewolf_battle()
        elif choice == "3":
            text = "\ncoward"
            return True
        else:
            print("Invalid input. Please try again")

def werewolf():
    prompt_msg = ("\nYou find the lumberjack by the edge of town. He looks like he's about to head out.\n"
    "He turns to you, axe in hand and asks: 'What're you doin' out here?'\n")
    anim_print(prompt_msg)
    while True:
        choice = input(("How do you respond?\n"
        "1. I'd like to ask you some questions.\n"
        "2. May I join you?\n"
        "3. Nothing much. You?\n\n"))

        if choice == "1" or "2" or "3":
            if question_werewolf():
                break
        else:
            print("Invalid input. Please try again")

def question_werewolf():
    prompt_msg = ("He doesn't reply. Instead, he turns towards the forrest and motions for you to follow.\n")
    anim_print(prompt_msg)
    while True:
        choice = input(("Do you go with him?\n"
        "1. yes\n"
        "2. no\n\n"))

        if choice == "1":
            text = "You ultimately decide to go with him. Following a winding path, you reach a clearing. " \
            "\nThere the Lumberjack takes his axe and starts swinging at a nearby tree. He fells it's very quickly...almost too quickly.\n" \
            "He appears to be in deep concentration with his job. You won't get much questioning done today, but you still stay to observe.\n" \
            "You note tufts of fur clinging to his jacket. As the sun sets, you start to hear the howls of wolves, yet he seems unbothered."
            anim_print(text)
            text = "\nEventually, he starts to head back, only acknowledging your existence when he looks back to make sure you follow.\n" \
            "Upon reaching town, he simply walks off towards his house. It seems he's just wasted your time.\n\n" \
            "Or has he? You bend down and pick up a tuft of fur that had fallen from him and put it in your bag."
            anim_print(text)
            new_item = "Tuft of Fur"
            new_use = "looks like wolf fur"
            add_item(filename, new_item, new_use)
            return True
        elif choice == "2":
            return True
        else:
            print("Invalid input. Please try again")

def vampire():
    while True:
        prompt_msg = ("\nYou wait until evening. From the shadows appears the Night Guard. He has a long cloak and pale face.\n"
        "As you intercpt his path, you notice the glint of a glass in his hand. It's filled with a red liquid. Wine?\n"
        "He stops infront of you, taking a sip from his glass.\n"
        "He demands: 'State your buiness. What you doing out so late?'")
        anim_print(prompt_msg)
        choice = input("How do you respond?\n"
        "1. I'd like to ask you a few questions.\n"
        "2. None of your buisness.\n"
        "3. Why do you have a drink and what is it?\n\n")
        if choice == "1":
            text = "The Night Guard replies coldly: 'I could say the samne.'"
            anim_print(text)
            if question_vampire():
                break
        elif choice == "2":
            text = "The Night Guard replies coldly: 'As the guard of this town, it is my buisness.'"
            anim_print(text)
            if question_vampire():
                break
        elif choice == "3":
            text = "The Night Guard replies coldly: 'What I do and drink is none of your concern.'"
            anim_print(text)
            if question_vampire():
                break
        else:
            print("Invalid input. Please try again")

def question_vampire():
    while True:
        text = "\nHe then sighs and swirls his glass. \n" \
        "He asks: 'I suppose you're here to ask me about a monster. I'll tell you right now you're not the first to ask.\n" \
        "I'd suggest you just drop the matter. Trust me, if there was a monster here, I'd know.\n" \
        "Everyone knows everyone. How do we know you're not the monster?'\n" 
        anim_print(text)
        input("")
        text = "After taking a large drink from his cup, the Night Guard sets the now empty glass on a near by table.\n" \
        "He turns to continue his patrol: 'Take it. I have nothing to hide from you.'"
        anim_print(text)
        new_item = "Empty Glass"
        new_use = "Used to hold mysterious red liquid"
        add_item(filename, new_item, new_use)
        return True

def final_choice():
    print("choose")

def werewolf_battle():
    player_hp = 50
    monster_hp = 60
    text = "You find the lumberjack in the woods."
    anim_print(text)
    while True:
        print(f"\n{player_hp} player hp")
        print(f"\n{monster_hp} monster hp\n")
        if player_hp != 0 and monster_hp !=0:
            random_number = random.randint(1,10)
            if random_number == 10:
                print(f"{random_number} player accuracy")
                print("player miss")
                input("")
            else:
                print(f"{random_number} player accuracy")
                print("player hit")
                monster_hp += -10  
                input("")
            random_number = random.randint(1,10)
            if random_number == 9 or random_number == 10:
                print(f"{random_number} monster accuracy")
                print("monster miss")
                input("")
            else:
                print(f"{random_number} monster accuracy")
                print("monster hit")
                player_hp += -10 
                input("")
        elif player_hp == 0:
            print("Monster Wins")
            break
        elif monster_hp == 0:
            print("Player Wins")
            break
        else:
            print("tie")
            break

def werewolf_lose():
    print("ya lost")

#  technical stuff
def visited():
    text = "You've already investigated them. Choose again."
    anim_print(text)
def anim_print(text):
    """Works like print, but animates the display of each character
    
    :param text: Text to print
    "type text: str
    """
    for charcter in text:
        print(charcter, end="", flush=True)
        time.sleep(0.04)
    print()
def add_item(filename, new_item, new_use):
    content = [f"{new_item},{new_use}\n"]
    with open(filename, 'a') as file:
        file.writelines(content)
def display_inventory(filename):
    with open(filename) as file:
            for line in file:
                item, use = line.rstrip().split(',')
                print(f"{item} - {use}")

if __name__ == "__main__":
    main()