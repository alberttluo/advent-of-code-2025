from argparse import ArgumentParser

TEST = "../inputs/day4_smallinput.txt"
FILE = "../inputs/day4_input.txt"

DIRS: list[list[int]] = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]

def part1Sol(grid: list[list[str]]) -> int:
    numAccessible: int = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):
            numAdj: int = 0

            if (grid[row][col] != '@'):
                continue

            for dir in DIRS:
                dx = col + dir[0]
                dy = row + dir[1]

                if (dx < 0 or dx >= len(grid) or dy < 0 or dy >= len(grid[0])):
                    continue

                numAdj += (grid[dy][dx] == '@')

            if (numAdj < 4):
                numAccessible += 1

    return numAccessible

def part2Sol(grid: list[list[str]]) -> int:
    numRemoved: int = 0
    passes: int = 0

    while True:
        removedList: list[(int, int)] = []
        for row in range(len(grid)):
            for col in range(len(grid[row])):
                numAdj: int = 0

                if (grid[row][col] != '@'):
                    continue

                for dir in DIRS:
                    dx = col + dir[0]
                    dy = row + dir[1]

                    if (dx < 0 or dx >= len(grid) or dy < 0 or dy >= len(grid[0])):
                        continue

                    numAdj += (grid[dy][dx] == '@')

                if (numAdj < 4):
                    numRemoved += 1
                    removedList.append((row, col))

        if (len(removedList) == 0):
            break

        for (remRow, remCol) in removedList:
            grid[remRow][remCol] = '.'

    return numRemoved

def main():
    parser = ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    input = TEST if args.test else FILE
    grid: list[list[str]] = [[]]

    with open(input, "r") as f:
        for line in f.readlines():
            grid.append(list(line.strip()))

    print(f"Day 4 Part 1 Solution: {part1Sol(grid[1:])}")
    print(f"Day 4 Part 2 Solution: {part2Sol(grid[1:])}")

if __name__ == "__main__":
    main()
