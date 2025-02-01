import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="sofascore_wrapper",  
    version="1.0.7",
    description="A Python API wrapper for https://www.sofascore.com",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/tommhe14/sofascore-wrapper",
    author="tommhe14",
    author_email="theckley@yahoo.co.uk",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    packages=find_packages(),  
    include_package_data=True,
    install_requires=["requests>=2.31.0", "pytest>=7.0.0"],
    python_requires=">=3.6",
)
