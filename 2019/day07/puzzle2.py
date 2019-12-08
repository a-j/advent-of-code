class Amplifier:
    def __init__(self, memory, phase_setting):
        self.memory = memory
        self.phase_setting = phase_setting
        self.instruction_pointer = 0
        self.first_iteration = True
        self.output_signal = 0
        self.program_halted = False

    def get_parameter(self, pointer, param_mode):
        if param_mode == 0:
            return self.memory[self.memory[pointer]]
        elif param_mode == 1:
            return self.memory[pointer]

    def process_intcode(self, input_signal=-1):
        opcode = self.memory[self.instruction_pointer] % 100

        while opcode != 99:
            increment = 0
            if opcode not in [1, 2, 3, 4, 5, 6, 7, 8]:
                print('invalid opcode')
                break
            param1_mode = (self.memory[self.instruction_pointer] // 100) % 10
            param2_mode = (self.memory[self.instruction_pointer] // 1000) % 10
            param3_mode = (self.memory[self.instruction_pointer] // 10000) % 10
            if opcode == 1:
                self.memory[self.memory[self.instruction_pointer + 3]] = self.get_parameter(self.instruction_pointer+1, param1_mode) + self.get_parameter(self.instruction_pointer+2, param2_mode)
                self.instruction_pointer = self.instruction_pointer + 4
            elif opcode == 2:
                self.memory[self.memory[self.instruction_pointer + 3]] = self.get_parameter(self.instruction_pointer+1, param1_mode) * self.get_parameter(self.instruction_pointer+2, param2_mode)
                self.instruction_pointer = self.instruction_pointer + 4
            elif opcode == 3:
                self.memory[self.memory[self.instruction_pointer + 1]] = self.phase_setting if self.first_iteration else input_signal
                self.first_iteration = False
                self.instruction_pointer = self.instruction_pointer + 2
            elif opcode == 4:
                if param1_mode == 0:
                    self.output_signal = self.memory[self.memory[self.instruction_pointer + 1]]
                else:
                    self.output_signal = self.memory[self.instruction_pointer + 1]
                self.instruction_pointer = self.instruction_pointer + 2
                return self.output_signal
            elif opcode == 5:
                if self.get_parameter(self.instruction_pointer+1, param1_mode):
                    self.instruction_pointer = self.get_parameter(self.instruction_pointer+2, param2_mode)
                else:
                    self.instruction_pointer = self.instruction_pointer + 3
            elif opcode == 6:
                if not self.get_parameter(self.instruction_pointer+1, param1_mode):
                    self.instruction_pointer = self.get_parameter(self.instruction_pointer+2, param2_mode)
                else:
                    self.instruction_pointer = self.instruction_pointer + 3
            elif opcode == 7:
                if self.get_parameter(self.instruction_pointer+1, param1_mode) < self.get_parameter(self.instruction_pointer+2, param2_mode):
                    self.memory[self.memory[self.instruction_pointer + 3]] = 1
                else:
                    self.memory[self.memory[self.instruction_pointer + 3]] = 0
                self.instruction_pointer = self.instruction_pointer + 4
            elif opcode == 8:
                if self.get_parameter(self.instruction_pointer+1, param1_mode) == self.get_parameter(self.instruction_pointer+2, param2_mode):
                    self.memory[self.memory[self.instruction_pointer + 3]] = 1
                else:
                    self.memory[self.memory[self.instruction_pointer + 3]] = 0
                self.instruction_pointer = self.instruction_pointer + 4
            opcode = self.memory[self.instruction_pointer] % 100
        self.program_halted = True

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

# memory = '3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10'.split(',')
with open('input.txt') as f:
    memory = f.read().split(',')
memory = [int(item) for item in memory]

phase_settings = [5, 6, 7, 8, 9]
max_thrust = 0
for phase_setting in permutation(phase_settings):
    amplifier_1 = Amplifier(memory.copy(), phase_setting[0])
    amplifier_2 = Amplifier(memory.copy(), phase_setting[1])
    amplifier_3 = Amplifier(memory.copy(), phase_setting[2])
    amplifier_4 = Amplifier(memory.copy(), phase_setting[3])
    amplifier_5 = Amplifier(memory.copy(), phase_setting[4])
    output = 0
    while True:
        output = amplifier_1.process_intcode(output)
        output = amplifier_2.process_intcode(output)
        output = amplifier_3.process_intcode(output)
        output = amplifier_4.process_intcode(output)
        output = amplifier_5.process_intcode(output)
        if amplifier_5.program_halted:
            break
    max_thrust = max(max_thrust, amplifier_5.output_signal)

print(max_thrust)
