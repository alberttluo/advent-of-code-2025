import sys
from argparse import ArgumentParser

TEST = "../inputs/day5_smallinput.txt"
FILE = "../inputs/day5_input.txt"

def part1Sol(ranges: list[str], nums: list[int]) -> int:
    numFresh: int = 0

    # An ingredient ID is fresh if it is >= some number in startSet, and <= some number in endSet.
    rangeSet: set = set()

    for r in ranges:
        midInd: int = r.find('-')
        start: int = int(r[:midInd].strip())
        end: int = int(r[midInd + 1:].strip())
        
        rangeSet.add((start, end))

    for num in nums:
        for rs in rangeSet:
            if (num >= rs[0] and num <= rs[1]):
                numFresh += 1
                break

    return numFresh

def part2Sol(ranges: list[str]) -> int:
    rangesList: list[tuple[int, int]] = list((int(x[:x.find('-')]), int(x[x.find('-') + 1:])) for x in ranges)

    # Sort by the starting value.
    rangesList.sort(key = lambda x: x[0])

    total: int = 0
    curStart: int = rangesList[0][0]
    curEnd: int = rangesList[0][1]

    for s, e in rangesList[1:]:
        # Overlapping or adjacent
        if (s <= curEnd + 1):
            # Extend interval if possible
            if e > curEnd:
                curEnd = e
        else:
            # Close current interval and start new one.
            total += (curEnd - curStart + 1)
            curStart = s
            curEnd = e

    # Factor in last interval.
    total += (curEnd - curStart + 1)
    return total

def main():
    parser = ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    input = TEST if args.test else FILE
    ranges = list[str]
    nums = list[int]

    with open(input, "r") as f:
        lines = f.readlines()
        blankInd: int = lines.index('\n')
        ranges = [x.strip() for x in lines[:blankInd]]
        nums = [int(x.strip()) for x in lines[blankInd + 1:]]

    print(f"Day 5 Part 1 Solution: {part1Sol(ranges, nums)}")
    print(f"Day 5 Part 2 Solution: {part2Sol(ranges)}")

if __name__ == "__main__":
    main()
