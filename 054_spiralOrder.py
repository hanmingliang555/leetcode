# 给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。
# 示例 1：
# 输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        # 特判：如果是空矩阵，直接返回
        if not matrix:
            return []
            
        res = []
        # 初始化四堵墙的位置
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        
        # 只要墙还没撞在一起（交错），就继续剥皮
        while top <= bottom and left <= right:
            
            # 1. 从左到右，贴着【上边界】走
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1  # 上墙往下压
            
            # 2. 从上到下，贴着【右边界】走
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1  # 右墙往左压
            
            # 🚨 极其致命的陷阱防御：
            # 因为刚才 top 和 right 都改变了，矩阵可能早就被剥成“一条线”了！
            # 如果不检查 top <= bottom，它可能会把中间那条线又倒着打印一遍！
            if top <= bottom:
                # 3. 从右到左，贴着【下边界】走
                # 看！这不就是你刚学过的倒序遍历吗？走到 left 停下，所以终点是 left - 1
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1  # 下墙往上推
                
            # 同理，必须再次检查左右墙是否交错
            if left <= right:
                # 4. 从下到上，贴着【左边界】走
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1  # 左墙往右推
                
        return res

def main():
    solution = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    result = solution.spiralOrder(matrix)
    print(result)

if __name__ == "__main__":
    main()