from qgis.core import QgsProcessingProvider
from .processing_algorithm import DataAwareMetadataEnricher


class MetadataProvider(QgsProcessingProvider):

    def loadAlgorithms(self):
        self.addAlgorithm(DataAwareMetadataEnricher())

    def id(self):
        return 'metadata_tools'

    def name(self):
        return 'Metadata Tools'

    def longName(self):
        return 'Metadata Tools – Data Aware Enricher'