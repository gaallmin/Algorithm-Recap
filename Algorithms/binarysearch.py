class BinarySearch:
    def __init__(self, data):
        self.data = data
    
    def biSearch(self, target):
        if len(self.data) == 0:
            return None
        else:
            low = 0
            high = len(self.data) -1
         
            while low <= high:
                mid = (low + high) // 2
                if target > self.data[mid]:
                    low = mid + 1
                elif target < self.data[mid]:
                    high = mid - 1
                else:
                    print('Found', mid)
                    return mid
            print("Can't Find")
            return None

data = [1,2,3,4,5,6,7]
search = BinarySearch(data)
search.biSearch(7)