def bubbleSort(arr):
    n = len(arr)
  
    # Traverse through all array elements
    for i in range(n):
  
        # Last i elements are already in place
        for j in range(0, n-i-1):
  
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
  
# Driver code to test above
sample_arr = [5,1,3,8,4,7,2,9,0,6]
  
bubbleSort(sample_arr)
  
print ("Sorted array is:")
for i in range(len(sample_arr)):
    print ("%d" %sample_arr[i]), 




