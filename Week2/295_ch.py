import heapq
class MedianFinder:
    def __init__(self):
        self.small = []#max heap
        self.large = []#min heap

    def addNum(self, num: int) -> None:
        print("add:",num)
        if len(self.small) == 0 and len(self.large) == 0:
            heapq.heappush(self.small, -num)
            return
        elif len(self.small) == 0 and len(self.large) != 0:
            peak_large = self.large[0]
            if num>peak_large:
                peak_large = heapq.heappop(self.large)
                heapq.heappush(self.small,-peak_large)
                heapq.heappush(self.large,num)
            else:
                heapq.heappush(self.small,-num)
        elif len(self.small) != 0 and len(self.large) == 0:
            peak_small = -self.small[0]
            if num>peak_small:
                heapq.heappush(self.large,num)
            else:
                peek_small = heapq.heappop(self.small)
                heapq.heappush(self.small,-num)
                heapq.heappush(self.large,peak_small)
        else:
            peek_small,peek_large = -self.small[0],self.large[0]
            if len(self.small)<len(self.large):
                if num>peek_large:
                    popped = heapq.heappop(self.large)
                    heapq.heappush(self.large,num)
                    heapq.heappush(self.small,-popped)
                else:
                    heapq.heappush(self.small,-num)
            else:
                if num<peek_small:
                    popoped = -heapq.heappop(self.small)
                    heapq.heappush(self.small,-num)
                    heapq.heappush(self.large,popoped)
                else:
                    heapq.heappush(self.large,num)
            
    def findMedian(self) -> float:
        print("find median")
        print("small:",self.small)
        print("large:",self.large)
        if len(self.small)<len(self.large):
            peek_large = self.large[0]
            return peek_large
        elif len(self.small) == len(self.large):
            peek_small, peek_large = -self.small[0],self.large[0]
            return (peek_small+peek_large)/2
        else:
            peek_small = -self.small[0]
            return peek_small
            

mf = MedianFinder()
mf.addNum(12)
ans = mf.findMedian()
print(ans)
mf.addNum(10)
ans = mf.findMedian()
print(ans)
mf.addNum(13)
ans = mf.findMedian()
print(ans)
# mf.addNum(-4)
# ans = mf.findMedian()
# print(ans)