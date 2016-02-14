from pyspots.data import data


def test_io():
    # split the data into normalized and summary
    # TODO rework this test to specifically poke the io functions, instead
    # of indirectly using them through loading the data from the data
    # subpackage
    norm_spot_data_list = [v for k, v in sorted(data.__dict__.items())
                           if 'normalized' in k]
    summary_data_list = [v for k, v in sorted(data.__dict__.items())
                         if 'QandPhiandI' in k]
    # grab one of the norm spot data sets
    norm_spot_data = norm_spot_data_list[0]
    summary_data = summary_data_list[0]
    assert len(norm_spot_data) == len(summary_data)
