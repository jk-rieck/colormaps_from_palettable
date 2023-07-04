"""colormaps_from_palettable

Python package to extract the continuous colormaps from the
palettable (https://jiffyclub.github.io/palettable/) package
for easier use. (Except for the Wes Anderson colour scales,
they do not make sense as continuous maps)

Example:
import numpy as np
from matplotlib import pyplot as plt
import colormaps_from_palettable as cfp
cmaps = cfp.extract()['scientific']
some_sin = np.sin(np.linspace(0, np.pi, 20))
some_cos = np.cos(np.linspace(0, np.pi, 20))
some_data = some_sin[:, None] * some_cos[None, :]
plt.pcolormesh(some_data, cmap=cmaps['Vik'])
plt.colorbar()
"""

def extract():
    import palettable as p
    import numpy as np
    packs = {}
    to_ignore = ['absolute_import', 'palette', 'utils', 'version',
                 'VERSION', 'cubehelix', 'wesanderson', 'tableau']
    for pack in p.__dict__.keys():
        if pack[0:2] != '__' and pack not in to_ignore:
            packs[pack] = {}
            for seq_or_div in ['sequential', 'diverging']:
                try:
                    getattr(getattr(p, pack), seq_or_div)
                    mapss = getattr(getattr(p, pack), seq_or_div)
                    test_highest = []
                    for test in mapss.__dict__.keys():
                        try:
                            test_highest = np.append(test_highest,
                                                     int(test[-4:-2]))
                        except:
                            try:
                                test_highest = np.append(test_highest,
                                                         int(test[-3:-2]))
                            except:
                                test_highest = 0
                    highest = str(int(test_highest.max()))
                    for maps in mapss.__dict__.keys():
                        if maps[-4::] == highest + '_r':
                            maps3 = maps[0:-2]
                            maps2 = maps[0:-5]
                            maps1 = maps2 + '_r'
                            packs[pack][maps1]\
                                = getattr(getattr(mapss, maps), 'mpl_colormap')
                            packs[pack][maps2]\
                                = getattr(getattr(mapss, maps3), 'mpl_colormap')
                        elif maps[-3::] == highest + '_r':
                            maps3 = maps[0:-2]
                            maps2 = maps[0:-4]
                            maps1 = maps2 + '_r'
                            packs[pack][maps1]\
                                = getattr(getattr(mapss, maps), 'mpl_colormap')
                            packs[pack][maps2]\
                                = getattr(getattr(mapss, maps3), 'mpl_colormap')
                except:
                    mapss = getattr(p, pack)
                    test_highest = []
                    for test in mapss.__dict__.keys():
                        try:
                            test_highest = np.append(test_highest,
                                                     int(test[-4:-2]))
                        except:
                            try:
                                test_highest = np.append(test_highest,
                                                         int(test[-3:-2]))
                            except:
                                test_highest = 0
                    highest = str(int(test_highest.max()))
                    for maps in mapss.__dict__.keys():
                        if maps[-4::] == highest + '_r':
                            maps3 = maps[0:-2]
                            maps2 = maps[0:-5]
                            maps1 = maps2 + '_r'
                            packs[pack][maps1]\
                                = getattr(getattr(mapss, maps), 'mpl_colormap')
                            packs[pack][maps2]\
                                = getattr(getattr(mapss, maps3), 'mpl_colormap')
                        elif maps[-3::] == highest + '_r':
                            maps3 = maps[0:-2]
                            maps2 = maps[0:-4]
                            maps1 = maps2 + '_r'
                            packs[pack][maps1]\
                                = getattr(getattr(mapss, maps), 'mpl_colormap')
                            packs[pack][maps2]\
                                = getattr(getattr(mapss, maps3), 'mpl_colormap')
    return packs
