class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = {}
        heap = []
        for i in nums:
            if i not in hmap:
                hmap[i] = 1
            else:
                hmap[i] += 1
        
        for num, freq in hmap.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq,num))
            else:
                heapq.heappushpop(heap, (freq,num))
        return [n[1] for n in heap]