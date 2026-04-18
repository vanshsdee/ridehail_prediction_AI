def test_import():
    import ridehail
    assert ridehail.__version__

def test_metrics():
    import numpy as np
    from ridehail.evaluation.metrics import mae, rmse
    a = np.array([1.0, 2.0, 3.0]); b = np.array([1.0, 2.0, 4.0])
    assert mae(a, b) > 0 and rmse(a, b) > 0
