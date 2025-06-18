"""Central logging configuration.

Call `setup_logging()` once, ideally at program start, to
configure the root logger from *config/logging.yaml*.
"""
import logging
import logging.config
from pathlib import Path
import yaml

DEFAULT_LEVEL = logging.INFO

def setup_logging(config_file: str | None = None, default_level: int = DEFAULT_LEVEL) -> None:
    """Set up logging configuration.

    Args:
        config_file: Path to a YAML file. If *None*, uses
                     *config/logging.yaml* relative to project root.
        default_level: Fallback level if config file is missing.
    """
    if config_file is None:
        config_file = Path(__file__).resolve().parent.parent.parent / "config" / "logging.yaml"

    config_path = Path(config_file)
    if config_path.is_file():
        with config_path.open("r", encoding="utf-8") as fh:
            config = yaml.safe_load(fh)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
        logging.warning("Logging config file not found: %s – using basicConfig", config_path)