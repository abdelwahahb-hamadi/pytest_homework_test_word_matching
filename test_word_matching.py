import pytest
from word_matching import count_word_matches


@pytest.mark.parametrize(
    "text, target, expected",
    [
        ("The cat sat on the mat", "cat", 1),
        ("Dog dog DOG dOg", "dog", 4),
        ("hello world", "world", 1),
        ("hello Hello HELLO", "hello", 3),
        ("No matches here", "yes", 0),
        ("catcat cat catdog", "cat", 1),
        ("a a a", "a", 3),
    ]
)
def test_basic_cases(text, target, expected):
    assert count_word_matches(text, target) == expected


@pytest.mark.parametrize(
    "text, target, expected",
    [
        ("", "word", 0),
        ("hello world", "", 0),
        ("", "", 0),
        ("hello   world", "world", 1),
        (" cat ", "cat", 1),
        ("cat,dog cat", "cat", 1),
    ]
)
def test_edge_cases(text, target, expected):
    assert count_word_matches(text, target) == expected


@pytest.mark.parametrize(
    "text, target",
    [
        (None, "word"),
        ("hello world", None),
        (123, "word"),
        ("hello world", 456),
        (["hello", "world"], "world"),
        ("hello world", ["world"]),
    ]
)
def test_invalid_inputs(text, target):
    with pytest.raises(TypeError):
        count_word_matches(text, target)
