import numpy as np
import pytest

from src.formatter1 import generate_np_array


@pytest.mark.parametrize(
    "size, expected_shape",
    [
        (1, (1,)),
        (10, (10,)),
        (100, (100,)),
        (1000, (1000,)),
        (10000, (10000,)),
    ],
)
@pytest.mark.timeout(5)  # Set a 5-second timeout
def test_generate_np_array(size, expected_shape):
    result = generate_np_array(size)
    assert result.shape == expected_shape
    assert len(result) == size
    assert isinstance(result, np.ndarray)
    assert result.dtype == np.float64
