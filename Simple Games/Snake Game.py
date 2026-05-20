import pygame
import sys
import random

 # Pygame Window setup #
pygame.init()

WIDTH = 600
HEIGHT = 400
CELL_SIZE = 20

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

def draw_checkerboard():
    for row in range(HEIGHT // CELL_SIZE):
        for col in range(WIDTH // CELL_SIZE):
            if (row + col) % 2 == 0:
                color = (170, 215, 81)
            else:
                color = (162, 209, 73)

            pygame.draw.rect(
                screen,
                color,
                (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            )

 # Snake Blueprint #
class Snake:
    def __init__(self):
        self.body = [(100, 100), (80, 100), (60, 100)]
        self.direction = "RIGHT"

    def move(self):
        head_x, head_y = self.body[0]

        if self.direction == "UP":
            head_y -= CELL_SIZE
        elif self.direction == "DOWN":
            head_y += CELL_SIZE
        elif self.direction == "LEFT":
            head_x -= CELL_SIZE
        elif self.direction == "RIGHT":
            head_x += CELL_SIZE

        new_head = (head_x, head_y)
        self.body.insert(0, new_head)
        return new_head

    def remove_tail(self):
         self.body.pop()

    def draw(self):
         for segment in self.body:
             pygame.draw.rect(screen, (79, 121, 66),
                              (segment[0], segment[1], CELL_SIZE, CELL_SIZE))

 # Food Blueprint #
class Food:
    def __init__(self, snake_body):
        self.position = self.spawn(snake_body)

    def spawn(self, snake_body):
        while True:
            x = random.randrange(0, WIDTH, CELL_SIZE)
            y = random.randrange(0, HEIGHT, CELL_SIZE)
            if (x, y) not in snake_body:
                return (x, y)

    def draw(self):
        pygame.draw.rect(screen, (219, 68, 55),
            (self.position[0], self.position[1], CELL_SIZE, CELL_SIZE))

 # Defined Functions & Game End Screen & Behavious #
def draw_score(score):
    text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(text, (10, 10))

def game_over_screen(score):
    screen.fill((0, 0, 0))
    text1 = font.render("Game Over", True, (255, 0, 0))
    text2 = font.render(f"Final Score: {score}", True, (255, 255, 255))
    text3 = font.render("Press R to Restart", True, (255, 255, 255))
    screen.blit(text1, (WIDTH // 2 - 80, HEIGHT // 2 - 60))
    screen.blit(text2, (WIDTH // 2 - 100, HEIGHT // 2 - 20))
    screen.blit(text3, (WIDTH // 2 - 120, HEIGHT // 2 + 20))
    pygame.display.update()

def main():
    snake = Snake()
    food = Food(snake.body)
    score = 0
    speed = 10
    running = True

    while running:
        clock.tick(speed)

        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 pygame.quit()
                 sys.exit()

             if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_UP and snake.direction != "DOWN":
                     snake.direction = "UP"
                 elif event.key == pygame.K_DOWN and snake.direction != "UP":
                     snake.direction = "DOWN"
                 elif event.key == pygame.K_LEFT and snake.direction != "RIGHT":
                     snake.direction = "LEFT"
                 elif event.key == pygame.K_RIGHT and snake.direction != "LEFT":
                     snake.direction = "RIGHT"

        new_head = snake.move()

        if (
            new_head[0] < 0 or
            new_head[0] >= WIDTH or
            new_head[1] < 0 or
            new_head[1] >= HEIGHT or
            new_head in snake.body[1:]
        ):
            return score

        if new_head == food.position:
            score += 1
            speed += 0.5
            food = Food(snake.body)
        else:
            snake.remove_tail()

        draw_checkerboard()
        snake.draw()
        food.draw()
        draw_score(score)
        pygame.display.update()

while True:
    final_score = main()
    game_over_screen(final_score)

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    waiting = False
