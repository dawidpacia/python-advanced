import logging
import os


def read_input(filename):
    input_path = os.path.abspath(os.path.join(os.path.dirname(__file__), filename))

    with open(input_path, "r") as read_file:
        tree_map = [line.strip() for line in read_file.readlines()]
    return tree_map


def count_trees(tree_map, step_x, step_y):
    x_len, y_len = len(tree_map[0]), len(tree_map)
    pointer_x = 0
    num_of_trees = 0

    for pointer_y in range(0, y_len, step_y):
        if tree_map[pointer_y][pointer_x % x_len] == "#":
            num_of_trees += 1
        pointer_x += step_x

    return num_of_trees


message_format = "%(asctime)s: %(message)s"
logging.basicConfig(format=message_format, level=logging.DEBUG, datefmt="%H:%M:%S")


tree_map = read_input("input.txt")
move_schema = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees_result = 1

for step in move_schema:
    trees_result *= count_trees(tree_map, *step)

logging.info(f"Total number of trees {trees_result}")
