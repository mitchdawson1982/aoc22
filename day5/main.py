def part_1():
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

    output = []
    keys = data_map.keys()
    for key in keys:
        output.append(data_map[key].pop())
    print("".join(output))


def part_2():
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
    with open("input.txt", "r") as file:
        data = file.read()
    lines = data.split("\n")
    for line in lines:
        values = line.split(" ")
        moves = int(values[1])
        from_stack = int(values[3])
        to_stack = int(values[5])

        new = data_map[from_stack][-moves:]
        data_map[from_stack] = data_map[from_stack][:-moves]
        data_map[to_stack].extend(new)

    output = []
    keys = data_map.keys()
    for key in keys:
        output.append(data_map[key].pop())
    print("".join(output))


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
