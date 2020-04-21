from setuptools import setup

setup(
    name="fds2020-fcbo-project",
    version="0.1",
    packages=[
        'fcbo2020',
        'fcbo2020.core',
        'fcbo2020.data',
    ], package_data={
        'fcbo2020.data': [
            'examples/*.cxt'
        ]
    },
    install_requires=[
        'intbitset'
    ],
    author="Nazarov Ivan",
    email="innazarov@edu.hse.ru",
    dscription="""
        Assigment #03: Python realisation of fast CbO with the possibility
        of recovering the full Formal Concept lattice.
    """
)
