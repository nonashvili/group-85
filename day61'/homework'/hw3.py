def delete_nth(order, n):
    result = []
    counts = {}

    for x in order:
        counts[x] = counts.get(x, 0) + 1
        if counts[x] <= n:
            result.append(x)

    return result