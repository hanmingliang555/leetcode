# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[[7,4,1],[8,5,2],[9,6,3]]

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        n = len(matrix)
        
        # 1. 沿主对角线翻折 (转置)
        # 注意：内层循环 j 必须从 i 开始！
        # 如果 j 从 0 开始，就会把已经换过去的数字又给换回来，等于没换！
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                
        # 2. 沿垂直中轴线翻折 (反转每一行)
        for i in range(n):
            # Python 的神级切片语法，直接原地翻转当前行
            matrix[i].reverse() 
            # 如果不用库函数，手写双指针也是极快的：
            # left, right = 0, n - 1
            # while left < right:
            #     matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
            #     left += 1
            #     right -= 1
    
def main():
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    solution.rotate(matrix)
    print(matrix)

if __name__ == "__main__":
    main()