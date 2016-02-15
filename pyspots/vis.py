import matplotlib.pyplot as plt
import numpy as np
from .fit import avrami_func
# Let's create a helper function to plot our data for us, since it is
# growing into a reasonably large piece of code.
def plot_fit_against_full_dataset(axes, full_time, full_data, fit,
                                  title=None, model=avrami_func):
    if axes is None:
        fig, axes = plt.subplots(ncols=2, figsize=(10,5))
    ax1, ax2 = axes
    fit_time = fit.userkws['t']
    fit_data = fit.data
    ax1.plot(fit_time, fit_data, 'ko', ms=10, label='Data used for fitting')
    ax1.plot(fit_time, fit.best_fit, 'r-', linewidth=3, label='Fit')
    ax1.plot(fit_time, (fit_data - fit.best_fit) - 0.15, 'ko-', linewidth=2,
             label="Residuals")
    ax1.plot(fit_time, [-0.15] * len(fit_time), 'k--', linewidth=1)
    ax1.legend(loc=0)
    t0 = fit.best_values['t0']
    arrow = np.asarray([.4, -.2, 3, .1]) * ax1.get_ylim()[1]
    ax1.arrow(t0, arrow[0], 0, arrow[1], head_width=arrow[2],
              head_length=arrow[3], fc='k', ec='k')
    ax1.text(t0, arrow[0], 't0')
    ax1.set_xlabel("Time (arb)")
    ax1.set_ylabel("Normalized Intensity, "r"$\alpha$")
    ax1.set_title('Fit values')


    # use a dictionary comprehension to extract the values of the parameters
    # compute the model against the time range
    full_model = model(full_time, **fit.best_values)
    # zero out all values before t0
    full_model[full_time < fit.params['t0']] = 0
    ax2.plot(full_time, full_data, 'ko', ms=10, label='Full dataset')
    ax2.plot(full_time, full_model, 'c-', linewidth=3, label='Full fit')
    ax2.plot(full_time, (full_data - full_model) - 0.15, 'ko-', linewidth=2,
                         label="Residuals")
    ax2.plot(full_time, [-0.15] * len(full_time), 'k--', linewidth=1)
    ax2.legend(loc=0)
    # draw an arrow where t0 is
    arrow = np.asarray([.4, -.2, 3, .1]) * ax2.get_ylim()[1]
    ax2.arrow(t0, arrow[0], 0, arrow[1], head_width=arrow[2],
              head_length=arrow[3], fc='k', ec='k')
    ax2.text(t0, arrow[0], 't0')
    ax2.set_xlabel("Time (arb)")
    ax2.set_ylabel("Normalized Intensity, "r"$\alpha$")
    ax2.set_title("Fit against full data set")

    return ax1, ax2