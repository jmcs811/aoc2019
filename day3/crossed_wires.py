def generate_grid(input):
    coords = {}
    x = 0
    y = 0
    step = 0

    for move in input:
        direction = move[0]
        distance = int(move[1:])
        move_x = 0
        move_y = 0

        if (direction == 'L'):
            move_x = -1
        elif (direction == 'R'):
            move_x = 1
        elif (direction == 'U'):
            move_y = 1
        elif (direction == 'D'):
            move_y = -1

        for _ in range(0, distance):
            x += move_x
            y += move_y
            step += 1
            if (x, y) not in coords:
                coords[(x, y)] = step

    return coords

def read_file_into_list(filename, output_list1, output_list2):
    '''
    read specified filename and put contents into
    output_list
    '''
    count = 0
    with open(filename, 'r') as filestream:
        for line in filestream:
            currentline = line.split(',')
            for item in currentline:
                if (count == 0):
                    output_list1.append(item)
                else:
                    output_list2.append(item)
            count += 1
    output_list1[len(output_list1) - 1] = 'L396'

def get_shortest(intersections):
    distances = []
    for intersection in intersections:
        dist = abs(intersection[0]) + abs(intersection[1])
        distances.append(dist)
    return min(distances)

def get_fewest(intersections, line1, line2):
    combined_steps = [line1[i] + line2[i] for i in intersections]
    return min(combined_steps)

output_list1 = []
output_list2 = []
read_file_into_list('input.txt', output_list1, output_list2)

line1 = generate_grid(output_list1)
line2 = generate_grid(output_list2)

intersections = list(set(line1.keys()) & set(line2.keys()))
print(get_shortest(intersections))
print(get_fewest(intersections, line1, line2))

