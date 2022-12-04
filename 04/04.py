from common import deserialize_input_file

input_list = deserialize_input_file("./test_input.txt")

def get_range_from_string(range_string: str):
    ''' convert a string in the form of '2-4' to a range of integer values '''
    min_value, max_value = range_string.split("-")
    value_range = range(int(min_value),int(max_value)+1)
    return value_range


def part_1(input_list: list):
    overlap_counter = 0

    for row in input_list:
        range_str_1, range_str_2 = row.split(",")
        range_1 = get_range_from_string(range_str_1)
        #print(*range_1)
        range_2 = get_range_from_string(range_str_2)
        #print(*range_1)
        range_intersect = set(range_1).intersection(range_2)
        # print(range_intersect)
        # print("-"*20)
        intersect_length = len(range_intersect)

        # if the length of either range equals the length of the intersection there is a full overlap
        if intersect_length == len(range_1) or intersect_length == len(range_2):
            overlap_counter+=1

    return overlap_counter


def part_2(input_list: list):
    overlap_counter = 0

    for row in input_list:
        range_str_1, range_str_2 = row.split(",")
        range_1 = get_range_from_string(range_str_1)
        #print(*range_1)
        range_2 = get_range_from_string(range_str_2)
        #print(*range_1)
        range_intersect = set(range_1).intersection(range_2)
        # print(range_intersect)
        # print("-"*20)
        intersect_length = len(range_intersect)

        if intersect_length > 0:
            overlap_counter+=1

    return overlap_counter


