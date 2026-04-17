# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
# 示例 1：
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # 特判：如果没有区间，直接返回空
        if not intervals:
            return []
            
        # 1. 核心大招：按区间的起始位置（左端点）从小到大排序
        # 比如 [[15,18], [1,3]] 排序后变成 [[1,3], [15,18]]
        intervals.sort(key=lambda x: x[0])
        
        # 结果收集袋，先把排好序的第一个区间放进去打底
        merged = [intervals[0]]
        
        # 2. 从第二个区间开始挨个遍历
        for i in range(1, len(intervals)):
            # 取出当前要处理的区间
            current_interval = intervals[i]
            # 取出收集袋里最后一个区间（我们要拿它的尾巴来做对比）
            last_merged = merged[-1]
            
            # 判断是否重叠：如果当前区间的“头” <= 最后一个区间的“尾巴”
            if current_interval[0] <= last_merged[1]:
                # 重叠了！更新最后一个区间的“尾巴”为两者中最大的那一个
                # 注意：这里必须用 max，比如 [1,4] 和 [2,3] 合并，尾巴依然是 4
                last_merged[1] = max(last_merged[1], current_interval[1])
            else:
                # 没重叠，直接作为独立的新区间加进收集袋
                merged.append(current_interval)
                
        return merged
    
def main():
    solution = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    result = solution.merge(intervals)
    print(result)

if __name__ == "__main__":
    main()