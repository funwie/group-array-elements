## Divide an array into N equally sized arrays.
All arrays are not guaranteed to be equal (especially the last array in the list)

#### Example 1 = [1, 2, 3, 4, 5]

##### Example 1 output
- n: 1, result: [[1, 2, 3, 4, 5]]
- n: 2, result: [[1, 2, 3], [4, 5]]
- n: 3, result: [[1, 2], [3, 4], [5]]
- n: 4, result: [[1], [2], [3], [4, 5]]
- n: 5, result: [[1], [2], [3], [4], [5]]


#### Example 2 = list(range(1, 21))

##### Example 2 output
```
- n: 1, result: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
- n: 2, result: [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
- n: 3, result: [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20]]
- n: 4, result: [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
- n: 5, result: [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
- n: 6, result: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18, 19, 20]]
- n: 7, result: [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20]]
- n: 8, result: [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16, 17, 18, 19, 20]]
- n: 9, result: [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18, 19, 20]]
- n: 10, result: [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
- n: 11, result: [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
- n: 12, result: [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12, 13, 14, 15, 16, 17, 18, 19, 20]]
- n: 13, result: [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13, 14, 15, 16, 17, 18, 19, 20]]
- n: 14, result: [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14, 15, 16, 17, 18, 19, 20]]
- n: 15, result: [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15, 16, 17, 18, 19, 20]]
- n: 16, result: [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16, 17, 18, 19, 20]]
- n: 17, result: [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17, 18, 19, 20]]
- n: 18, result: [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18, 19, 20]]
- n: 19, result: [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19, 20]]
- n: 20, result: [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]```
