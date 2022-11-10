import sys

from qgis.core import QgsApplication, QgsProcessingFeedback
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

colorado_counties_fn = r"C:\Users\lukas\Documents\LukasProjects\SolarProspectingApp\Data\Colorado_County_Boundaries.shp"
output_fn = r"C:\Users\lukas\Documents\LukasProjects\SolarProspectingApp\Data\output.shp"
expression = """"county" = 'GUNNISON'"""

gunnison = processing.run(
    'native:extractbyexpression',
    {'INPUT': colorado_counties_fn, 'EXPRESSION': expression, 'OUTPUT': output_fn},
    feedback=feedback
    )['OUTPUT']
 
print('gunnison:', gunnison)

qgs.exitQgis()
