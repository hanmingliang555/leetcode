# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。
# 示例 1：
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 1. 灵魂第一步：必须排序！
        nums.sort()
        ans = []
        n = len(nums)
        
        # 2. 遍历数组，选定“老大” nums[i]
        # 因为至少要留两个位置给小弟，所以循环到 n-2 就可以了
        for i in range(n - 2):
            # 【终极优化】：因为数组排过序了，如果老大自己都大于 0，
            # 后面的小弟肯定也大于 0，三个正数相加绝不可能等于 0，直接结束战斗！
            if nums[i] > 0:
                break
                
            # 【老大去重】：如果老大和前任一样，直接跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            # 3. 召唤左右双指针小弟
            left = i + 1
            right = n - 1
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total < 0:
                    left += 1   # 太小了，左边往右挪，找个大点的
                elif total > 0:
                    right -= 1  # 太大了，右边往左挪，找个小点的
                else:
                    # 找到啦！赶紧记进小本本
                    ans.append([nums[i], nums[left], nums[right]])
                    
                    # 【左小弟去重】：如果下一个人长得一样，跨过去
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # 【右小弟去重】：如果前一个人长得一样，跨过去
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                        
                    # 找完一组后，两个小弟同时往中间走一步，继续找其他的可能
                    left += 1
                    right -= 1
                    
        return ans

def main():
    solution = Solution()
    nums = [-1,0,1,2,-1,-4]
    result = solution.threeSum(nums)
    print(result)

if __name__ == "__main__":
    main()