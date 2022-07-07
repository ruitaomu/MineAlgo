from pythoncraft.codechallenge import Sort

def bubbleSort(arr):
    n = len(arr)
    steps = 0
 
    # 遍历所有数组元素
    for i in range(n):
 
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
                steps += 1
                pyc_sort.update(arr)
    return steps

def heapify(arr, n, i):
    steps = 0 
    largest = i  
    l = 2 * i + 1     # left = 2*i + 1 
    r = 2 * i + 2     # right = 2*i + 2 
  
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i]  # 交换
        pyc_sort.update(arr)
        steps += 1
  
        steps += heapify(arr, n, largest)

    return steps 
  
def heapSort(arr):
    steps = 0 
    n = len(arr) 
  
    # Build a maxheap. 
    for i in range(n, -1, -1): 
        steps += heapify(arr, n, i) 
  
    # 一个个交换元素
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i]   # 交换
        pyc_sort.update(arr)
        steps += 1
        steps += heapify(arr, i, 0) 
    
    return steps

#Program starts from here:
pyc_sort = Sort()

#Get the unsorted array by PythonClass.array(), then pass it to my own sorting function
steps = bubbleSort(pyc_sort.array())

pyc_sort.postToChat("Done! Total use steps: "+str(steps))