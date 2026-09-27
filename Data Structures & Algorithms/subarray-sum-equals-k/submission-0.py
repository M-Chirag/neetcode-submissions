class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        freq = {0:1}
        curr_prefix = 0

        for n in nums:
            curr_prefix += n 
            old_prefix = curr_prefix - k
            ans += freq.get(old_prefix, 0) 

            freq[curr_prefix] = 1 + freq.get(curr_prefix, 0)
        return ans

        