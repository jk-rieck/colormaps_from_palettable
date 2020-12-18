# colormaps_from_palettable

Python package to extract the continuous colormaps from the
[palettable](https://jiffyclub.github.io/palettable/) package
for easier use. (Except for the Wes Anderson colour scales,
they do not make sense as continuous maps)

## Requirements

[palettable](https://jiffyclub.github.io/palettable/) has to be installed.

## Install in existing environment

 Install from the repository using
  ```shell
  pip install git+https://github.com/jk-rieck/colormaps_from_palettable.git
  ```

## Usage

  Example of how to extract the continuous colormaps from the
  [Scientific](http://www.fabiocrameri.ch/colourmaps.php) package and use
  the `Vik` colormap. (Example requires packages [`numpy`](https://numpy.org/)
  and [`matplotlib`](https://matplotlib.org/))
  ```Python
  import numpy as np
  from matplotlib import pyplot as plt
  import colormaps_from_palettable as cfp
  cmaps = cfp.extract()['scientific']
  some_sin = np.sin(np.linspace(0, np.pi, 20))
  some_cos = np.cos(np.linspace(0, np.pi, 20))
  some_data = some_sin[:, None] * some_cos[None, :]
  plt.pcolormesh(some_data, cmap=cmaps['Vik'])
  plt.colorbar()
  ```

  Please see the [example notebook](./examples/example.ipynb) if you want to
  try out all the colormaps. (You need
  [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/) for that...)
