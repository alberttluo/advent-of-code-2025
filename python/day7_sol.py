from argparse import ArgumentParser
from functools import lru_cache
from typing import final
from collections import deque


TEST = "../inputs/day7_smallinput.txt"
FILE = "../inputs/day7_input.txt"

class TreeNode:
    def __init__(self, data: int):
        self.data: int | None = data
        self.left: TreeNode | None = None
        self.right: TreeNode | None = None

def makeTree(columns: list[tuple[str]], initCol: int, sol2: bool) -> TreeNode:
    root: TreeNode = TreeNode(0)
    dummyRoot: TreeNode = root
    initDepth: int = 0
    usedSplitters: dict[tuple[int, int], TreeNode] = dict()
    usedSplitters[(initCol, initDepth)] = root
    
    try:
        initDepth = columns[initCol].index('^')
    except ValueError:
        return root

    makeTreeHelper(columns, dummyRoot, initDepth, initCol, usedSplitters, sol2)

    return dummyRoot

def makeTreeHelper(columns: list[tuple[str]], node: TreeNode, currDepth: int, currInd: int, usedSplitters: dict[tuple[int, int], TreeNode], sol2: bool) -> None:
    if (node is None or currInd < 0 or currInd >= len(columns)):
        return

    lColInd: int = currInd - 1
    rColInd: int = currInd + 1

    lCol: tuple[str] = () if lColInd < 0 else columns[currInd - 1][currDepth + 1:]
    rCol: tuple[str] = () if rColInd >= len(columns) else columns[currInd + 1][currDepth + 1:]

    lColDepth: int = -1 if '^' not in lCol else lCol.index('^') + currDepth + 1
    rColDepth: int = -1 if '^' not in rCol else rCol.index('^') + currDepth + 1

    leftNew: bool = False
    rightNew: bool = False

    if (lColDepth == -1):
        node.left = None
    else:
        key: tuple[int, int] = (lColInd, lColDepth)
        if (key in usedSplitters):
            node.left = usedSplitters[key] if sol2 else None
        else:
            child: TreeNode = TreeNode(0)
            node.left = child
            usedSplitters[key] = child
            leftNew = True
                
    if (rColDepth == -1):
        node.right = None
    else:
        key: tuple[int, int] = (rColInd, rColDepth)
        if (key in usedSplitters):
            node.right = usedSplitters[key] if sol2 else None
        else:
            child: TreeNode = TreeNode(0)
            node.right = child
            usedSplitters[key] = child
            rightNew = True

    if (leftNew):
        makeTreeHelper(columns, node.left, lColDepth, lColInd, usedSplitters, sol2)
    if (rightNew):
        makeTreeHelper(columns, node.right, rColDepth, rColInd, usedSplitters, sol2)

def getNumNodes(root: TreeNode) -> int:
    if (root is None):
        return 0

    return 1 + getNumNodes(root.left) + getNumNodes(root.right)

State = tuple[int, int] # (colIndex, depthIndex)
def findChild(columns: list[tuple[str]], col: int, depth: int, dir: int) -> State | None:
    newCol: int = col + dir

    if (newCol < 0 or newCol >= len(columns)):
        return None

    colVals: tuple[str] = columns[newCol]
    start: int = depth + 1

    if (start >= len(colVals)):
        return None

    try:
        relativeIndex: int = colVals[start:].index('^')
    except ValueError:
        return None

    newDepth: int = start + relativeIndex

    return (newCol, newDepth)

def part1Sol(root: TreeNode) -> int:
    return getNumNodes(root)

def part2Sol(input) -> int:
    with open(input, 'r') as f:
        lines = f.read().splitlines()
        width: int = len(lines[0])
        center: int = width // 2

        splits: int = 0
        timelines = [0] * width
        timelines[center] = 1

        y: int = 0
        for row in lines[2::2]:
            start: int = center - y
            end: int = center + y + 1

            for x in range(start, end, 2):
                count = timelines[x]
                
                if (count > 0 and row[x] == '^'):
                    splits += 1
                    timelines[x] = 0
                    timelines[x - 1] += count
                    timelines[x + 1] += count

            y += 1

        return sum(timelines)

def main():
    parser = ArgumentParser()
    _ = parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    input = TEST if args.test else FILE

    grid: list[list[str]] = []

    with open(input, "r") as f:
        lines = f.readlines()

        for line in lines:
            grid.append(list(line.strip()))

    columns: list[tuple[str]] = list(zip(*grid))
    initCol: int = grid[0].index('S')

    root: TreeNode = makeTree(columns, initCol, False)

    print(f"Day 7 Part 1 Solution: {part1Sol(root)}")
    print(f"Day 7 Part 2 Solution: {part2Sol(input)}")

if __name__ == "__main__":
    main()
