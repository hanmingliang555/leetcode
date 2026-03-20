# 给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。
# 请你设计并实现时间复杂度为 O(n) 的算法解决此问题。
# 示例 1：
# 输入：nums = [100,4,200,1,3,2]
# 输出：4
# 解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # 特判：如果数组为空，直接返回 0
        if not nums:
            return 0
            
        # 1. 把列表转换成集合，去重并实现 O(1) 的查找速度，注意这里的set去重了，但是获得的set_nums顺序和set不一样
        num_set = set(nums)
        longest_streak = 0
        
        # 2. 遍历集合中的每一个数字
        for num in num_set:
            # 3. 判断当前数字是不是某个连续序列的“开头（龙头）”
            # 如果 num - 1 不在集合里，说明没人排在它前面，它就是开头
            if (num - 1) not in num_set:
                current_num = num
                current_streak = 1
                
                # 4. 既然找到了开头，就顺藤摸瓜，不断加 1 往后找
                while (current_num + 1) in num_set:
                    current_num += 1
                    current_streak += 1
                    
                # 5. 更新历史最长记录
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak
def main():
    solution = Solution()
    nums = [100, 4, 200, 1, 3, 2, 1, 5]
    result = solution.longestConsecutive(nums)
    print(result)

if __name__ == "__main__" :
    main()