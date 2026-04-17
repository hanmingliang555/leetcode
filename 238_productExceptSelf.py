# 给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除了 nums[i] 之外其余各元素的乘积 。
# 题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。
# 请不要使用除法，且在 O(n) 时间复杂度内完成此题。
# 示例 1:
# 输入: nums = [1,2,3,4]
# 输出: [24,12,8,6]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # 初始化结果数组，全填 1。这个数组不算作额外空间！
        answer = [1] * n
        
        # 第一轮：从左往右，计算每个数字【左边】所有数字的乘积
        # left_product 就像一个滚雪球的累乘器
        left_product = 1
        for i in range(n):
            # 先把当前积攒的左边乘积填进答案里
            answer[i] = left_product
            # 然后把当前数字 nums[i] 卷进雪球里，留给下一个人用
            left_product *= nums[i]
            
        # 第二轮：从右往左，计算每个数字【右边】所有数字的乘积，并直接乘进 answer 里
        # right_product 也是一个滚雪球的累乘器，不过是从右边开始滚
        right_product = 1
        for i in range(n - 1, -1, -1):
            # answer[i] 里面现在存的是左边的乘积，直接乘上右边的乘积，大功告成！
            answer[i] *= right_product
            # 把当前数字 nums[i] 卷进右边的雪球里，留给左边的人用
            right_product *= nums[i]
            
        return answer

def main():
    solution = Solution()
    nums = [1,2,3,4]
    result = solution.productExceptSelf(nums)
    print(result)

if __name__ == "__main__":
    main()