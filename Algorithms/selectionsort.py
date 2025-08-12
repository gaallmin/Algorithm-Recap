class SelectionSort:
    def __init__(self, array):
        self.array = array

    def sort(self):
        start_point = 0
        end_point = len(self.array)
        while start_point < end_point:
            smallest = self.array[start_point]
            smallest_idx = start_point
            for i in range(start_point+1, end_point):
                if self.array[i] < smallest:
                    smallest = self.array[i]
                    smallest_idx = i
    
            if smallest_idx != start_point:
                self.array[start_point], self.array[smallest_idx] = self.array[smallest_idx], self.array[start_point]
            start_point += 1
        return self.array

t1 = [5,2,9,1]
ss = SelectionSort(t1)
ss.sort()
print(ss.array)

