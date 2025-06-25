import random
import curses

# Initialize the curses module
stdscr = curses.initscr()
curses.curs_set(0)  # Hide the cursor
sh, sw = stdscr.getmaxyx()  # Get screen height and width
win = curses.newwin(sh, sw, 0, 0)  # Create a new window
win.keypad(1)
win.timeout(100)  # Refresh every 100ms

# Initial snake position and body
snk_x = sw//4
snk_y = sh//2
snake = [
    [snk_y, snk_x],
    [snk_y, snk_x-1],
    [snk_y, snk_x-2]
]

# Initial food position
food = [sh//2, sw//2]
win.addch(food[0], food[1], curses.ACS_PI)

key = curses.KEY_RIGHT  # Initial movement direction

while True:
    next_key = win.getch()
    key = key if next_key == -1 else next_key

    # Calculate new head of the snake
    y = snake[0][0]
    x = snake[0][1]
    if key == curses.KEY_DOWN:
        y += 1
    elif key == curses.KEY_UP:
        y -= 1
    elif key == curses.KEY_LEFT:
        x -= 1
    elif key == curses.KEY_RIGHT:
        x += 1

    new_head = [y, x]

    # Game over if snake runs into itself or the wall
    if (y in [0, sh] or x in [0, sw] or new_head in snake):
        curses.endwin()
        print("Game Over!")
        break

    snake.insert(0, new_head)

    # If snake eats the food
    if snake[0] == food:
        food = None
        while food is None:
            nf = [
                random.randint(1, sh-2),
                random.randint(1, sw-2)
            ]
            food = nf if nf not in snake else None
        win.addch(food[0], food[1], curses.ACS_PI)
    else:
        # Move the snake
        tail = snake.pop()
        win.addch(tail[0], tail[1], ' ')

    win.addch(snake[0][0], snake[0][1], curses.ACS_CKBOARD)