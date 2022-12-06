from unittest import TestCase as testcase

test_data = [
    ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
    ("nppdvjthqldpwncqszvftbrmjlhg", 6),
    ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
    ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
]

input_file = open("06_input.txt")
datastream = input_file.read()

WINDOW_SIZE = 4


def is_start_of_packet(string_slice: str):
    print(string_slice)
    return len(set(string_slice)) == WINDOW_SIZE


def find_start_marker(datastream: str):
    datastream_length = len(datastream)
    stop_index = datastream_length - WINDOW_SIZE

    # TODO: change to while loop?
    for index in range(datastream_length):
        # don't surpass end of string with window
        if index > stop_index:
            print("Reached end of datastream and found no start of packet marker")
            break

        if is_start_of_packet(datastream[index : index + WINDOW_SIZE]):
            return index + WINDOW_SIZE  # add one to account for zero indexing
        else:
            continue


# for test_data_instance in test_data:
#     testcase.assertEqual(
#         find_start_marker( test_data_instance[0]), test_data_instance[1]
#     )
