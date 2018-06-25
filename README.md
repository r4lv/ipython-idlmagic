# idlmagic

Use IDL ([interactive data language](https://www.harrisgeospatial.com/SoftwareTechnology/IDL.aspx)) inside IPython / Jupyter notebook cells. It uses the IDL-python bridge `idlpy`, which is bundled with your IDL installation.


## Installation


Install *idlmagic* with pip:

``` bash
pip install idlmagic
```

Then, enable *idlmagic* in your notbook:
``` python
%load_ext idlmagic
```

*idlmagic* relies on a valid installation of the IDL-python-bridge. To see if it is available, run
``` python
import idlpy
```
If the import fails, refer to the [documentation](https://r4lv.github.io/ipython-idlmagic) to see how `idlpy` can be set up.


## Usage

*idlmagic* provides you with `%idl` and `%%idl` to execute IDL commands, and `%idl_var` to pass an IDL variable to python.

``` python
In [1]: %load_ext idlmagic

# run IDL using the %idl line magic:
In [2]: %idl INDGEN(5)
       0       1       2       3       4

# or use the cell magic for multiple commands:
In [3]: %%idl
   ...: PRINT, INDGEN(5)
   ...: PRINT, INDGEN(6)
       0       1       2       3       4
       0       1       2       3       4       5

# to access IDL data in python, you'll first have to assign it:
In [9]: %idl a = INDGEN(4)

# then use the %idl_var magic to get the IDL variable into python:
In [11]: a = %idl_var a

In [16]: a + 10
Out[16]: array([10, 11, 12, 13], dtype=int16)
```

Check the [documentation](https://r4lv.github.io/ipython-idlmagic) for more examples.


## Changes

**v0.1.0**

- first release