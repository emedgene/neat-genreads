from setuptools import setup
from setuptools import find_packages

setup(
    name='neat_genreads',
    version='2.0',
    packages=find_packages(),
    package_data={
        'models': ['*.p'],
    },
    include_package_data=True,
    install_requires=['numpy>=1.9.1'],
    url='https://github.com/zstephens/neat-genreads',
    entry_points={
        'console_scripts': [
            'genreads=genReads:main',
        ],
    },
)
