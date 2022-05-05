//Method 1
#include<iostream>
using namespace std;
 
struct Pair{
  int max;
  int min;
}
struct Pair getMinMax(int arr[], int n)
{
  struct Pair minmax;
  int i;
  //If there is only one element
  if(n==1)
  {
    minmax.max = arr[0];
    minmax.min = arr[0];
    return minmax;
  }
  //If there are two element
  if(arr[0] > arr[1]){
    minmiax.max = arr[0];
    minmax.min = arr[1];
  }
  else{
    minmax.max = arr[1];
    minmax.min = arr[0];
  }
  //If there are more than two element
  for(i = 0; i<n; i++){
    if(arr[i] > minmax.max)
    {
      minmax.max = arr[i];
    }
    else if(arr[i] < minmax.min){
      minmax.min = arr[i];
    }
    return minmax;
  }
  
}

// Driver code
int main()
{
    int arr[] = { 1000, 11, 445,
                  1, 330, 3000 };
    int arr_size = 6;
     
    struct Pair minmax = getMinMax(arr, arr_size);
     
    cout << "Minimum element is "
         << minmax.min << endl;
    cout << "Maximum element is "
         << minmax.max;
          
    return 0;
}
 

//Method 2
// C++ program of above implementation
#include<iostream>
using namespace std;
 
struct Pair{
  int max;
  int min;  
}
struct pair getMinMax(int arr[], int low, int high){
  struct Pair minmax, mml, mmr;
  int i;
  
  //If there is one element
  if(low == high){
    minmax.max = arr[low];
    minmax.min = arr[low];    
  }
  //If there are two element
  if (high == low+1){
    if(arr[low] > arr[high]){
      minmax.max = arr[low];
      minmax.min = arr[high];
    }
    else{
      minmax.max = arr[high];
      minmax.min = arr[low];
    }
    return minmax;
  } 
  //If there are more than two element 
  mid = (low+mid)/2;
  mml = getMaxMin(arr, low, mid);
  mmr = getMaxMin(arr, mid+1, high);
  
  //Compare minimums of two parts
  if(mml.min  < mmr.min)
    minmax.min = mml.min;
  else
    minmax.min = mmr.min;
  
  //Compare maximun of two parts
  if(mml.max > mmr.max){
    minmax.max = mml.max;
  }
  else 
    minmax.max = mmr.max;
  
  return minmax;
}
