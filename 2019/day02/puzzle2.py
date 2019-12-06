def process_intcode(memory):
    if not memory:
        return
    instruction_pointer = 0
    while memory[instruction_pointer] != 99:
        if memory[instruction_pointer] not in [1, 2]:
            print('invalid opcode')
            break
        if memory[instruction_pointer] == 1:
            memory[memory[instruction_pointer + 3]] = memory[memory[instruction_pointer + 1]] + memory[memory[instruction_pointer + 2]]
        elif memory[instruction_pointer] == 2:
            memory[memory[instruction_pointer + 3]] = memory[memory[instruction_pointer + 1]] * memory[memory[instruction_pointer + 2]]
        instruction_pointer = instruction_pointer + 4

with open('input.txt') as file:
    line = file.readline()
    input = line.split(',')
    input = [int(item) for item in input]
    for noun in range(100):
        found = False
        for verb in range(100):
            memory = input.copy()
            memory[1] = noun
            memory[2] = verb
            process_intcode(memory)
            if memory[0] == 19690720:
                found = True
                break
        if found:
            break

print(100 * noun + verb)
