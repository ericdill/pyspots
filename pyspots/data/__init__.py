from ..io import read_normalized_file, read_spot_summary_file
import os

def _get_data():
    datapath = os.path.split(__file__)[0]
    data_files = [f for f in os.listdir(datapath) if f.endswith('.txt')]

    d = object()
    for data_file in data_files:
        full_path = os.path.join(datapath, data_file)
        if data_file.endswith('normalized_spot.txt'):
            data = read_normalized_file(full_path)
        elif data_file.endswith('QandPhiandI.txt'):
            data = read_spot_summary_file(full_path)
        d.__setattr__(os.path.splitext(data_file)[0], data)

    return d


data = _get_data()