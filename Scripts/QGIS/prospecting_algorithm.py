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
uri.setDataSource("public", "Parcels", "geom")
parcels_layer = QgsVectorLayer(uri.uri(), "Parcels", "postgres")


"""
Buffer powerlines 100m
"""
buffered_powerlines = utilities.buffer(
        input= transmission_lines_layer,
        meters = 100,
    )
print("buffered_powerlines:", buffered_powerlines, 'id:', buffered_powerlines.id(), 'feature count:', buffered_powerlines.featureCount())


"""
Select parcels intersecting the buffered powerlines
"""
print('feature count parcels:', parcels_layer.featureCount())
parcels_electrical_selection = utilities.select_by_location(
    input= parcels_layer,
    compare= buffered_powerlines,
    geometric_predicate= [0]
)
print("selected_parcels:", parcels_electrical_selection, 'id:', parcels_electrical_selection.id(), 'feature count:', parcels_electrical_selection.featureCount())

"""

"""