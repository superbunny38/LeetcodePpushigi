class TimeMap:
    def __init__(self):
        self.storage = dict()
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.storage:
            self.storage[key] = [(value,timestamp)]
        else:
            self.storage[key].append((value,timestamp))
        return

    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if key not in self.storage:
            return ans
        arr = self.storage[key]
        
        low_bs, high_bs = 0, len(arr)-1
        while low_bs<=high_bs:
            mid = (low_bs+high_bs)//2
            if arr[mid][1]<=timestamp:
                ans = arr[mid][0]
                low_bs=mid+1
            else:
                high_bs=mid-1
        return ans


                


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)