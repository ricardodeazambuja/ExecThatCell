"""ExecThatCell: Execute a Jupyter (colab) notebook cell programmatically by given it a label
Copyright (C) 2020 Ricardo de Azambuja

ExecThatCell is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
ExecThatCell is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.
You should have received a copy of the GNU General Public License
along with ExecThatCell.  If not, see <https://www.gnu.org/licenses/>.

Acknowledgement:
This work was possible thanks to the financial support from IVADO.ca (postdoctoral scholarship 2019/2020).

Disclaimer (adapted from Wikipedia):
None of the authors, contributors, supervisors, administrators, employers, friends, family, vandals, or anyone else 
connected (or not) with this project, in any way whatsoever, can be made responsible for your use of the information (code) 
contained or linked from here.

TODO:
1) Test it...
"""

__author__ = "Ricardo de Azambuja"
__copyright__ = "Copyright 2020, MISTLab.ca"
__credits__ = [""]
__license__ = "GPL"
__version__ = "0.1.2"
__maintainer__ = "Ricardo de Azambuja"
__email__ = "ricardo.azambuja@gmail.com"
__status__ = "Development"


class LabelNotFound(Exception):
   def __init__(self, cellmarker, label):
        super().__init__(f"The cellmarker '{cellmarker}' with label '{label}' was not found!")

class CellMarkerNotFound(Exception):
   def __init__(self, cellmarker):
        super().__init__(f"The cellmarker '{cellmarker}' was not found!")

def execthatcell(label, cell_marker="#@#", latest=True, exec_it=True):
  """Finds a cell according to its label / cell_marker and execute its content.
  The label must be the first thing in the first line of your cell!!

  Parameters
  ----------
  label : str
      The label you gave to your cell. It will come just after cell_marker.
  cell_marker : str
      The signature indicating that comment is a cell label.
  latest : bool, optional
      Executes the latest version of the cell according to the last time
      the cell was executed. If latest=False it will execute the oldest version.
  exec_it : bool, optional
      When set to False (default is True) it will return the index of the cell
      without executing it. Useful when you want to easily catch exceptions by
      directly using exec(In[index]).
  """

  assert type(label)==str, "label must be a string"
  assert type(cell_marker)==str, "cell_marker must be a string"
    
  ip = get_ipython()
  In = ip.user_ns["In"]
  
  cell_marker_found = False
  order, offset = (-1,-1) if latest else (1,0)
  for i,c in enumerate(In[::order]):
    if cell_marker in c:
      cell_marker_found = True
      # must be the first line
      if not c.find(cell_marker+label):
        # must exactly match the label
        if label == c[len(cell_marker):c.find("\n")]:
          if exec_it:
            _ = ip.run_cell(In[i*order+offset], store_history=False, silent=True)
            break
          else:
            return i*order+offset
        else:
          raise LabelNotFound(cell_marker,label)
  if not cell_marker_found:
    raise CellMarkerNotFound(cell_marker)
  else:
    raise LabelNotFound(cell_marker,label)