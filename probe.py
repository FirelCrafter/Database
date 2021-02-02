def levenshtein_distance(self, name):
    n, m = len(self), len(name)
    if n > m:
        self, name = name, self
        n, m = m, n
    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if self[j - 1] != name[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)

    return current_row[n]


