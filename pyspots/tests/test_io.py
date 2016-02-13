from pyspots import io
import os


def test_normalized_spot_io():
    path = os.path.join(os.path.split(io.__file__)[0], 'data',
                        'spots90FQ2_normalized_spot.txt')
    spots = io.read_normalized_file(path)
    assert len(spots) > 0