MOD = 10**9 + 7

# Step 1: Compute row fill ways using bottom-up
def ways_to_fill_row(m):
    dp = [1] + [0] * m
    for i in range(1, m + 1):
        for size in [1, 2, 3, 4]:
            if i - size >= 0:
                dp[i] = (dp[i] + dp[i - size]) % MOD
    return dp

# Step 2: Main function
def legoBlocks(n, m):
    row_ways = ways_to_fill_row(m)
    
    # Precompute powers: row_ways[i] ** n
    row_pow = [0] * (m + 1)
    for i in range(m + 1):
        row_pow[i] = pow(row_ways[i], n, MOD)

    total = [0] * (m + 1)
    total[0] = 1  # base case (empty wall)

    for i in range(1, m + 1):
        total[i] = row_pow[i]
        for j in range(1, i):
            total[i] = (total[i] - total[j] * row_pow[i - j]) % MOD
            if total[i] < 0:
                total[i] += MOD

    return total[m]
