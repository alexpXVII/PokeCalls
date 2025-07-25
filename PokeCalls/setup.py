from setuptools import setup, find_packages

setup(
    name='pokecalls',
    version='0.1.0',
    author='Alex Padilla',
    author_email='alexp.xvii@outlook.com',
    description='A Python library for interacting with the PokeAPI, providing models, services, and game logic for Pokémon data.',
    long_description=(
        "PokeCalls is a modular Python library that simplifies working with the PokeAPI. "
        "It provides structured models for Pokémon, moves, and related resources, "
        "service layers with caching for efficient API usage, and example game logic for building Pokémon-based applications."
    ),
    long_description_content_type='text/plain',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
    ],
    extras_require={
        'dev': ['pytest'],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)