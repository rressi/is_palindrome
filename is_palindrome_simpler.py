

def solution(text: str) -> bool:
    """This function checks if the given string can be a palindrome by 
    deleting at most one character.

    It uses a two-pointer approach to find the first mismatch and then checks if 
    either of the resulting substrings (after deleting one character) is a 
    palindrome.
    """

    # Helper function to find the first mismatch between two pointers
    # It returns the indices of the mismatch or None if the substring is already 
    # a palindrome
    def _find_mismatch(i: int, j: int) -> tuple[int, int] | None:
        while i < j:
            if text[i] != text[j]:
                return i, j
            i += 1
            j -= 1
        return None
    
    match _find_mismatch(0, len(text) - 1):
        case None:
            return True
        case (left, right):
            return (
                # Check if the substring after deleting the left character is a palindrome
                _find_mismatch(left + 1, right) is None
                # Check if the substring after deleting the right character is a palindrome
                or _find_mismatch(left, right - 1) is None
            )

