# class BubbleSort:
#     def __init__(self, array):
#         self.array = array
#     def sort(self): # ascending
#         j = len(self.array)
#         while j >= 1:
#             for i in range(j-1):
#                 if self.array[i] < self.array[i+1]:
#                     pass
#                 else:
#                     self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
#                 i += 1
#             j -= 1
#         return self.array

# nums = [5,2,9,1,5,6]
# bs = BubbleSort(nums)
# bs.sort()
# print(bs.array)

# Added EARLY EXIT (ADDED **SWAPPED**)
class BubbleSort:
    def __init__(self, array):
        self.array = array
    def sort(self): # ascending
        j = len(self.array)
        
        while j >= 1:
            swapped = False
            for i in range(j-1):
                if self.array[i] < self.array[i+1]:
                    pass
                else:
                    self.array[i], self.array[i+1] = self.array[i+1], self.array[i]
                    swapped = True
                    
            if not swapped:
                break
            j -= 1
        return self.array

nums = [5,2,9,1,5,6]
bs = BubbleSort(nums)
bs.sort()
print(bs.array)