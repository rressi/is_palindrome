def solution(text: str) -> bool:
    """Check if text can be a palindrome by deleting at most one character."""

    i, j = 0, len(text) - 1
    count_mismatches = 0
    while i < j:
        if text[i] != text[j]:
            if count_mismatches == 1:
                return False
            count_mismatches += 1
            if text[i + 1] == text[j]:
                i += 1
            elif text[i] == text[j - 1]:
                j -= 1
            else:
                return False
        else:
            i += 1
            j -= 1
    return True
