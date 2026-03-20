# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。
# 示例 1:
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 慢指针：指向下一个准备放非零元素的位置
        slow = 0
        
        # 快指针：遍历整个数组找非零元素
        for fast in range(len(nums)):
            # 如果快指针找到了非零元素
            if nums[fast] != 0:
                # 就把它和慢指针指向的值交换
                nums[slow], nums[fast] = nums[fast], nums[slow]
                # 慢指针往前走一步，准备迎接下一个非零元素
                slow += 1
        
def main():
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums)
    print(nums)

if __name__ == "__main__":
    main()