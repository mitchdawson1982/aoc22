def part_1():
    with open("input.txt", "r") as file:
        text = file.read()
    rows = text.splitlines()

    trees_visible = 0

    for row_index, row in enumerate(rows):
        last_row_index = len(rows) - 1
        if row_index == 0 or row_index == last_row_index:
            continue

        numbers = [int(number) for number in row]
        last_number_index = len(numbers) - 1
        for number_index, number in enumerate(numbers):
            if number_index == 0 or number_index == last_number_index:
                continue

            while True:
                # Calculate numbers to the left of number_index
                if number > max(numbers[:number_index]):
                    trees_visible += 1
                    break

                # Calculate numbers to the right of number_index
                if number > max(numbers[number_index + 1 :]):
                    trees_visible += 1
                    break

                # Calculate rows above
                numbers_in_above_rows = [
                    int(row_above[number_index]) for row_above in rows[:row_index]
                ]
                if number > max(numbers_in_above_rows):
                    trees_visible += 1
                    break

                # Calculate rows below
                numbers_in_below_rows = [
                    int(row_below[number_index]) for row_below in rows[row_index + 1 :]
                ]
                if number > max(numbers_in_below_rows):
                    trees_visible += 1
                break

    perimeter = (len(rows[0]) - 1) * 4
    print(
        f"Sum: {trees_visible + perimeter}",
    )


def part_2():
    with open("input.txt", "r") as file:
        text = file.read()
    rows = text.splitlines()

    totals = []

    for row_index, row in enumerate(rows):
        last_row_index = len(rows) - 1
        if row_index == 0 or row_index == last_row_index:
            continue

        numbers = [int(number) for number in row]
        last_number_index = len(numbers) - 1
        for number_index, number in enumerate(numbers):
            if number_index == 0 or number_index == last_number_index:
                continue

            # Calculate numbers left
            left_count = 0
            left_numbers = numbers[:number_index]
            left_numbers.reverse()
            print(f"Left {left_numbers}")
            for i in left_numbers:
                if number > i:
                    left_count += 1
                else:
                    left_count += 1
                    break

            # Calculate numbers right
            right_count = 0
            for i in numbers[number_index + 1 :]:
                if number > i:
                    right_count += 1
                else:
                    right_count += 1
                    break

            # Calculate rows above
            above_rows = rows[:row_index]
            above_rows.reverse()
            numbers_in_above_rows = [
                int(row_above[number_index]) for row_above in above_rows
            ]

            above_count = 0
            for i in numbers_in_above_rows:
                if number > i:
                    above_count += 1
                else:
                    above_count += 1
                    break

            # Calculate rows below
            numbers_in_below_rows = [
                int(row_below[number_index]) for row_below in rows[row_index + 1 :]
            ]

            below_count = 0
            for i in numbers_in_below_rows:
                if number > i:
                    below_count += 1
                else:
                    below_count += 1
                    break

            total = left_count * right_count * above_count * below_count
            totals.append(total)

    print(max(totals))


def main():
    part_1()
    part_2()


if __name__ == "__main__":
    main()
