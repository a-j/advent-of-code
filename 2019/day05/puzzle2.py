def get_parameter(memory, pointer, param_mode):
    if param_mode == 0:
        return memory[memory[pointer]]
    elif param_mode == 1:
        return memory[pointer]

def process_intcode(memory):
    if not memory:
        return
    instruction_pointer = 0
    x = memory[instruction_pointer]
    opcode = x % 100

    while opcode != 99:
        increment = 0
        if opcode not in [1, 2, 3, 4, 5, 6, 7, 8]:
            print('invalid opcode')
            break
        param1_mode = (x // 100) % 10
        param2_mode = (x // 1000) % 10
        param3_mode = (x // 10000) % 10
        # print(opcode)
        if opcode == 1:
            memory[memory[instruction_pointer + 3]] = get_parameter(memory, instruction_pointer+1, param1_mode) + get_parameter(memory, instruction_pointer+2, param2_mode)
            instruction_pointer = instruction_pointer + 4
        elif opcode == 2:
            # print(memory[instruction_pointer + 3])
            # print(get_parameter(memory, instruction_pointer+1, param1_mode))
            # print(get_parameter(memory, instruction_pointer+2, param1_mode))
            memory[memory[instruction_pointer + 3]] = get_parameter(memory, instruction_pointer+1, param1_mode) * get_parameter(memory, instruction_pointer+2, param2_mode)
            instruction_pointer = instruction_pointer + 4
        elif opcode == 3:
            # val = input('Enter value:')
            memory[memory[instruction_pointer + 1]] = 5
            instruction_pointer = instruction_pointer + 2
        elif opcode == 4:
            if param1_mode == 0:
                print(memory[memory[instruction_pointer + 1]])
            else:
                print(memory[instruction_pointer + 1])
            instruction_pointer = instruction_pointer + 2
        elif opcode == 5:
            if get_parameter(memory, instruction_pointer+1, param1_mode):
                instruction_pointer = get_parameter(memory, instruction_pointer+2, param2_mode)
            else:
                instruction_pointer = instruction_pointer + 3
        elif opcode == 6:
            if not get_parameter(memory, instruction_pointer+1, param1_mode):
                instruction_pointer = get_parameter(memory, instruction_pointer+2, param2_mode)
            else:
                instruction_pointer = instruction_pointer + 3
        elif opcode == 7:
            if get_parameter(memory, instruction_pointer+1, param1_mode) < get_parameter(memory, instruction_pointer+2, param2_mode):
                memory[memory[instruction_pointer + 3]] = 1
            else:
                memory[memory[instruction_pointer + 3]] = 0
            instruction_pointer = instruction_pointer + 4
        elif opcode == 8:
            if get_parameter(memory, instruction_pointer+1, param1_mode) == get_parameter(memory, instruction_pointer+2, param2_mode):
                memory[memory[instruction_pointer + 3]] = 1
            else:
                memory[memory[instruction_pointer + 3]] = 0
            instruction_pointer = instruction_pointer + 4
        x = memory[instruction_pointer]
        opcode = x % 100


input = '3,225,1,225,6,6,1100,1,238,225,104,0,101,71,150,224,101,-123,224,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,2,205,209,224,1001,224,-3403,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1101,55,24,224,1001,224,-79,224,4,224,1002,223,8,223,101,1,224,224,1,223,224,223,1,153,218,224,1001,224,-109,224,4,224,1002,223,8,223,101,5,224,224,1,224,223,223,1002,201,72,224,1001,224,-2088,224,4,224,102,8,223,223,101,3,224,224,1,223,224,223,1102,70,29,225,102,5,214,224,101,-250,224,224,4,224,1002,223,8,223,1001,224,3,224,1,223,224,223,1101,12,52,225,1101,60,71,225,1001,123,41,224,1001,224,-111,224,4,224,102,8,223,223,1001,224,2,224,1,223,224,223,1102,78,66,224,1001,224,-5148,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1101,29,77,225,1102,41,67,225,1102,83,32,225,1101,93,50,225,1102,53,49,225,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,1107,677,677,224,1002,223,2,223,1005,224,329,101,1,223,223,7,677,677,224,1002,223,2,223,1005,224,344,1001,223,1,223,7,226,677,224,102,2,223,223,1006,224,359,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,374,1001,223,1,223,8,226,677,224,1002,223,2,223,1006,224,389,1001,223,1,223,1108,226,677,224,1002,223,2,223,1006,224,404,101,1,223,223,1107,677,226,224,102,2,223,223,1006,224,419,101,1,223,223,1007,677,677,224,1002,223,2,223,1005,224,434,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,449,1001,223,1,223,1008,226,677,224,1002,223,2,223,1006,224,464,101,1,223,223,8,677,677,224,1002,223,2,223,1006,224,479,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,494,101,1,223,223,1107,226,677,224,1002,223,2,223,1006,224,509,101,1,223,223,107,226,226,224,1002,223,2,223,1006,224,524,1001,223,1,223,107,677,677,224,1002,223,2,223,1005,224,539,101,1,223,223,1007,226,226,224,102,2,223,223,1006,224,554,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,569,101,1,223,223,107,677,226,224,102,2,223,223,1005,224,584,101,1,223,223,1008,226,226,224,102,2,223,223,1006,224,599,101,1,223,223,1108,677,226,224,1002,223,2,223,1006,224,614,101,1,223,223,8,677,226,224,102,2,223,223,1005,224,629,1001,223,1,223,1008,677,677,224,102,2,223,223,1006,224,644,101,1,223,223,1007,226,677,224,102,2,223,223,1005,224,659,101,1,223,223,108,226,677,224,102,2,223,223,1006,224,674,101,1,223,223,4,223,99,226'
memory = input.split(',')
memory = [int(item) for item in memory]
process_intcode(memory)

# process_intcode([3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99])
