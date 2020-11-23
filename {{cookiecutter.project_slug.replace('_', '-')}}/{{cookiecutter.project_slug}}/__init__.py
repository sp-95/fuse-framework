from {{cookiecutter.project_slug}}.config import settings
from {{cookiecutter.project_slug}}.logger import log_config

__version__ = settings.PROJECT_META["version"]

log_config.setup()
