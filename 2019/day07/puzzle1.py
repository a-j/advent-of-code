def get_parameter(memory, pointer, param_mode):
    if param_mode == 0:
        return memory[memory[pointer]]
    elif param_mode == 1:
        return memory[pointer]

def process_intcode(memory, input_params):
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
            memory[memory[instruction_pointer + 1]] = input_params[0]
            input_params = input_params[1:]
            instruction_pointer = instruction_pointer + 2
        elif opcode == 4:
            if param1_mode == 0:
                return memory[memory[instruction_pointer + 1]]
            else:
                return memory[instruction_pointer + 1]
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

def permutation(lst):
    if not lst:
        return []
    if len(lst) == 1:
        return [lst]
    result = []
    for item in lst:
        dup = lst.copy()
        dup.remove(item)
        for subitem in permutation(dup):
            result.append([item] + subitem)
    return result

# memory = '3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0'.split(',')
with open('input.txt') as f:
    memory = f.read().split(',')
memory = [int(item) for item in memory]

phase_settings = [0, 1, 2, 3, 4]
max_thrust = 0
for phase_setting in permutation(phase_settings):
    input_signal = 0
    for phase_setting_item in phase_setting:
        input_signal = process_intcode(memory.copy(), [phase_setting_item, input_signal])
    if input_signal > max_thrust:
        max_thrust = input_signal
        max_thrust_setting = phase_setting

print(max_thrust)
print(max_thrust_setting)