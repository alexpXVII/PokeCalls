from setuptools import setup, find_packages

setup(
    name='pokecalls',
    version='0.1.0',
    author='Alex Padilla',
    author_email='alexp.xvii@outlook.com',
    description='A python wrapper for PokeAPI',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'requests',
        'setuptools',
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.12',
)