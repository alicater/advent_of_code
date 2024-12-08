

def find_word(input_file):
    with open(input_file, 'r') as file:
        grid = [line.strip() for line in file.readlines()]

    rows = len(grid)
    cols = len(grid[0])
    # word_length = len(word)
    count = 0

    # def check_direction(start_row, start_col, row_step, col_step): # from first potion
    #     for i in range(word_length):
    #         r = start_row + i * row_step
    #         c = start_col + i * col_step
    #         if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] != word[i]:
    #             return False
    #     return True

    def check_x_mas(row, col):
        if row - 1 >= 0 and row + 1 < rows and col - 1 >= 0 and col + 1 < cols:
            if (grid[row - 1][col - 1] == 'M' and grid[row][col] == 'A' and grid[row + 1][col + 1] == 'S'):
                if (grid[row - 1][col + 1] == 'S' and grid[row + 1][col - 1] == 'M'):
                    return True

            if (grid[row - 1][col + 1] == 'M' and grid[row][col] == 'A' and grid[row + 1][col - 1] == 'S'):
                if (grid[row - 1][col - 1] == 'S' and grid[row + 1][col + 1] == 'M'):
                    return True  

    for row in range(rows):
        for col in range(cols):
            if check_x_mas(row, col):
                count += 1

    # for row in range(rows): # from first portion
    #     for col in range(cols):
    #         direction = [
    #             (0, 1),
    #             (1,0),
    #             (1, 1),
    #             (-1, 0),
    #             (0, -1),
    #             (-1, -1),
    #             (-1, 1),
    #             (1, -1)
    #         ]
    #         for row_step, col_step in direction:
    #             if check_direction(row, col, row_step, col_step):
    #                 count += 1


    print(count)
    return count

input_file = 'test.txt'
#word = 'XMAS'
find_word(input_file)