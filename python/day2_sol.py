from argparse import ArgumentParser

TEST = "../inputs/day2_smallinput.txt"
FILE = "../inputs/day2_input.txt"

def doesRepeatTwice(num: str) -> bool:
    if (len(num) % 2 == 1):
        return False
    
    return num[:len(num) // 2] == num[len(num) // 2:]

def doesRepeatN(num: str) -> bool:
    numLen: int = len(num)
    parts: int = 2

    while (numLen // parts > 0):
        if (numLen % parts != 0):
            parts += 1
            continue

        partsList: list[str] = []
        chunkSize: int = numLen // parts
        for i in range(0, parts):
            startInd: int = i * chunkSize
            partsList.append(num[startInd:startInd + chunkSize])

        if (len(set(partsList)) == 1):
            return True

        parts += 1

    return False

def day2Sol(input: str, partSol: int) -> int:
    sum: int = 0
    with open(input, "r") as f:
        line = f.readline()
        ranges = [x.strip() for x in line.split(',')]

        for r in ranges:
            mid = r.find('-') 
            start: int = int(r[:mid])
            end: int = int(r[mid + 1:])

            for i in range(start, end + 1):
                if (doesRepeatTwice(str(i)) if partSol == 1 else doesRepeatN(str(i))):
                    sum += i
           
    return sum

def main():
    parser = ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    print(f"Day 2 Part 1 Solution: {day2Sol(TEST if args.test else FILE, 1)}")
    print(f"Day 2 Part 2 Solution: {day2Sol(TEST if args.test else FILE, 2)}")

if __name__ == "__main__":
    main()
