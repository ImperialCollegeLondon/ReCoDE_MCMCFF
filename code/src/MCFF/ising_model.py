"""ising_model provides functions specific to the 2D ising model such as computing its energy and generating special states.

States are represented by NxM numpy arrays with values +/-1. These functions are intended to be used with a markov chain monte carlo routine to sample from the thermal ensemble of the 2d Ising model.

"""

import numpy as np

def all_up_state(N):
    "The NxN all up state of the Ising model."
    return np.ones([N, N])

def all_down_state(N):
    "The NxN all down state of the Ising model."
    return -np.ones([N, N])

def random_state(N, magnetisation = 0.5, rng = np.random.default_rng())
    r"""Return the a random NxN state of the Ising model.

    Parameters
    ----------
    N : int
        The returned state will have shape (N,N)
    magnetisation : int, default = 0.5
        What proportion of the values will be +1
    rng : numpy.random._generator.Generator, default = np.random.default_rng()
        Optionally pass in the rng to be used, useful to get reproducable answers.

    Returns
    -------
    np.array
        A random NxN state.
    """
    return np.random.choice([+1, -1], size = (N,N), p = magnetisation)


# nopython=True instructs numba that we want all use of the python interpreter to removed from this function
# numba will throw and error if it cannot achieve this.
# nogil = True says that numba can release python's Global Interpreter Lock, read more about that here: https://numba.pydata.org/numba-doc/latest/user/jit.html#nogil
@jit(nopython=True, nogil = True) 
def energy(state):
    r"""Compute the energy of a state of the Ising Model with open boundary conditions.

    Parameters
    ----------
    state : array_like
        A NxM array containing only the values +1 and -1
    Returns
    -------
    float64
        The interaction energy per site.
    """
    E = 0
    N, M = state.shape
    for i in range(N):
        for j in range(M):
            # handle the north and south neighbours
            if 0 <= (i + 1) < N:
                E -= state[i,j] * state[i+1, j]
            
            # handle the east and west neighbours
            if 0 <= (j + 1) < M:
                E -= state[i,j] * state[i, j+1]
            
    return 2*E / (N*M)

def energy_numpy(state):
    r"""Compute the energy of a state of the Ising Model with open boundary conditions.
    
    An alternate implementation of `energy` using Numpy array operations, used for comparison and correctness checks.

    Parameters
    ----------
    state : array_like ()
        A 2D array containing only the values +1 and -1
    Returns
    -------
    float64
        The interaction energy per site.
    """
    E = - np.sum(state[:-1, :] * state[1:, :]) - np.sum(state[:, :-1] * state[:, 1:]) 
    return 2*E / np.product(state.shape)

