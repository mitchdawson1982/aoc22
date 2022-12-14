def part_1():
    with open("input.txt", "r") as file:
        data = file.read()
        lines = data.split("\n\n")
        summed_list = []

        for line in lines:
            cals = line.split("\n")  # cals is a list of lists
            cals = [int(cal) for cal in cals]  # convert the string to integers
            total = sum(cals)
            summed_list.append(total)  # append total for each elf
        print(max(summed_list))


def part_2():
    with open("input.txt", "r") as file:
        data = file.read()
        lines = data.split("\n\n")
        summed_list = []

        for line in lines:
            cals = line.split("\n")  # cals is a list of lists
            cals = [int(cal) for cal in cals]  # convert the string to integers
            total = sum(cals)
            summed_list.append(total)  # append total for each elf
        summed_list.sort(reverse=True)  # sort
        print(sum(summed_list[0:3]))


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
