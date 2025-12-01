

def summarize_adoptions(adoptions):
    """
    Given a list of animal type strings, return a dictionary mapping each
    distinct animal type to how many times it appears in the list.

    Example:
    summarize_adoptions(["cat", "dog", "cat"]) -> {"cat": 2, "dog": 1}
    """

    # TODO Step 1–3: Read the problem and identify inputs, outputs, and variables.
    # TODO Step 4: Plan how to loop over the list and update a data structure.
    # TODO Step 5: Write pseudocode (in comments or on paper) before coding.
    # TODO Step 6: Implement the algorithm in Python using a suitable data structure.
    # TODO Step 7: Test your function with small examples and fix bugs.
    # TODO Step 8: Check the time and space complexity of your final solution.
    summary = {}
    for animal in adoptions:
        if animal in summary:
            summary[animal] += 1
        else:
            summary[animal] = 1
    return summary


if __name__ == "__main__":
    # Optional manual test
    sample = ["cat", "dog", "cat", "rabbit", "dog", "cat"]
    print(summarize_adoptions(sample))
