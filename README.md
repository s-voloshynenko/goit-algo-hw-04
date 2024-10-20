# goit-algo-hw-04

### Results

##### Array size: 100
Sort time of merge_sort for 100 size array is 0.000820 secs.\
Sort time of insertion_sort for 100 size array is 0.001043 secs.\
Sort time of timsort for 100 size array is 0.000041 secs.

##### Array size: 1000
Sort time of merge_sort for 1000 size array is 0.009790 secs.\
Sort time of insertion_sort for 1000 size array is 0.084580 secs.\
Sort time of timsort for 1000 size array is 0.000360 secs.

##### Array size: 5000
Sort time of merge_sort for 5000 size array is 0.040381 secs.\
Sort time of insertion_sort for 5000 size array is 2.189870 secs.\
Sort time of timsort for 5000 size array is 0.002513 secs.

##### Array size: 10000
Sort time of merge_sort for 10000 size array is 0.088143 secs.\
Sort time of insertion_sort for 10000 size array is 8.821037 secs.\
Sort time of timsort for 10000 size array is 0.006033 secs.

### Summary

In summary, Timsort consistently outperforms both merge sort and insertion sort, particularly on larger arrays. Insertion sort, while acceptable for small arrays, becomes inefficient as array size increases. The results showed that Timsort, which combines `O(n log n)` merge sort with `O(n²)` insertion sort for small data segments, is much more efficient in practice. This efficiency comes from using insertion sort on smaller, nearly sorted subarrays and merge sort on larger unsorted portions, optimizing the overall performance to approximately `O(n log n)` in most real-world cases. This hybrid approach makes Timsort significantly faster than using either algorithm alone, particularly on partially sorted or real-world data.