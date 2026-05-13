import collections


def solution(text: str) -> bool:
    # We can delete at most one character and cannot replace.
    return _is_palindrome_with_tolerance(
        text=text,
        max_edit_distance=1,
        can_delete=True,
        can_replace=False,
    )


def _is_palindrome_with_tolerance(
    text: str,
    max_edit_distance: int = 0,
    can_delete: bool = True,
    can_replace: bool = True,
) -> bool:
    runners: collections.deque[tuple[int, int, int]] = collections.deque()
    runners.append((0, 0, len(text) - 1))

    while runners:
        for _ in range(len(runners)):
            distance, left, right = runners.popleft()
            if left >= right:
                return True

            if text[left] == text[right]:
                runners.append((distance, left + 1, right - 1))
            elif distance < max_edit_distance:
                new_distance = distance + 1
                if can_replace:
                    runners.append((new_distance, left + 1, right - 1))
                if can_delete:
                    runners.append((new_distance, left, right - 1))
                    runners.append((new_distance, left + 1, right))

    return False
