# Define the maximum allowed number of cubes for each color
dict_cubes = {'red': 12, 'green': 13, 'blue': 14}

# Open the specified file in read mode
f = open('adventofcode.com_2023_day_2_input.txt', 'r')

# Read all lines from the file and store them in the 'lines' list
lines = f.readlines()

# Initialize a variable to keep track of the count
count = 0

# Iterate over each line in the 'lines' list
for line in lines:
    # Extract the game number from the line
    game = int(line.split(':')[0].split()[-1])

    # Initialize a boolean variable to check if the cube conditions are met
    cube_bool = True

    # Initialize a temporary dictionary to store color-specific values
    dict_tmp = {'red': 0, 'green': 0, 'blue': 0}

    # Iterate over each draw in the line and extract color and value information
    for draw in line.split(':')[1].split(';'):
        for colors in draw.split(','):
            # Update the temporary dictionary with color-specific values
            dict_tmp[colors.split()[-1]] = int(colors.split()[-2])

        # Check if the number of cubes for each color is within the allowed limits
        for col, val in dict_cubes.items():
            cube_bool &= (dict_tmp[col] <= val)

    # If cube conditions are met, add the game number to the count
    if cube_bool:
        count += game

# Print the total count calculated from all lines
print(count)
