# 编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

# 每行的元素从左到右升序排列。
# 每列的元素从上到下升序排列。

# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# 输出：true
# 输入：matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# 输出：false

class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # 特判：如果矩阵为空，直接返回 False
        if not matrix or not matrix[0]:
            return False
            
        m, n = len(matrix), len(matrix[0])
        
        # 1. 站上“定海神针”的位置：右上角
        row = 0
        col = n - 1
        
        # 2. 只要探测器还没越界（没跑出矩阵），就继续找
        while row < m and col >= 0:
            current = matrix[row][col]
            
            if current == target:
                return True  # 找到了！
                
            elif current > target:
                # 当前值太大，且由于列是递增的，这列下面的数更大
                # 所以抛弃这一列，往左走找小一点的数
                col -= 1
                
            else:
                # 当前值太小，且由于行是递增的，这行左边的数更小
                # 所以抛弃这一行，往下走找大一点的数
                row += 1
                
        # 走到越界都没找到，说明目标不在矩阵里
        return False

def main():
    solution = Solution()
    matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
    target = 5
    result = solution.searchMatrix(matrix, target)
    print(result)

if __name__ == "__main__":
    main()