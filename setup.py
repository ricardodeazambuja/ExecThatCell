from setuptools import setup, find_packages
setup(
    name="ExecThatCell",
    version="0.1.1",
    packages=['execthatcell'],
    install_requires=['ipython'],

    # metadata to display on PyPI
    author="Ricardo de Azambuja",
    author_email="ricardo.azambuja@gmail.com",
    description="Execute a Jupyter (colab) notebook cell programmatically by searching for its label",
    keywords="Jupyter Notebook Colab",
    url="https://github.com/ricardodeazambuja/ExecThatCell",
    classifiers=[
        'Programming Language :: Python :: 3 :: Only' # https://pypi.org/classifiers/
    ]
)

# https://setuptools.readthedocs.io/en/latest/setuptools.html
