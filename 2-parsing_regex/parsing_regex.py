with open("input.txt", "r") as my_file:
    lines = my_file.readlines()

passports, passport, records = [], {}, []

for line in lines:
    if line.strip():
        records.extend(line.split())
    else:
        for record in records:
            key, value = record.split(":")
            passport[key] = value
        passports.append(passport)
        passport, records = {}, []

print(passports)

# \n, []. " ", {}, 0 -> False
