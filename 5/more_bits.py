def read_input():
    with open("input (2).txt", "r") as read_file:
        lines = read_file.readlines()

    instructions = []

    for line in lines:
        instructions.append(line.strip().replace(" ", "").split("="))

    return instructions


hidden_bit = "X"
end_value = 0
mask = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X"
mask_for_zeros = int(mask.replace(hidden_bit, "0"), 2)
mask_for_ones = int(mask.replace(hidden_bit, "1"), 2)


instructions = read_input()

mask = 0
registers = {}
for instruction in instructions:
    if "mask" in instruction[0]:
        mask = instruction[1]
        mask_for_zeros = int(mask.replace(hidden_bit, "0"), 2)
        mask_for_ones = int(mask.replace(hidden_bit, "1"), 2)
    else:
        mask_val = int(instruction[1])
        end_result = (mask_val | mask_for_zeros) & mask_for_ones
