import pygame
import time
import sys

user_input = ""

def main():
    pygame.init()
    pygame.display.set_caption("Curiosity Killed the Cat")
    resolution = (800, 600)
    fullscreen_resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution)
    running = True
    color = (0,0,0)
    font = pygame.font.Font(None, 24)
    text = font.render("Curiosity Killed the Cat", True, (255,0,0))
    text2 = font.render("Press ENTER to Start", True, (255,0,0))
    gameStart = False
    keyPress = 0
    # to cycle through text
    day_stages = ["You're in a bustling tavern. You take up a spot in the corner.->",
                  "You overhear that your fellow monster hunters have been going missing. ->",
                  "You've decided to investigate the cause. ->",
                  "Eveything seems to trace back to one secluded town... ->"]
    current_stage = 0
    days = 0
    # delays to make text readable
    last_key_time = 0
    key_delay = 400
    # to keep start text from contantly renewing
    
    while running:
        # Event Loops
        for event in pygame.event.get():
            Choices(keyPress, event, screen)
            if event.type == pygame.QUIT:
                running = False
       
        key = pygame.key.get_pressed()
        # Make fullscreen
        if key[pygame.K_f]:
            screen = pygame.display.set_mode(fullscreen_resolution)
            pygame.display.toggle_fullscreen()
            pygame.display.update()
        # Untoggle fullscreen
        if key[pygame.K_r]:
            pygame.display.toggle_fullscreen()
            screen = pygame.display.set_mode(resolution)
            pygame.display.update()
        screen.fill(color)
        # Adds text to display
        screen_width, screen_height = screen.get_size()
        if not gameStart:
            text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
            screen.blit(text, text_rect)
            text_rect = text.get_rect(center=(screen_width // 2 + 10, screen_height // 2 + 50))
            screen.blit(text2, text_rect)


        if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:  
            gameStart = True      

            
        elif gameStart:
            # Makes sure text is centered 
            screen.fill(color)
            screen_width, screen_height = screen.get_size()
            current_time = pygame.time.get_ticks()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and current_time - last_key_time > key_delay:
                    keyPress += 1
                    print(keyPress)
                    if current_stage < len(day_stages)-1:
                        current_stage += 1 
                        last_key_time = current_time
                    # transition to new day
                    elif days == 0:
                        screen.fill(color)
                        days = 1
                        day_stages= ["Day 1: Checking In ->",
                                        "You only have enough money to stay 5 days. ->",
                                        "It's been a long day of traveling and you find a small hotel to stay in. ->",
                                        "So far, the town is pretty unassuming other than the occasional glares cast your way. ->",
                                        "The front desk clerk greets you:'How may I be of service?' ->"]
                        current_stage = 0
                        last_key_time = current_time
                    elif days == 1:
                        screen.fill(color)
                        days = 2
                        day_stages= ["Adventure more",
                                        "Day 2 in town",
                                        "mmm yes",
                                        "<- To investigate the herbalist."]
                        current_stage = 0
                        last_key_time = current_time
                        if days == 1:
                            Choices(keyPress, event, screen)
                    elif days == 2:
                        screen.fill(color)
                        days = 2
                        day_stages= ["Day: 3",
                                        "hi"]
                        current_stage = 0
                        last_key_time = current_time
                            

            if 0 <= current_stage < len(day_stages):
                text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 250)) 
                text = font.render(day_stages[current_stage], True, (255,0,0))
                screen.blit(text, text_rect)
                        

        pygame.display.flip()
def Choices(keyPress, event, screen):
    if keyPress > 8:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Witch(event, screen)
def Witch(event, screen):
    font = pygame.font.Font(None, 24)
    running = True
    text = font.render("", True, (255,0,0))
    current_stage = 0
    screen_width, screen_height = screen.get_size()
    color = (0,0,0)
    shop_stages= ["Witch",
                    "spell",
                    "potion",
                    "book"]
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            screen.fill(color)
            text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 250)) 
            text = font.render(shop_stages[current_stage], True, (255,0,0))
            screen.blit(text, text_rect)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    if current_stage < len(shop_stages) - 1:
                        screen.fill(color)
                        current_stage += 1

                        screen.fill(color)
                        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 250)) 
                        text = font.render(shop_stages[current_stage], True, (255,0,0))
                        screen.blit(text, text_rect)
            
            pygame.display.flip()

if __name__ == "__main__":
    main()