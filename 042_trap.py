# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
# 示例 1：
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

class Solution:
    def trap(self, height: list[int]) -> int:
        # 特判：如果数组为空，直接返回 0
        if not height:
            return 0
            
        # 1. 初始化双指针在两端
        left = 0
        right = len(height) - 1
        
        # 2. 记录左右两边见过的历史最高墙
        left_max = height[left]
        right_max = height[right]
        
        # 3. 记录总蓄水量
        total_water = 0
        
        # 4. 双指针开始对撞
        while left < right:
            # 谁的历史最高墙矮，谁就计算积水并往前走
            if left_max < right_max:
                left += 1
                # 更新左边的历史最高墙
                left_max = max(left_max, height[left])
                # 计算当前柱子的积水量（历史最高墙 - 当前高度）
                # 注意：因为 left_max 刚刚更新过，所以 left_max 绝不会小于 height[left]
                # 这里算出来的值最小也就是 0，不可能出现负数
                total_water += left_max - height[left]
            else:
                right -= 1
                # 更新右边的历史最高墙
                right_max = max(right_max, height[right])
                # 计算当前柱子的积水量
                total_water += right_max - height[right]
                
        return total_water

def main():
    solution = Solution()
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    result = solution.trap(height)
    print(result)

if __name__ == "__main__":
    main() 