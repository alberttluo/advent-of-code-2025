from argparse import ArgumentParser

FILE = "inputs/day3_input.txt"
TEST = "test/day3_test.txt"

def part1Sol(input: str) -> int:
    totalJoltage: int = 0 

    with open(input, 'r') as f:
        banks: list[str] = f.readlines()

        for bank in banks:
            joltageList: list[int] = [int(x) for x in list(bank.strip())]
            numBatteries: int = len(joltageList)

            maxJoltageInd: int = joltageList.index(max(joltageList))

            if (maxJoltageInd == numBatteries - 1):
                maxJoltageInd = joltageList.index(max(joltageList[:numBatteries - 1]))

            maxSecond: int = max(joltageList[maxJoltageInd + 1:])

            print(joltageList[maxJoltageInd] * 10 + maxSecond)
            totalJoltage += joltageList[maxJoltageInd] * 10 + maxSecond

    return totalJoltage

def main():
    parser = ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    print(f"Day 3 Part 1 Solution: {part1Sol(TEST if args.test else FILE)}")

if __name__ == "__main__":
    main()
