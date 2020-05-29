class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1:
            return 0
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if obstacleGrid[row][col] == 1:
                    obstacleGrid[row][col] = 0
                    continue
                if row == 0 and col == 0:
                    obstacleGrid[row][col] = 1
                elif row == 0 and col != 0:
                    obstacleGrid[row][col] = obstacleGrid[row][col-1]
                elif row != 0 and col == 0:
                    obstacleGrid[row][col] = obstacleGrid[row-1][col]
                else:
                    obstacleGrid[row][col] = obstacleGrid[row][col-1] + \
                        obstacleGrid[row-1][col]
        return(obstacleGrid[-1][-1])
