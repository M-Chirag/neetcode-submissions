class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # freq = Counter(nums)
        #or 
        freq = {}
        for n in nums:
             freq[n] = 1 + freq.get(n, 0)

        heap = []
        

        for num, count in freq.items():
            heapq.heappush(heap,(count, num))
            if len(heap) > k:
                heapq.heappop(heap)
        return [num for count, num in heap]
        

