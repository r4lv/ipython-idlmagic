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

*idlmagic* provides you with a *line magic* `%idl` and a *cell magic* `%%idl`. Check the [documentation](https://r4lv.github.io/ipython-idlmagic) for some examples.