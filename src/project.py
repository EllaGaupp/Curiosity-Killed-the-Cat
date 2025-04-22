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
            text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2 + 150)) 
            # Instructions to player
            text = font.render("Game started", True, (255,0,0))
            screen.blit(text, text_rect)

        pygame.display.flip()

        
if __name__ == "__main__":
    main()