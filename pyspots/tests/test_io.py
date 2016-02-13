from pyspots import io
import os


def test_io():
    from pyspots.data import data
    # split the data into normalized and summary
    norm_spot_data_list = [v for k, v in sorted(data.__dict__.items())
                           if 'normalized' in k]
    summary_data_list = [v for k, v in sorted(data.__dict__.items())
                         if 'QandPhiandI' in k]
    # grab one of the norm spot data sets
    norm_spot_data = norm_spot_data_list[0]
    summary_data = summary_data_list[0]
    assert len(norm_spot_data) == len(summary_data)