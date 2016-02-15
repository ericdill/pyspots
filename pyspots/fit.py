import pandas as pd
import lmfit
import numpy as np


def avrami_func(t, kA, t0, n):
    """The avrami model

    Parameters
    ----------
    t : number or np.array
    kA : float
        Rate constant
    t0 : float
        initial nucleation time
    n : number
        The dimensionality of the transformation

    Returns
    -------
    alpha : float
    """
    t = np.asarray(t)
    a = 1 - np.exp(-1*((t - t0) * kA) ** n)
    # set all values less than t0 to 0
    a[t<t0] = 0
    return a


def init_default_avrami_model(init_n=3, init_kA=10**-5, init_t0=0):
    """Initalize the default Avrami model.  This fixes n to `init_n` and
    forces `kA` to be greater than 0
    """
    m = lmfit.Model(avrami_func)
    m.set_param_hint('kA', min=0, value=init_kA)
    m.set_param_hint('n', value=3, vary=False)
    m.set_param_hint('t0', value=init_t0)
    return m

def fit(x, y, fitting_function, params):
    """Run a fit

    Parameters
    ----------
    x : array
        Independent variable
    y : array
        Dependent variable
        Note: len(x) == len(y)
    fitting_function : function
        The model function
    params : dict
        Dictionary of initial values for the paramters that 'fitting_function'
        takes. Can also be `lmfit.Parameters` object
    """
    assert len(x) == len(y)
    x = np.asarray(x)
    y = np.asarray(y)
    if params is None:
        params = model.params
