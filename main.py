import pygame
import random
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

# randomly populates the grid with cells


def gen(num):
    return set([(random.randrange(0, GRID_WIDTH), random.randrange(0, GRID_HEIGHT)) for _ in range(num)])

# adjust the grid


def adjust_grid(positions):
    all_neighbors = set()
    new_positions = set()
    # delete or keep the cell alive
    for position in positions:
        neighbors = get_neighbors(position)
        all_neighbors.update(neighbors)
        neighbors = list(filter(lambda x: x in positions, neighbors))

        if len(neighbors) in [2, 3]:
            new_positions.add(position)
    # add new cells
    for position in all_neighbors:
        neighbors = get_neighbors(position)
        neighbors = list(filter(lambda x: x in positions, neighbors))
        if len(neighbors) == 3:
            new_positions.add(position)
    return new_positions

# get the neiboors of a cell


def get_neighbors(position):
    x, y = position
    neighbors = []
    for dx in [-1, 0, 1]:
        # check if the cell is on the screen or not
        if x+dx < 0 or x+dx >= GRID_WIDTH:
            continue
        if y+dy < 0 or y+dy >= GRID_HEIGHT:
            continue

        for dy in [-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue  # skip it's own position
            neighbors.append((x+dx, y+dy))
    return neighbors


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
    playing = False
    count = 0
    update_freq = 120

    positions = set()  # empty set

    while running:
        clock.tick(FPS)
        if playing:
            count += 1
        if count % update_freq == 0:
            positions = adjust_grid(positions)
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
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # pause/unpause
                    playing = not playing
                # clear the screen if user presses c
                if event.key == pygame.K_c:
                    positions.clear()
                    playing = False
                    count = 0
                # generates a new game if users presses g
                if event.key == pygame.K_g:
                    positions = gen(random.randrange(2, 5) * GRID_WIDTH)
                    playing = False

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
