import pytest
import numpy as np

from pycontest import elastic_collisions as ec
from pycontest.utils import momentum, E_kin


# a simple tests for equal masses (balls should exchange velocities)

# using default values of m1 and m2
def test_collision_1d_1():
    v1_i = 1
    v2_i = -2
    v1_f, v2_f = ec.collision_1d(v1_i=v1_i, v2_i=v2_i)

    assert v1_f == v2_i
    assert v2_f == v1_i

def test_collision_1d_2():
    v1_i = 1
    v2_i = -1
    m1 = 1
    m2 = 4
    v1_f, v2_f = ec.collision_1d(v1_i=v1_i, v2_i=v2_i, m1=m1, m2=m2)

    assert v1_f == -2.2
    np.allclose(v2_f, -0.2)
