

def test_data_smoke():
    """Basically make sure that we are reading in data
    """
    from pyspots import data
    assert len(data.data.__dict__) > 0
