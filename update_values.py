from qgis.core import *
from qgis.gui import *
from qgis.utils import iface
from qgis.PyQt.QtCore import QVariant

# create layer
layer = iface.mapCanvas().currentLayer() 
it = layer.getFeatures(QgsFeatureRequest())



layer.startEditing()

# add fields

new_Field1 = "L_M"
new_Field2 = "Lungime"
new_Field3 = "PR"
new_Field4 = "CTRL"

idq = layer.fieldNameIndex(new_Field1)
idw = layer.fieldNameIndex(new_Field2)
ide = layer.fieldNameIndex(new_Field3)
idr = layer.fieldNameIndex(new_Field4)

if idq == -1:
	layer.addAttribute(QgsField(new_Field1, QVariant.Double, 'double', 20, 4))
if idw == -1:
	layer.addAttribute(QgsField(new_Field2, QVariant.Double, 'double', 20, 3))
if ide == -1:
	layer.addAttribute(QgsField(new_Field3, QVariant.Double, 'double', 20, 3))
if idr == -1:
	layer.addAttribute(QgsField(new_Field4, QVariant.String, 'string', len=10))


layer.updateFields() # tell the vector layer to fetch changes from the provider

e = QgsExpression ("\"Length\" * 0.3048")
e.prepare(layer.pendingFields())

for feat in it:
	if feat['LengthUnit'] == 2:
		layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('L_M'), e.evaluate(feat))
	else:
		layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('L_M'), feat['Length'])

layer.updateFields() # tell the vector layer to fetch changes from the provider

for feat in it:
	flen = feat.geometry()
	layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('Lungime'), flen.length())

layer.updateFields() # tell the vector layer to fetch changes from the provider

for feat in it:
	layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('PR'), feat['Length']/feat['Lungime'] * 100)
	
for feat in it:
  if feat['Length'] != 555.555 and feat['Length'] != 777.777 and feat['Length'] != 888.888 and feat['Length'] != 999.999 and feat['PR'] > 120:
    layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('CTRL'), 'Gresit')
  elif feat['Length'] != 555.555 and feat['Length'] != 777.777 and feat['Length'] != 888.888 and feat['Length'] != 999.999 and feat['PR'] > 80:
    layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('CTRL'), 'Ok')
  elif feat['Length'] != 555.555 and feat['Length'] != 777.777 and feat['Length'] != 888.888 and feat['Length'] != 999.999 and feat['PR'] < 80:
    layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('CTRL'), 'Gresit')
  else:
    print ''
	
layer.updateFields() # tell the vector layer to fetch changes from the provider