# Method -1 Simple Linear Search
class pair:
  def __innit__(self):
    self.max = 0
    self.min = 0
def getMaxMin(arr: list, n: int) -> pair: 
  minmax = pair()
  
  #If there is only one element then assign max,min as the element
  
  if n == 1:
    minmax.max = arr[0]
    minmax.min = arr[0]
    return minmax
  # If there is more than one element then initialize the min max
  if arr[0] > arr[1]:
    minmax.max = arr[0]
    minmax.min = arr[1]
  else arr[0]< arr[1]:
    minmax.max = arr[1]
    minmax.min = arr[0]
  
  for i in range(2,n):
    if arr[i] > minmax.max:
      minmax.max = arr[i]      
    elif arr[i] < minmax.min:
      minmax.max = arr[i]
  return minmax
     
  
  
  #Method - 2 Tourament Method
  # Divide the array into two parts and compare the maximums and minimums of the two parts to get the maximum and the minimum of the whole array.
  
def getMinMax(low, high, arr):
  arr_max = arr[low]
  arr_min = arr[low]
  # If there is only one element
  
  if low == high:
    arr_max = arr[low]
    arr_min = arr[low]
    return (arr_max, arr_min)
  #If there is two element
  
  elif low == low+1:
    if arr[low] > arr[high]:
      arr_max = arr[low]
      arr_min = arr[high]
    else:
      arr_max = arr[high]
      arr_min = arr[low]
    return (arr_max, arr_min)
  else:
    #If there is more than two element
    mid = int((low+high) /2)
    arr_max1, arr_min1 = getMinMax(low, mid, arr)
    arr_max2, arr_min2 = getMinMAx(mid+1, high, arr)
  return (max(arr_max1,arr_max2), min(arr_min1,arr_min2))

#Derive Code
arr = [1000, 11, 445, 1, 330, 3000]
high = len(arr) - 1
low = 0
arr_max, arr_min = getMinMax(low, high, arr)
print('Minimum element is ', arr_min)
print('nMaximum element is ', arr_max)

    
  
