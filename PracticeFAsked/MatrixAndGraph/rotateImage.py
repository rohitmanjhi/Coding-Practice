
class Solution:
    def rotate(self, matrix):
        n = len(matrix)

        for i in range(n):
            for j in range(i+1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()        


# ----------------------------------------
# MAIN RUN (INPUT + OUTPUT)
# ----------------------------------------
if __name__ == "__main__":

    # -------- INPUT --------
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    for row in matrix:
        print(row)

    # -------- PROCESS --------
    sol = Solution()
    sol.rotate(matrix)

    # -------- OUTPUT --------
    print("\nMatrix After 90° Clockwise Rotation:")
    for row in matrix:
        print(row)
