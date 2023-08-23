# Remove Duplicates
You are given an unsorted array of integers. 
Your task s to remove all duplicates from the array while preserving the original order of the elements.

Examples
```
Input: [20, 21, 0, 18, 0, 2, 4, 3, 2, 1, 1]
Output: [20, 21, 0, 18, 2, 4, 3, 1]
```
# Solution
This seems so simple until they ask you to solve it within O(n).
During my interview, I managed to get it down to O(nlongn) and got stuck.
Unfortunately, I didn't realize that the `in` operation for a set is usually considered to be O(1).

1. **remove_dups_v1**: The initial "naive" approach - the first thing that came to mind. You will almost always be asked to improve it.
2. **remove_dups_v2**: The second attempt involves using  a dictionary to keep track of the first occurrence of each element along with its index. I thought of this because I didn't know what else to do and decided to throw a hashmap at the problem. Surprisingly, it turned out better than v1.
3. **remove_dups_v3**: Similar to v2, but it takes advantage of the fact that dictionary keys have preserved order since Python 3.7. This turned out to be an efficient solution.
4. **remove_dups_v4**: This is what interviewers tipically expect from you. The average time complexity of the `in` operation for a set is O(1), making this approach O(n) overall.
