class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        soln = [[] for _ in range(len(nums) + 1)]

        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] += 1
        
        for num, count in hmap.items():
            soln[count].append(num) 
        
        res = []
        for i in range(len(soln) -1, -1,-1):
            for num in soln[i]:
                res.append(num)
                if len(res) == k:
                    return res