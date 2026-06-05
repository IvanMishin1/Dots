from draw import *
from logic import *
from dataclasses import dataclass

pygame.init()

class GameData:
    def __init__(self):
        # Game config
        self.blueTurn = True
        self.screen_size = 512
        self.grid_size = 20
        self.padding = 70

        # Derived values
        self.step = (self.screen_size - 2 * self.padding) / self.grid_size

        # Colors / UI
        self.color_blue = (0, 0, 255)
        self.color_red = (255, 0, 0)

        # Game state
        self.score = {'B': 0, 'R': 0}
        self.grid = [[' ' for _ in range(self.grid_size + 1)] for _ in range(self.grid_size + 1)]
        self.captured = []
        self.last_move = None

        self.screen = pygame.display.set_mode((self.screen_size, self.screen_size))
        self.font = pygame.font.Font(pygame.font.get_default_font(), 40)

gd = GameData()
pygame.display.set_caption("Dots")
clock = pygame.time.Clock()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            gx = round((pos[0]- gd.padding) / gd.step)
            gy = round((pos[1]- gd.padding) / gd.step)

            if gx in range(0,gd.grid_size + 1) and gy in range(0,gd.grid_size + 1) and not gd.grid[gy][gx] != " ":
                new_point(gx,gy, gd)
                if gd.blueTurn:
                    check_borders("B","R", gd)
                    check_borders("R","B", gd)
                    gd.last_move = (gx,gy,gd.color_blue)
                else:
                    check_borders("R","B", gd)
                    check_borders("B","R", gd)
                    gd.last_move = (gx,gy,gd.color_red)
                gd.blueTurn = not gd.blueTurn
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                gd = GameData()

    gd.screen.fill("white")
    draw_grid(gd)
    draw_points(gd)
    draw_captured(gd)
    draw_score(gd)
    draw_last_move(gd)

    pygame.display.flip()
    clock.tick(60)
