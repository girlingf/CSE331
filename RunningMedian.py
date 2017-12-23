import heapq


class RunningMedian:

    def __init__(self):
        """
        @pre: constructor was properly called 
        @post: 4 values are initialized
        - minH  an array that represents a heap of elements
        - maxH an array that represents a heap of elements 
        - minL  size/length of minH
        - maxL = size/length of maxH
        """
        self.minH = []
        self.maxH = []
        self.minL = 0
        self.maxL = 0

    def heapq_remove(self, heap, index):
        """
        @pre: takes in index of value to remove
        @post: removes that value from the given heap 
        Helper function to take in a given heap, and index of a desired remove value 
        and removes it with the help of heapq function
        *** completely optional to use, not required.
        """
        while index > 0:
            up = (index + 1) / 2 - 1
            heap[int(index)] = heap[int(up)]
            index = up

        heapq.heappop(heap)
    
    def balance_heaps(self, h1, h2):
        """
        @pre: 2 heaps taken as input
        @post: the heaps are balanced
        The purpose of this method is to balance the two heaps so they have an equal number of elements or a difference
        of one.
        """
        heapq.heappush(h2, heapq.heappop(h1))

    def get_median(self):
        """
        @pre: there are 2 present heaps 
        @post: Known median post operation   
        returns the median value 
        """
        if self.maxL == self.minL:
            med = (self.maxH[0] + self.minH[0])/2

        else:
            if self.maxL > self.minL:
                med = self.maxH[0]

            else:
                med = self.minH[0]

        return med

    def find_median(self, command):
        """
        @pre: string with valid command as first char and number as last chars 
        @post: returns a valid median value (AS A INTEGER)
        parses commands does proper ordering to find the median  
        """

        command, val = command.strip().split()
        val = int(val)

        if command == 'a':
            if self.maxL == 0 or val < self.maxH[0]:
                heapq.heappush(self.maxH, val)
                self.maxL += 1
            else:
                heapq.heappush(self.minH, val)
                self.minL += 1

        else: 
            if self.maxL > 0 and val <= self.maxH[0]:
                self.heapq_remove(self.maxH, self.maxH.index(val))
                self.maxL -= 1

            else:
                self.heapq_remove(self.minH, self.minH.index(val))
                self.minL -= 1

        heapq._heapify_max(self.maxH)
        heapq.heapify(self.minH)

        if (self.maxL - self.minL) > 1:

            self.balance_heaps(self.maxH, self.minH)
            self.maxL -= 1
            self.minL += 1
            heapq._heapify_max(self.maxH)
            heapq.heapify(self.minH)

        if (self.minL - self.maxL) > 1:

            self.balance_heaps(self.minH, self.maxH)
            self.minL -= 1
            self.maxL += 1
            heapq._heapify_max(self.maxH)
            heapq.heapify(self.minH)

        return self.get_median()
