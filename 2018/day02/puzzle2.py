def get_differ_count(word1, word2):
    zipped = zip(word1, word2)
    differ_count = 0
    intersection = []
    for item in zipped:
        if item[0] != item[1]:
            differ_count += 1
        else:
            intersection.append(item[0])
    return differ_count, ''.join(intersection)

with open('input.txt') as file_handle:
    lines = file_handle.readlines()
    differ_count = 0
    for line1 in lines:
        for line2 in lines:
            line1 = line1.rstrip()
            line2 = line2.rstrip()
            if line1 == line2 or len(line1) != len(line2):
                continue
            differ_count, intersection = get_differ_count(line1, line2)
            if differ_count == 1:
                print(intersection)
                break
        if differ_count == 1:
            break
