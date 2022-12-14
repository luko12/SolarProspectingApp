import sys
from qgis.core import (
    QgsApplication,
    QgsVectorLayer,
    QgsRasterLayer,
    QgsProcessingFeedback,
    QgsVectorFileWriter,
    QgsProcessingFeatureSourceDefinition,
    QgsFeatureRequest,
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
from processing.tools import dataobjects


Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
feedback = QgsProcessingFeedback()

context = dataobjects.createContext()
context.setInvalidGeometryCheck(QgsFeatureRequest.GeometryNoCheck)


def buffer(input: QgsVectorLayer, meters: int, **kwargs) -> QgsVectorLayer:
    print("-----BUFFER " + get_name(input) + "-----")
    output_path = kwargs.get('output', 'TEMPORARY_OUTPUT')
    output = processing.run("native:buffer",
        {
            'INPUT': input,
            'DISTANCE':meters,
            'SEGMENTS':5,
            'END_CAP_STYLE':0,
            'JOIN_STYLE':0,
            'MITER_LIMIT':2,
            'DISSOLVE':False,
            'OUTPUT':output_path
        }
    )
    if output_path == 'TEMPORARY_OUTPUT':
        output['OUTPUT'].setName(input.name() + "_buffered")
    return output['OUTPUT']


def select_by_location(input: QgsVectorLayer, compare: QgsVectorLayer, geometric_predicate: list, **kwargs) -> QgsVectorLayer:
    print("-----SELECT BY LOCATION " + get_name(input) + "-----")
    output_path = kwargs.get('output', 'TEMPORARY_OUTPUT')
    processing.run(
        "native:selectbylocation",
        {
            'INPUT': input,
            'PREDICATE': geometric_predicate, 
            'INTERSECT': compare,
            'METHOD': 0
        }
    )

    output = save_selected_features(input, output_path)

    if output_path == 'TEMPORARY_OUTPUT':
        output['OUTPUT'].setName(input.name() + "_selected")
    return output['OUTPUT']


def difference(input: QgsVectorLayer, overlay: QgsVectorLayer, **kwargs) -> QgsVectorLayer:
    print("-----DIFFERENCE " + get_name(input) + "-----")

    # iterate across all overlays
    overlay_num = 0
    while overlay:
        if overlay_num == 0:
            overlay = overlay
        elif overlay_num >= 0:
            overlay = kwargs.get('overlay' + str(overlay_num), "")
            input = output['OUTPUT']

        if overlay:
            print('overlay:', get_name(overlay))
            output = processing.run(
                "native:difference", 
                {
                    'INPUT': input,
                    'OVERLAY': overlay,
                    'OUTPUT': 'TEMPORARY_OUTPUT',
                },
                context= context,
            )
            overlay_num += 1

    if (kwargs.get('output', '')):
        save_features(output['OUTPUT'], kwargs.get('output', ''))
    else:
        output['OUTPUT'].setName(input.name() + "_differenced")
    return output['OUTPUT']
    

def save_features(input: QgsVectorLayer, output: str):
    print("-----SAVE FEATURES " + get_name(input) + "-----")
    processing.run(
        "native:savefeatures",
        {
            'INPUT': input,
            'OUTPUT': output
        }
    )

def save_selected_features(input: QgsVectorLayer, output: str) -> any:
    print("-----SAVE SELECTED FEATURES " + get_name(input) + "-----")
    return (
        processing.run(
            "native:saveselectedfeatures", 
            {
                'INPUT': input,
                'OUTPUT':output
            }
        )
    )


def get_name(input: any) -> str:
    if type(input) == str:
        return input.rsplit('\\', 1)[1].split('.')[0]
    elif type(input) == QgsVectorLayer or type(input) == QgsRasterLayer:
        return input.name()

