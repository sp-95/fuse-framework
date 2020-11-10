from pathlib import Path

import toml
from dynaconf import Dynaconf


class Config(Dynaconf):
    BASE_PATH = Path(__file__).parent.parent

    CONFIG_PATH = BASE_PATH / "configs"
    LOG_PATH = BASE_PATH / "logs"

    PROJECT_META = toml.load(BASE_PATH / "pyproject.toml")["tool"]["poetry"]


settings = Config(
    envvar_prefix="FUSE",
    settings_files=[
        Config.CONFIG_PATH / "settings.yaml",
        Config.CONFIG_PATH / ".secrets.yaml",
    ],
    environments=True,
)

# `envvar_prefix` = export envvars with `export FUSE_FOO=bar`.
# `settings_files` = Load this files in the order.
# `environments` = Set Project environment with `export ENV_FOR_DYNACONF=development`
