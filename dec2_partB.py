
# Open the specified file in read mode
f = open('adventofcode.com_2023_day_2_input.txt', 'r')

# Read all lines from the file and store them in the 'lines' list
lines = f.readlines()

# Close the file after reading its contents
f.close()

# Initialize variables to keep track of the count and total powers
count = 0
powers = 0

# Iterate over each line in the 'lines' list
for line in lines:
    # Extract the game number from the line
    game = int(line.split(':')[0].split()[-1])

    # Initialize a boolean variable to check for cubes
    cube_bool = True

    # Initialize a dictionary to store color-specific values
    dict_tmp = {'red': [], 'green': [], 'blue': []}

    # Iterate over each draw in the line and extract color and value information
    for draw in line.split(':')[1].split(';'):
        for colors in draw.split(','):
            # Append the value to the corresponding color key in the dictionary
            dict_tmp[colors.split()[-1]].append(int(colors.split()[-2]))

    # Initialize a variable to calculate the power for the current line
    power = 1

    # Iterate over the color-specific values and calculate the product of maximum values
    for col, val in dict_tmp.items():
        power *= max(val)

    # Add the calculated power to the total powers
    powers += power

# Print the total powers calculated from all lines
print(powers)
