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

            totalJoltage += joltageList[maxJoltageInd] * 10 + maxSecond

    return totalJoltage

def part2Sol(input: str) -> int:
    totalJoltage: int = 0

    with open(input, 'r') as f:
        banks: list[str] = f.readlines()

        for bank in banks:
            joltageList: list[int] = [int(x) for x in list(bank.strip())]
            maxJoltageInd: list[int] = []
            maxJoltages: list[str] = []
            numBatteries: int = len(joltageList)

            for i in range(12):
                startInd: int = ((maxJoltageInd[i - 1] + 1) if i > 0 else 0)
                validJoltages: list[int] = joltageList[startInd:numBatteries - (11 - i)]
                maxValInd: int = validJoltages.index(max(validJoltages))
                maxJoltageInd.append(maxValInd + startInd)
                maxJoltages.append(str(validJoltages[maxValInd]))

            totalJoltage += int(''.join(maxJoltages))

    return totalJoltage

def main():
    parser = ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    print(f"Day 3 Part 1 Solution: {part1Sol(TEST if args.test else FILE)}")
    print(f"Day 3 Part 2 Solution: {part2Sol(TEST if args.test else FILE)}")

if __name__ == "__main__":
    main()
