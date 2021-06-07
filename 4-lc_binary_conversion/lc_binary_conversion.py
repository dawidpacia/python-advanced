with open("input.txt", "r") as read_file:
    lines = read_file.readlines()

seats = [line.strip() for line in lines]
seats_ids = []

for seat in seats:
    row = seat[:7].replace("B", "1").replace("F", "0")
    row_int = int(row, 2)
    column = seat[-3:].replace("R", "1").replace("L", "0")
    column_int = int(column, 2)
    seat_id = row_int * 8 + column_int
    seats_ids.append(seat_id)

print(max(seats_ids))
