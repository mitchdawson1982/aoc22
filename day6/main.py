def part_1():
    with open("input.txt", "r") as file:
        data = file.read()
    chars = list()
    for index, d in enumerate(data):
        chars.append(d)
        if len(set(chars[-4:])) == 4:
            print(index + 1)
            break


def part_2():
    with open("input.txt", "r") as file:
        data = file.read()
    chars = list()
    for index, d in enumerate(data):
        chars.append(d)
        if len(set(chars[-14:])) == 14:
            print(index + 1)
            break


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
