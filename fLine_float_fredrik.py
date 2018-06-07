from qgis.core import *
from qgis.gui import *
from qgis.utils import iface
import re

layer = iface.activeLayer()

selected_fid = []
r = re.compile(r"\d*\.0*[1-9]+\d*")

for feat in layer.getFeatures():
    if r.match(str(feat['Lenght'])):
        selected_fid.append(feat.id())
    else:
		print ''

layer.select(selected_fid)