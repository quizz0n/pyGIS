"PlotArea"  <> 888.8888
AND
"PlotArea"  <> 999.9999
AND
 "CTRL"  =  'Gresit' 


"PlotArea" < 888.8888
AND 
"PlotArea" > 888.8888 < 999.9999
AND
 "PlotArea" > 999.9999
 AND
  "Status"  =  'OK' 
  OR
   "Status"  = 'PART SURVEYED' 
   OR
    "Status"  =  'PENDING VERIFICATION' 
AND
  "CTRL" =  'Gresit' 





 "PlotArea"  <> 888.8888 AND "PlotArea"  <> 999.9999

AND "Status"  =  'OK' OR "Status"  = 'PART SURVEYED' OR "Status"  =  'PENDING VERIFICATION' 















if("PlotArea"  <> 888.8888 AND "PlotArea"  <> 999.9999 
AND
"Status"  ==  'PARTIAL' 
AND
 "PR" >120, 'Gresit', 
if("PlotArea"  <> 888.8888 AND "PlotArea"  <> 999.9999
AND
"Status"  ==  'PARTIAL'  
AND
"PR" >80, 'ok','Gresit'))











if("Status" IS  NOT  'PARTIAL' 
AND
"PlotArea"  <> 888.8888 AND "PlotArea"  <> 999.9999 
AND
 "PR" >120, 'Gresit', 
if("Status" IS  NOT  'PARTIAL'
AND
"PlotArea"  <> 888.8888 AND "PlotArea"  <> 999.9999
AND
"PR" >80, 'ok','Gresit'))


# First trial
cLayer = iface.mapCanvas().currentLayer() 

expr = QgsExpression('Status ILIKE \'%OK%\' OR Status ILIKE \'%PART SURVEYED%\' OR Status ILIKE \'%PENDING VERIFICATION%\'')

it = cLayer.getFeatures( QgsFeatureRequest( expr ) )
ids = [i.id() for i in it]


selection = ids
for feature in selection:
	if feature.attributes(PlotArea) <> '888.8888' and feature.attributes(PlotArea) <> '999.9999' and feature.attributes(PR) > '120':
	  feature.setAttribute(27, 'Gresit')
	elif feature.attributes(PlotArea) <> '888.8888' and feature.attributes(PlotArea) <> '999.9999' and feature.attributes(PR) > '80': 
	  feature.setAttribute(27, 'Ok')
	else:
	  print 'Cant find the specified entries'

cLayer.commitChanges()
		

		
		

#Working trial
from qgis.core import *
from qgis.gui import *
import qgis.utils

layer = iface.mapCanvas().currentLayer() 

expr = QgsExpression('Status ILIKE \'%OK%\' OR Status ILIKE \'%PART SURVEYED%\' OR Status ILIKE \'%PENDING VERIFICATION%\'')

it = layer.getFeatures(QgsFeatureRequest(expr))

layer.startEditing()
for feat in it:
  if feat['PlotArea'] != 888.8888 and feat['PlotArea'] != 999.9999 and feat['Pr'] > 120:
    layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('CTRL'), 'Gresit')
  elif feat['PlotArea'] != 888.8888 and feat['PlotArea'] != 999.9999 and feat['Pr'] > 80:
    layer.changeAttributeValue(feat.id(), layer.fieldNameIndex('CTRL'), 'Ok')
  else:
    print ''

layer.commitChanges()