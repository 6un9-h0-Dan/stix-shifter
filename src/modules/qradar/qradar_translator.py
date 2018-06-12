
from ..base.base_translator import BaseTranslator
from .stix_to_aql import StixToAQL
from ...json_to_stix.json_to_stix import JSONToStix


class Translator(BaseTranslator):

    def __init__(self):
        self.result_translator = JSONToStix(
            'src/modules/qradar/json/to_stix_map.json')
        self.query_translator = StixToAQL()