#Reference: https://github.com/engineer-man/youtube/tree/master/015
import random
import curses

# initialize screen
s = curses.initscr()                # initialize screen
curses.curs_set(0)                  # hide cursor
sh, sw = s.getmaxyx()               # get height and width of screen
w = curses.newwin(sh, sw, 0, 0)     # create window
w.keypad(1)                         # allow keyboard input
w.timeout(100)                      # refresh every 100ms

# initialize snake position, snake, direction
snk_x = int(sw/4)
snk_y = int(sh/2)
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2],
]
key = curses.KEY_RIGHT

# initialize food
food = [
    random.randint(1, sh-1),
    random.randint(1, sw-1)
    ]
while food in snake:
    food = [
        random.randint(1, sh-1),
        random.randint(1, sw-1)
    ]
w.addch(food[0], food[1], curses.ACS_DIAMOND)

# snake movement
while True:
    next_key = w.getch()
    key = key if next_key == -1 else next_key

    # lose game if snake height is 0 or height, snake width is 0 or width, or snake is in itself
    if snake[0][0] in [0, sh] or snake[0][1] in [0, sw] or snake[0] in snake[1:]: 
        curses.endwin()
        quit()

    # new head position
    new_head = [snake[0][0], snake[0][1]]

    if key == curses.KEY_DOWN:
        new_head[0] += 1
    if key == curses.KEY_UP:
        new_head[0] -= 1
    if key == curses.KEY_LEFT:
        new_head[1] -= 1
    if key == curses.KEY_RIGHT:
        new_head[1] += 1

    snake.insert(0, new_head)

    # food behaviour: if eaten, randomly place new food (not in snake)
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-1),
                random.randint(1, sw-1)
            ]
            food = nf if nf not in snake else None  # assign food pos only if not in snake
        w.addch(food[0], food[1], curses.ACS_DIAMOND)
    else:
        tail = snake.pop()
        w.addch(tail[0], tail[1], ' ')

    w.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)

