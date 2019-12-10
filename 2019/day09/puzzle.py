class IntCodeComputer:
    def __init__(self, memory):
        self.memory = memory
        self.instruction_pointer = 0
        self.output_signal = 0
        self.program_halted = False
        self.relative_base = 0

    def get_parameter(self, pointer, param_mode, write=False):
        if param_mode == 0:
            if write:
                return self.memory[pointer]
            else:
                return self.memory[self.memory[pointer]]
        elif param_mode == 1:
            return self.memory[pointer]
        elif param_mode == 2:
            if write:
                return self.relative_base + self.memory[pointer]
            else:
                return self.memory[self.relative_base + self.memory[pointer]]

    def process_intcode(self, input_signal):
        opcode = self.memory[self.instruction_pointer] % 100

        while opcode != 99:
            increment = 0
            if opcode not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
                print('invalid opcode')
                break
            param1_mode = (self.memory[self.instruction_pointer] // 100) % 10
            param2_mode = (self.memory[self.instruction_pointer] // 1000) % 10
            param3_mode = (self.memory[self.instruction_pointer] // 10000) % 10
            if opcode == 1:     # ADD
                p1 = self.get_parameter(self.instruction_pointer + 1, param1_mode)
                p2 = self.get_parameter(self.instruction_pointer + 2, param2_mode)
                p3 = self.get_parameter(self.instruction_pointer + 3, param3_mode, write=True)
                self.memory[p3] = p1 + p2
                self.instruction_pointer = self.instruction_pointer + 4
            elif opcode == 2:   # MUL
                p1 = self.get_parameter(self.instruction_pointer + 1, param1_mode)
                p2 = self.get_parameter(self.instruction_pointer + 2, param2_mode)
                p3 = self.get_parameter(self.instruction_pointer + 3, param3_mode, write=True)
                self.memory[p3] = p1 * p2
                self.instruction_pointer = self.instruction_pointer + 4
            elif opcode == 3:   # IN
                p1 = self.get_parameter(self.instruction_pointer + 1, param1_mode, write=True)
                self.memory[p1] = input_signal
                self.instruction_pointer = self.instruction_pointer + 2
            elif opcode == 4:   # OUT
                self.output_signal = self.get_parameter(self.instruction_pointer + 1, param1_mode)
                self.instruction_pointer = self.instruction_pointer + 2
                print(self.output_signal)
            elif opcode == 5:   # JUMP_IF_NON_ZERO
                p1 = self.get_parameter(self.instruction_pointer + 1, param1_mode)
                p2 = self.get_parameter(self.instruction_pointer + 2, param2_mode)
                if p1:
                    self.instruction_pointer = p2
                else:
                    self.instruction_pointer = self.instruction_pointer + 3
            elif opcode == 6:   # JUMP_IF_ZERO
                p1 = self.get_parameter(self.instruction_pointer + 1, param1_mode)
                p2 = self.get_parameter(self.instruction_pointer + 2, param2_mode)
                if not p1:
                    self.instruction_pointer = p2
                else:
                    self.instruction_pointer = self.instruction_pointer + 3
            elif opcode == 7:   # LESS_THAN
                p1 = self.get_parameter(self.instruction_pointer + 1, param1_mode)
                p2 = self.get_parameter(self.instruction_pointer + 2, param2_mode)
                p3 = self.get_parameter(self.instruction_pointer + 3, param3_mode, write=True)
                self.memory[p3] = 1 if p1 < p2 else 0
                self.instruction_pointer = self.instruction_pointer + 4
            elif opcode == 8:   # EQUALS
                p1 = self.get_parameter(self.instruction_pointer + 1, param1_mode)
                p2 = self.get_parameter(self.instruction_pointer + 2, param2_mode)
                p3 = self.get_parameter(self.instruction_pointer + 3, param3_mode, write=True)
                self.memory[p3] = 1 if p1 == p2 else 0
                self.instruction_pointer = self.instruction_pointer + 4
            elif opcode == 9:   # RELATIVE_BASE_OFFSET
                p1 = self.get_parameter(self.instruction_pointer + 1, param1_mode)
                self.relative_base = self.relative_base + p1
                self.instruction_pointer = self.instruction_pointer + 2

            opcode = self.memory[self.instruction_pointer] % 100
        self.program_halted = True


# memory = '104,1125899906842624,99'.split(',')
with open('input.txt') as f:
    memory = f.read().split(',')
memory = [int(item) for item in memory]
expanded_memory = [0]*2000
memory = memory + expanded_memory

# puzzle 1
computer = IntCodeComputer(memory.copy())
computer.process_intcode(1)
# puzzle 2
computer = IntCodeComputer(memory.copy())
computer.process_intcode(2)


## Another way to think about the problem - probably a better solution
## https://github.com/benediktwerner/AdventOfCode/blob/master/2019/day09/sol.py
