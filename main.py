import pygame
pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)
YELLOW = (255, 255, 0)

WIDTH, HEIGHT = 800, 800
TILE_SIZE = 20
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

# it will receive a set of positions (cells) and draw them


def draw_grid(positions):
    for position in positions:
        col, row = position
        pygame.draw.rect(
            screen,
            YELLOW,
            (col*TILE_SIZE, row*TILE_SIZE, TILE_SIZE, TILE_SIZE)
        )

    # draw horizontals
    for row in range(GRID_HEIGHT):
        pygame.draw.line(
            screen,
            BLACK,
            (0, row*TILE_SIZE),
            (WIDTH, row*TILE_SIZE)
        )
    # draw verticals
    for col in range(GRID_WIDTH):
        pygame.draw.line(
            screen,
            BLACK,
            (col*TILE_SIZE, 0),
            (col*TILE_SIZE, HEIGHT)
        )


def main():
    running = True

    # positions = set( (30,20)) won't work
    positions = set()
    positions.add((30, 20))

    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                col = x // TILE_SIZE
                row = y // TILE_SIZE
                if (col, row) in positions:
                    positions.remove((col, row))
                else:
                    positions.add((col, row))

        screen.fill(GREY)
        draw_grid(positions)
        pygame.display.update()

    print("Game ended by user.")
    print("Thank you for playing!")
    pygame.quit()


if __name__ == '__main__':
    # the usual boilerplate stuff
    # why do we always need this?
    # Python should have a more elegant way to do this
    main()
