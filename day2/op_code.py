def decode(opcode, first, second, dest, input):
    '''
    decode the instruction and apply the specified
    operation (add or mult)
    '''
    if (opcode == 1):
        # add
        input[dest] = add(input[first], input[second])
    elif (opcode == 2):
        # mult
        input[dest] = mult(input[first], input[second])
    elif (opcode == 99):
        # 99 end
        return
    else:
        print("unknown opcode")
    #print(input)
 
def add(first, second):
    '''
    add two operands
    '''
    return first + second
 
def mult(first, second):
    '''
    multiply two operands
    '''
    return first * second
 
def read_file_into_list(filename, output_list):
    '''
    read specified filename and put contents into
    output_list
    '''
    with open(filename, 'r') as filestream:
        for line in filestream:
            currentline = line.split(',')
            for item in currentline:
                output_list.append(int(item))
 
def iterate_list(input):
    '''
    iterate throught the list 4 items at a time
    '''
    for opcode, operand1, operand2, dest in zip(*[iter(input)]*4):
        decode(opcode, operand1, operand2, dest, input)

def reset_list(input):
    '''
    reset list to original values
    '''
    input.clear()
    read_file_into_list('input.txt', input)

def modify_list(pos1, pos2, input_list):
    '''
    modify position 1 and 2 
    '''
    input_list[1] = pos1
    input_list[2] = pos2

def multiple_guesses(input):
    '''
    try diff values at pos. 1 and 2
    until pos. 0 = 19690720
    '''
    for i in range(100):
        for j in range(100):
            modify_list(i, j, input)
            iterate_list(input)
            if (input[0] == 19690720):
                print(input)
                return
            # reset list and start over
            reset_list(input)

input_list = []

read_file_into_list('input.txt', input_list)
multiple_guesses(input_list)
 
# task 1 code
# read_file_into_list('input.txt', input_list)
# print("starting list")
# print(input_list)
# iterate_list(input_list)
# print("\n\nEnding list")
# print(input_list)