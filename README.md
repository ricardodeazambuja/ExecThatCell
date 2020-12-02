# ExecThatCell
(Re)Execute a Jupyter (colab) notebook cell programmatically by searching for its label.  


*__Note 1__: I added the "Re" because the cell needs to be executed at least once as this library is not using the ipynb notebook file, but the interpreter to find the cells and it will work even if the cell was not saved in the notebook file.   
__Note 2__: From version 5.0, [Jupyter notebooks can have a tag](https://jupyter-notebook.readthedocs.io/en/stable/changelog.html#cell-tags) that could be used to execute specific cells [reading the ipynb file](https://stackoverflow.com/a/59090523) or [using Javascript inside a notebook](https://stackoverflow.com/a/50921391). The tag embedded in the notebook file is [very useful when using Voila as it is based on the nbconvert](https://voila.readthedocs.io/en/stable/customize.html#hiding-output-and-code-cells-based-on-cell-tags). However, ExecThatCell still works using pure IPython. Additionally, Voila will not have any problems with ExecThatCell either, as long as the user remembers the cells will be executed following the order according to how they appear in the notebook file.*


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

In the case you just want to execute again a cell that you know the index (the number inside the square brackets after "In"), you could just do something like this (Jupyter notebook, Google Colab or IPython command line version):
```
i = 10 # the cell index you want to execute again
exec(In[i])
```


## TODO:
- Test it :D
