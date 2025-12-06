from argparse import ArgumentParser

TEST = "../inputs/day1_smallinput.txt"
FILE = "../inputs/day1_input.txt"

def part1Sol(input: str) -> int:
    # Dial is initially pointing at 50.
    currNum: int = 50

    # Number of times the dial points to zero (only valid after the first parsed line).
    numZeros: int = 0
    with open(input, "r") as f:
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

    return numZeros

def part2Sol(input: str) -> int:
    # Dial initially points at 50.
    currNum: int = 50

    # Number of times dial passes or reaches 0.
    numZeros: int = 0

    with open(input, "r") as f:
        lines = f.readlines()

        for line in lines:
            # Moving to the left corresponds with a subtraction, right with addition.
            dir: str = line[0]
            num: int = int(line[1:].strip())

            # Clicks needed in either direction to first reach 0.
            leftDiff: int = 100 if currNum == 0 else currNum
            rightDiff: int = 100 - currNum

            if (dir == 'L' and num >= leftDiff):
                numZeros += (num - leftDiff) // 100 + 1
            elif (dir == 'R' and num >= rightDiff):
                numZeros += (num - rightDiff) // 100 + 1

            currNum = (currNum + (-1 if dir == 'L' else 1)*num) % 100
                
    return numZeros

def main():
    parser = ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    print(f"Day 1 Part 1 Solution: {part1Sol(TEST if args.test else FILE)}")
    print(f"Day 1 Part 2 Solution: {part2Sol(TEST if args.test else FILE)}")

if __name__ == "__main__":
    main()
