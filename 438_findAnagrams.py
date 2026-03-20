# 给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。
# 示例 1:
# 输入: s = "cbaebabacd", p = "abc"
# 输出: [0,6]
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        s_len, p_len = len(s), len(p)
        
        # 特判：如果 s 比 p 还短，绝不可能有子串，直接返回空
        if s_len < p_len:
            return []
            
        ans = []
        # 用长度为 26 的数组代替字典，记录 a-z 出现的次数
        p_count = [0] * 26
        window_count = [0] * 26
        
        # 1. 统计模板串 p 的字母频率
        for char in p:
            p_count[ord(char) - ord('a')] += 1
            
        # 2. 初始化我们的第一个窗口（也就是 s 的前 p_len 个字符）
        for i in range(p_len):
            window_count[ord(s[i]) - ord('a')] += 1
            
        # 检查这第一框是不是就中了
        if window_count == p_count:
            ans.append(0)
            
        # 3. 框子开始向右滑动！
        # i 表示此时刚进入框子右边的新字母的下标
        for i in range(p_len, s_len):
            # 右边吞进一个新字母：频率 +1
            window_count[ord(s[i]) - ord('a')] += 1
            
            # 左边吐出一个老字母：频率 -1
            # 老字母的下标是 i - p_len
            left_char = s[i - p_len]
            window_count[ord(left_char) - ord('a')] -= 1
            
            # 每次滑动完，核对两张表是否一致
            if window_count == p_count:
                # 记录框子最左端的起始下标
                ans.append(i - p_len + 1)
                
        return ans

def main():
    solution = Solution()
    s = "cbaebabacd"
    p = "abc"
    result = solution.findAnagrams(s,p)
    print(result)

if __name__ == "__main__":
    main()