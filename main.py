import pygame
import random
import time

# Set the grid size in pixels
global grid_size
grid_size = 150

# Define the grid
grid = [
    [0, 0, 0, 1],
    [0, 2, 0, -1],
    [0, 0, 0, 0]
    ]

# Define policies. Moves are defined as a number from 1 to 4, where 0 = up, 1 = right, 2 = down, 4 = left
policies = {
    "0.01": [
        [2, 2, 2, 0],
        [1, 0, 4, 0],
        [1, 4, 4, 3]
    ],
    "0.03": [
        [2, 2, 2, 0],
        [1, 0, 1, 0],
        [1, 4, 4, 4]
    ], 
    "0.4": [
        [2, 2, 2, 0],
        [1, 0, 1, 0],
        [1, 2, 1, 4]
    ],
    "2.0": [
        [2, 2, 2, 0],
        [1, 0, 2, 0],
        [2, 2, 2, 1]
    ]
}

# Set start position
position = [0, 2]


# Draw the grid given the grid
def draw_grid(grid, position):
    # For each row
    for i in range(3):
        # For each column
        for j in range(4):
            # If it is empty, make a dark grey square
            if grid[i][j] == 0:
                pygame.draw.rect(window, (180, 180, 180), (j * grid_size, i * grid_size, grid_size, grid_size))
            # If it is the positive goal, make it green
            elif grid[i][j] == 1:
                pygame.draw.rect(window, (0, 255, 0), (j * grid_size, i * grid_size, grid_size, grid_size))
            # If it is the negative goal, make it red
            elif grid[i][j] == -1:
                pygame.draw.rect(window, (255, 0, 0), (j * grid_size, i * grid_size, grid_size, grid_size))
            # if it is a wall, make it dark grey
            elif grid[i][j] == 2:
                pygame.draw.rect(window, (70, 70, 70), (j * grid_size, i * grid_size, grid_size, grid_size))

    # Draw current position as a blue square
    pygame.draw.rect(window, (0, 0, 255), (position[0] * grid_size + 1/6 * grid_size, position[1] * grid_size + 1/6 * grid_size, grid_size * 2/3, grid_size * 2/3))

    # Draw arrow left
    pygame.draw.polygon(window, (0, 0, 0), ((position[0] * grid_size + 4/24 * grid_size, position[1] * grid_size + 4/9 * grid_size),
                                            (position[0] * grid_size + 4/24 * grid_size, position[1] * grid_size + 5/9 * grid_size),
                                            (position[0] * grid_size + 2/24 * grid_size, position[1] * grid_size + 5/9 * grid_size),
                                            (position[0] * grid_size + 2/24 * grid_size, position[1] * grid_size + 5/8 * grid_size),
                                            (position[0] * grid_size + 0/24 * grid_size, position[1] * grid_size + 1/2 * grid_size),
                                            (position[0] * grid_size + 2/24 * grid_size, position[1] * grid_size + 3/8 * grid_size),
                                            (position[0] * grid_size + 2/24 * grid_size, position[1] * grid_size + 4/9 * grid_size)))

    # Draw arrow right
    pygame.draw.polygon(window, (0, 0, 0), ((position[0] * grid_size + 20/24 * grid_size, position[1] * grid_size + 4/9 * grid_size),
                                            (position[0] * grid_size + 20/24 * grid_size, position[1] * grid_size + 5/9 * grid_size),
                                            (position[0] * grid_size + 22/24 * grid_size, position[1] * grid_size + 5/9 * grid_size),
                                            (position[0] * grid_size + 22/24 * grid_size, position[1] * grid_size + 5/8 * grid_size),
                                            (position[0] * grid_size + 24/24 * grid_size, position[1] * grid_size + 1/2 * grid_size),
                                            (position[0] * grid_size + 22/24 * grid_size, position[1] * grid_size + 3/8 * grid_size),
                                            (position[0] * grid_size + 22/24 * grid_size, position[1] * grid_size + 4/9 * grid_size)))
    # Draw arrow up
    pygame.draw.polygon(window, (0, 0, 0), ((position[0] * grid_size + 4/9 * grid_size, position[1] * grid_size + 4/24 * grid_size),
                                            (position[0] * grid_size + 5/9 * grid_size, position[1] * grid_size + 4/24 * grid_size),
                                            (position[0] * grid_size + 5/9 * grid_size, position[1] * grid_size + 2/24 * grid_size),
                                            (position[0] * grid_size + 5/8 * grid_size, position[1] * grid_size + 2/24 * grid_size),
                                            (position[0] * grid_size + 1/2 * grid_size, position[1] * grid_size + 0/24 * grid_size),
                                            (position[0] * grid_size + 3/8 * grid_size, position[1] * grid_size + 2/24 * grid_size),
                                            (position[0] * grid_size + 4/9 * grid_size, position[1] * grid_size + 2/24 * grid_size)))

    # Draw arrow down
    pygame.draw.polygon(window, (0, 0, 0), ((position[0] * grid_size + 4/9 * grid_size, position[1] * grid_size + 20/24 * grid_size),
                                            (position[0] * grid_size + 5/9 * grid_size, position[1] * grid_size + 20/24 * grid_size),
                                            (position[0] * grid_size + 5/9 * grid_size, position[1] * grid_size + 22/24 * grid_size),
                                            (position[0] * grid_size + 5/8 * grid_size, position[1] * grid_size + 22/24 * grid_size),
                                            (position[0] * grid_size + 1/2 * grid_size, position[1] * grid_size + 24/24 * grid_size),
                                            (position[0] * grid_size + 3/8 * grid_size, position[1] * grid_size + 22/24 * grid_size),
                                            (position[0] * grid_size + 4/9 * grid_size, position[1] * grid_size + 22/24 * grid_size)))

    # Update the display
    pygame.display.update()


