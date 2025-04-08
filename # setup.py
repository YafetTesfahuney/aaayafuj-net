# setup.py
from setuptools import setup, find_packages

setup(
    name='aaayafuj',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'scapy',
        'requests',  # For web vulnerability scanning
        # Add other dependencies
    ],
    entry_points={
        'console_scripts': [
            'aaayafuj=aaayafuj.cli:main',  # The CLI entry point
        ],
    },
)
