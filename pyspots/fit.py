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


def do_fit(t, normed):
    model = init_default_avrami_model()
    # fit the full dataset to get a good estimate of t0
    first_fit = model.fit(normed, t=t, t0=1)
    # then fit it again after we have a good idea of t0, but only fit
    # alpha < 0.5 and fit until it converges
    max_calls = 100
    def is_converged(p1, p2):
        p1 = abs(p1)
        p2 = abs(p2)
        diff = ((p1 - p2) / p1)
        print("difference between %s and %s is %s" % (p1, p2, diff))
        return abs(diff) < 0.01
    first_half = normed < 0.5
    ncalls = 0
    fits = [first_fit]
    prev_fit = first_fit
    while ncalls < max_calls:
        new_fit = model.fit(normed[first_half], prev_fit.params, t=t[first_half])
        fits.append(new_fit)
        if np.all([is_converged(new_fit.best_values[k], prev_fit.best_values[k]) for k in prev_fit.best_values]):
            break
        prev_fit = new_fit
        ncalls += 1
    return fits