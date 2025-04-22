import pygame
import time

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
    # to cyclt through text
    day_stages = ["You're in a bustling tavern. You take up a spot in the corner.->",
                  "You overhear that your fellow monster hunters have been going missing. ->",
                  "You've decided to investigate the cause. ->",
                  "Eveything seems to trace back to one secluded town... ->"]
    current_stage = 0
    days = 0
    # delays to make text readable
    last_key_time = 0
    key_delay = 500
    
    while running:
        # Event Loops
        for event in pygame.event.get():
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
        text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
        screen.blit(text, text_rect)
        text_rect = text.get_rect(center=(screen_width // 2 + 10, screen_height // 2 + 50))
        screen.blit(text2, text_rect)
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:  
                    gameStart = True      

            
        if gameStart:
            # Makes sure text is centered 
            screen.fill(color)
            screen_width, screen_height = screen.get_size()
            current_time = pygame.time.get_ticks()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT and current_time - last_key_time > key_delay:
                    if current_stage < len(day_stages)-1:
                        current_stage += 1 
                        last_key_time = current_time
                    else:
                            current_stage = 0

            text = font.render(day_stages[current_stage], True, (255,0,0))
            text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 150)) 
            screen.blit(text, text_rect)

                        

        pygame.display.flip()

        
if __name__ == "__main__":
    main()