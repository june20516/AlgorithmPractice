# #2750
# nums = []
# for i in range(int(input())):
#     nums.append(int(input()))

# nums.sort()

# for j in nums:
#     print(j)

# #2751
def quickSort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quickSort(less) + [pivot] + quickSort(greater)

quickNums = [int(input()) for i in range(int(input()))]

# print(quickSort(quickNums))


mergeSort
def mergeSort(array):
    if len(array) < 2:
        return array
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left, right)

def merge(left, right):
    result = []
    while True:
            if len(left) == 0 or len(right) == 0:
                result += (left + right)
                return sorted
            elif left[0] <= right[0]:
                result.append(left[0])
                del left[0]
            else:
                result.append(right[0])
                del right[0]


#heap sort
def heapify(array, index, size):
    largest = index
    leftIndex = 2 * index + 1
    rightIndex = 2 * index + 2
    if leftIndex < size and array[leftIndex] > array[largest]:
        largest = leftIndex
    if rightIndex < size and array[rightIndex] > array[largest]:
        largest = rightIndex
    if largest != index:
        array[largest], array[index] = array[index], array[largest]
        heapify(array, largest, size)

def heapSort(array):
    heapSize = len(array)
    for i in range(heapSize//2-1, -1, -1):
        heapify(array, i, heapSize)
    for i in range(heapSize-1,0,-1):
        array[0], array[i] = array[i], array[0]
        heapify(array, 0, i)
    return array
unsorted = []
for i in range(int(input())):
    unsorted.append(input())
    
sorted = heapSort(list(map(int, unsorted)))

for i in sorted:
    print(i)