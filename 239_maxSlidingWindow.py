# # 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。
# # 返回 滑动窗口中的最大值 。
# 示例 1：

# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # 完全不用 import！用原生列表充当队列，存元素的下标
        q = []       
        # 自己造一个“队头指针”，用来代替慢吞吞的 pop(0)
        head = 0     
        ans = []
        
        for i in range(len(nums)):
            # 1. 新人入职：踢掉队尾比自己弱的人
            # 注意现在的判断条件：只要 head < len(q)，就说明队列里还有人
            while head < len(q) and nums[q[-1]] <= nums[i]:
                q.pop()
                
            # 2. 新人拿着自己的工号入队
            q.append(i)
            
            # 3. 检查队头老大是否退休（过期）
            # q[head] 是当前队头老大的工号
            if q[head] < i - k + 1:
                # 终极奥义：不删他，直接把头指针往后移一步，O(1) 极速！
                head += 1
                
            # 4. 窗口达到规模，记录老大的能力值
            if i >= k - 1:
                ans.append(nums[q[head]])
                
        return ans

def main():
    solution = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    result = solution.maxSlidingWindow(nums, k)
    print(result)

if __name__ == "__main__":
    main()