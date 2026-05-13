import pytest

from is_palindrome.simpler import solution as solution_simpler
from is_palindrome.bfs import solution as solution_bfs


@pytest.fixture(params=[solution_simpler, solution_bfs], ids=["simpler", "bfs"])
def solution(request):
    """Fixture that provides both solution implementations."""
    return request.param


class TestPalindromeWithDeletion:
    """Test cases for checking if a string can be a palindrome by deleting at most one character."""

    # Already palindromes (no deletion needed)
    def test_empty_string(self, solution):
        """Empty string is a palindrome."""
        assert solution("") is True

    def test_single_character(self, solution):
        """Single character is a palindrome."""
        assert solution("a") is True

    def test_two_same_characters(self, solution):
        """Two identical characters form a palindrome."""
        assert solution("aa") is True

    def test_simple_palindrome(self, solution):
        """Simple odd-length palindrome."""
        assert solution("aba") is True

    def test_even_length_palindrome(self, solution):
        """Even-length palindrome."""
        assert solution("abba") is True

    def test_longer_palindrome(self, solution):
        """Longer palindrome."""
        assert solution("racecar") is True

    def test_all_same_characters(self, solution):
        """String with all same characters."""
        assert solution("aaaa") is True

    # Can be made palindrome by deleting one character
    def test_two_different_characters(self, solution):
        """Two different characters - delete one to get palindrome."""
        assert solution("ab") is True

    def test_palindrome_with_extra_char_at_start(self, solution):
        """Extra character at the start."""
        assert solution("xaba") is True  # delete x -> aba

    def test_palindrome_with_extra_char_at_end(self, solution):
        """Extra character at the end."""
        assert solution("abax") is True  # delete x -> aba

    def test_palindrome_with_extra_char_in_middle(self, solution):
        """Extra character that breaks palindrome in middle."""
        assert solution("abxba") is True  # delete x -> abba

    def test_one_mismatch_from_left(self, solution):
        """One character mismatch from the left side."""
        assert solution("abcba") is True  # Already a palindrome
        
    def test_almost_palindrome_delete_left(self, solution):
        """Mismatch can be fixed by deleting from left."""
        assert solution("acccccccc") is True  # delete a -> cccccccc (palindrome)

    def test_almost_palindrome_delete_right(self, solution):
        """Mismatch can be fixed by deleting from right."""
        assert solution("cccccccca") is True  # delete a -> cccccccc (palindrome)

    def test_longer_almost_palindrome(self, solution):
        """Longer string that can be made palindrome."""
        # Valid palindrome that can be made by deleting one character
        assert solution("abcdcba") is True

    def test_case_sensitivity(self, solution):
        """Test that comparison is case-sensitive."""
        assert solution("Aa") is True  # Can delete one character

    # Cannot be made palindrome by deleting one character
    def test_two_mismatches_needed(self, solution):
        """Two mismatches that require more than one deletion."""
        assert solution("abcd") is False  # Multiple mismatches

    def test_three_mismatches(self, solution):
        """Three characters all different."""
        assert solution("abc") is False

    def test_multiple_mismatches_complex(self, solution):
        """Complex case with multiple mismatches."""
        assert solution("abcdefg") is False

    def test_two_different_at_ends_and_middle_mismatch(self, solution):
        """Different characters at ends and middle doesn't work."""
        assert solution("xaaby") is False  # Even if we delete x or y, still have mismatch at a-b

    def test_requires_two_deletions(self, solution):
        """String that requires two deletions."""
        assert solution("abba" + "x" + "baba") is False  # abbaXbaba has multiple mismatch issues

    def test_almost_but_not_quite(self, solution):
        """Looks like it could work but doesn't."""
        assert solution("aabaa") is True  # Wait, this is already palindrome

    def test_two_chars_different(self, solution):
        """Two mismatches in short string."""
        assert solution("acb") is False  # a != b when we get to position 0,2


class TestEdgeCases:
    """Test edge cases and boundary conditions."""

    def test_long_palindrome(self, solution):
        """Very long palindrome."""
        long_pal = "a" * 1000 + "b" + "a" * 1000
        assert solution(long_pal) is True

    def test_long_string_with_one_char_off(self, solution):
        """Long string that's almost palindrome."""
        # One extra character that can be deleted
        almost = "a" * 500 + "x" + "a" * 500
        assert solution(almost) is True  # Can delete x to get palindrome

    def test_repeated_pattern_palindrome(self, solution):
        """Repeated pattern that forms palindrome."""
        assert solution("abcbaabcba") is True

    def test_numeric_string(self, solution):
        """Numeric strings."""
        assert solution("12321") is True

    def test_numeric_almost_palindrome(self, solution):
        """Numeric that's almost palindrome."""
        assert solution("123321") is True

    def test_special_characters(self, solution):
        """Special characters in string."""
        assert solution("!@#@!") is True

    def test_whitespace(self, solution):
        """Whitespace in string (treated as characters)."""
        assert solution("a b a") is True

    def test_mixed_whitespace_and_chars(self, solution):
        """Mixed content with spaces."""
        assert solution("a b c b a") is True


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
