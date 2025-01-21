class TimeMap:
    # Key is to have key: [value,timestamp] relation
    # And for each key, run binary search to find closest to target time
    # What is this

    def __init__(self):
        self.storage = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # All the timestamp is increasing
        if key not in self.storage:
            self.storage[key] = []
        self.storage[key].append([value,timestamp])    

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.storage.get(key, []) # value time
        l,r = 0, len(values) - 1
        mid = 0
        while l <= r:
            m = (l+r) // 2
            if values[m][1] <= timestamp:
                # get larger time 
                res = values[m][0]
                l = m +1
            else:
                r = m - 1
        return res


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)