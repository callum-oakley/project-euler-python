def squareDifference(ns):
    return sum(ns) ** 2 - sum(n ** 2 for n in ns)

# squareDifference(range(1, 101)) = 25164150
