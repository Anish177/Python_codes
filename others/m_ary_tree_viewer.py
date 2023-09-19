# WIP - breaks for some m_values

# %%
from math import log2
import pygame

# %%
# Function to draw the m_value-ary tree
def draw_tree(screen, nodes, m_value, x, y, level, spacing):
    if level < len(nodes) and nodes[level] is not None:
        # Draw current node
        pygame.draw.circle(screen, NODE_COLOR, (x, y), NODE_RADIUS)
        font = pygame.font.Font(None, 36)
        text = font.render(str(nodes[level]), True, (124, 167, 255))
        text_rect = text.get_rect(center=(x, y))
        screen.blit(text, text_rect)

        # Calculate positions for child nodes
        child_x = x - (spacing * (m_value - 1) / 2)
        child_y = y + 100

        # Draw lines to child nodes
        for i in range(m_value):
            next_level = level * m_value + i + 1
            if next_level < len(nodes) and nodes[next_level] is not None:  # Check for None before drawing edge
                pygame.draw.line(screen, LINE_COLOR, (x, y + NODE_RADIUS), (child_x, child_y - NODE_RADIUS), 2)
                draw_tree(screen, nodes, m_value, int(child_x), int(child_y), next_level, spacing // m_value)
            child_x += spacing


# Main function
def draw(nodes, m_value):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("m-ary Tree Viewer")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((69, 76, 90))
        draw_tree(screen, nodes, m_value, SCREEN_WIDTH // 2, 100, 0, SCREEN_WIDTH // (log2(len(nodes) + 1)))
        pygame.display.flip()

    pygame.quit()
    # sys.exit()
    
# %%
if __name__ == "__main__":
    pygame.init()
    nodes = [1, 21, 31, None, 42, 53, None, 55, 56, 57]
    # Constants
    SCREEN_WIDTH = (log2(len(nodes) + 1)) * 200
    SCREEN_HEIGHT = (log2(len(nodes) + 1)) * 150
    NODE_RADIUS = 25
    NODE_COLOR = (7, 37, 99)
    LINE_COLOR = (2, 23, 66)
    m_value = 3
    draw(nodes, m_value)

# %%
