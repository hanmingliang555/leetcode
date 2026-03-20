# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。
# 示例 1:
# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。注意 "bca" 和 "cab" 也是正确答案。
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()  # 我们的“鱼塘”，专门用来快速查重
        left = 0          # 左指针，负责清理
        max_len = 0       # 记录历史最长记录
        
        # 右指针 right 主动往右走，遍历整个字符串
        for right in range(len(s)):
            # 【核心逻辑】：如果 right 指向的新字符已经存在于集合里
            # 说明有重复了！left 必须不断把最左边的字符踢出去，直到不重复为止
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
                
            # 此时窗口里肯定没有重复字符了，把新字符加进去
            char_set.add(s[right])
            
            # 计算当前窗口的长度，并更新历史最大值
            # 长度 = 右端点 - 左端点 + 1
            max_len = max(max_len, right - left + 1)
            
        return max_len

def main():
    solution = Solution()
    s = "abcabcbb"
    result = solution.lengthOfLongestSubstring(s)
    print(result)

if __name__ == "__main__":
    main()