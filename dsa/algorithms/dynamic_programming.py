"""Dynamic programming classics."""


def fibonacci(n):
    """nth Fibonacci number, O(n) time, O(1) space."""
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def climb_stairs(n):
    """Ways to climb n stairs taking 1 or 2 steps at a time."""
    return fibonacci(n + 1)


def coin_change(coins, amount):
    """Fewest coins summing to amount, or -1 if impossible."""
    INF = amount + 1
    dp = [0] + [INF] * amount
    for total in range(1, amount + 1):
        for coin in coins:
            if coin <= total and dp[total - coin] + 1 < dp[total]:
                dp[total] = dp[total - coin] + 1
    return dp[amount] if dp[amount] != INF else -1


def longest_common_subsequence(a, b):
    """Return one LCS of sequences a and b as a string or list (matching a's type)."""
    m, n = len(a), len(b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if a[i] == b[j]:
                dp[i][j] = 1 + dp[i + 1][j + 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])
    out, i, j = [], 0, 0
    while i < m and j < n:
        if a[i] == b[j]:
            out.append(a[i])
            i += 1
            j += 1
        elif dp[i + 1][j] >= dp[i][j + 1]:
            i += 1
        else:
            j += 1
    return "".join(out) if isinstance(a, str) else out


def edit_distance(a, b):
    """Levenshtein distance using O(min(m, n)) space."""
    if len(a) < len(b):
        a, b = b, a
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i] + [0] * len(b)
        for j, cb in enumerate(b, 1):
            cur[j] = min(
                prev[j] + 1,               # delete
                cur[j - 1] + 1,            # insert
                prev[j - 1] + (ca != cb),  # replace
            )
        prev = cur
    return prev[-1]


def knapsack_01(weights, values, capacity):
    """Maximum value achievable with each item used at most once."""
    dp = [0] * (capacity + 1)
    for w, v in zip(weights, values):
        for c in range(capacity, w - 1, -1):
            dp[c] = max(dp[c], dp[c - w] + v)
    return dp[capacity]


def longest_increasing_subsequence(nums):
    """Length of the longest strictly increasing subsequence. O(n log n)."""
    from bisect import bisect_left

    tails = []
    for x in nums:
        i = bisect_left(tails, x)
        if i == len(tails):
            tails.append(x)
        else:
            tails[i] = x
    return len(tails)


def max_subarray(nums):
    """Kadane's algorithm: largest sum of a non-empty contiguous subarray."""
    if not nums:
        raise ValueError("nums must be non-empty")
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best
