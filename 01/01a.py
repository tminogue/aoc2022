from common import deserialize_input_file


def part_1(elf_calorie_counts: list):
    return max(elf_calorie_counts)


def part_2(elf_calorie_counts: list):
    # sort in descending order
    elf_calorie_counts.sort(reverse=True)
    # slice the top 3 vales and return sum
    return sum(elf_calorie_counts[:3])


def count_elf_calories(input_list: list):
    """ """
    elf_calorie_counts = []
    elf_calorie_count = 0
    for log_entry in input_list:
        if log_entry == "":
            elf_calorie_counts.append(elf_calorie_count)
            # reset counter for next elf
            elf_calorie_count = 0
        else:
            elf_calorie_count += int(log_entry)
    return elf_calorie_counts


def main(part: str, input_file_path: str):
    input_list = deserialize_input_file(input_file_path)
    elf_calorie_counts = count_elf_calories(input_list)
    if part == "1":
        part_1(elf_calorie_counts)
    elif part == "2":
        part_2(elf_calorie_counts)
