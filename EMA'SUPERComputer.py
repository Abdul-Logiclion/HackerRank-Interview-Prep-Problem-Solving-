def twoPluses(grid):
    pulses = []
    rows = len(grid)
    cols = len(grid[0])
    
    # Visited array to mark already processed cells
    visited = [[False] * cols for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'G' and not visited[i][j]:
                arm = 0
                while True:
                    # Check if the plus can grow in all 4 directions
                    if (
                        i - arm >= 0 and i + arm < rows and
                        j - arm >= 0 and j + arm < cols and
                        grid[i - arm][j] == 'G' and
                        grid[i + arm][j] == 'G' and
                        grid[i][j - arm] == 'G' and
                        grid[i][j + arm] == 'G'
                    ):
                        # Mark cells as visited to avoid revisiting
                        visited[i - arm][j] = True
                        visited[i + arm][j] = True
                        visited[i][j - arm] = True
                        visited[i][j + arm] = True
                        area = 1 + arm * 4  # Center + arms
                        pulses.append(area)
                        arm += 1
                    else:
                        break

    print(pulses)
    if len(pulses) == 1:
        return pulses[0]
    else:
        pulses.sort(reverse=True)
        return pulses[0] * pulses[1]
