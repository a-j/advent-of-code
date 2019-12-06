def process_intcode(input):
    if not input:
        return
    opcode_pos = 0
    while input[opcode_pos] != 99:
        if input[opcode_pos] not in [1, 2]:
            print('invalid opcode')
            break
        if input[opcode_pos] == 1:
            input[input[opcode_pos + 3]] = input[input[opcode_pos + 1]] + input[input[opcode_pos + 2]]
        elif input[opcode_pos] == 2:
            input[input[opcode_pos + 3]] = input[input[opcode_pos + 1]] * input[input[opcode_pos + 2]]
        opcode_pos = opcode_pos + 4

with open('input.txt') as file:
    line = file.readline()
    input = line.split(',')
    input = [int(item) for item in input]
    input[1] = 12
    input[2] = 2
    process_intcode(input)
    print(input)        

# test = [1,1,1,4,99,5,6,0,99]
# process_intcode(test)
# print(test)