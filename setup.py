from setuptools import setup

setup(
    name="fds2020-fcbo-project",
    version="0.1",
    packages=[
        'fcbo2020',
        'fcbo2020.core',
        'fcbo2020.data',
    ],
    install_requires=[
        'intbitset'
    ]
)
