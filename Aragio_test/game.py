import pygame as pg
from random import randrange
from sys import exit


# global variables
WINDOW = 1000
TILE_SIZE = 50
RANGE = (TILE_SIZE // 2, WINDOW - TILE_SIZE // 2, TILE_SIZE)


# helper function
def get_random_position(): return [randrange(*RANGE), randrange(*RANGE)]


# snake data
snake = pg.rect.Rect([0, 0, TILE_SIZE - 2, TILE_SIZE - 2])
snake.center = get_random_position()  # head of snake
length = 1
segments = [snake.copy()]
snake_dir = (0, 0)
dirs = {pg.K_w: 1, pg.K_s: 1, pg.K_a: 1, pg.K_d: 1}

# food data
food = snake.copy()
food.center = get_random_position()

# game set up
time, time_step = 0, 110
screen = pg.display.set_mode([WINDOW]*2)
clock = pg.time.Clock()

# game loop
while True:
    clock.tick(60)
    screen.fill('black')

    # draw food
    pg.draw.rect(screen, 'red', food)

    ################################
    # TODO 1: Draw the snake! HINT: Look at how food is drawn and use a for loop to loop over `segments`
    # Write in here

    ################################

    for event in pg.event.get():
        if event.type == pg.QUIT:
            exit()
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w and dirs[pg.K_w]:  # go up when w is pressed
                snake_dir = (0, -TILE_SIZE)
                dirs = {pg.K_w: 1, pg.K_s: 0, pg.K_a: 1, pg.K_d: 1}
            #################################
            # TODO 2: implement going in the other 3 directions!
            # Write in here

            #################################
    # check borders and selfeating
    self_eating = pg.Rect.collidelist(snake, segments[:-1]) != -1
    # TODO 3: Implement top and bottom boundaries in the if statement below
    if snake.left < 0 or snake.right > WINDOW or self_eating:
        #################################
        # TODO 4: What happens when the snake loses? The game starts over!
        #         So re-initialize `snake.center`, `food.center`, `length`, `snake_dir`, and `dirs`
        #         `segments` is already re-initialized for you!
        # Write in here
        segments = [snake.copy()]

        #################################

    # check food
    if snake.center == food.center:
        food.center = get_random_position()
        length += 1

    # move snake
    time_now = pg.time.get_ticks()
    if time_now - time > time_step:
        time = time_now
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-length:]

    # update screen
    pg.display.update()
