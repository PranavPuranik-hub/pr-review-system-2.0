"""A small sample module for testing the PR review workflow."""


def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def greet(name):
    """Return a greeting string for the given name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet("World"))
    print(add(2, 3))
