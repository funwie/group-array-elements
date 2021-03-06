## Divide an array into N equally sized arrays.
All arrays are not guaranteed to be equal (especially the last array in the list)

#### Example 1 = [1, 2, 3, 4, 5]

##### Example 1 output
- n: 1, = [[1, 2, 3, 4, 5]]
- n: 2, = [[1, 2, 3], [4, 5]]
- n: 3, = [[1, 2], [3, 4], [5]]
- n: 4, = [[1], [2], [3], [4, 5]]
- n: 5, = [[1], [2], [3], [4], [5]]


#### Example 2 = list(range(1, 21))

##### Example 2 output
```
- n: 1, = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
- n: 2, = [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
- n: 3, = [[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14], [15, 16, 17, 18, 19, 20]]
- n: 4, = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20]]
- n: 5, = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16], [17, 18, 19, 20]]
- n: 6, = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18, 19, 20]]
- n: 7, = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18], [19, 20]]
- n: 8, = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16, 17, 18, 19, 20]]
- n: 9, = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18, 19, 20]]
- n: 10, = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [15, 16], [17, 18], [19, 20]]
- n: 11, = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
- n: 12, = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12, 13, 14, 15, 16, 17, 18, 19, 20]]
- n: 13, = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13, 14, 15, 16, 17, 18, 19, 20]]
- n: 14, = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14, 15, 16, 17, 18, 19, 20]]
- n: 15, = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15, 16, 17, 18, 19, 20]]
- n: 16, = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16, 17, 18, 19, 20]]
- n: 17, = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17, 18, 19, 20]]
- n: 18, = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18, 19, 20]]
- n: 19, = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19, 20]]
- n: 20, = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10], [11], [12], [13], [14], [15], [16], [17], [18], [19], [20]]```
