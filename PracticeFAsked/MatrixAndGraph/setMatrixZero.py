
class Solution:
    def setZeroes(self, matrix):
        rows, cols = len(matrix), len(matrix[0])

        first_row_zero = False
        first_col_zero = False

        # Step 1: check first row
        for c in range(cols):
            if matrix[0][c] == 0:
                first_row_zero = True

        # Step 2: check first column
        for r in range(rows):
            if matrix[r][0] == 0:
                first_col_zero = True

        # Step 3: use first row & column as markers
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0

        # Step 4: zero rows based on markers
        for r in range(1, rows):
            if matrix[r][0] == 0:
                for c in range(1, cols):
                    matrix[r][c] = 0      

        # Step 5: zero columns based on markers
        for c in range(1, cols):
            if matrix[0][c] == 0:
                for r in range(1, rows):
                    matrix[r][c] = 0    

        # Step 6: handle first row
        if first_row_zero:
            for c in range(cols):
                matrix[0][c] = 0

        # Step 7: handle first column
        if first_col_zero:
            for r in range(rows):
                matrix[r][0] = 0                                          

# ----------------------------------------
# MAIN RUN (INPUT + OUTPUT)
# ----------------------------------------
if __name__ == "__main__":

    # -------- INPUT --------
    matrix = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]

    print("Original Matrix:")
    for row in matrix:
        print(row)

    # -------- PROCESS --------
    sol = Solution()
    sol.setZeroes(matrix)

    # -------- OUTPUT --------
    print("\nMatrix After Setting Zeroes:")
    for row in matrix:
        print(row)
