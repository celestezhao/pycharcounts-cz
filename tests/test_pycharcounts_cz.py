from pycharcounts_cz.pycharcounts_cz import count_characters

def test_count_characters():
    """Test character counting from a text file."""
    expected = 1289
    path = "tests/Can We Touch Your Hair.txt"
    actual = count_characters(path)
    assert actual == expected, "The characters in the poem 'Can We Touch Your Hair' counted incorrectly!"