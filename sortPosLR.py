import numpy as np
def aaa(input, pos):
    pos_idx = np.argsort(pos)
    input_sort = [input[i] for i in pos_idx]
    return input_sort