import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Curiosity Killed the Cat")
    resolution = (800, 600)
    fullscreen_resolution = (1920, 1080)
    screen = pygame.display.set_mode(resolution)
    running = True
    color = (0,0,0)
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
        pygame.display.flip()

if __name__ == "__main__":
    main()