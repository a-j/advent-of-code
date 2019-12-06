# using itertools.groupby() would have greatly simplified below logic
#    for key, grp in groupby(str(number)):
#        if len(list(grp)) == 2 then an exact double is found
def two_adjacent_digits_same(number):
    nums = [int(x) for x in str(number)]
    prev = -1
    count = 0
    for n in nums:
        if n == prev:
            count += 1
            if count > 2:
                count = -99
        else:
            if count == 2:
                return True
            count = 1
        prev = n
    return count == 2

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

# print(two_adjacent_digits_same(112233) and are_increasing_digits(112233))
# print(two_adjacent_digits_same(123444) and are_increasing_digits(123444))
# print(two_adjacent_digits_same(111122) and are_increasing_digits(111122))
# print(two_adjacent_digits_same(111111) and are_increasing_digits(111111))