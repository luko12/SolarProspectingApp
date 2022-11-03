"""
Double-click on the history item or paste the command below to re-run the algorithm
"""

processing.run("native:extractbylocation",
               {
                   'INPUT': QgsProcessingFeatureSourceDefinition(
                       'dbname=\'SolarProspectingApp\' host=database-1.czskhcqd4krm.us-east-1.rds.amazonaws.com port=5432 sslmode=disable key=\'id\' srid=2232 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table="public"."Parcels" (geom)', selectedFeaturesOnly=False, featureLimit=-1, flags=QgsProcessingFeatureSourceDefinition.FlagOverrideDefaultGeometryCheck, geometryCheck=QgsFeatureRequest.GeometrySkipInvalid), 'PREDICATE': [0, 1, 4, 5, 6, 7], 'INTERSECT': QgsProcessingFeatureSourceDefinition('dbname=\'SolarProspectingApp\' host=database-1.czskhcqd4krm.us-east-1.rds.amazonaws.com port=5432 sslmode=disable key=\'id\' srid=3857 type=MultiLineString checkPrimaryKeyUnicity=\'1\' table="public"."transmission_lines" (geom)', selectedFeaturesOnly=False, featureLimit=-1, flags=QgsProcessingFeatureSourceDefinition.FlagOverrideDefaultGeometryCheck, geometryCheck=QgsFeatureRequest.GeometrySkipInvalid),
                   'OUTPUT': 'TEMPORARY_OUTPUT'
               })


processing.run(
    "native:selectbylocation",
    {
        'INPUT': 'dbname=\'SolarProspectingApp\'host=database-1.czskhcqd4krm.us-east-1.rds.amazonaws.com port=5432 sslmode=disable key=\'id\' srid=2232 type=MultiPolygon checkPrimaryKeyUnicity=\'1\' table="public"."Parcels" (geom)',
        'PREDICATE': [0],
        'INTERSECT': 'postgres://dbname=\'SolarProspectingApp\' host=database-1.czskhcqd4krm.us-east-1.rds.amazonaws.com port=5432 sslmode=disable key=\'id\' srid=3857 type=MultiLineString checkPrimaryKeyUnicity=\'1\' table="public"."transmission_lines" (geom)',
        'METHOD': 0
    }
)

layer = qgis.utils.iface.activeLayer()
print('layer:', layer, 'layer id:', layer.id(), 'layer feature count:', layer.featureCount())