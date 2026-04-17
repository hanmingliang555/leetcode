# 给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。
# 示例 1：
# 输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
# 输出：[[1,0,1],[0,0,0],[1,0,1]]

class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        
        # 这个变量专门用来记录【第一列】原本有没有 0
        col0_is_zero = False
        
        # 1. 第一遍扫荡：把 0 的标记打在第一行和第一列上
        for i in range(m):
            # 先检查第一列的这个元素是不是 0，如果是，做好标记
            if matrix[i][0] == 0:
                col0_is_zero = True
                
            # 然后检查这一行后面的元素（注意 j 从 1 开始！）
            for j in range(1, n):
                if matrix[i][j] == 0:
                    # 在行首和列首打上 0 的标记
                    matrix[i][0] = 0
                    matrix[0][j] = 0
                    
        # 2. 第二遍扫荡：根据边缘的标记，把【内部】的元素置零
        # 注意：这里我们只处理 i从1开始，j从1开始的内部区域
        # 因为我们要留着第一行和第一列的标记最后再处理！
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # 3. 处理边缘：处理第一行
        # 如果 matrix[0][0] 是 0，说明第一行原本就有 0，或者内部有 0 映射上来了
        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0
                
        # 4. 处理边缘：处理第一列
        # 如果我们最开始请的那个专属保镖是 True，说明第一列全得变成 0
        if col0_is_zero:
            for i in range(m):
                matrix[i][0] = 0
        
        return matrix

def main():
    solution = Solution()
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    result = solution.setZeroes(matrix)
    print(result)

if __name__ == "__main__":
    main()