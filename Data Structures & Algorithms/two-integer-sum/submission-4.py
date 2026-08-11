class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}
        for i, n in enumerate(nums):
            h_map[n] = i
        print(h_map)
        for i,n in enumerate(nums):
            diff = target -n 
            if diff in h_map and h_map[diff]!=i:
                return [i,h_map[diff]]
        return []

            
        