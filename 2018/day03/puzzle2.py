import re

def parse_string(str):
    numbers = re.findall(r'\d+', str)
    return (numbers[0], int(numbers[1]), int(numbers[2]), int(numbers[3]), int(numbers[4]))

def process_claim(str, fabric):
    id, left, top, width, height = parse_string(str)
    for i in range(height):
        for j in range(width):
            fabric[top + i][left + j] = id if fabric[top + i][left + j]  == '.' else 'x'

def check_overlap(str, fabric):
    id, left, top, width, height = parse_string(str)
    count = 0
    for i in range(height):
        for j in range(width):
            if fabric[top + i][left + j] == id:
                count += 1
    
    if count == height * width:
        print(id)

with open('input.txt') as file_handle:
    lines = file_handle.readlines()
    m = 1000
    fabric = [['.'] * m for i in range(m)]
    for line in lines:
        process_claim(line, fabric)

    for line in lines:
        check_overlap(line, fabric)