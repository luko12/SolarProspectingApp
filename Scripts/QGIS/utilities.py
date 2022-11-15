import sys
from qgis.core import (
    QgsApplication,
    QgsVectorLayer,
    QgsProcessingFeedback,
    QgsVectorFileWriter,
)
from qgis.analysis import QgsNativeAlgorithms


QgsApplication.setPrefixPath(r'C:\OSGeo4W\apps\qgis-dev', True)
qgs = QgsApplication([], False)
qgs.initQgis()


# Add the path to processing so we can import it next
sys.path.append(r'C:\OSGeo4W\apps\qgis-dev\python\plugins')
# Imports usually should be at the top of a script but this unconventional
# order is necessary here because QGIS has to be initialized first
import processing
from processing.core.Processing import Processing


Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
feedback = QgsProcessingFeedback()


def buffer(input: QgsVectorLayer, meters: int, **kwargs) -> dict:
    print("-----BUFFER-----")
    output = kwargs.get('output', 'TEMPORARY_OUTPUT')
    output = processing.run("native:buffer",
        {
            'INPUT': input,
            'DISTANCE':meters,
            'SEGMENTS':5,
            'END_CAP_STYLE':0,
            'JOIN_STYLE':0,
            'MITER_LIMIT':2,
            'DISSOLVE':False,
            'OUTPUT':output
        }
    )
    return output['OUTPUT']

def select_by_location(input: QgsVectorLayer, compare: QgsVectorLayer, geometric_predicate: list) -> dict:
    print("-----SELECT BY LOCATION-----")
    processing.run(
        "native:selectbylocation",
        {
            'INPUT': input,
            'PREDICATE': geometric_predicate, 
            'INTERSECT': compare,
            'METHOD': 0
        }
    )
    # _writer = QgsVectorFileWriter.writeAsVectorFormat(
    #     layer= input, 
    #     fileName= r"C:\Users\lukas\Documents\LukasProjects\SolarProspectingApp\Data\myselection.shp", 
    #     fileEncoding= "utf-8",
    #     destCRS= input.crs(), 
    #     driverName= "ESRI Shapefile",
    #     onlySelected=True
    # )
    # QgsVectorLayer()
    # tempLayer = QgsVectorLayer("Polygon", "temporary_points", "memory")

    output = processing.run('native:savefeatures', {'INPUT': input, 'OUTPUT':"TEMPORARY_OUTPUT"})


    return output
