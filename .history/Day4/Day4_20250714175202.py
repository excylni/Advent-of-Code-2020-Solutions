with open('Passports.txt', 'r') as file:
    data = file.read()
    data = data.split('\n\n')
    
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

valid_passports = 0
passports = []


for i in data:
    if all(j in i for j in fields):
        valid_passports += 1
        clean_passportdata = i.replace("\n", " ")
        pass_dict = {}

        for field in clean_passportdata.split():
            key, value = field.split(":")
            pass_dict[key] = value

        passports.append(pass_dict)


# Making a dictionary

print(valid_passports)

eye_color = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

# Validations:


def valid(passport):
    byr = passport.get("byr")
    iyr = passport.get("iyr")
    eyr = passport.get("eyr")
    hgt = passport.get("hgt")
    hcl = passport.get("hcl")
    ecl = passport.get("ecl")
    pid = passport.get("pid")

    if not (len(byr) == 4 and 1920 <= int(byr) <= 2002):
        return False
    if not (len(iyr) == 4 and 2010 <= int(iyr) <= 2020):
        return False
    if not (len(eyr) == 4 and 2020 <= int(eyr) <= 2030):
        return False
    if "cm" in hgt:
        num = hgt[:-2]
        if not 150 <= int(num) <= 193:
            return False
    elif "in" in hgt:
        num = hgt[:-2]
        if not 59 <= int(num) <= 76:
            return False
    else:
        return False
    if not ("#" in hcl and len(hcl) == 7):
        return False
    if ecl not in eye_color:
        return False
    if not len(pid) == 9:
        return False
    return True

# Part 2
right_passports = 0

for passport in passports:
    if valid(passport):
        right_passports+=1
    
print(right_passports)