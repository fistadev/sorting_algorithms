# Sorting Algorithms

Study of sorting algorithms using python.

1. [Bubble Sort](#bubble)
2. [Selection Sort](#selection)
3. [Insertion Sort](#insertion)
4. [Merge Sort](#merge)
5. [Quick Sort](#quick)

&nbsp;

<a name="bubble"></a>
### Bubble Sort

Bubble Sort is one of the most straightforward sorting algorithms and the simplest one. Iterates over the list, in each iteration it compares elements in pairs and keeps swapping them such that the larger element is moved towards the end of the list.

```python
def bubbleSort(arr):
    n = len(arr)
 
    for i in range(n):
  
        for j in range(0, n-i-1):
  
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
```

* Non recursive
* Stable
* In place
* O(n²)

#
&nbsp;

<a name="selection"></a>
### Selection Sort

In this algorithm we create two segments of the list one sorted and other unsorted. We continuously remove the smallest element from the unsorted segment of the list and append it to the sorted segment. We don’t swap intermediate elements. Hence this algorithm sorts the array in minimum number of swaps.

```python
def selectionSort(array):
    for i in range(len(array)-1):
        min_idx = i
        
        for idx in range(i + 1, len(array)-1):
            if array[idx] < array[min_idx]:
                min_idx = idx
        array[i], array[min_idx] = array[min_idx], array[i]

    return array
```

* Non recursive
* Unstable
* In place
* O(n²)

#
&nbsp;

<a name="insertion"></a>
###  Insertion Sort

Like Selection Sort, in this algorithm we segment the list into sorted and unsorted parts. Then we iterate over the unsorted segment, and insert the element from this segment into the correct position in the sorted list.

```python
def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while array[j] > key and j >= 0:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key
    return array
```

* Non-recursive
* Stable
* In place
* O(n²)

#
&nbsp;

<a name="merge"></a>
### Merge Sort

Merge sort is a very efficient sorting algorithm. It’s based on the divide-and-conquer approach, a powerful algorithmic technique used to solve complex problems.

In this algorithm we split a list in half, and keeps splitting the list by 2 until it only has single element. Then we merge the sorted sorted list. We keep doing this until we get a sorted list with all the elements of the unsorted input list.

```python
def mergeSort(arr):
    if len(arr) > 1:

        r = len(arr)//2
        left = arr[:r]
        right = arr[r:]

        mergeSort(left)
        mergeSort(right)

        i = j = k = 0

       
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

       
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
```

* Recursive
* Stable
* Needs extra space
* O(nlogn)


#
&nbsp;

<a name="quick"></a>
### Quick Sort

In this algorithm we partition the list around a pivot element, sorting values around the pivot. In my solution I used the the last element from the list as pivot value. Best performance is achieved when the pivot value splits the list in two almost equal halves.

Just like merge sort, the Quicksort algorithm applies the divide-and-conquer principle to divide the input array into two lists, the first with small items and the second with large items. The algorithm then sorts both lists recursively until the resultant list is completely sorted.

Dividing the input list is referred to as partitioning the list. Quicksort first selects a pivot element and partitions the list around the pivot, putting every smaller element into a low array and every larger element into a high array.

Putting every element from the low list to the left of the pivot and every element from the high list to the right positions the pivot precisely where it needs to be in the final sorted list. This means that the function can now recursively apply the same procedure to low and then high until the entire list is sorted.


```python
def quickSort(array):
    if len(array)> 1:
        pivot=array.pop()
        grtr_lst, equal_lst, smlr_lst = [], [pivot], []
        for item in array:
            if item == pivot:
                equal_lst.append(item)
            elif item > pivot:
                grtr_lst.append(item)
            else:
                smlr_lst.append(item)
        return (quickSort(smlr_lst) + equal_lst + quickSort(grtr_lst))
    else:
        return array
```
* Recursive
* In place
* Unstable
* O(nlogn)


