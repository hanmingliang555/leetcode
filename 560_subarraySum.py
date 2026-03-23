# 给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。
# 子数组是数组中元素的连续非空序列。
# 示例 1：
# 输入：nums = [1,1,1], k = 2
# 输出：2
# 示例 2：
# 输入：nums = [1,2,3], k = 3
# 输出：2

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # 历史账单本（字典）：记录【前缀和】以及它出现的【次数】
        # 极其重要的一步：初始化 {0: 1}。
        # 意思是“在还没开始遍历数组时，前缀和为 0 的情况已经出现了 1 次”。
        # 如果不加这个，从头开始且正好等于 k 的子数组就会被漏掉！
        prefix_dict = {0: 1} 
        
        current_sum = 0
        count = 0
        
        for num in nums:
            # 1. 记今天的总账
            current_sum += num
            
            # 2. 查历史账单：看看 (当前余额 - k) 这个数字以前出现过没？
            target = current_sum - k
            if target in prefix_dict:
                # 如果出现过，出现过几次，就说明有几个符合条件的子数组
                count += prefix_dict[target]
                
            # 3. 把今天的总账也登记到账单本里，留给未来的人去查
            # dict.get(key, 默认值) 是个安全获取字典值的神技
            prefix_dict[current_sum] = prefix_dict.get(current_sum, 0) + 1
            
        return count
    
def main():
    solution = Solution()
    nums = [1,1,1]
    k = 2
    result = solution.subarraySum(nums, k)
    print(result)

if __name__ == "__main__":
    main()