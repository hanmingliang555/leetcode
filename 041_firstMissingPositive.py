# 给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。
# 请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
# 示例 1：
# 输入：nums = [1,2,0]
# 输出：3
# 解释：范围 [1,2] 中的数字都在数组中。

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # 第一遍：监考老师强行让所有人对号入座
        for i in range(n):
            # 只要这个人是本考场的（1 <= nums[i] <= n）
            # 并且他没坐在自己的专属座位上（他的专属座位应该是 nums[i] - 1）
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # 把他揪起来，换到他该去的位置！
                # 注意：为了安全交换，我们先把他该去的位置存下来
                correct_idx = nums[i] - 1
                
                # Python 经典交换语法
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
                
                # 交换完之后，原本坐在 correct_idx 的人被换到了 i 这个位置。
                # 因为用了 while，代码会继续检查这个新换过来的人需不需要也滚去他的专属座位。

        # 第二遍：重新巡视考场，找空场
        for i in range(n):
            # 1 号座位（下标0）应该坐 1，2 号座位（下标1）应该坐 2...
            # 如果谁没对号入座，说明这个正数压根没来考试！
            if nums[i] != i + 1:
                return i + 1
                
        # 如果从 1 到 n 大家都整整齐齐坐满了，那缺考的只能是 n + 1 啦！
        return n + 1

def main():
    solution = Solution()
    nums = [1,2,0]
    result = solution.firstMissingPositive(nums)
    print(result)

if __name__ == "__main__":
    main()
