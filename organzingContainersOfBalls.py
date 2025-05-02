def organizingContainers(container):
    column_sums = []
    row_sums = []
    n = len(container)

    for j in range(n):
        colSum = 0
        for i in range(n):
            colSum += container[i][j]
        column_sums.append(colSum)

    for i in range(n):
        rowSum = 0
        for j in range(n):
            rowSum += container[i][j]
        row_sums.append(rowSum)

    row_sums.sort()
    column_sums.sort()

    if row_sums == column_sums:
        return "Possible"
    else:
        return "Impossible"