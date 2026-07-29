class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums = Counter(nums)
        nums = [(-1*nums[key], key) for key in nums.keys()]
        heapq.heapify(nums)
        res = []
        for _ in range(k):
            _, n = heapq.heappop(nums)
            res.append(n)
        return res
        