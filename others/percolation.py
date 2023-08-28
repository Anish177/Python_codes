# %%
import pygame
import pygame_gui
import random

# %%
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
PERCOLATION_PROBABILITY = 0.6
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Create the grid with randomly activated cells
grid = [[random.random() < PERCOLATION_PROBABILITY for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Percolation Simulation")

# Initialize pygame_gui
ui_manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Create a slider to control percolation probability
slider_rect = pygame.Rect(10, HEIGHT - 40, WIDTH - 20, 30)
slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider_rect, start_value=PERCOLATION_PROBABILITY,
                                                value_range=(0.1, 1.0), manager=ui_manager, click_increment=0.05)

# Main loop
clock = pygame.time.Clock()
running = True
while running:
    time_delta = clock.tick(60) / 1000.0  # Calculate time delta in seconds

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                # Update the percolation probability based on the slider value
                PERCOLATION_PROBABILITY = event.value
                grid = [[random.random() < PERCOLATION_PROBABILITY for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

        ui_manager.process_events(event)

    ui_manager.update(time_delta)

    # Clear the screen
    screen.fill(WHITE)

    # Draw the grid
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            color = BLACK if grid[row][col] else WHITE
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    ui_manager.draw_ui(screen)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
# %%
