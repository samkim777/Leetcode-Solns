class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = {i:0 for i in nums} # [1,1,1,2,2,3] - > {'1':0,'2':0,'3':0}
        res = []

        for j in nums:
            numdict[j] += 1 # {'1':3, '2':2, '3':1}

        dictSet = sorted(numdict, key = numdict.get, reverse = True) # Sort in descending order
  
        for t in range(k):
            res.append(dictSet[t])

        return res           
