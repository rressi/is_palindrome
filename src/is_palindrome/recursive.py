def solution(text: str) -> bool:
    """Check if text can be a palindrome by deleting at most one character.

    Uses a recursive two-pointer approach with a 'can_skip' flag that tracks
    whether the one allowed deletion has been used.
    """

    def _check(lo: int, hi: int, can_skip: bool) -> bool:
        while lo < hi:
            if text[lo] == text[hi]:
                lo += 1
                hi -= 1
            elif can_skip:
                return _check(lo + 1, hi, False) or _check(lo, hi - 1, False)
            else:
                return False
        return True

    return _check(0, len(text) - 1, True)
