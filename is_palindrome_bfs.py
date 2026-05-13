import collections

def solution(text: str) -> bool:
    # According to the problem we can delete at most one character,
    # but we cannot replace any character. Therefore, we set max_edit_distance to 1,
    # can_delete to True, and can_replace to False.
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
        can_replace: bool = True
) -> bool:

    # Initialize a queue to hold the runners, which are tuples of 
    # (edit_distance, left_index, right_index)
    runners: collections.deque[tuple[int, int, int]] = collections.deque()
    runners.append((0, 0, len(text) - 1))  # (edit_distance, left_index, right_index)

    # Process the runners for half the length of the text
    while runners:
        for _ in range(len(runners)):
            runner = runners.popleft()
            distance, left, right = runner
            if left >= right:
                # At least one runner has successfully reached the middle, meaning 
                # the string is a palindrome:
                return True

            if text[left] == text[right]:
                # Perfect match, continue without increasing the edit distance
                runners.append((distance, left + 1, right - 1))

            elif distance < max_edit_distance:
                # If the characters do not match, we can consider three operations: 
                # replace, delete left, or delete right.
                new_distance = distance + 1
                if can_replace:
                    runners.append((new_distance, left + 1, right - 1))  # Replace
                if can_delete:
                    runners.append((new_distance, left, right - 1))  # Delete right
                    runners.append((new_distance, left + 1, right))  # Delete left

    return False


if __name__ == "__main__":
    text: str = input("Enter a string: ")
    if solution(text):
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")
