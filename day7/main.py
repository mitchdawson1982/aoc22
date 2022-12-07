from collections import defaultdict
import random


pwd = []
dir_sizes = defaultdict(int)


def part_1():
    with open("input.txt", "r") as file:
        text = file.read()

    for line in text.splitlines():

        if line.startswith("$ cd .."):
            if pwd:
                pwd.pop()

        elif line.startswith("$ cd "):
            if line.split("$ cd ")[1] not in dir_sizes:
                pwd.append(line.split("$ cd ")[1])

            else:
                d = line.split("$ cd ")[1] + str(random.randint(1, 100000))
                pwd.append(d)

        elif line.startswith("$ ls"):
            continue

        elif line.split(" ")[0].isnumeric():
            for p in pwd:
                dir_sizes[p] += int(line.split(" ")[0])

    print(f"Part One Result = {sum(d for d in dir_sizes.values() if d <= 100000)}")

    # Part 2
    need = 30000000 - (70000000 - dir_sizes["/"])
    print(f"Part Two Result = {min(d for d in dir_sizes.values() if d > need)}")


def main():
    part_1()


if __name__ == "__main__":
    main()
