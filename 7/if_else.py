with open("input.txt", "r") as read_file:
    instructions = [line.split() for line in read_file.readlines() if line]


idxs_list = []
idx, accumulator = 0, 0

while idx not in idxs_list:
    idxs_list.append(idx)
    if instructions[idx][0] == "nop":
        idx += 1
    elif instructions[idx][0] == "acc":
        accumulator += int(instructions[idx][1])
        idx += 1
    elif instructions[idx][0] == "jmp":
        idx += int(instructions[idx][1])

print(idx, accumulator)
