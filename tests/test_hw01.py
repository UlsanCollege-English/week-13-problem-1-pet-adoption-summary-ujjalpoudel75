import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from main import summarize_adoptions
from main import summarize_adoptions

import pytest

from main import summarize_adoptions


@pytest.mark.parametrize(
    "adoptions, expected",
    [
        (["cat", "dog", "cat"], {"cat": 2, "dog": 1}),
        (["rabbit"], {"rabbit": 1}),
        (["cat", "cat", "cat"], {"cat": 3}),
        (["dog", "cat", "dog", "bird"], {"dog": 2, "cat": 1, "bird": 1}),
    ],
)
def test_normal_cases(adoptions, expected):
    assert summarize_adoptions(adoptions) == expected


@pytest.mark.parametrize(
    "adoptions, expected",
    [
        ([], {}),
        (["Cat", "cat"], {"Cat": 1, "cat": 1}),  # case-sensitive
        (["", ""], {"": 2}),
    ],
)
def test_edge_cases(adoptions, expected):
    assert summarize_adoptions(adoptions) == expected


@pytest.mark.parametrize(
    "adoptions, expected_keys_count",
    [
        (["a"] * 1000, 1),
        ([str(i % 10) for i in range(1000)], 10),
        (
            ["dog"] * 500 + ["cat"] * 300 + ["rabbit"] * 200,
            3,
        ),
    ],
)
def test_larger_inputs(adoptions, expected_keys_count):
    result = summarize_adoptions(adoptions)
    assert sum(result.values()) == len(adoptions)
    assert len(result.keys()) == expected_keys_count
