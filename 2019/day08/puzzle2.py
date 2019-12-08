# image_data = list(map(int, '0222112222120000'))
# width = 2
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

result = layers[1]
for layer in layers:
    for i, row in enumerate(layers[layer]):
        for j, pixel in enumerate(row):
            if result[i][j] == 2:
                result[i][j] = pixel
for row in result:
    converted = list(map(str, row))
    res = ''.join(converted)
    res = res.replace('0', ' ')
    res = res.replace('1', 'X')
    print(res)
