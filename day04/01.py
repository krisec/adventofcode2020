expected_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]


def get_inputs(path):
    file = open(path, "r")
    passports = []
    passport = []
    for line in file:
        if line == "\n":
            passports.append(passport)
            passport = []
            #print(len(line))
        else:
            key_value_pairs = line.strip().split(" ")
            for pair in key_value_pairs:
                passport.append(pair.split(":"))
    return passports

def is_valid(passport):
    global expected_fields
    #print(passport)
    num_expected_fields = 0
    num_valid_fields = 0
    for pair in passport:
        key = pair[0]
        value = pair[1]
        if key in expected_fields:
            num_expected_fields += 1
        if key == "byr":
            try:
                val = int(value)
                if val >= 1920 and val <= 2002:
                    num_valid_fields += 1
                else:
                    return False
            except:
                return False
        elif key == "iyr":
            try:
                val = int(value)
                if val >= 2010 and val <= 2020:
                    num_valid_fields += 1
                else:
                    return False
            except:
                return False
        elif key == "eyr":
            try:
                val = int(value)
                if val >= 2020 and val <= 2030:
                    num_valid_fields += 1
                else:
                    return False
            except:
                return False
        elif key == "hgt":
            try:
                val = int(value[:-2])
                if value[-2:] == "in":
                    if val >= 59 and val <= 76:
                        num_valid_fields += 1
                    else:
                        return False
                elif value[-2:] == "cm":
                    if val >= 150 and val <= 193:
                        num_valid_fields += 1
                    else:
                        return False
                else:
                    return False
            except:
                return False
        elif key == "hcl":
            if len(value) > 7:
                return False
            if value[0] != "#":
                return False
            for c in value[1:]:
                if not c in "0123456789abcdef":
                    return False
            num_valid_fields += 1
        elif key == "ecl":
            if not value in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                return False
            num_valid_fields += 1
        elif key == "pid":
            if len(value) != 9:
                return False
            try:
                val = int(value)
                num_valid_fields += 1
            except:
                return False
        
                
    return num_expected_fields == len(expected_fields) \
        and num_valid_fields == len(expected_fields)


valid_passports = 0
passports = get_inputs("input.txt")
print(len(passports))
for passport in passports:
    if is_valid(passport):
        valid_passports += 1

print(valid_passports)

