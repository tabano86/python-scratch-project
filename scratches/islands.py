from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total_islands = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                total_islands = total_islands + (1 if self.bfs(grid, i, j) > 0 else 0)
        return total_islands

    def bfs(self, grid: List[List[str]], i: int, j: int) -> int:
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == 0:
            return 0
        grid[i][j] = 0
        coord: List[List[int]] = [[0,1],[1,0],[0,-1],[-1,0]]
        total = 0
        for c in range(0, 4):
            total = total + self.bfs(grid, i + coord[c][0], j + coord[c][1])
        return total
