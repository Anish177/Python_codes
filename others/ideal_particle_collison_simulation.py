# %%
import random
import sys
import pygame
from pygame.math import Vector2

# %%
# Ball class definition
class Ball:
    def __init__(self, pos: list[int], vel: list[int], radius: int, color):
        self.pos = Vector2(pos)
        self.vel = Vector2(vel)
        self.radius = radius
        self.color = color

    def update(self, dt: int):
        self.pos += self.vel * dt

    def collide_with_screen_edges(self, screen_width: int, screen_height: int):
        if self.pos.x < self.radius or self.pos.x > screen_width - self.radius:
            self.vel.x *= -1
        if self.pos.y < self.radius or self.pos.y > screen_height - self.radius:
            self.vel.y *= -1

    def collide_with_ball(self, other: 'Ball'):
        distance = self.pos.distance_to(other.pos)
        if distance < self.radius + other.radius:
            normal = (self.pos - other.pos).normalize()
            tangent = Vector2(-normal.y, normal.x)
            self_vel_normal = normal.dot(self.vel)
            self_vel_tangent = tangent.dot(self.vel)
            other_vel_normal = normal.dot(other.vel)
            other_vel_tangent = tangent.dot(other.vel)
            self_vel_normal, other_vel_normal = get_new_velocities(self_vel_normal, other_vel_normal, self.radius, other.radius)
            self.vel = self_vel_normal * normal + self_vel_tangent * tangent
            other.vel = other_vel_normal * normal + other_vel_tangent * tangent


    def draw(self, surface: pygame.surface.Surface):
        pygame.draw.circle(surface, self.color, (int(self.pos.x), int(self.pos.y)), self.radius)

def get_new_velocities(v1: float, v2: float, r1: int, r2: int):
    # Calculate new velocities with some randomness
    new_v1 = ((v1 + v2) / 2 + random.uniform(-1, 1)) * (r2 ** 2) * 0.001
    new_v2 = ((v1 + v2) / 2 + random.uniform(-1, 1)) * (r1 ** 2) * 0.001
    return new_v1, new_v2

# %%
pygame.init()

# Set up the window
win_width = 700
win_height = 700
screen = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Ideal Particle Simulation")

# Set up the balls
ball0 = Ball((300, 300), (-2, 4), 25, (124, 120, 255))
ball1 = Ball((200, 200), (-5, -5), 30, (120, 255, 208))
ball2 = Ball((100, 150), (5, 5), 20, (255, 120, 158))
# ball3 = Ball((100, 100), (5, 5), 20, (255, 219, 120))
# ball4 = Ball((350, 200), (-2, 4), 25, (237, 120, 255))
# ball5 = Ball((250, 250), (-5, -5), 30, (255, 192, 120))
balls = [ball0, ball1, ball2]
# Set up the clock
clock = pygame.time.Clock()
frame_rate = 240

# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Create a new ball at the position of the mouse click
            pos = pygame.mouse.get_pos()
            vel = Vector2(random.uniform(-5, 5), random.uniform(-5, 5))
            radius = random.randint(10, 30)
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            ball = Ball(pos, vel, radius, color)
            balls.append(ball)

    # Clear screen
    screen.fill((36, 36, 36))

    # Update and draw balls
    for ball in balls:
        ball.update(1)
        ball.collide_with_screen_edges(win_width, win_height)
        for other_ball in balls:
            if ball != other_ball:
                ball.collide_with_ball(other_ball)
        ball.draw(screen)

    # Update screen
    pygame.display.update()
    pygame.time.delay(int(2000 / frame_rate))
    
# %%
