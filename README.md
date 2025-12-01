[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/95fC7feI)
# hw01 – Pet Adoption Summary (Dictionaries)

## Story

A small city animal shelter wants a simple monthly report.

Every time an animal goes to a new home, staff record only the **animal type**:
`"cat"`, `"dog"`, `"rabbit"`, and so on.

At the end of the month, they want to know:
- How many cats found homes?
- How many dogs?
- How many of each type in total?

You will build a function that turns a **list of adopted animal types** into a
**summary dictionary**.

---

## Technical Description

Write a function:

```python
def summarize_adoptions(adoptions):
    ...
```
`adoptions`: a list of strings, each string is an animal type
(for example: `"cat"`, `"dog"`, `"parrot"`).

Return value: a dictionary mapping each animal type to how many times it appears.

Example:

```python
summarize_adoptions(["cat", "dog", "cat"])
# -> {"cat": 2, "dog": 1}
```

### Constraints
- `len(adoptions)` can be from `0` to `100_000`.

- Each animal type is a non-empty string.

- Strings are case-sensitive: `"Cat"` and `"cat"` are different keys.

### Expected Complexity
- Time: O(n), where n is the number of adoptions.

- Space: O(k), where k is the number of distinct animal types.

#### Use a data structure that lets you:

- Look up a count by animal type quickly.

- Update the count in constant time on average.
---
## 8 Steps of Coding – Scaffold (hw01)
For this homework, use the 8 Steps of Coding. Please write your answers in
comments or on paper before you start coding.

1. Read & Understand the problem

- Write one simple sentence in your own words that explains the task.

2. Re-phrase the problem
- Write another sentence that uses the words input and output.

- Example format:

    “Input: a list of …, Output: a dictionary that …”.

3. Identify input, output, variables

- List the input: what is its type and meaning?

- List the output: what is its type and meaning?

- List the key variables you will need inside the function.

4. Break down the problem

- Describe, step by step, how you will go from the list to the dictionary.

- Hint: think of a loop and updating a count.

5. Pseudocode the solution

- Write a short pseudocode block (in English or simple code-like lines)
that describes your loop and your data structure operations.

#### 6–8. Write code, Debug, Optimize

- Step 6: Translate your pseudocode into Python in main.py.

- Step 7: Test your function with small examples (see tests).

- Step 8: Check that your solution is O(n) time and O(k) space.
----

## Hints (not full solutions)
- Think about which structure lets you store key → count pairs.

- Start from an empty structure and update it inside a for loop.

- For an empty list, what should the result be? (Test it.)
---
### How to Run Tests
```
python -m pytest -q
```
___
## FAQ
Q1: Do I read from input() or use function arguments?
Use function arguments only. Do not read from standard input in this homework.
We will test your function by importing it and calling it.

Q2: Can I print inside my function?
You may print while debugging, but remove prints before you submit. The tests
do not look at printed output, only return values.

Q3: What Big-O is expected?
We expect O(n) time, where n is the length of the adoptions list.
A simple loop plus a suitable data structure is enough.

Q4: My tests fail with ImportError: cannot import name ...
Make sure your function name is exactly summarize_adoptions, and it is defined
in hw01/main.py. Do not rename the file.

Q5: The pytest error messages look long. How do I read them?
Look for lines that start with E and for the line assert .... That line
tells you what the test expected and what your function returned.

Q6: How will grading work?
We will run our own hidden tests, plus these visible tests. We will also review
your code for correct use of data structures and reasonable complexity.

Q7: Can I use libraries like NumPy or pandas?
No. Use only the Python standard library. For this task, you do not need any
extra library.