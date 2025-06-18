import logging

setup_logging()
logger = logging.getLogger(__name__)

class BrainMapper:

    _db: str
    _collection: dict[str, str]
    _columns: dict[str, str]
    _query_methods: dict[str, str]
    _filters: dict[str, str]
    _projections: dict[str, str]

    def __init__(self, learningData: dict[str, str]):
