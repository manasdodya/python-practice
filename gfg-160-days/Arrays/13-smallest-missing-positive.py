def smallest_missing_positive(arr):
    n = len(arr)
    
    # Step 1: Replace out-of-range numbers with a dummy value (n+1)
    for i in range(n):
        if arr[i] <= 0 or arr[i] > n:
            arr[i] = n + 1
    
    # Step 2: Use index marking
    for i in range(n):
        num = abs(arr[i])
        if 1 <= num <= n:
            arr[num - 1] = -abs(arr[num - 1])
    
    # Step 3: Find the first missing positive number
    for i in range(n):
        if arr[i] > 0:
            return i + 1
    
    # If all numbers from 1 to n are present
    return n + 1

# Example usage
print(smallest_missing_positive([2, -3, 4, 1, 1, 7]))  # Output: 3
print(smallest_missing_positive([5, 3, 2, 5, 1]))      # Output: 4
print(smallest_missing_positive([-8, 0, -1, -4, -3]))  # Output: 1
