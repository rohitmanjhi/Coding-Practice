class Solution:
    def exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def DFS(r, c, i):
            if i == len(word):
                return True

            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False

            if board[r][c] != word[i]:
                return False 

            temp = board[r][c]
            board[r][c] = "*"

            found = (
                DFS(r+1, c, i+1) or
                DFS(r-1, c, i+1) or
                DFS(r, c+1, i+1) or
                DFS(r, c-1, i+1)
            )

            board[r][c] = temp
            return found

        for r in range(rows):
            for c in range(cols):
                if DFS(r,c,0):
                    return True  
        return False                        

# ----------------------------------------
# MAIN RUN (INPUT + OUTPUT)
# ----------------------------------------

if __name__ == '__main__':
    # -------- INPUT --------
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
        # -------- PROCESS --------
    sol = Solution()
    result = sol.exist(board, word)

    print(result)
