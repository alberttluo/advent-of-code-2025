import math
from argparse import ArgumentParser

TEST = "../inputs/day8_smallinput.txt"
FILE = "../inputs/day8_input.txt"

def part1Sol(numCoords: int, distList: list[tuple[int, int, int, int, int]]) -> int:
    circuits: dict[int, list[int]] = {
        x + 1: [x + 1] for x in range(numCoords)
    }

    def findRoot(v: int) -> int:
        first = circuits[v][0]
        return -first if first < 0 else first

    for i in range(1000):
        _, ind1, ind2, _, _ = distList[i]
        root1: int = findRoot(ind1)
        root2: int = findRoot(ind2)

        if (root1 == root2):
            continue

        # Union by size.
        if (len(circuits[root1]) < len(circuits[root2])):
            root1, root2 = root2, root1

        members2: list[int] = circuits[root2][:]
        for node in members2:
            circuits[node] = [-root1]
        circuits[root1].extend(members2)
        circuits[root2] = [-root1]

    compSizes: list[int] = []
    for v, lst in circuits.items():
        # v is a root.
        if (lst[0] >= 0 and v == lst[0]):
            compSizes.append(len(lst))

    sortedLens = sorted(compSizes, reverse = True)
    return sortedLens[0] * sortedLens[1] * sortedLens[2]

def part2Sol(numCoords: int, distList: list[tuple[int, int, int, int, int]]) -> int:
    circuits: dict[int, list[int]] = {
        x + 1: [x + 1] for x in range(numCoords)
    }

    def findRoot(v: int) -> int:
        first = circuits[v][0]
        return -first if first < 0 else first

    for i in range(len(distList)):
        _, ind1, ind2, x1, x2 = distList[i]
        root1: int = findRoot(ind1)
        root2: int = findRoot(ind2)

        if (root1 == root2):
            continue

        # Union by size.
        if (len(circuits[root1]) < len(circuits[root2])):
            root1, root2 = root2, root1

        members2: list[int] = circuits[root2][:]
        for node in members2:
            circuits[node] = [-root1]
        circuits[root1].extend(members2)
        circuits[root2] = [-root1]
        if (len(circuits[root1]) == numCoords):
            return x1 * x2

    return 0

def dist(coord1: tuple[int, int, int], coord2: tuple[int, int, int]) -> int:
    return (coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2 + (coord1[2] - coord2[2]) ** 2

def main():
    parser = ArgumentParser()
    parser.add_argument('--test', action='store_true')
    args = parser.parse_args()

    input = TEST if args.test else FILE
    coords: list[tuple[int, int, int]] = []

    with open(input, 'r') as f:
        lines = f.readlines()

        for line in lines:
            filtered: list[int] = [int(x.strip()) for x in line.split(',')]
            coords.append(tuple(filtered))

    numCoords: int = len(coords)

    distList: list[tuple[int, int, int, int, int]] = []

    for i, coord1 in enumerate(coords):
        for j, coord2 in enumerate(coords[i + 1:], start = i + 1):
            distList.append((dist(coord1, coord2), i + 1, j + 1, coord1[0], coord2[0]))

    distList = sorted(distList)

    print(f"Day 8 Part 1 Solution: {part1Sol(numCoords, distList)}")
    print(f"Day 8 Part 2 Solution: {part2Sol(numCoords, distList)}")

if __name__ == "__main__":
    main()
