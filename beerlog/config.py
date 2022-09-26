from importlib.resources import path
import os
from posixpath import dirname
from dynaconf import Dynaconf


settings = Dynaconf(
    envvar_prefix="BEERLOG",
    root_path=os.path.dirname(__file__),
    settings_files=["settings.toml"],
)
