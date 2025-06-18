import logging

from app.logging_config import setup_logging

def main() -> None:
    setup_logging()  # configure root logger
    logger = logging.getLogger(__name__)
    logger.info("Application started")

if __name__ == "__main__":
    main()