# Cumulative Sum Problem 

This problem comes from the final stage of an interview process.  

The task was to write a function that takes a **series or an array of integers** and returns the cumulative sum of the sequence - with one twist:  

- Whenever the cumulative sum becomes **positive**, it should be reset to `0`.

### Example  
Input:  
```
[10, -4, 12, -16, 40, 50]
```
Output:
```
[0, -4, 0, -16, 0, 0]
```

## Solutions

I first encountered this problem during an interview, where I wrote a straightforward iterative solution that worked. Then they asked me to improve it.

Under the pressure, I completely failed to come up with a better approach, and the interviewer pointed out that it could be solved with Pandas.

Later, I revisited the problem and implemented the Pandas approach - and it turned out to be much simpler and more elegant than my original attempt.  

### 1. Iterative Approach  
A simple loop-based solution where we keep track of the cumulative sum and reset it to `0` whenever it becomes positive.  


### 2. Vectorized Pandas Approach  
A more concise and efficient solution using Pandas’ `cumsum()` and `cummax()` functions.  
This avoids manual looping and makes the logic both cleaner and faster for larger inputs.  
