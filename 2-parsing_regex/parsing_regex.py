# []. " ", {}, 0, None -> False
import re


def read_input() -> list:
    with open("input.txt", "r") as my_file:
        lines = my_file.readlines()

    passports, passport, records = [], {}, []

    for line in lines:
        if line.strip():
            records.extend(line.split())
        else:
            for record in records:
                key, record_value = record.split(":")
                passport[key] = record_value
            passports.append(passport)
            passport, records = {}, []
    return passports


passports = read_input()

mandatory_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
optional_fields = ["cid"]

invalid_passport = 0
for passport in passports:
    for field in mandatory_fields:
        if field not in passport:
            invalid_passport += 1
            break

print(len(passports) - invalid_passport)


def byr(year):
    min_year, max_year = 1920, 2002
    try:
        if min_year <= int(year) <= max_year:
            return True
    except ValueError:
        return False
    return False


def iyr(year):
    min_year, max_year = 2010, 2020
    try:
        if min_year <= int(year) <= max_year:
            return True
    except ValueError:
        return False
    return False


def eyr(year):
    min_year, max_year = 2020, 2030
    try:
        if min_year <= int(year) <= max_year:
            return True
    except ValueError:
        return False
    return False


def hgt(height):
    height_value, unit = int(height[:-2]), height[-2:]
    min_cm, max_cm, min_in, max_in = 150, 193, 59, 76
    try:
        if unit == "cm" and min_cm <= height_value <= max_cm:
            return True
        elif unit == "in" and min_in <= height_value <= max_in:
            return True
    except ValueError:
        return False
    return False


def hcl(color):
    return bool(re.search("[0-9a-f]{6}", color))


def ecl(color):
    return bool(color in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"})


def pid(pass_id):
    return bool(re.search("[0-9]{9}", pass_id))


def cid(c_id):
    return bool(c_id)


invalid_passport = 0
for passport in passports:
    for field_name, field_value in passport.items():
        if not locals()[field_name](field_value):
            invalid_passport += 1
            break
