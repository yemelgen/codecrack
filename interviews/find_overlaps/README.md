# Find Overlaps
Given an input list of integer ranges, find and output the ranges that overlap with at least 1 other range.
Two ranges are considered overlapping even if they only touch on the boundaries.
For instance, (40, 52) and (52, 60) are considered overlapping because "52" is shared.

The order of ranges in the output is not important.

If a range appears more than once in the list, then it is considered an overlap with other instances of the
same range, the range must appear in the output as many times as it does in the input.
Input 3 illustrates such a case.

Feel free to define your own data structures.

The code should be maintainable, reusable and well tested.


Examples
```
 Input 1:
 [
    (1, 10),
    (15, 20),
    (101, 110),
 ]

 Output 1:
 [
 ]

 Input 2:
 [
    (1, 10),
    (15, 20),
    (101, 110),
    (18, 22),
 ]

 Output 2:
 [
    (15, 20),
    (18, 22),
 ]

 Input 3:
 [
    (1, 10),
    (15, 20),
    (101, 110),
    (1, 10),
    (1, 10),
    (105, 120),
 ]


 Output 3:
 [
    (1, 10),
    (1, 10),
    (1, 10),
    (101, 110),
    (105, 120),
 ]

 Input 4:
 [
    (1, 10),
    (15, 20),
    (101, 110),
    (18, 30),
    (27, 35),
 ]

 Output 4:
 [
    (15, 20),
    (18, 30),
    (27, 35),
 ]

 Input 5:
 [
    (5, 10),
    (301, 400),
    (180, 200),
    (100, 300),
    (120, 150),
    (160, 170),
    (195, 220),
 ]

 Output 5:
 [
    (180, 200),
    (100, 300),
    (120, 150),
    (160, 170),
    (195, 220),
 ]
 ```
## Solutions

This was one of the first coding challenges I encountered in a technical interview. I wasn't able to solve it within the time limit, but I revisited it multiple times afterward -each time refining my approach.

History:
1. **find_overlaps_v1**: My initial attempt - a basic nested loop comparing every range, but failed to identify overlaps correctly.
2. **find_overlaps_v2**: A working brute-force solution with O(n^2) complexity. It correctly detects overlaps using using nested loops, but is inefficient for large inputs.
3. **find_overlaps_v2_1**: A slightly cleaner O(n^2) version of v2.
4. **find_overlaps_v3**: Uses a hash map to count how many ranges cover each number. Complexity O(n * m) where m is the range width. Better structure, but not optimal.
5. **find_overlaps_v4**: Optimized and final solution. Uses sorting to bring down the complexity to O(n log n). Iterates through sorted ranges and efficiently detects overlaps using only adjacent comparisons.
