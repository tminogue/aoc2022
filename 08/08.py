from common import deserialize_input_file
import numpy as np

tree_list = deserialize_input_file("./test_input.txt")


def create_tree_grid(tree_list):
    # initialize array
    tree_array = np.zeros((len(tree_list), len(tree_list[0])), dtype=int)
    # read in values to array
    for idx, row in enumerate(tree_list):
        tree_array[idx, :] = np.array(list(row))
    return tree_array


def find_visible_tree_count(tree_array):
    # edge trees are all visible, don't double count corners
    edge_trees = 2 * (len(tree_list[0]) + (len(tree_list) - 2))

    # count interior trees
    visible_interior_trees = 0

    # start with second tree (index is 1)
    for x in range(1, tree_array.shape[0] - 1):
        for y in range(1, tree_array.shape[1] - 1):
            tree_height = tree_array[x, y]
            # one dimensional array for both row and column of current tree at (x,y)
            row = tree_array[x, :]
            column = tree_array[:, y]

            is_visible_from_left = max(row[:y]) < tree_height
            is_visible_from_right = max(row[y + 1 :]) < tree_height
            is_visible_from_top = max(column[:x]) < tree_height
            is_visible_from_bottom = max(column[x + 1 :]) < tree_height

            is_visible = (
                is_visible_from_left
                | is_visible_from_right
                | is_visible_from_top
                | is_visible_from_bottom
            )

            if is_visible:
                visible_interior_trees += 1

    return edge_trees + visible_interior_trees


def find_max_scenic_score(tree_array):

    max_scenic_score = 0

    for x in range(0, tree_array.shape[0]):
        for y in range(0, tree_array.shape[1]):
            tree_height = tree_array[x, y]
            # one dimensional array for both row and column of current tree at (x,y)
            row = tree_array[x, :]
            column = tree_array[:, y]

            # need to reverse order of array of adjacents when looking left and up to top
            distance_to_left = compute_directional_distance(tree_height, row[:y][::-1]) # reversed
            distance_to_right = compute_directional_distance(tree_height, row[y + 1 :])
            distance_to_top = compute_directional_distance(tree_height, column[:x][::-1]) # reversed
            distance_to_bottom = compute_directional_distance(tree_height, column[x + 1 :])


            tree_scenic_score = (
                distance_to_left
                * distance_to_right
                * distance_to_top
                * distance_to_bottom
            )

            if tree_scenic_score > max_scenic_score:
                max_scenic_score = tree_scenic_score

    return max_scenic_score

def compute_directional_distance(tree_height, adjacent_trees):
    # if no adjacent trees (edge) then distance is zero
    if not adjacent_trees.any():
        return 0
    else:
        # if not the edge then at least one is visible
        visible_distance = 1
        # check up to edge only since if all other visible trees
        for i in range(0, len(adjacent_trees) - 1 ):
            if tree_height > adjacent_trees[i]:
                visible_distance += 1
            else:
                return visible_distance
        return visible_distance


def part_1(tree_list):
    trees = create_tree_grid(tree_list)
    print(find_visible_tree_count(trees))



def part_2(tree_list):
    trees = create_tree_grid(tree_list)
    print(find_max_scenic_score(trees))