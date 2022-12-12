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

    cycle_results = defaultdict(int)

    for line in input_list:
        x_before = x
        split_command = line.split()
        command = split_command[0]

        step_count += 1

        if command == "noop":
            processing_cycle_count += 1

        if command == "addx":
            processing_cycle_count += 2
            x_after = x + int(split_command[1])

        cycle_results[processing_cycle_count] = x_after

    return cycle_results


def get_beginning_cycle_signal_strength(sample_cycle_value, cycle_results):
    previous_cycle_index = sample_cycle_value - 1
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
        signal_strength = get_beginning_cycle_signal_strength(
            sample_index, cycle_results
        )
        # print(sample_index, signal_strength)
        total_signal_strength += signal_strength

    return total_signal_strength


def process_crt_inputs(input_list):
    step_count = 0
    processing_cycle_count = 0

    x = 1
    cycle_results = defaultdict(int)

    for line in input_list:

        split_command = line.split()
        command = split_command[0]
        step_count += 1

        if command == "noop":
            processing_cycle_count += 1

        if command == "addx":
            processing_cycle_count += 2
            x += int(split_command[1])

        cycle_results[processing_cycle_count] = x

    return cycle_results


def get_position_value(cycle_value, cycle_results, current_sprite_start):
    # only shift on discrete processing steps
    if cycle_value in cycle_results.keys():
        return cycle_results[cycle_value] - 1
    else:
        return current_sprite_start


def part_2(input_list):
    CRT_WIDTH = 40
    CRT_HEIGHT = 6
    SPRITE_WIDTH = 3

    crt_inputs = process_crt_inputs(input_list)
    sprite_positions = list(range(SPRITE_WIDTH))
    step = 1

    for j in range(CRT_HEIGHT):
        # process one crt row, start sprite in initial position
        crt_row = []

        for i in range(CRT_WIDTH):
            if i in sprite_positions:
                crt_row.append("#")
            else:
                crt_row.append(".")

            # process cycle key is row number * character position
            position = get_position_value(step, crt_inputs, sprite_positions[0])
            sprite_positions = [position + index for index in range(SPRITE_WIDTH)]
            step += 1

            # if j >= 0:
            #     print(
            #         f"row: {j}, pos: {i}, cycle: {step}, position: {position}, sprite: {sprite_positions}"
            #     )

        print("".join(crt_row))
