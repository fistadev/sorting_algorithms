# Sorting Algorithms

Study of sorting algorithms using python.

&nbsp;

### Bubble Sort

Bubble Sort is one of the most straightforward sorting algorithms. Its name comes from the way the algorithm works: With every new pass, the largest element in the list “bubbles up” toward its correct position.

Bubble sort consists of making multiple passes through a list, comparing elements one by one, and swapping adjacent items that are out of order.

#
&nbsp;

###  Insertion Sort

Like bubble sort, the insertion sort algorithm is straightforward to implement and understand. But unlike bubble sort, it builds the sorted list one element at a time by comparing each item with the rest of the list and inserting it into its correct position. This “insertion” procedure gives the algorithm its name.

An excellent analogy to explain insertion sort is the way you would sort a deck of cards. Imagine that you’re holding a group of cards in your hands, and you want to arrange them in order. You’d start by comparing a single card step by step with the rest of the cards until you find its correct position. At that point, you’d insert the card in the correct location and start over with a new card, repeating until all the cards in your hand were sorted.

#
&nbsp;

### Selection Sort

Selection sort is an in-place comparison sorting algorithm. It has an O(n2) time complexity, which makes it inefficient on large lists, and generally performs worse than the similar insertion sort. Selection sort is noted for its simplicity and has performance advantages over more complicated algorithms in certain situations, particularly where auxiliary memory is limited.

#
&nbsp;

### Merge Sort

Merge sort is a very efficient sorting algorithm. It’s based on the divide-and-conquer approach, a powerful algorithmic technique used to solve complex problems.

To properly understand divide and conquer, you should first understand the concept of recursion. Recursion involves breaking a problem down into smaller subproblems until they’re small enough to manage. In programming, recursion is usually expressed by a function calling itself.

#
&nbsp;

### Quick Sort

Just like merge sort, the Quicksort algorithm applies the divide-and-conquer principle to divide the input array into two lists, the first with small items and the second with large items. The algorithm then sorts both lists recursively until the resultant list is completely sorted.

Dividing the input list is referred to as partitioning the list. Quicksort first selects a pivot element and partitions the list around the pivot, putting every smaller element into a low array and every larger element into a high array.

Putting every element from the low list to the left of the pivot and every element from the high list to the right positions the pivot precisely where it needs to be in the final sorted list. This means that the function can now recursively apply the same procedure to low and then high until the entire list is sorted.


