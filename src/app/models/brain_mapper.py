import logging

from app import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

class BrainMapper:

    _db: str
    _collection: dict[str, str]
    _columns: dict[str, str]
    _query_methods: dict[str, str]
    _filters: dict[str, str]
    _projections: dict[str, str]

    def __init__(self, learning_data: dict[str, str]):
        for sentence in learning_data:
            logger.info(sentence)
            logger.info(learning_data[sentence])