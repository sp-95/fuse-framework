from pathlib import Path

import toml
from dynaconf import Dynaconf


class Config(Dynaconf):
    PROJECT_META = toml.load("pyproject.toml")["tool"]["poetry"]

    BASE_PATH = Path(__file__).parent


settings = Config(
    envvar_prefix="FUSE",
    settings_files=["configs/settings.yaml", "configs/.secrets.yaml"],
    environments=True,
)

# `envvar_prefix` = export envvars with `export FUSE_FOO=bar`.
# `settings_files` = Load this files in the order.
# `environments` = Set Project environment with `export ENV_FOR_DYNACONF=development`
