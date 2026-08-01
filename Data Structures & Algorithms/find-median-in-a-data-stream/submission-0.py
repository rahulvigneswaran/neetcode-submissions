class MedianFinder:

    def __init__(self):
        self.left = [] #max heap
        self.right = [] # min heap


    def addNum(self, num: int) -> None:
        heapq.heappush(self.left, num*-1)

        if self.left and self.right and self.left[0]*(-1) > self.right[0]:
            temp = heapq.heappop(self.left)*(-1)
            heapq.heappush(self.right, temp)

        if len(self.left) > len(self.right) + 1:
            temp = heapq.heappop(self.left)*-1
            heapq.heappush(self.right, temp)
        elif len(self.right) > len(self.left) + 1:
            temp = heapq.heappop(self.right)*(-1)
            heapq.heappush(self.left, temp)

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return self.left[0]*-1
        elif len(self.left) < len(self.right):
            return self.right[0]
        else:
            return (self.left[0]*-1 + self.right[0]) / 2


        
        