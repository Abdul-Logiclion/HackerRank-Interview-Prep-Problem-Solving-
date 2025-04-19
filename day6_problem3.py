import heapq  # Importing heapq module for using min-heap functionality

def cookies(k, A):
    # Convert the input list A into a min-heap in-place
    # After this, the smallest element will always be at index 0
    heapq.heapify(A)

    count = 0  # Counter to track the number of operations performed

    # Continue combining cookies until the smallest cookie is at least 'k'
    # and there are at least 2 cookies to combine
    while len(A) >= 2 and A[0] < k:
        # Extract the two least sweet cookies (smallest values)
        first = heapq.heappop(A)  # Least sweet cookie
        second = heapq.heappop(A) # Second least sweet cookie

        # Combine them into a new cookie with new sweetness formula:
        # new_cookie = least + 2 * second_least
        new_cookie = first + 2 * second

        # Push the new cookie back into the heap to maintain the heap structure
        heapq.heappush(A, new_cookie)

        # Increment the operation counter
        count += 1

    # After processing, if the smallest remaining cookie is still less than 'k',
    # and there's no way to combine further (only 1 cookie left), return -1
    return count if A and A[0] >= k else -1
