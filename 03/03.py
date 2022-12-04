import string
from common import deserialize_input_file

item_list = deserialize_input_file("./test_input.txt")

letter_values = {}
lower_alphabet = string.ascii_lowercase
upper_alphabet = string.ascii_uppercase

for index, letter in enumerate(lower_alphabet + upper_alphabet):
    letter_values[letter] = index + 1


def part_1(item_list):
    priority_total = 0
    for row in item_list:
        compartment_width = int(len(row) / 2)
        compartment_1_content, compartment_2_content = (
            row[:compartment_width],
            row[compartment_width:],
        )
        duplicate_item = set(compartment_1_content).intersection(
            set(compartment_2_content)
        )
        priority_total += letter_values[duplicate_item.pop()]
    return priority_total


def part_2(item_list):
    priority_total = 0
    group_list = []
    for index, row in enumerate(item_list):
        group_list.append(set(row))
        if len(group_list) == 3:
            # intersection of first set with remaining sets yields duplicate(s)
            duplicate_item = group_list[0].intersection(*group_list)
            # pop will also flush
            priority_total += letter_values[duplicate_item.pop()]
            # flush the group
            group_list = []
    return priority_total
