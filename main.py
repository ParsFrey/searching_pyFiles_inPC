import os

# Specify the directory to search and the pattern to search for
directory_to_search = r'C:\Users\LENOVO\OneDrive\Desktop\Codes2\auoto\searching_pyFiles_inPC'
pattern_to_search = 'py'

# List to store matches
matches = []

# Walk through the directory
for root, dirs, files in os.walk(directory_to_search):
    for file in files:
        if pattern_to_search in file:
            matches.append(os.path.join(root, file))

# Print the found files
for file in matches:
    print(file)