# Determine the move using the 80-10-10 rule (80% chance of getting the requested move, 10% for left/right of your requested move)
def determine_move(chosen_move):
    determined_move = chosen_move

    # Get a random number from 1-10
    random_number = random.randrange(10)
    
    # If the number is 0 (10% chance), go right from chosen move
    if random_number == 0:
        determined_move += 1
    # if the number is 1 (10% chance), go left from chosen move
    elif random_number == 1:
        determined_move -= 1

    # Check numbers for 5 (right of 4) and 0 (left of 1)
    if determined_move == 0:
        determined_move = 4
        arrow_left = [11, 11, 11]
    elif determined_move == 5:
        determined_move = 1
        arrow_up = [11, 11, 11]
    elif determined_move == 2:
        arrow_right = [11, 11, 11]
    elif determined_move == 3:
        arrow_down = [11, 11, 11]

    # Return the move
    return determined_move


# Update the position given the current position and the move to make
def make_move(move, current_position):
    # Update the x/y coordinate based on the move
    if move == 1:
        new_position = [current_position[0], current_position[1] - 1]
    elif move == 2:
        new_position = [current_position[0] + 1, current_position[1]]
    elif move == 3:
        new_position = [current_position[0], current_position[1] + 1]
    elif move == 4:
        new_position = [current_position[0] - 1, current_position[1]]

    # Check if move is legal, if not, return original position
    if new_position[0] < 0 or new_position[0] > 3 or new_position[1] < 0 or new_position[1] > 2 or new_position == [1, 1]:
        new_position = current_position

    return new_position


# Initializing pygame and variables
pygame.init()
window = pygame.display.set_mode((4 * grid_size, 3 * grid_size))
pygame.display.set_caption("Reinforcement learning")

# Ask user for which policy
chosen_policy = policies[input("De robot kan 0.01, 0.03, 0.4 of 2.0 energie verbruiken als hij een hokje verplaatst. Hoeveel energie wil je dat hij verbruikt? ")]

# Start running the pygame
run = True
while run:
    # Check if the game is quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Draw the grid
    draw_grid(grid, position)

    # Determine move
    move_to_make = determine_move(chosen_policy[position[1]][position[0]])

    # Make the move
    position = make_move(move_to_make, position)

    if position == [3, 0] or position == [3, 1]:
        # Wait a second before making next move
        time.sleep(1)

        # Draw the grid
        draw_grid(grid, position)

        # Reset position
        position = [0, 2]

    # Wait a second before making next move
    time.sleep(1)

pygame.quit()
