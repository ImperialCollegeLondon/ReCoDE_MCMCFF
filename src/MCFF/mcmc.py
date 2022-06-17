"""mcmc provides routines for performin Markov Chain Monte Carlo


"""
import numpy as np
from numba import jit
from .ising_model import energy, energy_difference


def mcmc_original(initial_state, steps, T, rng=np.random.default_rng()):
    r"""Return the state after performing `steps` monte carlo steps starting from `initial_state` at temperature `T`.

    This is the original version of the algorithm, written in notebook 03.

    Parameters
    ----------
    initial_state : array_like
        Numpy array of shape (N,N) with values +1,-1
    steps : int
        The number of steps to take.
    T : float
        The temperature at which to perform the simulation.
    rng : numpy.random._generator.Generator, default = np.random.default_rng()
        Optionally pass in the rng to be used, useful to get reproducable answers.

    Returns
    -------
    np.array
        The final state.
    """
    N, M = initial_state.shape
    assert N == M

    current_state = initial_state.copy()
    E = energy(initial_state)
    for i in range(steps):
        i, j = rng.integers(N, size=2)

        new_state = current_state.copy()
        new_state[i, j] *= -1
        new_E = energy(new_state)

        if (new_E < E) or np.exp(-(new_E - E) / T) > rng.uniform():
            current_state = new_state
            E = new_E

    return current_state


@jit(nopython=True, nogil=True)
def mcmc_generator(
    initial_state, steps, T, stepsize=1000, energy_difference=energy_difference
):
    r"""Yields the state after each MCMC step. Performs `steps` monte carlo steps each of size `stepsize` starting from `initial_state` at temperature `T`.

    Parameters
    ----------
    initial_state : array_like
        Numpy array of shape (N,N) with values +1,-1
    steps : int
        The number of steps to take.
    T : float
        The temperature at which to perform the simulation.
    stepsize : int, default = 1000
        How many times to try to flip a pixel between for each step.

    energy_difference : function(state, site), default = ising_model.energy_difference
        A function that gives the energy change from flippings `site = (i, j)`of `state`.

    Yields
    -------
    np.array
        The final state.
    """
    N, M = initial_state.shape
    assert N == M

    current_state = initial_state.copy()
    for _ in range(steps):
        for _ in range(stepsize):
            i, j = np.random.randint(N), np.random.randint(N)

            # calculate the energy change if we were to flip this pixel but don't actually do it
            change_in_E = energy_difference(current_state, (i, j))

            if change_in_E < 0 or np.exp(-change_in_E / T) > np.random.random():
                current_state[i, j] *= -1  # accept the change!

        yield current_state.copy()
    return
