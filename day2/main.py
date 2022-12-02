def part_1():
    match = {
        "A X": 4,
        "A Y": 8,
        "A Z": 3,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 7,
        "C Y": 2,
        "C Z": 6,
    }
    with open("input.txt", "r") as file:
        data = file.read()
        lines = data.split("\n")
        total = 0

        for line in lines:
            total += match[line]
        print(total)


def part_2():
    match = {
        "A X": 3,
        "A Y": 4,
        "A Z": 8,
        "B X": 1,
        "B Y": 5,
        "B Z": 9,
        "C X": 2,
        "C Y": 6,
        "C Z": 7,
    }
    with open("input.txt", "r") as file:
        data = file.read()
        lines = data.split("\n")
        total = 0

        for line in lines:
            total += match[line]
        print(total)


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
