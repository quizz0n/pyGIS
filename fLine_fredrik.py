from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

layer = iface.mapCanvas().currentLayer() 

it = layer.getFeatures(QgsFeatureRequest())

layer.startEditing()
for feat in it:
  if feat['Length'] != 555.555 and feat['Length'] != 777.777 and feat['Length'] != 888.888 and feat['Length'] != 999.999 and feat['PR'] > 120:
    layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('CTRL'), 'Gresit')
  elif feat['Length'] != 555.555 and feat['Length'] != 777.777 and feat['Length'] != 888.888 and feat['Length'] != 999.999 and feat['PR'] > 80:
    layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('CTRL'), 'Ok')
  elif feat['Length'] != 555.555 and feat['Length'] != 777.777 and feat['Length'] != 888.888 and feat['Length'] != 999.999 and feat['PR'] < 80:
    layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('CTRL'), 'Gresit')
  else:
    print ''

layer.commitChanges()