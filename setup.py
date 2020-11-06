import re
from setuptools import find_packages, setup

# Read repository information - use as the package description
with open("README.md", "r") as fh:
    long_description = fh.read()

PKG = 'myaml'

# Read version
with open(f'{PKG}/__init__.py', 'rt') as fh:
    match = re.search(r"(__version__\s*=\s*)'([0-9\.]+)'", fh.read().strip())
    version = match.groups()[1]

# Read requirements
with open('requirements.txt', 'rt') as fh:
    reqs = [x.strip() for x in fh.readlines()]

setup(
    name=PKG,
    version=version,
    description='M(ath)YAML: evaluate math expressions in YAML files.',
    author='Alexandru Dinu',
    author_email='alex.dinu07@gmail.com',
    url=f'https://github.com/alexandru-dinu/{PKG}',
    license='Apache 2.0',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=reqs,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering"
    ],
)