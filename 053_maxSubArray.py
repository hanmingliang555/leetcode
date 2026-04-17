# 给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 子数组是数组中的一个连续部分。
# 示例 1：
# 输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
# 输出：6
# 解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        # 第一天开始，手里攥着的钱和历史最高纪录，都是第一个数字
        current_sum = nums[0]
        max_sum = nums[0]
        
        # 从第二天（下标 1）开始遍历
        for i in range(1, len(nums)):
            num = nums[i]
            
            # 核心法则：如果之前的积累是烂账（负数），就果断扔掉，从自己重新开始
            # 如果之前的积累是正的，就加到自己身上继续做大做强
            # 等价于：current_sum = max(num, current_sum + num)
            if current_sum < 0:
                current_sum = num
            else:
                current_sum += num
                
            # 每天结算后，看看有没有打破历史最高纪录
            max_sum = max(max_sum, current_sum)
            
        return max_sum
    
def main():
    solution = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    result = solution.maxSubArray(nums)
    print(result)

if __name__ == "__main__":
    main()