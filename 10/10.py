from common import deserialize_input_file
from collections import defaultdict




input_list = deserialize_input_file("./test_input.txt")
# input_strings= f"noop\naddx 3\naddx -5"

START_INDEX = 20
SAMPLE_INTERVAL = 40


def process_inputs(input_list):
    step_count = 0
    processing_cycle_count = 0
    x = 1

    cycle_results =  defaultdict(int)

    for line in input_list:
        x_before = x
        split_command = line.split()
        command = split_command[0]

        step_count += 1

        if command == "noop":
            processing_cycle_count += 1

        if command == "addx":
            processing_cycle_count += 2
            x_after = x+ int(split_command[1])

        cycle_results[processing_cycle_count]=x_after

    return cycle_results


def get_previous_cycle_index(cycle_index, cycle_results):
    # if cycle_index not in cycle_results.keys():
    #     # decrement one since steps are two maximum
    #     cycle_index -= cycle_index
    # else:
    #     # decrement again to find previous (-2 case)
    #     cycle_index = get_previous_cycle_index(cycle_index-1, cycle_results)
    return cycle_index -1

def get_beginning_cycle_signal_strength(sample_cycle_value, cycle_results):
    previous_cycle_index = sample_cycle_value -1
    if previous_cycle_index not in cycle_results.keys():
        # would need to change to recersive if max step is > 2
        previous_cycle_index -= 1

    signal_strength = sample_cycle_value * cycle_results[previous_cycle_index]
    # print(sample_cycle_value, previous_cycle_index, signal_strength)
    return signal_strength

def part_1(input_list):
    cycle_results = process_inputs(input_list)
    total_signal_strength = 0

    index_list = []
    index = START_INDEX
    # need to iterate through max key value, not length
    while index < max(cycle_results.keys()):
        index_list.append(index)
        index += SAMPLE_INTERVAL

    for sample_index in index_list:
        signal_strength = get_beginning_cycle_signal_strength(sample_index, cycle_results)
        # print(sample_index, signal_strength)
        total_signal_strength += signal_strength

    return total_signal_strength



