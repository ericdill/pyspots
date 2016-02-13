from collections import namedtuple
import numpy as np
spot = namedtuple('spot', ['idx', 'q', 'phi', 'x', 'y', 'data'])

def read_normalized_file(filepath):
    spots = []
    with open(filepath, 'r') as f:
        gen = (line for line in f.readlines())
        indices = next(gen).split()[1:]
        min_values = next(gen)
        max_values = next(gen)
        q_vals = next(gen).split()[1:]
        phi_vals = next(gen).split()[1:]
        x_vals = next(gen).split()[1:]
        y_vals = next(gen).split()[1:]
        # grab all the remaining lines
        lines = np.array([line.split() for line in gen], dtype=float).T
        # because I transposed the data set, the times are now the first line
        times = lines[0]
        # and the data is the rest
        data = np.array(lines[1:], dtype=int)
        for idx, (q, phi, d, x, y) in enumerate(
            zip(q_vals, phi_vals, data, x_vals, y_vals)):
            spots.append(spot(idx, q, phi, x, y, d))

    return spots
