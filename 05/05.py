from common import deserialize_input_file
import re

# input_list = deserialize_input_file("./test_input.txt")
input_list = deserialize_input_file("./05_input.txt")

input_divider_index = input_list.index("")
map_values = input_list[:input_divider_index]
move_values = input_list[input_divider_index + 1 :]


def build_map(map_list):
    """
    Build a dictionary of stack locations and lists of crates.
    Crate lists are order from top of stack to bottom
    """
    stack_row = map_values[-1]
    stack_keys = stack_row.split()
    # initialize map with empty lists
    stack_map = dict()
    for key in stack_keys:
        stack_map[key] = []

    # fill lists with crate values appearing in top-to-bottom order in each stack list
    for row in map_values[:-1]:
        for key in stack_keys:
            # crate value is determined by its key location in string
            crate = row[stack_row.index(key)]
            if crate != " ":
                stack_map[key].append(crate)

    return stack_map


def build_moves(moves_list: list):
    moves = []
    regex_pattern = (
        "^move (?P<quantity>\d+) from (?P<from_stack>\d+) to (?P<to_stack>\d+)$"
    )

    for move in moves_list:
        match = re.match(regex_pattern, move)
        moves.append(
            (
                int(match["quantity"]),
                match["from_stack"],
                match["to_stack"],
            )
        )

    return moves


def move_crates(moves: list, reverse: bool):

    crate_map = build_map(map_values)
    # print(crate_map)

    for move in moves:
        # print(move)

        quantity, from_stack, to_stack = move[0], move[1], move[2]
        # don't leave a None value when stack is depleted, instead replace with empty list
        if not crate_map[from_stack]:
            crate_map[from_stack] = []

        # remove crates from beginning (top) of list - "one at a time" for part 1, as a stack for part 2
        # for part 1 reverse the list because the topmost crate is the first moved to the new stack, and the others
        # follow with the bottom-most crate removed from the "from" stack becoming the topmost crate on the "to" stack
        crates_to_move = crate_map[from_stack][:quantity]
        if reverse:
            crates_to_move.reverse()
        crate_map[from_stack] = crate_map[from_stack][quantity:]
        # add crates to beginning (top) of list
        crates_to_move.extend(crate_map[to_stack])
        crate_map[to_stack] = crates_to_move
        # print(crate_map)
        # print("-"*40)
    return crate_map


def solve(move_values: list, problem_part: int):

    reverse_crates = problem_part == 1
    moves = build_moves(move_values)

    final_crate_map = move_crates(moves, reverse_crates)

    top_crates_list = [(final_crate_map[k][0]) for k in final_crate_map.keys()]

    return "".join(top_crates_list)

