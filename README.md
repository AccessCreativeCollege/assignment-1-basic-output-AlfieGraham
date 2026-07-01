# Assignment 1: Basic Output

Practice using `print()` to produce output in Python.

## Your tasks

Open `task.py` and complete each TODO comment. Do not change the file name
or remove any of the existing comments.

| Task | What to do |
|------|-----------|
| 1 | Print your first name |
| 2 | Print exactly: `Hello, World!` |
| 3 | Print the number `42` |
| 4 | Print the result of `10 + 5` |
| 5 | Print `Line one` and `Line two` on separate lines using a **single** `print()` call |

## Hint for Task 5

You can print two lines with one `print()` by putting `\n` in the middle of your string:

```python
print("first line\nsecond line")
```

## Running the tests yourself

Open the terminal in VS Code and run:

```
pytest tests/ -v
```

A green tick means that test passed. A red cross means something needs fixing.
Read the message underneath the red cross carefully - it will tell you what went wrong.

## Submitting

When you are happy with your work:

```
git add .
git commit -m "Completed assignment 1"
git push
```

Then go to your repository on GitHub and click the **Actions** tab to see
your results. A green tick on the workflow run means all tests passed.
