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
## Solution
This is one of the first challenges on my coding interviews, and I haven't managed solving it in a limited amount of time. I tried a few times afterward, and this is the result of all the effors. 

1. **find_overlaps_v1**: Initial attempt, doesn't work. Compares each range with all other ranges, but doesn't account for overlaps properly.
2. **find_overlaps_v2**: Working solution with O(n^2) complexity. Compares each range with all others using nested loops, correctly identifies overlaps, but inefficient for larger inputs.
3. **find_overlaps_v2_1**: Improved version of v2, still O(n^2). Uses a set to track overlapping indices, then generates the result list based on those indices.
4. **find_overlaps_v3**: Working solution using a hash map, but still with O(n * m) complexity. Counts occurrences of numbers within ranges, identifies overlaps, and generates the result list based on counts.
5. **find_overlaps_v4**: Optimized solution with O(n) complexity. Sorts intervals based on start values, iterates through sorted intervals, detecting overlaps using adjacent ranges, resulting in an efficient solution.

