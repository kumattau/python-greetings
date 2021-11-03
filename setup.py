from setuptools import setup

version_py = "greetings/greetings.py"

__version__ = None
with open(version_py, "r") as file:
    for line in file:
        if line.startswith("__version__"):
            exec(line)
            break
assert __version__ is not None

setup(version=__version__)
