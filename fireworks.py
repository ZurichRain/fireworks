import pygame
import random
import sys

pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))

BLACK = (0, 0, 0)
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]

class Particle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.vel_x = random.randint(-5, 5)
        self.vel_y = random.randint(-5, 5)
        self.lifetime = random.randint(20, 50)

    def update(self):
        self.x += self.vel_x
        self.y += self.vel_y
        self.lifetime -= 1

    def draw(self):
        if self.lifetime > 0:
            pygame.draw.circle(screen, self.color, (self.x, self.y), 3)

class Firework:
    def __init__(self):
        self.x = random.randint(0, screen_width)
        self.y = screen_height
        self.color = random.choice(colors)
        self.explosions = []
        self.vel_y = -random.randint(10, 20)
        # self.vel_y = 1
        self.exploded = False

    def update(self):
        if not self.exploded:
            self.y += self.vel_y
            # print(self.vel_y)
            if self.y <= 100:
                self.exploded = True
                self.explode()
        else:
            for explosion in self.explosions:
                explosion.update()

    def draw(self):
        if not self.exploded:
            pygame.draw.circle(screen, self.color, (self.x, self.y), 5)
        else:
            for explosion in self.explosions:
                explosion.draw()

    def explode(self):
        for _ in range(50):
            self.explosions.append(Particle(self.x, self.y, self.color))



def main():
    clock = pygame.time.Clock()
    
    fireworks = [Firework() for _ in range(5)]
    # print(clock)
    # print(fireworks)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        for firework in fireworks:
            firework.update()
            firework.draw()

        pygame.display.flip()
        clock.tick(30)  # 控制帧率

if __name__ == "__main__":
    main()
