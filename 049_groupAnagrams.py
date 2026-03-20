

class Solution:
    def groupAnagrams_Onklogk(self, strs: list[str]) -> list[list[str]]:
        ans = {}  # 使用普通的空字典
        
        for s in strs:
            key = "".join(sorted(s))

            # 【核心改变】手动检查 Key 是否存在
            if key not in ans:
                # 如果这个身份证第一次出现，先给它建一个专属的空列表
                ans[key] = []
                
            # 现在可以放心地把单词塞进去了
            ans[key].append(s)
            
        # 返回字典中所有的列表
        return list(ans.values())

    def groupAnagrams_Onk(self, strs: list[str]) -> list[list[str]]:
            ans={}

            for s in strs:
                # 创建一个长度为 26 的计数器，初始全为 0
                # count[0] 代表 'a' 的数量，count[1] 代表 'b'，以此类推
                count = [0] * 26
                
                for char in s:
                    # 利用 ord() 计算字符在 0-25 之间的位置
                    count[ord(char) - ord('a')] += 1
                # 注意：列表不能直接做字典的 Key，必须转成元组（不可变类型）
                key = tuple(count)

                if key not in ans.keys():
                    ans[key] = []
                ans[key].append(s)
                
                # ans.setdefault(key, []).append(s)
                
            return list(ans.values())

def main():
    solution = Solution()
    input = ["eat","tea","tan","ate","nat","bat"]
    output_1 = solution.groupAnagrams_Onklogk(input)
    output_2 = solution.groupAnagrams_Onk(input)
    print(output_1)
    print(output_2)


if __name__ == "__main__":
    main()