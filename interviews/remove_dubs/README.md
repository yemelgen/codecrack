# Remove Duplicates
You are given an unsorted array of integers. 
Your task s to remove all duplicates from the array while preserving the original order of the elements.

Examples
```
Input: [20, 21, 0, 18, 0, 2, 4, 3, 2, 1, 1]
Output: [20, 21, 0, 18, 2, 4, 3, 1]
```
# Solution
This challenge look simple - until they asked me to solve it in O(n) time complexity.

During the interview, I managed to get it down to O(n log n), but got stuck trying to go further.
What I didn't realize at the time: checking membership with a set is O(1) on average, which makes all the difference in optimizing this problem.

History:
1. **remove_dups_v1**: This was the first solution that came to mind - a basic, naive approach. During the interview, they immediately asked me to improve it.
2. **remove_dups_v2**: The second attempt involves using a dict to keep track of the first occurrence of each element along with its index. I thought of this because I didn't know what else to do and decided to throw a hashmap at the problem. Surprisingly, it turned out better than v1.
3. **remove_dups_v3**: Improved version of v2 that leverages the fact that Python dicts preserve insertion order since version 3.7. This turned out to be an efficient solution.
4. **remove_dups_v4**:  The "expected" solution in interviews. It uses a set for constant-time lookups and a list for building the result. This approach O(n) and performs well even on large inputs.
