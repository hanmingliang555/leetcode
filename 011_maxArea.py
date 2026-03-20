# 给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。
# 找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
# 返回容器可以储存的最大水量。
# 说明：你不能倾斜容器。
# 示例 1：
# 输入：[1,8,6,2,5,4,8,3,7]
# 输出：49 

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height)-1
        max_area = 0 
        while left < right:
            current_width = right - left
            current_area = current_width * min(height[left], height[right])
            max_area = max(max_area, current_area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_area
    
def main():
    solution = Solution()
    height = [1,8,6,2,5,4,8,3,7]
    max_area = solution.maxArea(height)
    print(max_area)

if __name__ == "__main__":
    main()