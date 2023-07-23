# graduation-ceremony-probablity

# Run a code

To Run a code , simply run python main.py in your terminal. Make sure Python is installed on your machine.
The version used: Python 3.8

It will ask for user input for the Nth day, Make sure its an integer value.

# Code Flow

This code is designed to calculate the probability of a student not attending consecutive days of class for a given duration, n. The student can miss 0, 1, 2, or 3 consecutive days but cannot miss 4 consecutive days.

The function ways_to_attend_graduation(n) where n represents the total number of days.

dp = [[0]*4 for _ in range(n+1)] initializes a two-dimensional list (or matrix) called dp with n+1 rows and 4 columns. Each element in the matrix is initially set to 0. This matrix is used to keep track of the different ways to attend class for each day i with the condition that there are not 4 consecutive absent days.

dp[0][0] = 1 is setting the base case where the student attends on the first day. So, there's only one way for 0 days.

The outer loop for i in range(1, n+1): iterates from day 1 to day n.

Inside the outer loop, dp[i][0] = sum(dp[i-1][:4]) means that if the student attends on day i, then the total number of ways would be the sum of all the ways for the previous day i-1 (including attending and all possible consecutive absent days).

The inner loop for j in range(1, 4): iterates over possible consecutive absent days (1 to 3). Inside this loop, dp[i][j] = dp[i-1][j-1] indicates that if the student was absent on day i, then the total number of ways for this would be the total number of ways where the student was absent j-1 consecutive days till the previous day i-1.

Number of ways to attend classes would be sum(dp[n])

Finally, return str(sum(dp[n][1:])) + '/' + str(sum(dp[n])) returns the ratio of the number of ways the student can attend without missing 4 consecutive days (i.e., absent for 1, 2, or 3 days) to the total number of ways the student can attend or be absent.




