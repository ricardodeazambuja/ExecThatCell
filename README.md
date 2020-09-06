# ExecThatCell
(Re)Execute a Jupyter (colab) notebook cell programmatically by searching for its label.  


(I added the "Re" because the cell needs to be executed at least once as this library is not using the ipynb notebook file, but the interpreter to find the cells and it will work even if the cell was not saved in the notebook file)


## Installation (Python3 because [you should not use Python2 anymore](https://www.python.org/doc/sunset-python-2/)):
Option #1: Clone the repo so you will get everything
```
$ git clone https://github.com/ricardodeazambuja/ExecThatCell.git
$ cd ExecThatCell
$ sudo pip3 install .
```

Option #2: Install directly from git
```
$ sudo pip3 install git+git://github.com/ricardodeazambuja/ExecThatCell
```

## Usage:
See the [Example.ipynb](https://github.com/ricardodeazambuja/ExecThatCell/blob/master/Example.ipynb).  
It also works with the IPython interpreter (you know, when you use it directly from a command line without Jupyter). However, to add a label to a cell you need to add a linefeed after it and that means [pressing Ctrl+q followed by Ctrl+j](https://stackoverflow.com/a/46060692).


## TODO:
- Test it :D
