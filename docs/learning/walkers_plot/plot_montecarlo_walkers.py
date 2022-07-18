#!/usr/bin/env python3
"""
This script plots the monte carlo walkers plot Fig. 2 in the paper {link}
To regenerate the plot:

$ conda env create -p ./env -f environment.yml # generate the environment in a local env folder
$ conda active ./env # activate it
$ python generate_montecarlo_walkers.py # creates data.pickle
$ python plot_montecarlo_walkers.py # creates plot.pdf

Last tested and working with MCFF commit hash 63523481e89ae8c8f74a900ae43b035e3312f9c8
"""
import numpy as np
import matplotlib.pyplot as plt
from numba import jit
import pickle

# This loads some custom styles for matplotlib
import json, matplotlib

with open("../../_static/matplotlibrc.json") as f:
    matplotlib.rcParams.update(json.load(f))

from itertools import count

with open("./data.pickle", "rb") as f:
    data = pickle.load(f)

# splat the keys and values back into the global namespace,
# beware that this could overwrite previously defined variables like 'count' by accident
globals().update(**data)
globals().update(**data["inputs"])


fig, axes = plt.subplots(
    figsize=(15, 7),
    nrows=3,
    ncols=2,
    sharey="row",
    sharex="col",
    gridspec_kw=dict(hspace=0, wspace=0, width_ratios=(4, 1)),
)

for i, ax, hist_ax in zip(count(), axes[:, 0], axes[:, 1]):
    c = average_color_data[i]
    indiv_line, *_ = ax.plot(flips, c.T, alpha=0.4, color="k", linewidth=0.9)
    (mean_line,) = ax.plot(flips, np.mean(c, axis=0))
    hist_ax.hist(c.flatten(), orientation="horizontal", label=f"T = {Ts[i]}")

axes[-1, 0].set(xlabel=f"Monte Carlo Flip Attempts")
axes[-1, 1].set(xlabel="Probability Density")
axes[1, 0].set(ylabel=r"Average Color $\langle c \rangle$")
axes[-1, 0].legend([mean_line, indiv_line], ["Mean", "Individual walker"])
for ax in axes[:, 1]:
    ax.legend(loc=4)

fig.savefig("./plot.pdf")
