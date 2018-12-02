with open('input.txt', 'r') as file_handle:
    lines = file_handle.readlines()
    sum = 0
    for line in lines:
        sum += int(line.rstrip())
    print(sum)