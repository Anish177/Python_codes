# %%
import sys
import random
import pygame
import pygame_gui
sys.setrecursionlimit(5000)

# %%
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
CELL_SIZE = 10
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE
PERCOLATION_PROBABILITY = 0.6
WHITE = (255, 255, 255)

# Create the grid with randomly activated cells
grid = [[random.random() < PERCOLATION_PROBABILITY for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

# Initialize Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Percolation Simulation")

# Initialize pygame_gui
ui_manager = pygame_gui.UIManager((WIDTH, HEIGHT))

# Create a slider to control percolation probability
slider_rect = pygame.Rect(10, HEIGHT - 40, WIDTH - 20, 30)
slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=slider_rect,
                                                start_value=PERCOLATION_PROBABILITY,
                                                value_range=(0.1, 1.0),
                                                manager=ui_manager,
                                                click_increment=0.05, )
def find_connected_group(row, col, group_number):
    if row < 0 or row >= GRID_HEIGHT or col < 0 or col >= GRID_WIDTH:
        return
    if not grid[row][col]:
        return
    if groups[row][col] != 0:
        return
    
    groups[row][col] = group_number
    
    find_connected_group(row - 1, col, group_number)
    find_connected_group(row + 1, col, group_number)
    find_connected_group(row, col - 1, group_number)
    find_connected_group(row, col + 1, group_number)

def generate_grid(probability):
    return [[random.random() < probability for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]

def generate_cell_colors():
    return [pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            for _ in range(GRID_HEIGHT * GRID_WIDTH)]

grid = generate_grid(PERCOLATION_PROBABILITY)

cell_colors = generate_cell_colors()

group_colors = [pygame.Color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                for _ in range(GRID_HEIGHT * GRID_WIDTH)]

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
                grid = generate_grid(PERCOLATION_PROBABILITY)
                pygame.display.flip

        ui_manager.process_events(event)

    ui_manager.update(time_delta)

    # Clear the screen
    screen.fill(WHITE)
    
    groups = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
    group_number = 0
    
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if grid[row][col] and groups[row][col] == 0:
                group_number += 1
                find_connected_group(row, col, group_number)
    
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            if grid[row][col]:
                group_num = groups[row][col]
                color = group_colors[group_num - 1]  # Subtract 1 because group numbers start from 1
            else:
                color = cell_colors[row * GRID_WIDTH + col]
            
            pygame.draw.rect(screen, color, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

    ui_manager.draw_ui(screen)

    # Update the display
    pygame.display.flip()

# Clean up
pygame.quit()
# %%
