import pytest

from src.formatter1 import format_file_size


@pytest.mark.parametrize(
    "size_bytes, expected_result",
    [
        (0, "0B"),
        (1, "1.00 B"),
        (1024, "1.00 KB"),
        (1024**2, "1.00 MB"),
        (1024**3, "1.00 GB"),
        (1024**4, "1.00 TB"),
    ],
)
@pytest.mark.timeout(5)  # Set a 5-second timeout
def test_format_file_size(size_bytes, expected_result):
    assert format_file_size(size_bytes) == expected_result
