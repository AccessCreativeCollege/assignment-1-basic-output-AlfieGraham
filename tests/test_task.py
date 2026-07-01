import subprocess
import sys
import os

def run_task():
    """Run task.py and return its stdout as a list of lines."""
    result = subprocess.run(
        [sys.executable, "task.py"],
        capture_output=True,
        text=True,
        cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    return result.stdout.strip().splitlines()


def test_file_runs_without_errors():
    """task.py must run without crashing."""
    result = subprocess.run(
        [sys.executable, "task.py"],
        capture_output=True,
        text=True,
        cwd=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    assert result.returncode == 0, (
        f"task.py crashed with an error:\n{result.stderr}\n"
        "Fix any syntax errors before running the other tests."
    )


def test_task1_prints_a_name():
    """Task 1: Something must be printed on the first line."""
    lines = run_task()
    assert len(lines) >= 1, (
        "No output found at all. Have you written any print() statements?"
    )
    assert len(lines[0].strip()) > 0, (
        "The first line is empty. Task 1 asks you to print your first name."
    )


def test_task2_hello_world():
    """Task 2: Second line must be exactly 'Hello, World!'"""
    lines = run_task()
    assert len(lines) >= 2, (
        "Expected at least 2 lines of output. "
        "Check that Tasks 1 and 2 both have print() statements."
    )
    assert lines[1] == "Hello, World!", (
        f"Task 2: expected 'Hello, World!' but got '{lines[1]}'.\n"
        "Check your spelling, punctuation, and capitalisation exactly."
    )


def test_task3_prints_42():
    """Task 3: Third line must be 42."""
    lines = run_task()
    assert len(lines) >= 3, (
        "Expected at least 3 lines of output. Check Tasks 1, 2, and 3."
    )
    assert lines[2] == "42", (
        f"Task 3: expected '42' but got '{lines[2]}'.\n"
        "Print the number 42 on its own line."
    )


def test_task4_prints_sum():
    """Task 4: Fourth line must be 15 (the result of 10 + 5)."""
    lines = run_task()
    assert len(lines) >= 4, (
        "Expected at least 4 lines of output. Check Tasks 1 through 4."
    )
    assert lines[3] == "15", (
        f"Task 4: expected '15' but got '{lines[3]}'.\n"
        "Use print(10 + 5) to print the result of the addition."
    )


def test_task5_two_lines():
    """Task 5: Lines 5 and 6 must be 'Line one' and 'Line two'."""
    lines = run_task()
    assert len(lines) >= 6, (
        f"Expected at least 6 lines of output but got {len(lines)}.\n"
        "Task 5 requires two lines of output. Use \\n inside a single print() call."
    )
    assert lines[4] == "Line one", (
        f"Task 5: expected 'Line one' on line 5 but got '{lines[4]}'.\n"
        "Check your spelling and capitalisation."
    )
    assert lines[5] == "Line two", (
        f"Task 5: expected 'Line two' on line 6 but got '{lines[5]}'.\n"
        "Check your spelling and capitalisation."
    )
