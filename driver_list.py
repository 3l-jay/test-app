# Open the file in read mode
with open('drivers.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()

    # Print each line
    for line in lines:
        print(line.strip())  # Strip to remove any leading or trailing whitespace
