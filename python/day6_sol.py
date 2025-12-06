import sys
import re
from argparse import ArgumentParser

TEST = "../inputs/day6_smallinput.txt"
FILE = "../inputs/day6_input.txt"

def part1Sol(operandList: list[list[int]], operationList: list[str]) -> int:
    sum: int = 0

    for i, ops in enumerate(operandList):
        listSum: int = ops[0]
        operation = operationList[i]

        if (operation == '*'):
            for op in ops[1:]:
                listSum *= op
        else:
            for op in ops[1:]:
                listSum += op

        sum += listSum

    return sum

def part2Sol(input) -> int:
    sum = 0
    with open(input, "r") as f:
        flines = f.readlines()
        lines = [line.rstrip("\n") for line in flines[:-1]]
        operationList = [x.strip() for x in list(flines[-1].split())]
        tokenSpansPerLine = [
            [m.span() for m in re.finditer('\S+', line)]
            for line in lines
        ]

        ncols = len(tokenSpansPerLine[0])

        spans = []

        for c in range(ncols):
            start = min(spans_line[c][0] for spans_line in tokenSpansPerLine)
            end = max(spans_line[c][1] for spans_line in tokenSpansPerLine)
            spans.append((start, end))


        cols = []

        for (start, end) in spans:
            col_vals = []
            width = end - start

            for line in lines:
                if len(line) < end:
                    line = line.ljust(end)
                field = line[start:end]
                col_vals.append(field)
            cols.append(col_vals)

        realOps = []

        for col in cols:
            maxLen = max([len(c) for c in col]) 
            tempList = []

            for i in reversed(range(maxLen)):
                num = ''
                for c in col:
                    if i < len(c):
                        num = num + c[i]
                tempList.append(int(num))
            realOps.append(tempList)

        for i, op in enumerate(realOps):
            listSum = op[0]

            if (operationList[i] == '*'):
                for o in op[1:]:
                    listSum *= o
            else:
                for o in op[1:]:
                    listSum += o

            sum += listSum
    
    return sum

def main():
    parser = ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    input = TEST if args.test else FILE

    operandList: list[list[int]] = []
    operationList: list[str] = []

    with open(input, "r") as f:
        lines = f.readlines()

        operationList = [x.strip() for x in list(lines[-1].split())]

        for _, line in enumerate(lines[:-1]):
            operandList.append([int(x.strip()) for x in line.split()])

    # Transpose the list.
    operandList = list(map(list, zip(*operandList)))

    print(f"Day 6 Part 1 Solution: {part1Sol(operandList, operationList)}")
    print(f"Day 6 Part 2 Solution: {part2Sol(input)}")

if __name__ == "__main__":
    main()
