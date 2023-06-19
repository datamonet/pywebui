"""DataBamboo CLI Tool
"""
import importlib_resources as _resources
try:
    from configparser import ConfigParser as _ConfigParser
except ImportError:  # Python 2
    from ConfigParser import ConfigParser as _ConfigParser

__version__ = "0.0.1"

# Read URL from config file
_cfg = _ConfigParser()
with _resources.path("webuipy", "config.cfg") as _path:
    _cfg.read(str(_path))
URL = _cfg.get("website", "url")
