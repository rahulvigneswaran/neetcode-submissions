class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for _ in range(len(nums)+1)]
        nums = Counter(nums)
        for n, val in nums.items():
            bucket[val].append(n)
        res = []
        for i in range(len(bucket)-1, -1, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res) == k:
                    return res

        