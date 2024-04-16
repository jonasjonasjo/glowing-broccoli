import pytest
from module import main

@pytest.mark.parametrize(
    "i, j, expected",
    [
        # expected inputs
        (
                1,
                1,
                True
        ),
        (
                2,
                2,
                True
        ),
        (
                2,
                3,
                False
        ),
        # unexpected inputs
        (
                "str",
                "light",
                False
        ),
        (
                "https://www.youtube.com/watch?v=-zd62MxKXp8",
                "light",
                False
        )
    ]
)
def test_main_true(i: int,j: int, expected: bool):
    assert main.example(i,j) is expected