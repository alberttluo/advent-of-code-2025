FILE = "day1_input.txt"

# Dial is initially pointing at 50.
currNum: int = 50

# Number of times the dial points to zero (only valid after the first parsed line).
numZeros: int = 0

with open(FILE, "r") as f:
    lines = f.readlines()

    for line in lines:
        # Moving to the left corresponds with a subtraction, right with addition.
        dir: int = -1 if line[0] == 'L' else 1
        num: int = int(line[1:].strip())

        # The dial is circular, so we take everything mod 100.
        currNum = (currNum + dir * num) % 100

        # Check that the dial is pointing to 0 after the instruction.
        if (currNum == 0):
            numZeros += 1

print(numZeros)
