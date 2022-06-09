"""mcmc provides routines for performin Markov Chain Monte Carlo


"""


def mcmc(initial_state, steps, T, rng=np.random.default_rng()):
    r"""Return the state after performing `steps` monte carlo steps starting from `initial_state` at temperature `T`.

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
    E = N**2 * energy(state)
    for i in range(steps):
        i, j = rng.integers(N, size=2)

        new_state = current_state.copy()
        new_state[i, j] *= -1
        new_E = N**2 * energy(new_state)

        if (new_E < E) or np.exp(-(new_E - E) / T) > rng.uniform():
            current_state = new_state
            E = new_E

    return current_state
