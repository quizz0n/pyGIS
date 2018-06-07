from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

layer = iface.activeLayer()

selected_fid = []


for feat in layer.getFeatures():
    if feat['Length'] != 555.555 and feat['Length'] != 777.777 and feat['Length'] != 888.888 and feat['Length'] != 999.999 and feat['CTRL'] == "Gresit":
        selected_fid.append(feat.id())
    else:
		print ''

layer.select(selected_fid)