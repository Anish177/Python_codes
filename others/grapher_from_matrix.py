# WIP

# %%
import sys
import pygame
import math
from scipy.sparse.csgraph import minimum_spanning_tree as mst
from scipy.sparse import csr_matrix

# %%
# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
NODE_RADIUS = 20
FONT = pygame.font.Font(None, 24)

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Create a screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Graph Visualizer")

# Helper function to draw text on the screen
def draw_text(text, x, y, color=BLACK):
    text_surface = FONT.render(text, True, color)
    screen.blit(text_surface, (x, y))

# Helper function to draw a node
def draw_node(x, y, label):
    pygame.draw.circle(screen, GRAY, (x, y), NODE_RADIUS)
    draw_text(label, x - 10, y - 10)

# Helper function to draw an edge with weight
def draw_edge(x1, y1, x2, y2, weight):
    pygame.draw.line(screen, BLACK, (x1, y1), (x2, y2), 2)
    draw_text(str(weight), (x1 + x2) // 2, (y1 + y2) // 2)

# Example adjacency matrix with weights
adjacency_matrix = [
    [0, 2, 4, 0, 0],
    [2, 0, 3, 7, 0],
    [4, 3, 0, 1, 5],
    [0, 7, 1, 0, 6],
    [0, 0, 5, 6, 0]
]

adjacency_matrix = mst(adjacency_matrix).toarray().astype(int)
# Calculate node positions
num_nodes = len(adjacency_matrix)
node_positions = [
    [
        WIDTH // 2 + 200 * math.cos(2 * math.pi * i / num_nodes),
        HEIGHT // 2 + 200 * math.sin(2 * math.pi * i / num_nodes)
    ]
    for i in range(num_nodes)
]

selected_node = None
offset = [0, 0]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for i, pos in enumerate(node_positions):
                if math.sqrt((pos[0] - mouse_pos[0])**2 + (pos[1] - mouse_pos[1])**2) < NODE_RADIUS:
                    selected_node = i
                    offset = [pos[0] - mouse_pos[0], pos[1] - mouse_pos[1]]
        elif event.type == pygame.MOUSEBUTTONUP:
            selected_node = None

    if selected_node is not None:
        mouse_pos = pygame.mouse.get_pos()
        node_positions[selected_node][0] = mouse_pos[0] + offset[0]
        node_positions[selected_node][1] = mouse_pos[1] + offset[1]

    screen.fill(WHITE)

    # Draw edges and nodes
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes):
            if adjacency_matrix[i][j] > 0:
                draw_edge(node_positions[i][0], node_positions[i][1],
                          node_positions[j][0], node_positions[j][1],
                          adjacency_matrix[i][j])
        draw_node(node_positions[i][0], node_positions[i][1], str(i + 1))

    pygame.display.flip()

pygame.quit()
sys.exit()



# %%
