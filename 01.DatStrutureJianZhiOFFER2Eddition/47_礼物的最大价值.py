'''
剑指offer(47)：礼物的最大值（动态规划详解，python版）_dugudaibo的博客-CSDN博客_礼物的最大价值
https://blog.csdn.net/dugudaibo/article/details/79678890

'''

def get_max_value1(matrix):
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not isinstance(matrix[0], list) or len(matrix[0]) == 0:
        return

    num_row = len(matrix)
    num_col = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list) or len(row) != num_col:
            return

    max_value_matrix = [[0] * num_col for _ in range(num_row)]
    # print(len(max_value_matrix), len(max_value_matrix[0]))
    for i in range(num_row):
        for j in range(num_col):
            up = 0
            left = 0
            if i > 0:
                up = max_value_matrix[i - 1][j]

            if j > 0:
                left = max_value_matrix[i][j - 1]
            max_value_matrix[i][j] = matrix[i][j] +  max(up, left)
    return max_value_matrix[-1][-1]


def get_max_value2(matrix):
    if not isinstance(matrix, list) or len(matrix) == 0 or \
            not isinstance(matrix[0], list) or len(matrix[0]) == 0:
        return

    num_row = len(matrix)
    num_col = len(matrix[0])
    for row in matrix:
        if not isinstance(row, list) or len(row) != num_col:
            return

    max_values = [0] * num_col

    for i in range(num_row):
        for j in range(num_col):
            up = 0
            left = 0
            if i > 0:
                up = max_values[j]

            if j > 0:
                left = max_values[j - 1]
            max_values[j] = matrix[i][j] + max(up, left)
    return max_values[-1]



def get_max_value3_test(matrix):
    if not matrix or (not isinstance(matrix, list)):
        return None
    matrixCache = [0]*len(matrix)
    for i, ele in enumerate(matrix):
        matrixCache[i] = [0]*len(ele)

    for row in range(len( matrix)):
        for col in range(len(matrix[0])):
            up = 0
            left = 0
            if col > 0:
                left = matrix[row][col - 1]

            if row>0:
                up = matrix[row - 1][col]

            if row !=0  and col!=0:
                matrixCache[row][col] = matrix[row][col] + max(up, left) + matrixCache[row-1][col-1]
            elif row==0 and col==0:
                matrixCache[row][col] = matrix[row][col]
            elif row ==0:
                matrixCache[row][col] = matrix[row][col] + max(up, left) + matrixCache[row][col - 1]
            elif col ==0:
                matrixCache[row][col] = matrix[row][col] + max(up, left) + matrixCache[row-1][col ]

    print(matrixCache)
    return matrixCache[-1][-1]






    # print(len(matrix), len(matrixCache),matrixCache)

    pass


def get_max_value4_test(matrix):
    if not matrix or (not isinstance(matrix, list)):
        return None
    matrixCache = [0]*len(matrix)
    for i, ele in enumerate(matrix):
        matrixCache[i] = [0]*len(ele)

    for row in range(len( matrix)):
        for col in range(len(matrix[0])):
            up = 0
            left = 0
            if col > 0:
                left =  matrixCache[row][col - 1]

            if row>0:
                up =  matrixCache[row-1][col ]

            # if row !=0  and col!=0:
            #     matrixCache[row][col] = matrix[row][col] + max(up, left) + matrixCache[row-1][col-1]
            # elif row==0 and col==0:
            #     matrixCache[row][col] = matrix[row][col] + max(up, left) + matrixCache[0][0]
            # elif row ==0:
            #     matrixCache[row][col] = matrix[row][col] + max(up, left) + matrixCache[row][col - 1]
            # elif col ==0:
            #     matrixCache[row][col] = matrix[row][col] + max(up, left) + matrixCache[row-1][col ]
            matrixCache[row][col] = matrix[row][col] + max(up, left)

    print(matrixCache)
    return matrixCache[-1][-1]






    # print(len(matrix), len(matrixCache),matrixCache)

    pass


class Solution:
    def minPathSum(self, grid) -> int:
        if not grid:
            return None
        rowLen = len(grid)
        colLen = len(grid[0])

        minList = [0] * rowLen
        minList = [[0] * colLen for r in range(rowLen)]
        maxValue = sorted( sum(grid, []) )[-1] +1
        print(maxValue)
        for r in range(rowLen):
            for c in range(colLen):
                # left, up = maxValue, maxValue
                left, up = 0,0
                if c > 0:
                    left = minList[r][c - 1]
                if r > 0:
                    up = minList[r - 1][c]
                if c >0 and r ==0:
                    minList[r][c] = grid[r][c] + left
                elif  c ==0 and r >0:
                    minList[r][c] = grid[r][c] + up
                else:
                    minList[r][c] = grid[r][c] + min( left, up)

        print(minList)
        return minList[-1][-1]


if __name__ == "__main__":
#     m = [[1, 10, 3, 8],
#          [12, 2, 9, 6],
#          [5, 7, 4, 11]]
#          # [3, 7, 16, 5]]
#     print(m)
    # print(get_max_value1(m))
    # print(get_max_value3_test(m))
    # print(get_max_value4_test(m))

    m = [[1,3,1],
         [1,5,1],
         [4,2,1]]
    print(m, '?',sorted( sum(m, []) )[-1])
    print(m)
    a = Solution()
    print( a.minPathSum(m))