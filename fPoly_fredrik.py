from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

layer = iface.mapCanvas().currentLayer() 

expr = QgsExpression('Status ILIKE \'%OK%\' OR Status ILIKE \'%PART SURVEYED%\' OR Status ILIKE \'%PENDING VERIFICATION%\'')

it = layer.getFeatures(QgsFeatureRequest(expr))

layer.startEditing()
for feat in it:
  if feat['PlotArea'] != 888.8888 and feat['PlotArea'] != 999.9999 and feat['PR'] > 120:
    layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('CTRL'), 'Gresit')
  elif feat['PlotArea'] != 888.8888 and feat['PlotArea'] != 999.9999 and feat['PR'] > 80:
    layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('CTRL'), 'Ok')
  elif feat['PlotArea'] != 888.8888 and feat['PlotArea'] != 999.9999 and feat['PR'] < 80:
    layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('CTRL'), 'Gresit')
  else:
    print ''

layer.commitChanges()