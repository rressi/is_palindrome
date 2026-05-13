def solution(text: str) -> bool:
    """Check if text can be a palindrome by deleting at most one character."""

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
                _find_mismatch(left + 1, right) is None
                or _find_mismatch(left, right - 1) is None
            )
