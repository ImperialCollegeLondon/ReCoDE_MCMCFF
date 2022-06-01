import numpy as np
from hypothesis import given
from hypothesis import strategies as st
from hypothesis.extra import numpy as hnp

from MCFF.ising_model import energy, energy_numpy

@given(hnp.arrays(dtype = int,
                 shape = hnp.array_shapes(min_dims = 2, max_dims = 2),
                 elements = st.sampled_from([1, -1])))
def test_generated_states(state):
    assert np.allclose(energy(state), energy_numpy(state))