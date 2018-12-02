with open('input.txt', 'r') as file_handle:
    lines = file_handle.readlines()
    sum = 0
    frequency = set()
    duplicate_found = False
    while True:
        for line in lines:
            sum += int(line.rstrip())
            if sum in frequency:
                print(sum)
                duplicate_found = True
                break
            frequency.add(sum)
        if duplicate_found:
            break
