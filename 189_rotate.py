# 给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
# 示例 1:
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右轮转 1 步: [7,1,2,3,4,5,6]
# 向右轮转 2 步: [6,7,1,2,3,4,5]
# 向右轮转 3 步: [5,6,7,1,2,3,4]

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 时间复杂度ON，空间复杂度O1
        n = len(nums)
        # 1. 防止 k 大于数组长度，这步极其重要！
        k = k % n 
        
        # 特判：如果 k 是 0，或者数组为空，直接不用转了
        if k == 0 or n <= 1:
            return

        # 辅助函数：用来翻转 nums 在 [start, end] 区间内的元素
        def reverse(start: int, end: int) -> None:
            # 经典的双指针向中间逼近翻转
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
                
        # 魔法开始：三次翻转
        # 第 1 次：翻转所有元素
        reverse(0, n - 1)
        # 第 2 次：翻转前 k 个元素 (下标 0 到 k - 1)
        reverse(0, k - 1)
        # 第 3 次：翻转剩下的元素 (下标 k 到末尾)
        reverse(k, n - 1)
        print(nums)

    def rotate_ON(self, nums: list[int], k: int) -> None:
        # 时间复杂度ON，空间复杂度ON
        n = len(nums)
        k = k % n
        # Python 的切片赋值，极度优雅
        nums[:] = nums[-k:] + nums[:-k]
        print(nums)

def main():
    solution = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    solution.rotate(nums, k)
    solution.rotate_ON(nums, k)

if __name__ == "__main__":
    main()