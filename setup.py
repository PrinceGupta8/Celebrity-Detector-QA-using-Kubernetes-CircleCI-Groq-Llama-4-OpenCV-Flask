from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements=f.read().splitlines()

setup(
    name="Celebrity Detector and QA",
    version=1.0,
    author="Prince Gupta",
    packages=find_packages(),
    install_requires=requirements
)