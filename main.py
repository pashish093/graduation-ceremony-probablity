def ways_to_attend_graduation(n):
    dp = [[0]*4 for ele in range(n+1)] 
    dp[0][0] = 1  # Setting the base case where the student attends on the first day. So, there's only one way for 0 days.
    for i in range(1, n+1):
        # If student attends on day i , number of ways will be sum of all previous ways.
        dp[i][0] = sum(dp[i-1][:4])
        # Iterates over possible absent days, 
        for j in range(1, 4):
            dp[i][j] = dp[i-1][j-1]
    number_ways_to_attend_class = sum(dp[n])
    print(f"The number of ways to attend classes over N days is ---> {number_ways_to_attend_class}")
    return str(sum(dp[n][1:])) + '/' + str(number_ways_to_attend_class)


try:
    user_input = int(input("Please enter your input for N value for graduation day - "))
    result = ways_to_attend_graduation(user_input)
    print(f"The probability that you will miss your graduation ceremony ---> {result}")
except ValueError:
    print("Accepted value will only be integer, Please enter only integer value")