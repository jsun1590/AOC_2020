import string

with open("input.txt") as file:
    passports = [i.strip() for i in file.read().split("\n\n")]

fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

def part_1():
    output = 0
    for passport in passports:
        passport_dict = dict([i.split(":") for i in passport.split()])
        check = 0

        if all(i in passport for i in fields):
            output += 1
            
    return output

def part_2():
    output = 0
    colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    
    for passport in passports:
        passport_dict = dict([i.split(":") for i in passport.split()])
        check = 0

        if all(i in passport for i in fields):
            for key, val in zip(passport_dict.keys(), passport_dict.values()):
                if key == "byr" and 1920 <= int(val) <= 2002:
                    check += 1

                elif key == "iyr" and 2010 <= int(val) <= 2020:
                    check += 1
                    
                elif key == "eyr" and 2020 <= int(val) <= 2030:
                    check += 1
                    
                elif key == "hgt":
                    if(val[-2:] == "in"):
                        if 59 <= int(val.strip("in")) <= 76:
                            check+=1
                                
                    if(val[-2:] == "cm"):
                        if 150 <= int(val.strip("cm")) <= 193:
                            check+=1
                  
                elif key == "hcl" and val[0] == "#" and len(val) == 7 and all(i in string.hexdigits for i in val.strip("#")):
                    check+=1

                elif key == "ecl" and val in colors:
                    check += 1
                        
                elif key == "pid" and len(val) == 9 and val.isnumeric():
                    check += 1

                if check == 7:
                    output+=1
                    break
    return output

print("part 1:", part_1())
print("part 2:", part_2())
