from setuptools import setup

def get_metadata(file, key):
    with open(file, "r") as fp:
        for line in fp:
            if line.startswith(key):
                return eval(line.split("=")[-1])
    raise ValueError("can not find {} in {}".format(key, file))

metadata_file = "greetings/greetings.py"

setup(
    author=get_metadata(metadata_file, "__author__"),
    author_email=get_metadata(metadata_file, "__email__"),
    version=get_metadata(metadata_file, "__version__"),
    license=get_metadata(metadata_file, "__license__"),
)
