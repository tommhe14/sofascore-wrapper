import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

setup(
    name="sofascore_wrapper",
    version="1.1.1",
    description="Python API wrapper for SofaScore",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/tommhe14/sofascore-wrapper",
    author="tommhe14",
    author_email="theckley@yahoo.co.uk",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "playwright>=1.42.0",
    ],
    python_requires=">=3.8",
)