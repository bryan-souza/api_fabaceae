# Built-ins
import os
import json
from pathlib import Path

# Internals
from app.exceptions import AcessViolationError

class PathRouter(object):
    _instances = {}

    _app_root_path = Path(__file__).parent.resolve()
    _config_path   = Path(_app_root_path, 'config')
    _default_cache_path = Path(_app_root_path, 'cache')

    _default_paths = {
        "APP_ROOT_PATH": _app_root_path,
        "CONFIG_PATH"  : _config_path,
        "CACHE_PATH"   : _default_cache_path
    } 

    def __new__(cls):
        if cls not in cls._instances:
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def __init__(self) -> None:
        self._pathspec = { **self._default_paths, **self._load_json() }
        self._validate()
    
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
            for alias, path in config.items():
                config.update({ alias: Path(path).resolve() })
        
        return {}

    def _validate(self) -> None:
        for path in self._pathspec.values():
            if not ( path.exists() ):
                absolute_path = path.resolve()
                os.mkdir(absolute_path)
