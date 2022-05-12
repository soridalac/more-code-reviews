import pytest
from functions.palindrome_number import palindrome_number

def test_returns_true_for_99():
    # Arrange
    n = 99

    # Act
    answer = palindrome_number(99)

    # Assert
    assert answer == True
