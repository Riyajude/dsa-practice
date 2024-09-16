class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count=0
        transpose = [[grid[j][i] for j in range(len(grid))] for i in range(len(grid))]

        for row in grid:
            for col in transpose:
                if row==col:
                    count+=1
        return count
