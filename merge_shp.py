import processing

registry = QgsMapLayerRegistry.instance()


lines_fin_z440_Fredrik = registry.mapLayersByName('lines_fin_z440_Fredrik')
lines_fin_z441_Roxana = registry.mapLayersByName('lines_fin_z441_Roxana')
lines_fin_z442_Mircea = registry.mapLayersByName('lines_fin_z442_Mircea')
lines_fin_z443_Diana = registry.mapLayersByName('lines_fin_z443_Diana')

processing.runandload('qgis:mergevectorlayers', lines_fin_z440_Fredrik + lines_fin_z441_Roxana + lines_fin_z442_Mircea + lines_fin_z443_Diana , None)


points_fin_z440_Fredrik = registry.mapLayersByName('points_fin_z440_Fredrik')
points_fin_z441_Roxana = registry.mapLayersByName('points_fin_z441_Roxana')
points_fin_z442_Mircea = registry.mapLayersByName('points_fin_z442_Mircea')
points_fin_z443_Diana = registry.mapLayersByName('points_fin_z443_Diana')


processing.runandload('qgis:mergevectorlayers', points_fin_z440_Fredrik + points_fin_z441_Roxana + points_fin_z442_Mircea + points_fin_z443_Diana , None)






PUNCTE_ZONA4_MPIGI = registry.mapLayersByName('PUNCTE_ZONA4_MPIGI')
Mpigi_z44_points_fin_merged = registry.mapLayersByName('Mpigi_z44_points_fin_merged')
mpigi_zona4_puncte_diana = registry.mapLayersByName('mpigi_zona4_puncte_diana')


processing.runandload('qgis:mergevectorlayers', PUNCTE_ZONA4_MPIGI + Mpigi_z44_points_fin_merged + mpigi_zona4_puncte_diana, None)