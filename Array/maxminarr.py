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
  
