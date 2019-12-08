# image_data = list(map(int, '123456789012'))
# width = 3
# height = 2
with open('input.txt') as f:
    image_data = list(map(int, f.readline()))
width = 25
height = 6

layers = {}
layer_count = 0
part = image_data[(height*width*layer_count) : (height*width*(layer_count+1))]
while part:
    layer = []
    for i in range(height):
        row = []
        for j in range(width):
            index = (height*width*(layer_count)) + (i*width) + j
            row.append(image_data[index])
        layer.append(row)
    layer_count += 1
    layers[layer_count] = layer
    part = image_data[(height*width*layer_count) : (height*width*(layer_count+1))]

fewest_zeroes_layer = 1
min_zeroes = -1
for layer in layers:
    zero_count = 0
    for row in layers[layer]:
        for pixel in row:
            if pixel == 0:
                zero_count += 1
    if zero_count < min_zeroes or min_zeroes == -1:
        fewest_zeroes_layer = layer
        min_zeroes = zero_count

print(f'Layer with least zeroes: {fewest_zeroes_layer}')

one_digits = 0
two_digits = 0
for row in layers[fewest_zeroes_layer]:
    for pixel in row:
        if pixel == 1:
            one_digits += 1
        elif pixel == 2:
            two_digits += 1

print(f'# of 1 digits: {one_digits}')
print(f'# of 2 digits: {two_digits}')
print(f'Product: {one_digits * two_digits}')