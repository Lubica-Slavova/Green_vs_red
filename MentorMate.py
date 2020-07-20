def is_valid(m, row, col):
    size = len(m)
    result = 0 <= row < size and 0 <= col < size and m[row][col] >= 0
    return result


def around_cell(matrix, row, col):
    green_c = 0
    red_c = 0
    if is_valid(matrix, row-1, col):
        up = matrix[row - 1][col]
        if up == 1:
            green_c += 1
        else:
            red_c += 1
    if is_valid(matrix, row-1, col+1):
        up_right = matrix[row - 1][col + 1]
        if up_right == 1:
            green_c += 1
        else:
            red_c += 1
    if is_valid(matrix, row, col+1):
        right = matrix[row][col + 1]
        if right == 1:
            green_c += 1
        else:
            red_c += 1
    if is_valid(matrix, row+1, col+1):
        right_down = matrix[row + 1][col + 1]
        if right_down == 1:
            green_c += 1
        else:
            red_c += 1
    if is_valid(matrix, row+1, col):
        down = matrix[row + 1][col]
        if down == 1:
            green_c += 1
        else:
            red_c += 1
    if is_valid(matrix, row+1, col-1):
        down_left = matrix[row + 1][col - 1]
        if down_left == 1:
            green_c += 1
        else:
            red_c += 1
    if is_valid(matrix, row, col-1):
        left = matrix[row][col - 1]
        if left == 1:
            green_c += 1
        else:
            red_c += 1
    if is_valid(matrix, row-1, col-1):
        left_up = matrix[row - 1][col - 1]
        if left_up == 1:
            green_c += 1
        else:
            red_c += 1
    if matrix[row][col] == 0:
        if green_c == 3 or green_c == 6:
            new_array[row][col] = 1
    else:
        if green_c == 0 or green_c == 1 or green_c == 4 or green_c == 5 or green_c == 7 or green_c == 8:
            new_array[row][col] = 0


def generation(m, row, col):
    for current_row in range(0, len(m)):
        for current_col in range(0, len(m)):
            neighbor_row = current_row
            neighbor_col = current_col

            if is_valid(matrix, neighbor_row, neighbor_col):
                around_cell(matrix, neighbor_row, neighbor_col)


(rows, columns) = map(int, input().split(', '))
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input()])

(position_col, position_row, turns) = map(int, input().split(', '))
new_array = [row[:] for row in matrix]

counter = 0
for i in range(turns + 1):
    if matrix[position_row][position_col] == 1:
        counter += 1
    matrix = [row[:] for row in new_array]
    generation(matrix, position_row, position_col)

print(counter)
