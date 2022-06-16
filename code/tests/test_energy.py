import numpy as np
from matplotlib.image import imread
from pathlib import Path

from MCFF.ising_model import all_up_state, all_down_state, random_state
from MCFF.ising_model import energy, energy_numpy

# create some test states
all_up = np.ones([100, 100])
all_down = -np.ones([100, 100])
random = np.random.choice([-1, 1], size=(100, 100))
custom = (
    1 - 2 * imread(Path(__file__).parents[2] / "learning/data/test_state.png")[:, :, 0]
)  # load a 100x100 png, take the red channel, remap 0,1 to -1,1

states = [all_up, all_down, random, custom]


def E_prediction_all_the_same(L):
    "The exact energy in for the case where all spins are up or down"
    return -(4 * (L - 2) ** 2 + 12 * (L - 2) + 8)


def test_exact_energies():
    for state in [all_up, all_down]:
        L = state.shape[0]
        assert energy(state) == E_prediction_all_the_same(L)


def test_energy_implementations():
    for state in states:
        assert np.allclose(energy(state), energy_numpy(state))
