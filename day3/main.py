def part_1():
    priorities = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52
    }
    half = 0
    total = 0

    with open("input.txt", "r") as file:
        data = file.read()
        lines = data.split("\n")
    
    for line in lines:
        half = int(len(line)/2)
        first_compartment = line[0:half]
        second_compartment = line[half:half*2]
        print(first_compartment)
        print(second_compartment)

        dedup_first_compartment = "".join(set(first_compartment))
        dedup_second_comparment = "".join(set(second_compartment))
        print(dedup_first_compartment)
        print(dedup_second_comparment)

        for item in dedup_first_compartment:
            if item in dedup_second_comparment:
                total += priorities[item]
                print(item)
                print(priorities[item])
                print(total)

def part_2():
    priorities = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26,
        "A": 27,
        "B": 28,
        "C": 29,
        "D": 30,
        "E": 31,
        "F": 32,
        "G": 33,
        "H": 34,
        "I": 35,
        "J": 36,
        "K": 37,
        "L": 38,
        "M": 39,
        "N": 40,
        "O": 41,
        "P": 42,
        "Q": 43,
        "R": 44,
        "S": 45,
        "T": 46,
        "U": 47,
        "V": 48,
        "W": 49,
        "X": 50,
        "Y": 51,
        "Z": 52
    }
    group_size = 3
    count = 0
    badge_total = 0

    with open("input.txt", "r") as file:
        data = file.read()
        lines = data.split("\n")
        number_of_lines = len(lines)
        number_of_groups = int(number_of_lines/group_size)
    
    for group in lines[0:number_of_groups]:
        count = count + group_size
        nth_group = lines[(count - group_size):count]
        badge = ''.join(sorted(set.intersection(*map(set,nth_group))))
        badge_total += priorities[badge]
        print(badge_total)

def main():
    part_1()
    part_2()

if __name__ == "__main__":
    main()
