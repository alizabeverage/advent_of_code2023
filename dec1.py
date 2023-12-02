# Open the file in read mode and read all lines into a list
f = open('/Users/alizabeverage/Downloads/adventofcode.com_2023_day_1_input.txt','r')
lines = f.readlines()
f.close()

# Dictionary mapping words to their corresponding numerical representations
nums_str = {'one':'1','two':'2','three':'3','four':'4','five':'5','six':'6','seven':'7','eight':'8','nine':'9'}

# Function to replace words in a line with their numerical representations
def get_string(line):
    found1 = 0
    switch = 'on'
    
    # Loop through the characters in the line
    for i,ch in enumerate(line):
        if switch == 'off':continue
        # Check if a word from nums_str is present in the substring before the current character
        for string,num in nums_str.items():
            if string in line[:i]:
                # Replace the word with its numerical representation
                line_tmp1 = line.replace(string,num)
                switch = 'off'
                found1+=1

    found2 = 0
    switch = 'on'
    # Loop through the characters in the line in reverse order
    for i,ch in enumerate(line):
        if switch == 'off':continue
        # Check if a word from nums_str is present in the substring after the current character
        for string,num in nums_str.items():
            if string in line[-(i+1):]:
                # Replace the word with its numerical representation
                line_tmp2 = line.replace(string,num)
                switch = 'off'
                found2+=1

    # If no word is found in the second search direction, use the original line
    if found2==0:
        line_tmp2 = line
    # If no word is found in the first search direction, use the original line
    if found1 == 0:
        line_tmp1 = line
    return line_tmp1, line_tmp2

# Initialize an empty list to store the numerical representations extracted from each line
arr = []
# Loop through each line in the list of lines
for line in lines:
    # Call the get_string function to replace words with numerical representations
    left, right = get_string(line)
    
    # Initialize an empty string to store the final numerical representation
    x = ''
    switch = 'on'
    
    # Loop through the characters in the modified left part of the line
    for ch in left:
        if switch == 'off': continue
        # Append numerical characters to the string 'x'
        if ch in ['0','1','2','3','4','5','6','7','8','9']:
            x+=ch
            switch = 'off'

    switch = 'on'
    
    # Loop through the characters in the modified right part of the line in reverse order
    for ch in right[::-1]:
        if switch == 'off': continue
        # Append numerical characters to the string 'x'
        if ch in ['0','1','2','3','4','5','6','7','8','9']:
            x+=ch
            switch = 'off'

    # Append the final numerical representation to the list 'arr'
    arr.append(x)

# Convert the list 'arr' to a NumPy array and convert its data type to integers
arrint = np.array(arr).astype(int)

# Print the sum of the integers in the array
print(arrint.sum())