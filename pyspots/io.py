from collections import namedtuple
import numpy as np

# Store each column of output from Ramdog as a 'spot' namedtuple
spot = namedtuple('spot', ['idx', 'q', 'phi', 'x', 'y', 'data'])


def read_normalized_file(filepath):
    """
    Read in the Ramdog output file that ends with '_normalized_spot.txt'

    Parameters
    ----------
    filepath : str
        The path to the output file

    Returns
    -------
    spots : list
        List of `spot` namedtuples that contain the following fields.
        idx : int
            Incremental index that goes from 0 -> num_spots
        q : float
            The q value of the spot center
        phi : float
            The angluar position on the 2-D detector of the spot center
        x : float
            Sub-pixel resolution spot center in x
        y :
            Sub-pixel resolution spot center in y
        data : array
            The intensity data of the spot in all frames
    """
    spots = []
    with open(filepath, 'r') as f:
        gen = (line for line in f.readlines())
        indices = next(gen).split()[1:]
        # Discard the min/max values of the spot because `np.min()` and
        # `np.max()` are a thing
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
