Quickstart
----------

.. code-block:: python

   from MCFF.mcmc import mcmc_generator
   from MCFF.ising_model import show_state

   ### Simulation Inputs ###
   N = 500  # Use an NxN system

   initial_state = np.random.choice(
      np.array([-1, 1], dtype=np.int8), size=(N, N)
   )  # the intial state to use

   ### Simulation Code ###
   critical_states = [
      s for s in mcmc_generator(initial_state, steps=5, stepsize=5*N**2, T= 3.5)
   ]

   fig, axes = plt.subplots(
      ncols=len(critical_states), figsize=(5 * len(critical_states), 5)
   )

   for s, ax in zip(critical_states, axes):
      show_state(s, ax=ax)

.. image:: _static/states.png
  :width: 100%
  :alt: 5 grids showing black and white Ising Model states
