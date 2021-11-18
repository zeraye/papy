import sys
import re
import random

with open(sys.argv[1], "r") as file:
    source = file.readlines()

code = {}

i = 0

for arg in source:
    row = arg.split()

    if len(row) == 1:
        code[i] = ["", row[0], ""]
    elif len(row) == 2:
        code[i] = ["", row[0], row[1]]
    elif len(row) == 3:
        code[i] = [row[0], row[1], row[2]]
    else:
        continue

    i += 1

memory = {}
registers = {str(i):random.randint(-2**31, 2**31-1) for i in range(16)}

def num_from_val(value):
    return int("".join(re.findall("[\d]", value)))

def addr_from_val(value):
    return "".join(re.findall("[A-Z]", value))

n = 0

while n < len(code):
    line = code[n]
    
    if line[1] == "DC":
        memory[line[0]] = num_from_val(line[2])
    elif line[1] == "DS":
        if line[2] == "INTEGER":
            memory[line[0]] = 0
        else:
            memory[line[0]] = [random.randint(-99, 99) for i in range(num_from_val(line[2]))]
    elif line[1] == "L":
        reg, mem = line[2].split(",")
        registers[reg] = memory[mem]
    elif line[1] == "LR":
        reg1, reg2 = line[2].split(",")
        registers[reg1] = registers[reg2]
    elif line[1] == "ST":
        reg, mem = line[2].split(",")
        if "(" in mem:
            addr = addr_from_val(mem)
            num = str(num_from_val(mem))
            index = int(registers[num]/4)
            memory[addr][index] = registers[reg]
        else:
            memory[mem] = registers[reg]
    elif line[1] == "A":
        reg, mem = line[2].split(",")
        if "(" in mem:
            addr = addr_from_val(mem)
            num = str(num_from_val(mem))
            index = int(registers[num]/4)
            registers[reg] += memory[addr][index]
        else:
            registers[reg] += memory[mem]
    elif line[1] == "S":
        reg, mem = line[2].split(",")
        if "(" in mem:
            addr = addr_from_val(mem)
            num = str(num_from_val(mem))
            index = int(registers[num]/4)
            registers[reg] -= memory[addr][index]
        else:
            registers[reg] -= memory[mem]
    elif line[1] == "M":
        reg, mem = line[2].split(",")
        if "(" in mem:
            addr = addr_from_val(mem)
            num = str(num_from_val(mem))
            index = int(registers[num]/4)
            registers[reg] *= memory[addr][index]
        else:
            registers[reg] *= memory[mem]
    elif line[1] == "D":
        reg, mem = line[2].split(",")
        if "(" in mem:
            addr = addr_from_val(mem)
            num = str(num_from_val(mem))
            index = int(registers[num]/4)
            registers[reg] = int(registers[reg]/memory[addr][index])
        else:
            registers[reg] = int(registers[reg]/memory[mem])
    elif line[1] == "AR":
        reg1, reg2 = line[2].split(",")
        registers[reg1] += registers[reg2]
    elif line[1] == "SR":
        reg1, reg2 = line[2].split(",")
        registers[reg1] -= registers[reg2]
    elif line[1] == "MR":
        reg1, reg2 = line[2].split(",")
        registers[reg1] *= registers[reg2]
    elif line[1] == "DR":
        reg1, reg2 = line[2].split(",")
        registers[reg1] = int(registers[reg1]/registers[reg2])
    elif line[1] == "C":
        reg, mem = line[2].split(",")
        if "(" in mem:
            addr = addr_from_val(mem)
            num = str(num_from_val(mem))
            index = int(registers[num]/4)
            registers['0'] = registers[reg] - memory[addr][index]
        else:
            registers['0'] = registers[reg] - memory[mem]
    elif line[1] == "CR":
        reg1, reg2 = line[2].split(",")
        registers['0'] = registers[reg1] - registers[reg2]
    elif line[1] == "J":
        label = line[2]
        for _line in code:
            if code[_line][0] == label:
                n = _line - 1
    elif line[1] == "JZ":
        if registers['0'] == 0:
            label = line[2]
            for _line in code:
                if code[_line][0] == label:
                    n = _line - 1
    elif line[1] == "JN":
        if registers['0'] < 0:
            label = line[2]
            for _line in code:
                if code[_line][0] == label:
                    n = _line - 1
    elif line[1] == "JP":
        if registers['0'] > 0:
            label = line[2]
            for _line in code:
                if code[_line][0] == label:
                    n = _line - 1
    elif line[1] == "P":
        mem = line[2]
        if "(" in mem:
            addr = addr_from_val(mem)
            num = str(num_from_val(mem))
            index = int(registers[num]/4)
            print(memory[addr][index])
        else:
            print(memory[mem])
    elif line[1] == "PR":
        reg = line[2]
        print(registers[reg])
    elif line[1] == "?M":
        print("[DEBUG] -------------------")
        print(f"[DEBUG] MEMORY")
        for mem in memory:
            print(f"[DEBUG] {mem}\t{memory[mem]}")
        print("[DEBUG] -------------------")

    elif line[1] == "?R":
        print("[DEBUG] -------------------")
        print(f"[DEBUG] REGISTERS")
        for reg in registers:
            print(f"[DEBUG] {reg}\t{registers[reg]}")
        print("[DEBUG] -------------------")

    n += 1
