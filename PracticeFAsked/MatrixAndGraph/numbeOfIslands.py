
class Solution:
    def numIslands(self, grid):
        # edge case
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        # DFS function to mark connected land
        def dfs(r,c):
            # boundary check
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 
            # water or already visited
            if grid[r][c] == "0":
                return    

            # mark current land as visited
            grid[r][c] = "0"

            # explore 4 directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        # scan entire grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    islands += 1    # new island found
                    dfs(r,c)        # clear whole island   
        return islands            


# ----------------------------------------
# MAIN RUN (INPUT + OUTPUT)
# ----------------------------------------

if __name__ == '__main__':
    # -------- INPUT --------
    grid = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
        # -------- PROCESS --------
    sol = Solution()
    result = sol.numIslands(grid)

    print(result)
