import pathlib
from setuptools import setup, find_packages
from setuptools.command.install import install
import subprocess
import sys

HERE = pathlib.Path(__file__).parent
README = (HERE / "README.md").read_text()

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)
        if not self._called_from_setup:
            try:
                subprocess.check_call([sys.executable, '-m', 'playwright', 'install', 'chromium'])
                subprocess.check_call([sys.executable, '-m', 'playwright', 'install-deps'])
            except subprocess.CalledProcessError as e:
                print(f"Playwright installation failed: {e}")
                print("Please manually run:")
                print("  python -m playwright install chromium")
                print("  python -m playwright install-deps")

setup(
    name="sofascore_wrapper",
    version="1.1.0",
    description="Python API wrapper for SofaScore using Playwright",
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
    cmdclass={
        'install': PostInstallCommand,
    },
)