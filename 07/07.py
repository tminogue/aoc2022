from common import deserialize_input_file
from collections import defaultdict
import ipdb
from pprint import pprint


# command marker is '$'
# action markers are 'cd' and 'ls'
# contents are directory if 'dir' and file if number
# name of file/directory follows node type


command_output = deserialize_input_file("./test_input.txt")

def compute_directory_sizes(output):
    # dictionary with key as full path name of directory, size
    directory_sizes = defaultdict(int)

    # start at the root
    current_path = "/"
    directory_sizes[current_path] = 0


    for line in output:
        line_parts = line.split()
        # it's a command
        if line.startswith("$"):
            command = line_parts[1]

            if command == "cd":
                dir_reference = line_parts[2]

                if dir_reference == "..":
                    # change reference point
                    # if current_path != "/":
                    current_directory = current_path[:-1].split("/").pop()

                    # first get size of child directory
                    directory_size = directory_sizes[current_path]

                    # update path to parent
                    current_path = current_path[:-len(f"{current_directory}/")]

                    directory_sizes[current_path] += directory_size

                elif dir_reference != "/":
                    # inside new directory
                    current_directory = dir_reference
                    current_path = f"{current_path}{current_directory}/"
                else:
                    continue

            # no op
            elif command == "ls":
                continue
        # it's a directory in current path, noop
        elif line.startswith("dir"):
            continue
        # it's a file, so add
        else:
            file_size = int(line_parts[0])
            # compute size of files in individual directory
            directory_sizes[current_path] += file_size

    return directory_sizes

def part_1():
    directory_sizes = compute_directory_sizes(command_output)
    return sum(size for size in directory_sizes.values() if size < 100000)

def part_2():
    TOTAL_DISK_SIZE = 70000000
    MINIMUM_FREE_SIZE = 30000000

    directory_sizes = compute_directory_sizes(command_output)
    total_used_size = directory_sizes["/"]

    unused_space = TOTAL_DISK_SIZE - total_used_size
    space_to_free = MINIMUM_FREE_SIZE - unused_space
    print(directory_sizes)

    deletion_candidates = defaultdict(int)
    for dir_path, size in directory_sizes.items():
        if size >= space_to_free and dir_path != "/":
            deletion_candidates[dir_path]=size

    return min(deletion_candidates, key=deletion_candidates.get)
