"""Setup colormaps_from_palettable"""

from setuptools import setup

setup(name='colormaps_from_palettable',
      version='0.1',
      description='Extract the continuous colormaps from palettable',
      author='Jan Klaus Rieck',
      packages=['colormaps_from_palettable'],
      package_dir={'colormaps_from_palettable': 'colormaps_from_palettable'},
      install_requires=['setuptools', 'palettable',],
      zip_safe=False)
