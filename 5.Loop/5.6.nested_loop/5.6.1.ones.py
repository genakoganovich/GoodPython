import numpy as np
n = int(input())
a = np.ones((n, n), dtype=int)
a[:, ~0] = 5
list(map(lambda row: print(' '.join(map(str, row))), a))
