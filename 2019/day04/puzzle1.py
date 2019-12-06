def two_adjacent_digits_same(number):
    prev = -1
    while number != 0:
        curr = number % 10
        if prev != -1 and curr == prev:
            return True
        prev = curr
        number = number // 10
    return False

def are_increasing_digits(number):
    prev = 10
    while number != 0:
        curr = number % 10
        if curr > prev:
            return False
        prev = curr
        number = number // 10
    return True

begin = 246515
end = 739105

count = 0
for i in range(begin, end+1):
    if two_adjacent_digits_same(i) and are_increasing_digits(i):
        count += 1

print(count)