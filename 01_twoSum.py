from typing import List

class Solution:
    def twoSum_On2(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    def twoSum_On1(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []

def main():
    solution = Solution()
    nums = [15,7,11,2]
    target = 9
    result = solution.twoSum_On2(nums, target)
    result_On1 = solution.twoSum_On1(nums, target)
    print(f"Output: {result}")
    print(f"Output: {result_On1}")

if __name__ == "__main__":
    main()