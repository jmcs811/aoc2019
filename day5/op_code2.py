def read_file_into_list(filename):
    '''
    read specified filename and put contents into
    output_list
    '''
    output_list = []
    with open(filename, 'r') as filestream:
        for line in filestream:
            currentline = line.split(',')
            for item in currentline:
                output_list.append(int(item))
    return output_list

def parse(code):
    DE = code % 100
    C = code // 100 % 10
    B = code // 1000 % 10
    A = code // 10000 % 10
    return (DE, C, B, A)

def decode(input_list, input=0, immedate=False):
    i = 0
    while 1:
        opcode = parse(input_list[i])
        # opcode 99 Exit
        if (opcode[0] == 99):
            if immedate:
                return input_list
            return input_list[0]
        # opcode 1 Add
        elif (opcode[0] == 1):
            param1 = input_list[i+1] if opcode[1] == 0 else i+1
            param2 = input_list[i+2] if opcode[2] == 0 else i+2
            input_list[input_list[i+3]] = input_list[param1] + input_list[param2]
            i += 4
        # opcode 2 Mult
        elif (opcode[0] == 2):
            param1 = input_list[i+1] if opcode[1] == 0 else i+1
            param2 = input_list[i+2] if opcode[2] == 0 else i+2
            input_list[input_list[i+3]] = input_list[param1] * input_list[param2]
            i += 4
        # opcode 3 Store
        elif (opcode[0] == 3):
            input_list[input_list[i+1]] = input
            i += 2
        # opcode 4 Load
        elif (opcode[0] == 4):
            load = input_list[i+1] if opcode[1] == 0 else i+1
            input_list[0] = input_list[load]
            i += 2
        # opcode 5/6 JMP if true/false
        elif (opcode[0] in [5, 6]):
            load1 = input_list[i + 1] if opcode[1] == 0 else i+1
            if opcode[0] == 5 and input_list[load1] or opcode[0] == 6 and not input_list[load1]:
                load2 = input_list[i+2] if opcode[2] == 0 else i+2
                i = input_list[load2]
            else:
                i += 3
        # opcode 7/8 less than / equal
        elif (opcode[0] in [7,8]):
            param1 = input_list[i+1] if opcode[1] == 0 else i+1
            param2 = input_list[i+2] if opcode[2] == 0 else i+2
            input_list[input_list[i+3]] = 1 if opcode[0] == 7 and input_list[param1] < input_list[param2] or \
                opcode[0] == 8 and input_list[param1] == input_list[param2] else 0
            i += 4

input_list = read_file_into_list('input.txt')
print(decode(input_list, input=5))