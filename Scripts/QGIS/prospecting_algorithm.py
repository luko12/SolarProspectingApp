import utilities
# import psycopg2
from qgis.core import (
    QgsVectorLayer,
    QgsDataSourceUri,
)


"""
Prospecting steps:
1. Buffer powerlines X meters
2. Select parcels by location (if touching powerlines buffer)
3. Clip wetlands & floodplains to parcel selection to reduce working file size
4. Buffer wetlands & floodplains X meters
5. Difference? 
"""


# db_connection = psycopg2.connect(
#     host="database-1.czskhcqd4krm.us-east-1.rds.amazonaws.com",
#     port=5432,
#     database='SolarProspectingApp',
#     user="postgres",
#     password="password")


uri = QgsDataSourceUri()
uri.setConnection(
    "database-1.czskhcqd4krm.us-east-1.rds.amazonaws.com",
    "5432",
    'SolarProspectingApp',
    "postgres",
    "password",
)

"""
Declare Layers
"""
uri.setDataSource("public", "transmission_lines", "geom")
transmission_lines_layer = QgsVectorLayer(uri.uri(), "transmission_lines", "postgres")
uri.setDataSource("public", "floodzones", "geom")
floodzones_layer = QgsVectorLayer(uri.uri(), "floodzones", "postgres")
uri.setDataSource("public", "wetlands", "geom")
wetlands_layer = QgsVectorLayer(uri.uri(), "wetlands", "postgres")
uri.setDataSource("public", "Parcels", "geom")
parcels_layer = QgsVectorLayer(uri.uri(), "Parcels", "postgres")


"""
Buffer powerlines 100m
"""
buffered_powerlines_layer = utilities.buffer(
    input= transmission_lines_layer,
    meters= 100,
)
# print("buffered_powerlines_layer:", buffered_powerlines_layer, 'id:', buffered_powerlines_layer.id(), 'feature count:', buffered_powerlines_layer.featureCount())


"""
Buffer floodzones and wetlands 100m
"""
buffered_floodzones_layer = utilities.buffer(
    input= floodzones_layer,
    meters= 100,
    # output= r"C:\Users\lukas\Documents\LukasProjects\SolarProspectingApp\Data\flood_buffered.shp"
)
# print("buffered_floodzones_layer:", buffered_floodzones_layer, 'id:', buffered_floodzones_layer.id(), 'feature count:', buffered_floodzones_layer.featureCount())
buffered_wetlands_layer = utilities.buffer(
    input= wetlands_layer,
    meters= 100,    
)
# print("buffered_wetlands_layer:", buffered_wetlands_layer, 'id:', buffered_wetlands_layer.id(), 'feature count:', buffered_wetlands_layer.featureCount())


"""
Select parcels intersecting the buffered powerlines
"""
parcels_electrical_selection_layer = utilities.select_by_location(
    input= parcels_layer,
    compare= buffered_powerlines_layer,
    geometric_predicate= [0]
)
# print("selected_parcels:", parcels_electrical_selection_layer, 'id:', parcels_electrical_selection_layer.id(), 'feature count:', parcels_electrical_selection_layer.featureCount())


"""
Inverse buffer selected parcels 100m
"""
parcels_electrical_selection_buffered_layer = utilities.buffer(
    input= parcels_electrical_selection_layer,
    meters= -200,
)


"""
Difference inverse buffered selected parcels from floodzones and wetlands
"""
difference_output = utilities.difference(
    input= parcels_electrical_selection_buffered_layer,
    overlay= buffered_floodzones_layer,
    overlay1= buffered_wetlands_layer,
    output= r"C:\Users\lukas\Documents\LukasProjects\SolarProspectingApp\Data\differenceall.shp"
)
# print('difference:', difference_output)