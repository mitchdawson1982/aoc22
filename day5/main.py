data_map = {
    1: ["D", "M", "S", "Z", "R", "F", "W", "N"],
    2: ["W", "P", "Q", "G", "S"],
    3: ["W", "R", "V", "Q", "F", "N", "J", "C"],
    4: ["F", "Z", "P", "C", "G", "D", "L"],
    5: ["T", "P", "S"],
    6: ["H", "D", "F", "W", "R", "L"],
    7: ["Z", "N", "D", "C"],
    8: ["W", "N", "R", "F", "V", "S", "J", "Q"],
    9: ["R", "M", "S", "G", "Z", "W", "V"],
}


def part_1():
    with open("input.txt", "r") as file:
        data = file.read()
    lines = data.split("\n")
    for line in lines:
        values = line.split(" ")
        moves = int(values[1])
        from_stack = int(values[3])
        to_stack = int(values[5])

        count = 0
        while count < moves:
            val = data_map[from_stack].pop()
            data_map[to_stack].append(val)
            count += 1

    # print(data_map)
    output = []
    keys = data_map.keys()
    for key in keys:
        output.append(data_map[key].pop())
    print(output)


def part_2():
    with open("input.txt", "r") as file:
        data = file.read()
    lines = data.split("\n")
    for line in lines:
        values = line.split(" ")
        moves = int(values[1])
        from_stack = int(values[3])
        to_stack = int(values[5])

        # print(data_map[from_stack])
        # print(moves)
        new = data_map[from_stack][-moves:]
        # print(new)
        data_map[from_stack] = data_map[from_stack][:-moves]
        data_map[to_stack].extend(new)
        # print(data_map[from_stack])

        # for n in new:
        #     data_map[from_stack].remove(n)
        #     data_map[to_stack].append(n)

    # print(data_map)
    output = []
    keys = data_map.keys()
    for key in keys:
        output.append(data_map[key].pop())
    print(output)


def main():
    # part_1()
    part_2()


if __name__ == "__main__":
    main()
