from typing import List

class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int: 
        xy_proj = 0  # Area of projection on xy-plane
        yz_proj = 0  # Area of projection on yz-plane
        zx_proj = 0  # Area of projection on zx-plane

        n = len(grid)  # Get the dimensions of the grid
        
        # Calculate xy_proj
        for i in range(n):
            for j in range(n):
                if grid[i][j] > 0:
                    xy_proj += 1
        
        # Calculate yz_proj
        for i in range(n):
            max_height_row = 0  # Max height in the current row
            for j in range(n):
                max_height_row = max(max_height_row, grid[i][j])
            yz_proj += max_height_row
        
        # Calculate zx_proj
        for j in range(n):
            max_height_col = 0  # Max height in the current column
            for i in range(n):
                max_height_col = max(max_height_col, grid[i][j])
            zx_proj += max_height_col
        
        # Total area of all three projections
        total_area = xy_proj + yz_proj + zx_proj
        
        return total_area

if __name__ == "__main__":
    s = Solution()
    print(s.projectionArea([[2, 1], [1, 2]]))  # Expected output: 9
    print(s.projectionArea([[1, 0], [0, 2]]))  # Expected output: 8
    print(s.projectionArea([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))  # Expected output: 14
    print(s.projectionArea([[2]]))  # Expected output: 5