#!/usr/bin/env python3
# The above lets us run this script by just typing ./generate_montecarlo_walkers.py at the command line
"""
This script generates the data for the monte carlo walkers plot Fig. 2 in the paper {link}
To regenerate the plot:

$ conda env create -p ./env -f environment.yml # generate the environment in a local env folder
$ conda active ./env # activate it
$ python generate_montecarlo_walkers.py # creates data.pickle
$ python plot_montecarlo_walkers.py # creates plot.pdf

Last tested and working with MCFF commit hash 63523481e89ae8c8f74a900ae43b035e3312f9c8
"""
import numpy as np
import pickle
from datetime import datetime, timezone

import MCFF
from MCFF.mcmc import mcmc_generator

import subprocess
from pathlib import Path


def get_module_git_hash(module):
    "Get the commit hash of a module installed from a git repo with pip install -e ."
    cwd = Path(module.__file__).parent
    return (
        subprocess.run(
            ["git", "rev-parse", "HEAD"], check=True, capture_output=True, cwd=cwd
        )
        .stdout.decode()
        .strip()
    )


seed = [
    2937053738,
    1783364611,
    3145507090,
]  # generated once with rng.integers(2**63, size = 3) and then saved

np.random.seed(
    seed
)  # This makes our random numbers reproducable when the notebook is rerun in order

### The measurement we will make ###
def average_color(state):
    return np.mean(state)


### Simulation Inputs ###
N = 20  # Use an NxN system
Ts = [10, 4.5, 3]  # What temperatures to use
steps = 200  # How many times to sample the state
stepsize = N**2  # How many individual monte carlo flips to do in between each sample
N_repeats = 10  # How many times to repeat each run at fixed temperature
initial_state = np.ones(shape=(N, N))  # the intial state to use
flips = (
    np.arange(steps) * stepsize
)  # Use this to plot the data in terms of individual flip attemps
inputs = dict(
    N=N,
    Ts=Ts,
    steps=steps,
    stepsize=stepsize,
    N_repeats=10,
    initial_state=initial_state,
    flips=flips,
)

### Simulation Code ###
average_color_data = np.array(
    [
        [
            [
                average_color(s)
                for s in mcmc_generator(initial_state, steps, stepsize=stepsize, T=T)
            ]
            for _ in range(N_repeats)
        ]
        for T in Ts
    ]
)

data = dict(
    MCFF_commit_hash=get_module_git_hash(MCFF),
    date=datetime.now(timezone.utc),
    inputs=inputs,
    average_color_data=average_color_data,
)

# save the data to data.pickle
with open("./data.pickle", "wb") as f:
    pickle.dump(data, f)
