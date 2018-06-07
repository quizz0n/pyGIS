layerA = feat['L_M']
layerB = feat['Lungime']
layerC = feat['PR']
layerD = feat['CTRL']

#Loop           
for A in layerA.getFeatures():
    if feat['Length'] == 2:
    	layer.changeAttributeValue(feat.id(), feat['Length'] * 0.3048)
    for b in layerB.getFeatures():
        layer.changeAttributeValue(feat.id(), feat['Lungime'], geom.length())
        for c in layerC.getFeatures():
            #print "Layer Intersection :" + str(i)
            #if "your condition"
            provider.changeAttributeValues({j.id() : {provider.fieldNameMap()['new_field'] : i[0]}})
            layerJ.updateFeature(j)