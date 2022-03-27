# Built-ins
import json
from pathlib import Path
from typing import Any

# Internals
from app.exceptions import AcessViolationError
from app.cerebrum import Identifier


class PathRouterMeta(type):
    _instances = {}

    def __call__(cls, *args: Any, **kwargs: Any) -> Any:
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class PathRouter(object, metaclass=PathRouterMeta):
    _app_root_path = Path(__file__).resolve()
    _config_path   = Path(_app_root_path, 'config')
    _default_cache_path = Path(_app_root_path, 'cache')

    _default_paths = {
        "APP_ROOT_PATH": _app_root_path,
        "CONFIG_PATH"  : _config_path,
        "CACHE_PATH"   : _default_cache_path
    } 


    def __init__(self) -> None:
        self._pathspec = { **self._default_paths, **self._load_json() }
    
    def __dict__(self) -> dict:
        return self._pathspec

    def __getitem__(self, path):
        return self._pathspec[path]

    def __setitem__(self, path, data):
        raise AcessViolationError(
            """
            Pathspec is read-only.
            User defined paths must be specified under the `config/config.json` file.
            """
        )

    def __missing__(self):
        raise ValueError(
            """
            Path not found.
            Check the file `config/config.json` for typos.
            """
        )


    def _load_json(self) -> dict:
        config_file = Path( self._config_path, 'config.json' )
        if ( config_file.is_file() ):
            config = json.load( open(config_file) )['paths']
            return config
        
        return {}


def get_identifier():
    instance = Identifier()
    return instance