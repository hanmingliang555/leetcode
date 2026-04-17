# 给定两个字符串 s 和 t，长度分别是 m 和 n，返回 s 中的 最短窗口 子串，使得该子串包含 t 中的每一个字符（包括重复字符）。如果没有这样的子串，返回空字符串 ""。
# 测试用例保证答案唯一。
# 示例 1：
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 解释：最小覆盖子串 "BANC" 包含来自字符串 t 的 'A'、'B' 和 'C'。

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 特判：如果超市里的货还没清单上的多，直接回家
        if len(s) < len(t):
            return ""
            
        # 1. 纯手工打造“采购清单” (完美替代 collections.Counter)
        need = {}
        for char in t:
            # 用你在 560 题学过的神技：如果字典里没有这个字符，就默认为 0，然后 +1
            need[char] = need.get(char, 0) + 1
            
        # 2. 纯手工打造“购物车” (完美替代 collections.defaultdict)
        window = {}
        # 为了防止后面在购物车里查不到报错，我们把清单上需要的货，在购物车里全初始化为 0
        for char in need:
            window[char] = 0
            
        left = 0
        right = 0
        valid = 0  # 记录已经凑齐的商品种类数
        
        start = 0
        min_len = float('inf') # 初始无穷大
        
        while right < len(s):
            # c 是刚放进购物车的货
            c = s[right]
            right += 1
            
            # 如果这件货是清单上需要的
            if c in need:
                window[c] += 1
                # 数量刚好达标，打个勾
                if window[c] == need[c]:
                    valid += 1
                    
            # 只要清单上的种类全都凑齐了，就开始精简购物车！
            while valid == len(need):
                # 记录目前发现的最小购物车尺寸
                if right - left < min_len:
                    start = left
                    min_len = right - left
                    
                # d 是准备从左边扔出去的废品
                d = s[left]
                left += 1
                
                # 如果扔掉的恰好是清单上的关键商品
                if d in need:
                    # 如果扔之前数量刚好够，扔完就不够了，赶紧把勾划掉！
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
                    
        return "" if min_len == float('inf') else s[start:start+min_len]

def main():
    solution = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"
    result = solution.minWindow(s, t)
    print(result)

if __name__ == "__main__":
    main()