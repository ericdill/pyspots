import os
from pyspots.io import read_normalized_file, read_spot_summary_file


class _Data():
    def __init__(self, datapath=None):
        super(_Data, self).__init__()
        # default to the files in this directory
        if datapath is None:
            datapath = os.path.split(__file__)[0]
        d = {}
        self.__dict__ = d
        # find all data files in `datapath`
        data_files = [f for f in os.listdir(datapath) if f.endswith('.dat')]
        for data_file in data_files:
            full_path = os.path.join(datapath, data_file)
            # pick the correct io reader
            if data_file.endswith('normalized_spot.dat'):
                data = read_normalized_file(full_path)
            elif data_file.endswith('QandPhiandI.dat'):
                data = read_spot_summary_file(full_path)
            self.__dict__[os.path.splitext(data_file)[0]] = data

data = _Data()